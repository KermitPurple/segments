import pygame, math
import pygame_tools as pgt

class Segment: # forward declaration
    pass

class Segment:
    '''A line segment'''

    def __init__(
        self,
        start: pgt.Point,
        length: float,
        theta: float,
        color: pgt.Color,
        width: int = 1
    ):
        self.start = start
        self.length = length
        self.theta = theta
        self.calc_end()
        self.color = color
        self.width = width

    def follow(self, target: pgt.Point):
        '''Move start and end while retaining length'''
        x, y = diff = target - self.start
        self.theta = math.atan2(y, x)
        mag = math.sqrt(diff.x ** 2 + diff.y ** 2)
        diff *= -self.length / mag
        self.start = target + diff

    def calc_end(self):
        '''Calculate the position of the end Point'''
        self.end = self.start + (
            self.length * math.cos(self.theta),
            self.length * math.sin(self.theta)
        )

    def update(self):
        self.calc_end()

    def draw(self, screen: pygame.Surface):
        '''Draw a segment to the screen'''
        pygame.draw.line(
            screen,
            self.color,
            self.start,
            self.end,
            self.width
        )
