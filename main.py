class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def __is_valid_color(self, r, g, b):
        if (isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and
                0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def __is_valid_sides(self, *sides):
        for i in sides:
            if not (isinstance(i, int) and i > 0 and i == self.sides_count):
                return False
        return True

    def __len__(self):
        return sum(self.__sides)
    
    def about(self):
        print(self.__sides)
        print(self.__color)
        print(self.filled)


f1 = Figure(6, [15, 45, 132], True)
f1.about()
print(f1.get_color())
f1.set_color(2, 31, 154)
print(f1.get_color())
