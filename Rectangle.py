class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        result = self.width * self.length
        return result
    
    def perimeter(self):
        result = 2 * (self.width * self.length)
        return result
    
    def display(self):
        print(f"Rong : {self.width},  Dai: {self.length}, Chu vi: {self.perimeter()}, Dien tich: {self.area()}")
        