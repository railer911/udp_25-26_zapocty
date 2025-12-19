from abc import abstractmethod, ABC
from math import sqrt


class AGO(ABC):
    def __init__(self, color: str, width: int, layer: int):
        self._color: str = color
        self._width: int = width
        self._layer: int = layer

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str) -> None:
        self._color = color

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width: int) -> None:
        self._width = width

    @property
    def layer(self) -> int:
        return self._layer

    @layer.setter
    def layer(self, layer: int) -> None:
        self._layer = layer

    @abstractmethod
    def print(self) -> None:
        pass

    @abstractmethod
    def length(self) -> float:
        pass


class Point2D:
    def __init__(self, x: int, y: int):
        self._x: int = x
        self._y: int = y

    @property
    def pos(self) -> tuple[int, int]:
        return self._x, self._y

    @pos.setter
    def pos(self, pos: tuple[int, int]) -> None:
        self._x, self._y = pos

    def print_pos(self) -> None:
        print("Point coords:", self.pos)


class Point(Point2D, AGO):
    def __init__(self, x: int, y: int, color: str, width: int, layer: int):
        Point2D.__init__(self, x, y)
        AGO.__init__(self, color, width, layer)

    def print(self) -> None:
        self.print_pos()

    def length(self) -> float:
        return 0.0


class PolyLine(AGO):
    def __init__(self, point_a: Point2D, point_b: Point2D, color: str, width: int, layer: int):
        self._point_a: Point2D = point_a
        self._point_b: Point2D = point_b
        AGO.__init__(self, color, width, layer)

    def print(self) -> None:
        print("Line points:")
        self._point_a.print_pos()
        self._point_b.print_pos()

    def length(self) -> float:
        a = self._point_a.pos
        b = self._point_b.pos
        xes = abs(a[0] - b[0])
        yes = abs(a[1] - b[1])

        return sqrt(xes ** 2 + yes ** 2)


class Polygon(AGO):
    def __init__(self, lines: list[PolyLine], color: str, width: int, layer: int):
        self._lines: list[PolyLine] = lines
        AGO.__init__(self, color, width, layer)

    def print(self) -> None:
        print("Polygon lines:")

        for line in self._lines:
            line.print()

        print()

    def length(self) -> float:
        result: float = 0.0
        for line in self._lines:
            result += line.length()

        return result


def main():
    print("point_1")
    point_1 = Point(1, 2, "black", 1, 1)
    print(point_1.length())
    point_1.print()
    print()

    print("point_2")
    point_2 = Point(3, 4, "red", 7, 6)
    print(point_2.length())
    point_2.print()
    print()

    print("point_2d_1")
    point_2d_1 = Point2D(14, 88)
    point_2d_1.print_pos()
    print()

    print("point_2d_2")
    point_2d_2 = Point2D(67, 69)
    point_2d_2.print_pos()
    print()

    print("polyline_1")
    polyline_1 = PolyLine(point_2d_1, point_2, "crimson", 5, 1)
    print(round(polyline_1.length(), 4))
    polyline_1.print()
    print()

    print("polyline_2")
    polyline_2 = PolyLine(point_2, point_1, "blue", 10, 3)
    print(round(polyline_2.length(), 4))
    polyline_2.print()
    print()

    print("polyline_3")
    polyline_3 = PolyLine(point_1, point_2d_1, "gray", 1488, 88)
    print(round(polyline_3.length(), 4))
    polyline_3.print()
    print()

    print("polygon")
    polygon = Polygon([polyline_1, polyline_2, polyline_3], "brown", 10, 3)
    print(round(polygon.length(), 4))
    polygon.print()
    print()


if __name__ == "__main__":
    main()
