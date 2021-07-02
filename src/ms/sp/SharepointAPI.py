from shareplum import Office365, Site
from shareplum.site import Version
from src.ms.sp import StringUtils


class SharepointAPI:
    __site = None

    def login(self):
        authcookie = Office365(StringUtils.StringUtils.website, username=StringUtils.StringUtils.email,
                               password=StringUtils.StringUtils.passwort).GetCookies()
        self.__site = Site(StringUtils.StringUtils.websiteAPI, version=Version.v365,
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
#test.infoList()
