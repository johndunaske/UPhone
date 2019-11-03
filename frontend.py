from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition,
SlideTransition, CardTransition, SwapTransition,
FadeTransition, WipeTransition, FallOutTransition, RiseInTransition)

class MyScreenManager(ScreenManager):
    pass


class LoginScreen(Screen):
    pass

class CallScreen(Screen):
    pass

class CallScreenData(Screen):
    pass

# def displayCallScreen(a):
#     ## TODO: Add database



class UPhoneApp(App):

    def build(self):
        return MyScreenManager()





if __name__ == '__main__':
    UPhoneApp().run()
