from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.widget import Widget

class LoginPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
        self.companylogo = Image(source = "images\messaging_communication_services.png", size_hint = (0.75,0.75), pos_hint = {"x":0.12, "y":0.45})
        self.add_widget(self.companylogo)

        self.welcomemessage = Label(text = "Welcome to the Future of\n  Secure Communication", font_size = 26, pos_hint = {"y":0.12})
        self.add_widget(self.welcomemessage)

        self.username= TextInput(hint_text = "USERNAME", size_hint = (0.7,0.05), pos_hint = {"x":0.15, "y": 0.45})
        self.add_widget(self.username)

        self.password = TextInput(hint_text = "PASSWORD", size_hint = (0.7,0.05), pos_hint = {"x":0.15, "y": 0.38}, )
        self.add_widget(self.password)

        self.loginbutton = Button(text = "LOGIN", size_hint = (0.5,0.05), pos_hint = {"x":0.25, "y":0.27}, background_color = "#00FF00")
        #self.loginbutton.bind(on_press = RootWidget)
        self.add_widget(self.loginbutton)

        self.signupbutton = Button(text = "SIGNUP", size_hint = (0.5,0.05), pos_hint = {"x":0.25, "y":0.20}, background_color = "#00FF00")
        self.add_widget(self.signupbutton)

class MainScreen(Screen):
        name = StringProperty("MessagingCommunicationServicesLoginPage")

class RootWidget(Widget):
    state = StringProperty('MessagingCommunicationServicesLoginPage')
    screen_manager = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

    def on_state(self, instance, value):
        if value == 'MessagingCommunicationServicesLoginPage':
            self.screen_manager.current = 'MessagingCommunicationServicesLoginPage'

    def set_state(self, state):
        if state == 'MessagingCommunicationServicesLoginPage':
            self.screen_manager.current = 'MessagingCommunicationServicesSignUpPage'

class MessagingCommunicationServicesApp(App):
    def build(self):
        return LoginPage()

MessagingCommunicationServicesApp().run()
