MODULE 5
class create_rectangle():
    """ A class to manufacture rectangle objects """
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def shift_rectangle(self, dx, dy):
        """ Shift the rectangle by dx units horizontally and dy units vertically """
        self.corner = (self.corner[0] + dx, self.corner[1] + dy)

    def offset_rectangle(self, dx, dy):
        """ Create a new rectangle by shifting the original rectangle by dx units horizontally and dy units vertically """
        new_corner = (self.corner[0] + dx, self.corner[1] + dy)
        return create_rectangle(new_corner, self.width, self.height)

# Example usage:
r1 = create_rectangle((10, 20), 30, 40)
print(str(r1))
r1.shift_rectangle(-10, -20)
print(str(r1))
r2 = r1.offset_rectangle(100, 100)
print(str(r2))