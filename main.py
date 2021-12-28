import pygame
import pygame_tools as pgt
from segment import Segment

class SegmentSim(pgt.GameScreen):
    '''A simulation of segments following the mouse'''

    BG = pygame.Color('black')
    FG = pygame.Color('white')

    def __init__(self):
        size = pgt.Point(1400, 750)
        super().__init__(
            pygame.display.set_mode(size),
            size
        )
        pygame.display.set_caption('Segments')
        self.segments = []
        self.segments.append(Segment(
            self.window_size // 2,
            100,
            0,
            self.FG,
            3
        ))

    def update(self):
        self.screen.fill(self.BG)
        for seg in self.segments:
            seg.follow(self.get_scaled_mouse_pos())
            seg.update()
            seg.draw(self.screen)

def main():
    '''Driver code'''
    SegmentSim().run()

if __name__ == '__main__':
    main()
