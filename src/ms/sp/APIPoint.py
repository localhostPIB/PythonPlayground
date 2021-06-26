from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext


# https://pypi.org/project/Office365-REST-Python-Client/
class APIPoint:

    def login(self):
        site_url = "https://satzweiss.sharepoint.com"
        ctx = ClientContext(site_url).with_credentials(UserCredential("", ""))
        web = ctx.web
        ctx.load(web)
        ctx.execute_query()
        print("Web title: {0}".format(web.properties['Title']))


apiTest = APIPoint()
apiTest.login()
