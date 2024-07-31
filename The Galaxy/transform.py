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
    factor_y = pow(factor_y, 4)
    tr_x = self.perspective_point_x + diff_x*factor_y
    tr_y = self.perspective_point_y - factor_y*self.perspective_point_y
    return int(tr_x), int(tr_y)