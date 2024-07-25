import math
class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=True):
        self.__sides = list(sides)
        self.__color = color
        self.filled = filled

    def set_sides(self, *new_sides):
        counter = 0
        for i in new_sides:
            counter += 1
        if counter == self.sides_count:
            self.__sides = list(new_sides)

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
        counter = 0
        for i in sides:
            counter += 1
            if i < 0 and not isinstance(i, int):
                return False
        if counter != self.sides_count:
            return False
        return True

    def __len__(self):
        return sum(self.__sides)

    def about(self):
        print(self.__sides)
        print(self.__color)
        print(self.filled)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides, filled=True,):
        super().__init__(color, sides, filled=True)
        self.__radius = sides[0] // (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2




