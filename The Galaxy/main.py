from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line

class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    vertical_lines = []
    NB_LINES = 7
    LINE_SPACING = .1  #percentage of the screen width


    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        #print(f"X: {self.width}, Y: {self.height}")
        self.init_vertical_lines()

    
    def on_parent(self, *args):
        # print(f"X: {self.width}, Y: {self.height}")
        pass

    def on_size(self, *args):
        # print(f"X: {self.width}, Y: {self.height}")
        # self.perspective_point_x = self.width / 2
        # self.perspective_point_y = self.height * .75
        self.update_vertical_lines()
    
    def on_perspective_point_x(self, widget, value):
        print(f"PX: {str(value)}")
    
    def on_perspective_point_y(self, widget, value):
        print(f"PY: {str(value)}")

    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            # self.line = Line(points=(100, 0, 100, 100))
            for i in range(0, self.NB_LINES):
                self.vertical_lines.append(Line())


    def update_vertical_lines(self):
        # center_x = int(self.width / 2)
        # self.line.points = (self.center_x, 0, self.center_x, 100)
        central_line_x = int(self.width / 2)
        spacing = self.width * self.LINE_SPACING
        offset = -int(self.NB_LINES/2)
        with self.canvas:
            for i in range(0, self.NB_LINES):
                x = int(central_line_x + offset * spacing)
                x1, y1 = self.transform(x, 0)
                x2, y2 = self.transform(x, self.height) 
                self.vertical_lines[i].points = (
                    x1, y1, x2, y2)
                offset += 1
    
    def transform(self, x, y):
        # return self.transform_2D(x, y)
        return self.transform_perspective(x, y)
    
    def transform_2D(self, x, y):
        return int(x), int(y)
    
    def transform_perspective(self, x, y):
        tr_y = y * self.perspective_point_y / self.height
        if tr_y > self.perspective_point_y:
            tr_y = self.perspective_point_y

        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - tr_y
        factor_y = diff_y / self.perspective_point_y # equal 1 if perspective_y == dff_y, 0 if dff_y == 0
        tr_x = self.perspective_point_x + diff_x*factor_y
        return int(tr_x), int(tr_y)

class GalaxyApp(App):
    pass

GalaxyApp().run()