from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class FloatGridLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.box= Button(text = "", background_color = "#0000FF", size_hint = (1,0.1), pos_hint = {"y":0.9})
        self.add_widget(self.box)

        self.iconimage = Image(source = "images\icon.png", size_hint = (0.15,0.15), pos_hint = {"x":0.02, "y":0.875})
        self.add_widget(self.iconimage)

        self.pagename = Label(text = "Chat", font_size = 25, pos_hint = {"y":0.455})
        self.add_widget(self.pagename)

        self.groupicon = Image(source = "images\groupicon.png", size_hint = (0.15,0.15), pos_hint = {"x":0.80, "y":0.875})
        self.add_widget(self.groupicon)

        self.userone = Button(text = "", size_hint = (1,0.1), pos_hint = {"y":0.8})
        self.add_widget(self.userone)

        self.profilepictureuserone = Image(source = "images\character.png", size_hint = (0.17, 0.17), pos_hint = {"x":0.03 , "y":0.765})
        self.add_widget(self.profilepictureuserone)

        self.characterone = Label(text = "John Smith", font_size = 20, pos_hint = {"x":0.03, "y":0.37})
        self.add_widget(self.characterone)

        self.characteroneconversation = Label(text = "Conversation", font_size = 15, pos_hint = {"x":0.03, "y":0.33})
        self.add_widget(self.characteroneconversation)

        self.usertwo = Button(text = "", size_hint = (1,0.1), pos_hint = {"y":0.7})
        self.add_widget(self.usertwo)

        self.profilepictureusertwo = Image(source = "images\character.png", size_hint = (0.17, 0.17), pos_hint = {"x":0.03 , "y":0.665})
        self.add_widget(self.profilepictureusertwo)

        self.charactertwo = Label(text = "Sam Jake", font_size = 20, pos_hint = {"x":0.03, "y":0.27})
        self.add_widget(self.charactertwo)

        self.charactertwoconversation = Label(text = "Conversation", font_size = 15, pos_hint = {"x":0.03, "y":0.23})
        self.add_widget(self.charactertwoconversation)

        self.userthree = Button(text = "", size_hint = (1,0.1), pos_hint = {"y":0.6})
        self.add_widget(self.userthree)

        self.profilepictureuserthree = Image(source = "images\character.png", size_hint = (0.17, 0.17), pos_hint = {"x":0.03 , "y":0.565})
        self.add_widget(self.profilepictureuserthree)

        self.characterthree = Label(text = "Dextor Nikolas", font_size = 20, pos_hint = {"x":0.03, "y":0.17})
        self.add_widget(self.characterthree)

        self.characterthreeconversation = Label(text = "Conversation", font_size = 15, pos_hint = {"x":0.03, "y":0.13})
        self.add_widget(self.characterthreeconversation)

        self.userfour = Button(text = "", size_hint = (1,0.1), pos_hint = {"y":0.5})
        self.add_widget(self.userfour)

        self.profilepictureuserfour = Image(source = "images\character.png", size_hint = (0.17, 0.17), pos_hint = {"x":0.03 , "y":0.465})
        self.add_widget(self.profilepictureuserfour)

        self.characterfour = Label(text = "Carson Jake", font_size = 20, pos_hint = {"x":0.03, "y":0.07})
        self.add_widget(self.characterfour)

        self.characterfourconversation = Label(text = "Conversation", font_size = 15, pos_hint = {"x":0.03, "y":0.03})
        self.add_widget(self.characterfourconversation)

        self.userfive = Button(text = "", size_hint = (1,0.1), pos_hint = {"y":0.4})
        self.add_widget(self.userfive)

        self.profilepictureuserfive = Image(source = "images\character.png", size_hint = (0.17, 0.17), pos_hint = {"x":0.03 , "y":0.365})
        self.add_widget(self.profilepictureuserfive)

        self.characterfive = Label(text = "Tory Hayes", font_size = 20, pos_hint = {"x":0.03, "y":-0.03})
        self.add_widget(self.characterfive)

        self.characterfiveconversation = Label(text = "Conversation", font_size = 15, pos_hint = {"x":0.03, "y":-0.07})
        self.add_widget(self.characterfiveconversation)

        self.usersix = Button(text = "", size_hint = (1,0.1), pos_hint = {"y":0.4})
        self.add_widget(self.usersix)

        self.profilepictureusersix = Image(source = "images\character.png", size_hint = (0.17, 0.17), pos_hint = {"x":0.03 , "y":0.365})
        self.add_widget(self.profilepictureusersix)

        self.charactersix = Label(text = "Ajaz Ali", font_size = 20, pos_hint = {"x":0.03, "y":-0.03})
        self.add_widget(self.charactersix)

        self.charactersixconversation = Label(text = "Conversation", font_size = 15, pos_hint = {"x":0.03, "y":-0.07})
        self.add_widget(self.charactersixconversation)

        self.userseven = Button(text = "", size_hint = (1,0.1), pos_hint = {"y":0.4})
        self.add_widget(self.userseven)

        self.profilepictureuserseven = Image(source = "images\character.png", size_hint = (0.17, 0.17), pos_hint = {"x":0.03 , "y":0.365})
        self.add_widget(self.profilepictureuserseven)

        self.characterseven = Label(text = "Tory Hayes", font_size = 20, pos_hint = {"x":0.03, "y":-0.03})
        self.add_widget(self.characterseven)

        self.charactersevenconversation = Label(text = "Conversation", font_size = 15, pos_hint = {"x":0.03, "y":-0.07})
        self.add_widget(self.charactersevenconversation)

        self.usereight = Button(text = "", size_hint = (1,0.1), pos_hint = {"y":0.3})
        self.add_widget(self.usereight)

        self.profilepictureusereight = Image(source = "images\character.png", size_hint = (0.17, 0.17), pos_hint = {"x":0.03 , "y":0.265})
        self.add_widget(self.profilepictureusereight)

        self.charactereight = Label(text = "Omar Elvin", font_size = 20, pos_hint = {"x":0.03, "y":-0.13})
        self.add_widget(self.charactereight)

        self.charactereightconversation = Label(text = "Conversation", font_size = 15, pos_hint = {"x":0.03, "y":-0.17})
        self.add_widget(self.charactereightconversation)

        self.usernine = Button(text = "", size_hint = (1,0.1), pos_hint = {"y":0.2})
        self.add_widget(self.usernine)

        self.profilepictureusernine = Image(source = "images\character.png", size_hint = (0.17, 0.17), pos_hint = {"x":0.03 , "y":0.165})
        self.add_widget(self.profilepictureusernine)

        self.characternine = Label(text = "Eddy Owen", font_size = 20, pos_hint = {"x":0.03, "y":-0.23})
        self.add_widget(self.characternine)

        self.characternineconversation = Label(text = "Conversation", font_size = 15, pos_hint = {"x":0.03, "y":-0.27})
        self.add_widget(self.characternineconversation)

        self.userten = Button(text = "", size_hint = (1,0.1), pos_hint = {"y":0.1})
        self.add_widget(self.userten)

        self.profilepictureuserten = Image(source = "images\character.png", size_hint = (0.17, 0.17), pos_hint = {"x":0.03 , "y":0.065})
        self.add_widget(self.profilepictureuserten)

        self.characterten = Label(text = "Frank Edward", font_size = 20, pos_hint = {"x":0.03, "y":-0.33})
        self.add_widget(self.characterten)

        self.charactertenconversation = Label(text = "Conversation", font_size = 15, pos_hint = {"x":0.03, "y":-0.37})
        self.add_widget(self.charactertenconversation)

        self.box= Button(text = "", background_color = "#0000FF", size_hint = (1,0.1))
        self.add_widget(self.box)
        
        self.icons = Image(source = "images\icons.png", pos_hint = {"y":-0.45})
        self.add_widget(self.icons) 

class MessagingCommunicationServicesMainInterfacePageApp(App):
    def build(self):
        return FloatGridLayout()

MessagingCommunicationServicesMainInterfacePageApp().run()