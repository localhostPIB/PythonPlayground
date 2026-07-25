#!/usr/bin/env python3
"""
Exportiert alle Reporter-E-Mail-Adressen aus Jira-Issues mit Status=Spam.
Paginiert automatisch durch alle Ergebnisse.

Voraussetzungen:
  pip install requests

Konfiguration:
  - JIRA_BASE_URL: Deine Jira-Cloud-URL
  - JIRA_EMAIL: Deine Atlassian-Account-E-Mail
  - JIRA_API_TOKEN: API-Token (erstellen unter https://comapndyid.atlassian.com/manage-profile/security/api-tokens)
"""

import csv
import requests
from requests.auth import HTTPBasicAuth

# === KONFIGURATION ===
JIRA_BASE_URL = ""
JIRA_EMAIL = ""  # <-- ANPASSEN
JIRA_API_TOKEN = ""             # <-- ANPASSEN

# === EINSTELLUNGEN ===
JQL = "project = SUPPORT AND status = Spam ORDER BY created DESC"
PAGE_SIZE = 100  # Max 100 pro Seite bei der REST API v3
OUTPUT_FILE = "spam-absender-emails.csv"
DEDUPLIZIEREN = False  # True = nur unique E-Mails, False = alle (eine pro Issue)

# === SCRIPT ===
def main():
    session = requests.Session()
    session.auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
    session.headers.update({"Accept": "application/json"})

    emails = []
    start_at = 0
    total = None

    print(f"Starte Export mit JQL: {JQL}")
    print(f"Seitengröße: {PAGE_SIZE}")

    while True:
        url = f"{JIRA_BASE_URL}/rest/api/3/search"
        params = {
            "jql": JQL,
            "fields": "reporter",
            "maxResults": PAGE_SIZE,
            "startAt": start_at,
        }

        response = session.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if total is None:
            total = data["total"]
            print(f"Gesamt: {total} Issues")

        issues = data.get("issues", [])
        if not issues:
            break

        for issue in issues:
            reporter = issue.get("fields", {}).get("reporter")
            if reporter:
                email = reporter.get("emailAddress", "")
                if email:
                    emails.append(email)
                else:
                    # Fallback: displayName wenn keine E-Mail sichtbar
                    emails.append(reporter.get("displayName", "unbekannt"))
            else:
                emails.append("")

        start_at += len(issues)
        print(f"  Fortschritt: {start_at}/{total} ({start_at*100//total}%)")

        if start_at >= total:
            break

    # Deduplizieren falls gewünscht
    if DEDUPLIZIEREN:
        emails = sorted(set(emails))
        print(f"\nNach Deduplizierung: {len(emails)} unique Adressen")

    # CSV schreiben
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["email"])
        for email in emails:
            writer.writerow([email])

    print(f"\n✅ Fertig! {len(emails)} E-Mails exportiert nach: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
