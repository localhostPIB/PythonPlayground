from shareplum import Site
from shareplum import Office365
from shareplum.site import Version


class SharepointAPI:
    __site = None

    def login(self):
        authcookie = Office365('', username='',
                               password='').GetCookies()
        self.__site = Site('', version=Version.v365,
                           authcookie=authcookie)

    def addList(self):
        self.__site.AddList('My new new new list', description='Great List created by Phyton',
                            template_id='Custom List')


test = SharepointAPI()
test.login()
