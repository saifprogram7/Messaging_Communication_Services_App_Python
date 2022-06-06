from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class FloatGridLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.companylogo = Image(source = "images\messaging_communication_services.png", size_hint = (0.75,0.75), pos_hint = {"x":0.12, "y":0.45})
        self.add_widget(self.companylogo)

        self.setupmessage = Label(text = "Lets set up your account", font_size = 26, pos_hint = {"y":0.12})
        self.add_widget(self.setupmessage)

        self.profilepicture = Image(source = "images\character.png", size_hint = (0.25, 0.25), pos_hint = {"x":0.1 , "y":0.35})
        self.add_widget(self.profilepicture)

        self.profilename= TextInput(hint_text = "Profile Name", size_hint = (0.5,0.05), pos_hint = {"x":0.38, "y": 0.45})
        self.add_widget(self.profilename)

        self.nextbutton = Button(text = "Next", size_hint = (0.5,0.05), pos_hint = {"x":0.30, "y":0.30}, background_color = "#00FF00")
        self.add_widget(self.nextbutton)

class MessagingCommunicationServicesProfileSetUpPageApp(App):
    def build(self):
        return FloatGridLayout()

MessagingCommunicationServicesProfileSetUpPageApp().run()