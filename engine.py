from pyglet.window import key
from pyglet.sprite import Sprite


class Size(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Player(object):
    def __init__(self, x, y, image, batch, windowSize):
        self.windowSize = windowSize

        self.sprite = Sprite(image, x=x, y=y, batch=batch)

        self.halfHeight = image.height / 2
        self.halfWidth = image.width / 2

        self.dx = 0
        self.dy = 0

        self.gravity = -100

        self.key_handler = key.KeyStateHandler()

    def update(self, dt):
        self.dy += self.gravity * dt

        self.sprite.y += self.dy * dt
        self.sprite.x += self.dx * dt

        if self.y - self.halfHeight < 0:
            self.y = 0 + self.halfHeight

        elif self.y + self.halfHeight > self.windowSize.height:
            self.y = self.windowSize.height - self.halfHeight

        if self.key_handler[key.SPACE]:
            self.gravity = -self.gravity