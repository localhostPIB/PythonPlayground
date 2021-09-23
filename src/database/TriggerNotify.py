import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import select


def dblisten():
    connection = psycopg2.connect(
            host="128.0.0.0",
            database="DB",
            user="###",
            password="....")

    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = connection.cursor()
    cur.execute("LISTEN new_Id;")
    print("Starte")
    while True:
        if (select.select([connection], [], [], 240) == ([], [], [])) and not subscription:
           break
        connection.poll()
        connection.commit()

        while connection.notifies:
            notify = connection.notifies.pop()
            print("Got NOTIFY:", notify.pid, notify.channel, notify.payload)


if __name__ == '__main__':
    dblisten()
