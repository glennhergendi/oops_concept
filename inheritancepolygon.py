class polygon:
    def __init__(self, sides):
        self.sides = sides
    def perimeter(self):
        perimeter = sum(self.sides)
        return perimeter
class quadrilateral(polygon):
    def info(self):
        print('hello this is quadrilateral')

class pentagon(polygon):
    def info(self):
        print("hello this is pentagon")

quadobj = quadrilateral([3,6,7,9])
pentobj = pentagon([2,4,6,8,10])

peri = quadobj.perimeter()
peripent = pentobj.perimeter()

print("the perimeter is", peri)
print("the perimeter is", peripent)