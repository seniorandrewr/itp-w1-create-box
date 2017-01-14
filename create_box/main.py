"""This is the entry point of the program."""


def create_box(height, width, character):
    s = ''
    for i in range(height):
        for i in range(width):
            s += character
        s += '\n'
    return s


if __name__ == '__main__':
    create_box(3, 4, '*')