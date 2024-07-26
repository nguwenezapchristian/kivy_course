from kivy.app import App
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.properties import Clock


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
        # print(self.rect.pos)
        # print(self.width)
        # if (x + 100) < self.width:
        #     print(x + 100)
        #     x += dp(10)
        #     self.rect.pos = (x, y)
        w, h = self.rect.size
        diff = self.width - (x + w)
        incr = dp(10)
        if diff < incr:
            incr = diff
        x += incr
        self.rect.pos = (x, y)

class ExampleCanvas5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(20)
        self.vx = dp(3)
        self.vy = dp(3)
        with self.canvas:
            self.ball = Ellipse(pos=(self.center), size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/60)
    
    def on_size(self, *args):
        """ Function that is called when the screen size is changed"""
        # print(f"width: {self.width}")
        self.ball.pos = self.center_x - self.ball_size/2, self.center_y - self.ball_size/2
    
    def update(self, dt):
        """ update the pos of the ball """
        x, y = self.ball.pos
        diff_y = self.height - (y+self.ball_size)
        diff_x = self.width - (x+self.ball_size)
        if diff_x < self.vx:
            """ if the ball hits the right of the screen, invert the x velocity"""
            self.vx = - self.vx
        if diff_y < self.vy:
            """ if the ball hits the top of the screen, invert the y velocity"""
            self.vy = - self.vy
        if x < 0:
            """ if the ball hits the left of the screen, invert the x velocity"""
            self.vx = -self.vx
        if y < 0:
            """ if the ball hits the bottom of the screen, invert the y velocity"""
            self.vy = -(self.vy)
        
        x += self.vx
        y += self.vy
        self.ball.pos = (x, y)


class TheLabCanvasApp(App):
    pass

TheLabCanvasApp().run()
