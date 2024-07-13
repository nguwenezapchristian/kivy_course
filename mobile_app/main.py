from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty


class ButtonWidgetExample(GridLayout):
    my_text = StringProperty("1")
    count = 1
    def on_press_func(self):
        """
        This function will be called when the button is pressed"""
        print("I Love Coding")
        self.count += 1
        self.my_text = f"{self.count}"
    def reset_count(self):
        """
        This function will be called when the button is pressed"""
        self.count = 1
        self.my_text = f"{self.count}"
    def on_state_toggle_button(self, toggleButton):
        """
        This function will be called when the button is pressed"""
        print("ToggleButton State: ", toggleButton.state)
        if toggleButton.state == "normal":
            #OFF
            toggleButton.text = "OFF"
        else:
            #ON
            toggleButton.text = "ON"



class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(1, 100):
            # b = Button(text=f"{i}", size_hint=(.1, .1))
            size = dp(100)
            b = Button(text=f"{i}", size_hint=(None, None), size=(size, size))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
    # pass


class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    #     b1 = Button(text="Hello")
    #     b2 = Button(text="World")
    #     b3 = Button(text="!")

    #     self.orientation = "vertical"
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)
    pass

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()

