from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image

class FloatGridLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.banner = Button(text = "", size_hint = (1, 0.1), pos_hint = {"y":0.9}, background_color = "blue")
        self.add_widget(self.banner)
        
        self.backbutton = Button(text = "<-", size_hint = (0.15, 0.05), background_color = "blue", font_size = 38, pos_hint = {"x": 0.05,"y": 0.925})
        self.add_widget(self.backbutton)

        self.charactername = Label(text = "John Smith", font_size = 22, pos_hint = {"y":0.45})
        self.add_widget(self.charactername)

        self.groupicon = Image(source = "images\groupicon.png", size_hint = (0.15,0.15), pos_hint = {"x":0.80, "y":0.875})
        self.add_widget(self.groupicon)

        self.chatbox = Button(text = "", size_hint = (1, 0.9))
        self.add_widget(self.chatbox)

        self.banner = Button(text = "", size_hint = (1, 0.1), background_color = "blue")
        self.add_widget(self.banner)

        self.addbutton = Button(text = "+", size_hint = (0.15,0.05), pos_hint = {"x": 0.05, "y":0.025})
        self.add_widget(self.addbutton)
        
        self.messagebox = TextInput(hint_text = "Enter your Message", size_hint = (0.45, 0.05), pos_hint = {"x": 0.25, "y":0.025})
        self.add_widget(self.messagebox)

        self.submitbutton = Button(text = "Send", size_hint = (0.15,0.05), pos_hint = {"x": 0.75, "y":0.025})
        self.add_widget(self.submitbutton)

class MessagingCommunicationServicesJohnSmithChatBoxPageApp(App):
    def build(self):
        return FloatGridLayout()

MessagingCommunicationServicesJohnSmithChatBoxPageApp().run()