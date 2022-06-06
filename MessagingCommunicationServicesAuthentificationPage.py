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

        self.authentificationmessage = Label(text = "We need to verify\nyour phone number to set\nup your account", font_size = 26, pos_hint = {"y":0.12})
        self.add_widget(self.authentificationmessage)

        self.locationcode= TextInput(hint_text = "Code", size_hint = (0.15,0.05), pos_hint = {"x":0.15, "y": 0.45})
        self.add_widget(self.locationcode)

        self.phonenumber= TextInput(hint_text = "Phone number", size_hint = (0.5,0.05), pos_hint = {"x":0.32, "y": 0.45})
        self.add_widget(self.phonenumber)

        self.nextbutton = Button(text = "Next", size_hint = (0.5,0.05), pos_hint = {"x":0.25, "y":0.35}, background_color = "#00FF00")
        self.add_widget(self.nextbutton)

class MessagingCommunicationServicesAuthentificationPageApp(App):
    def build(self):
        return FloatGridLayout()

MessagingCommunicationServicesAuthentificationPageApp().run()