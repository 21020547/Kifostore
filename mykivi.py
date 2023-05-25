from kivy.config import Config
Config.set('graphics', 'resizable', False)

from PopupWindow import AppPopup
from kivymd.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager 
from database import Database
import filetype



class WindowManager(ScreenManager):
    pass

class CreateAccountScreen(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    passw = ObjectProperty(None)

    def LoginBtn(self):
        sm.current = "Login"
        self.reset()


    def SubmitBtn(self):
        if (user.search_email(self.email.text) == True):
            AppPopup().CreatedPopup()
            self.reset()

        elif (self.PasswordCheck() == False
            or self.EmailCheck() == False 
            or self.Namecheck() == False ):

            AppPopup().InvalidFormPopup()
            self.reset()

        else:
            user.CreateFolder(self.email.text)
            user.save_data(self.namee.text, self.email.text, self.passw.text)
            self.reset()
            sm.current = "Login"

    def PasswordCheck(self):
        if len(self.passw.text) < 6:
            return False
        return True

    def EmailCheck(self):
        if ("@" not in self.email.text
        or ".com" not in self.email.text
        or self.email.text.index("@") > self.email.text.index(".com")):
            return False
        
        return True

    def Namecheck(self):
        if (self.namee.text.isalnum() == False):
            return False
        else : 
            return True

    def reset(self):
        self.namee.text = ''
        self.email.text = ''
        self.passw.text = ''

    def PressPassword(self):  
        self.passw.password = False

    def ReleasePassword(self):
        self.passw.password = True

    

class LoginScreen(Screen):
    BtnHeight = ObjectProperty(None)
    email = ObjectProperty(None)
    passwordie = ObjectProperty(None)

    def CreateAccountBtn(self):
        self.reset()
        sm.current = "CreateAccount"
        
    def LoginBtn(self):

        if (user.search_data(self.email.text, self.passwordie.text) == True):

            MainScreen.current = user.UserDict[self.email.text][3].replace("\\", '/') 

            self.reset()

            sm.current = "Main"

        else :
            AppPopup().InvalidLoginPopup()

    def PressPassword(self):  
        self.passwordie.password = False
        

    def ReleasePassword(self):
        self.passwordie.password = True

    def reset(self):
        self.email.text = ''
        self.passwordie.text = ''


    def DesignMode(self):
        MainScreen.current = "C:/Users/Long/Desktop/kivy/long"
        sm.current = "Main"

    



class MainScreen(Screen):
    current = 'C:/Users/Long/Desktop/kivy/blank_folder'
    folder_path = StringProperty(current)


    def on_pre_enter(self, *args):
        self.folder_path = self.current

    def LogoutBtn(self):
        sm.current = "Login"

    def ImageSelected(self, file_name):
            try:
                if (filetype.guess_mime(file_name[0])[0:5] == "image" ):
                    ImageScreen.current = file_name[0]
                    ImageScreen.folder_path = self.folder_path
                    sm.current = "Image"

                else:
                    print("Not correct type")
            except:
                pass
        

    def on_leave(self, *args):
        MainScreen.current = 'C:/Users/Long/Desktop/kivy/blank_folder'


class ImageScreen(Screen):
    folder_path = ''
    current = ''
    source = StringProperty(current)
    
    def on_pre_enter(self, *args):
        self.source = self.current

    def XBtn(self):
        MainScreen.current = self.folder_path
        sm.current = "Main"


kv = Builder.load_file("mykivi.kv")


user = Database("C:/Users/Long\Desktop/database.txt", "C:/Users/Long/Desktop/kivy")

sm = WindowManager()


ScreenList = [LoginScreen(name = "Login"), CreateAccountScreen(name = "CreateAccount"), MainScreen(name = "Main"), ImageScreen(name = "Image")]
for screen in ScreenList:
    sm.add_widget(screen)

sm.current = "Login"



class MyMainApp (App) :
    def build(self):
        return sm


MyMainApp().run()