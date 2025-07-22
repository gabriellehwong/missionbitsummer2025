from PIL import Image, ImageDraw
import pprint
import random

class ArtElement:
    def __init__(self, attributes):
        self.attributes = attributes

    def draw(self, draw_context):
        shape = self.attributes['shape']
        x, y = self.attributes['position']
        size = self.attributes['size']
        color = self.attributes['color']
        if self.attributes['shape'] == "circle":
            draw_context.ellipse([(x - size, y - size), (x + size, y + size)], fill=color)
        if self.attributes['shape'] == "square":
            draw_context.rectangle((x, y, x + size, y + size), fill=color)

    def __str__(self):
        return pprint.pformat(self.attributes)

class Canvas:
    def __init__(self, width, height, background_color):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.elements = []
        self.image = Image.new("RGB", (width, height), background_color)

    def add_element(self, element):
        self.elements.append(element)

    def render(self):
        draw = ImageDraw.Draw(self.image)
        for element in self.elements:
            element.draw(draw)
        self.image.show()
        self.image.save("generative_art.png")

    def __str__(self):
       return pprint.pformat(f"{str(self.width)}, {str(self.height)}, {str(self.bg_color)}")

def main():
    canvas = Canvas(500, 500, (255, 255, 255))
    for _ in range(50):
        attributes = {
            'shape': "circle",
            'position': (random.randint(20, 380), random.randint(20, 380)),
            'size': random.randint(10, 40),
            'color': (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        }
        circle = ArtElement(attributes)
        canvas.add_element(circle)
    for _ in range(50):
        attributes = {
            'shape': "square",
            'position': (random.randint(20, 380), random.randint(20, 380)),
            'size': random.randint(10, 40),
            'color': (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        }
        square = ArtElement(attributes)
        canvas.add_element(square)
    canvas.render()

main()