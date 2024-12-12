def circle(radius):
    radius = float(radius)
    if radius <= 0:
        raise TypeError("Radius must be positive")
    return 3.14159 * radius * radius

def square(side):
    side = float(side)
    if side <= 0:
        raise TypeError("Side length must be positive")
    return side * side

def rectangle(length, width):
    length, width = float(length), float(width)
    if length <= 0 or width <= 0:
        raise TypeError("Length and width must be positive")
    return length * width

def triangle(base, height):
    base, height = float(base), float(height)
    if base <= 0 or height <= 0:
        raise TypeError("Base and height must be positive")
    return 0.5 * base * height