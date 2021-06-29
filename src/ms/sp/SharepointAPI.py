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

    def infoList(self):
        #folder = self.__site.Folder('Freigegebene Dokumente')
        #file = folder.get_file('conf.py')
        file = self.__site.get_list_templates()
        print(file)
        return file


test = SharepointAPI()
test.login()
test.infoList()
