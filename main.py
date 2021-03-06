#!/usr/bin/env python3

import pygame
import pygame_tools as pgt
from segment import Segment

class SegmentSim(pgt.GameScreen):
    '''A simulation of segments following the mouse'''

    BG = pygame.Color('black')
    FGs = [
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'indigo',
        'violet'
    ]
    FGs_LEN = len(FGs)

    def __init__(self, number_of_segments: int, segment_length: int, width: int = 3):
        if number_of_segments < 1:
            raise ValueError('There cannot be less than 1 segment')
        size = pgt.Point(1400, 750)
        super().__init__(
            pygame.display.set_mode(size),
            size
        )
        pygame.display.set_caption('Segments')
        self.segments = []
        for i in range(number_of_segments):
            self.segments.append(Segment(
                self.window_size // 2,
                segment_length,
                0,
                self.FGs[(i + 1) % self.FGs_LEN],
                width
            ))

    def update(self):
        self.screen.fill(self.BG)
        prev = None
        for seg in self.segments:
            if prev is None:
                seg.follow(self.get_scaled_mouse_pos())
            else:
                seg.follow(prev.start)
            seg.update()
            seg.draw(self.screen)
            prev = seg

    def key_down(event: pygame.event.Event):
        if event.unicode == 'q':
            exit(0)

def main():
    '''Driver code'''
    SegmentSim(150, 10).run()

if __name__ == '__main__':
    main()
