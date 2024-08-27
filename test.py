class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        return a + b > c or a + c > b or b + c > a

    def display(self):
        return f"Triagle size -> {a}|{b}|{c}"

    def perimetr(self):
        return a+b+c

    def _type(self):
        if self.a == self.b == self.c:
            return "Equilateral Triangle"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "Isosceles Triangle"
        return "Scalene Triangle"

    ...



