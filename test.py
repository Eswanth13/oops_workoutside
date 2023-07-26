class Mathfun:
    def square(self, num):
        return num ** 2

    def cube(self, num):
        return num ** 3

class Area(Mathfun):

    pi = 3.14

    def circle(self, radious):
        return self.pi * self.square(radious)

    def cylinder(self, radious, height):
        return (2 * self.pi * radious * height) + self.pi * self.square(radious)



obj = Area();
print(obj.circle(2))
print(obj.cylinder(2,3))
