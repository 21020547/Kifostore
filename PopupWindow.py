from kivy.uix.label import Label 
from kivy.uix.popup import Popup

class AppPopup():
    def CreatedPopup(self):
        showPop = Popup( 
            title = "Invalid Email", 
            content = Label(text = "Your Email Has Been Used", pos_hint = {"x" : 0.25, "top" : 0.8 }, size_hint = (0.5, 0.15), font_size = Popup().width/5) , 
            size_hint = (0.5, 0.5)
        )

        showPop.open()



    def InvalidLoginPopup(self):
        showPop = Popup(
            title = "Invalid Login", 
            content = Label(text = "Your Email Or Password Is Not Correct", pos_hint = {"x" : 0.25, "top" : 0.8 }, size_hint = (0.5, 0.15), font_size = Popup().width/5) ,
            size_hint = (0.5, 0.5)
        )

        showPop.open()

    def InvalidFormPopup(self):
        showPop = Popup(
            title = "Invalid Form",
            content = Label(text = "Your Email Or Password Is In Invalid Form", pos_hint = {"x" : 0.25, "top" : 0.8 }, size_hint = (0.5, 0.15), font_size = Popup().width/5),
            size_hint = (0.5, 0.5)
        )

        showPop.open()