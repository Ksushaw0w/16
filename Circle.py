from classCircle import Rectangle, Square, Circle
# далее создадим два прямоугольника
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
# вывод площади (S) наших двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)
print(square_1.get_area_square(),
      square_2.get_area_square())

сircle_1 = Circle(4)
сircle_2 = Circle(14)
print(сircle_1.get_сircle(),
      сircle_2.get_сircle())

figures = [rect_1, rect_2, square_1, square_2, сircle_1, сircle_2]
for figure in figures:
      if isinstance(figure, Circle):
          print(figure.get_сircle())
      if isinstance(figure, Square):
          print(figure.get_area_square())
      if isinstance(figure, Rectangle):
          print(figure.get_area())
