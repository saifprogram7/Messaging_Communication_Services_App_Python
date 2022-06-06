from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

class Signupform(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.companylogo = Image(source = "images\messaging_communication_services.png", size_hint = (0.75,0.75), pos_hint = {"x":0.12, "y":0.45})
        self.add_widget(self.companylogo)

        self.signupmessage = Label(text = "Fill out the form below\nTo signup to secure\ncommunication", font_size = 26, pos_hint = {"y":0.12})
        self.add_widget(self.signupmessage)

        self.name= TextInput(hint_text = "Name", size_hint = (0.7,0.05), pos_hint = {"x":0.15, "y": 0.45})
        self.add_widget(self.name)

        self.phonenumber = TextInput(hint_text = "Phone Number", size_hint = (0.7,0.05), pos_hint = {"x":0.15, "y": 0.38})
        self.add_widget(self.phonenumber)

        self.email= TextInput(hint_text = "Email", size_hint = (0.7,0.05), pos_hint = {"x":0.15, "y": 0.31})
        self.add_widget(self.email)

        self.password = TextInput(hint_text = "Password", size_hint = (0.7,0.05), pos_hint = {"x":0.15, "y": 0.24})
        self.add_widget(self.password)

        self.nextbutton = Button(text = "Next", size_hint = (0.5,0.05), pos_hint = {"x":0.25, "y":0.15}, background_color = "#00FF00")
        self.add_widget(self.nextbutton)

class MessagingCommunicationServicesSignUpPageApp(App):
    def build(self):
        return Signupform()

if __name__ == '__main__':
    MessagingCommunicationServicesSignUpPageApp().run()