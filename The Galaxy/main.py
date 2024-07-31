from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy.properties import Clock
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
from kivy import platform


class MainWidget(Widget):
    from transform import transform, transform_perspective, transform_2D
    from user_actions import keyboard_closed, on_keyboard_down, on_keyboard_up, on_touch_down, on_touch_up
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    vertical_lines = []
    V_NB_LINES = 10
    V_LINE_SPACING = .25  # percentage of the screen width

    horizontal_lines = []
    H_NB_LINES = 15
    H_LINE_SPACING = .1  # percentage of the screen height

    current_offset_y = 0
    SPEED = 4

    current_offset_x = 0
    SPEED_X = 12
    current_speed_x = 0

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print(f"X: {self.width}, Y: {self.height}")
        self.init_vertical_lines()
        self.init_horizontal_lines()

        if self.is_desktop():
            self._keyboard = Window.request_keyboard(
                self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)
        Clock.schedule_interval(self.update, 1.0/60.0)

    def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        return False

    def on_parent(self, *args):
        # print(f"X: {self.width}, Y: {self.height}")
        pass

    def on_size(self, *args):
        # print(f"X: {self.width}, Y: {self.height}")
        # self.perspective_point_x = self.width / 2
        # self.perspective_point_y = self.height * .75
        # self.update_vertical_lines()
        # self.update_horizontal_lines()
        pass

    def on_perspective_point_x(self, widget, value):
        print(f"PX: {str(value)}")

    def on_perspective_point_y(self, widget, value):
        print(f"PY: {str(value)}")

    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            # self.line = Line(points=(100, 0, 100, 100))
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def update_vertical_lines(self):
        # center_x = int(self.width / 2)
        # self.line.points = (self.center_x, 0, self.center_x, 100)
        central_line_x = int(self.width / 2)
        spacing = self.width * self.V_LINE_SPACING
        offset = -int(self.V_NB_LINES/2) + 0.5
        with self.canvas:
            for i in range(0, self.V_NB_LINES):
                x = int(central_line_x + offset * spacing) + \
                    self.current_offset_x  # move to R
                x1, y1 = self.transform(x, 0)
                x2, y2 = self.transform(x, self.height)
                self.vertical_lines[i].points = (
                    x1, y1, x2, y2)
                offset += 1

    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            # self.line = Line(points=(100, 0, 100, 100))
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())

    def update_horizontal_lines(self):
        central_line_x = int(self.width / 2)
        spacing = self.width * self.V_LINE_SPACING
        offset = -int(self.V_NB_LINES/2) + 0.5
        min_x = central_line_x + offset*spacing + self.current_offset_x  # move to R
        max_x = central_line_x - offset*spacing + self.current_offset_x  # move to R
        spacing_y = self.H_LINE_SPACING*self.height
        with self.canvas:
            for i in range(0, self.V_NB_LINES):
                y = 0 + i*spacing_y - self.current_offset_y
                x1, y1 = self.transform(min_x, y)
                x2, y2 = self.transform(max_x, y)
                self.horizontal_lines[i].points = (
                    x1, y1, x2, y2)

    def update(self, dt):
        """ delta time is the time btn function calls
        in this case the time btn update calls"""
        # print(f"dt: {dt*60}, 1/60: {1.0/60.0}")
        time_factor = dt*60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.current_offset_y += self.SPEED * time_factor  # move Down
        spacing_y = self.H_LINE_SPACING*self.height

        if self.current_offset_y >= spacing_y:
            self.current_offset_y -= spacing_y  # move Up

        self.current_offset_x += self.current_speed_x * time_factor  # move to R


class GalaxyApp(App):
    pass


GalaxyApp().run()
