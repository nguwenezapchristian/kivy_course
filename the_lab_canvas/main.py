from kivy.app import App
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.graphics.context_instructions import Color
from kivy.uix.widget import Widget
from kivy.metrics import dp


class ExampleCanvas4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 0)
            Line(points=(100, 50, 100, 150), width=2)
            Color(0, 1, 0)
            Line(ellipse=(50, 150, 100, 50), width=2)
            Color(0,0,1)
            self.rect = Rectangle(pos=(50, 0), size=(100, 50))
    
    def on_click_action(self):
        x, y = self.rect.pos
        x += dp(10)
        self.rect.pos = (x, y)

class TheLabCanvasApp(App):
    pass

TheLabCanvasApp().run()
