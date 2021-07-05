from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from office365.runtime.http.request_options import RequestOptions
from .UserForm import User
from Products.Five.browser import BrowserView
import json    
from plone import api


#http://localhost:8080/PloneSec/@@helloWorld
class SampleView(BrowserView):

    __email = None
    __pw    = None
    __timeStamp = " "
    __ctx = None
    __site_url = None
    __count = 0
    __user  = User()


    def __init__(self, *args):
        super(SampleView, self).__init__(*args)


    def __call__(self):   
        form                = self.request.form
        submitButton        = form.get('Submit', 'OFF') != 'OFF'
        self.__email        = form.get('Email', "")
        self.__pw           = form.get('Passwort',"")

        if submitButton:
            try:
                self.handleAuthentication(self.__email, self.__pw)
                return self.request.response.redirect("...")
            except ValueError as ve:
                return self.index()

        return self.index()


    def handleAuthentication(self, email, password):
            try:
                self.__site_url = 'https://....'
                self.__ctx = ClientContext(self.__site_url).with_credentials(UserCredential(email, password))
                web = self.__ctx.web
                self.__ctx.load(web)
                self.__ctx.execute_query()
                self.__user.setEmail(email)
                self.__user.setPassword(password)
                self.setSession(self.__user)
            except ValueError as ve:
                api.portal.show_message(message='Falsches Passwort' ,request=self.request ,type='error')
                raise ValueError(ve)



    def getEmail(self):
        return self.__user.getEmail()


    def setSession(self, user):
        sdm     = self.context.session_data_manager
        session = sdm.getSessionData(create=True)
        session.set("userSession", user)
        session.set("ctx", self.__ctx)
