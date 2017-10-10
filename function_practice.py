def make_greeting1():
    """
        This Function Says Hello.
        It Takes No parameters
        and returns the string hello
    """
    return "hello"


def make_greeting2(greeting):
    """
        This function says Hello.
        It Takes one string argument and
        returns the string.
    """
    return greeting


def make_greeting3():
    greeting = input("Please type a greeting: ")

    return greeting


def get_triangle_area(base, height):
    area = base * height * 0.5
    return "The area of this triangle is " + str(area)


def get_rectangle_area(length, width):
    return "The area of this rectangle is " + str(length * width)


def get_circle_area(radius):
    PI = 3.14159265359
    area = PI * radius
    return "The area of this circle is {}".format(area)


def general_get_area(shape, **kwargs):

    if shape == "rectangle":
        length = kwargs.pop('length')
        width = kwargs.pop('width')
        return get_rectangle_area(length, width)

    elif shape == "circle":
        radius = kwargs.pop('radius')
        return get_circle_area(radius)
    elif shape == "triangle":
        base = kwargs.pop('base')
        height = kwargs.pop('height')
        return get_triangle_area(base, height)