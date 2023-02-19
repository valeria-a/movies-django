from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, units):
        self._units = units

    @abstractmethod
    def area(self):
        raise NotImplemented()


class Colored:

    # def __init__(self, color):
    #     self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

# class Rectangle(Shape, ABC):
#     pass

class Triangle(Shape, Colored):

    def area(self):
        pass

    def __init__(self, sides: list, units):
        super().__init__(units)
        self._sides = sides

if __name__ == '__main__':
    t = Triangle([1,2,3], 'mm')
    t.set_color('red')
    print(t.get_color())
