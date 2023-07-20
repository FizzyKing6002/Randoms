"""
Main file
"""

import pygame

class Screen:
    def __init__(self):
        self._win = None
        self._title = ""
        self._size = [0, 0]

    def __call__(self, frame_time):
        mouse_state = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        size = [self._win.get_width(), self._win.get_height()]

        self._size = size

        pygame.display.update()

    def boot(self):
        """
        Mirror of __call__ function where frame_time is zero and resize_objects is True
        """

        self._win = pygame.display.set_mode((1200, 880), pygame.RESIZABLE)

        self.make_banana()

    def make_banana(self):
        position = [600, 440]
        accuracy = 5
        flat_edge_accuracy_divs = 25
        flat_edge_low_accuracy_divs = 18
        flat_edge_top_bot_accuracy_divs = 15
        flat_edge_bot_accuracy_divs = 10
        banana_tip_bottom_extra_accuracy_divs = -5
        width = 1000
        height = 350
        banana_h = 170
        k_top = (height - banana_h)/((width / 2)**2)
        k_bot = height/((width / 2)**2)
        m_tip = 0.5
        width_tip = 70

        coords = []
        coords_new = []

        for i in range(flat_edge_top_bot_accuracy_divs, width//accuracy + 1 - flat_edge_accuracy_divs):
            coords.append([i * accuracy + position[0] - (width / 2), -k_top * ((i * accuracy - (width/2))**2) + position[1] + height / 2 - banana_h])

        banana_tip_h = -k_top * (((width//accuracy + 1 - flat_edge_accuracy_divs) * accuracy - (width/2))**2) + position[1] + height / 2 - banana_h
        banana_bot_tip_h = -k_bot * (((width//accuracy + 1 - flat_edge_low_accuracy_divs) * accuracy - (width/2))**2) + position[1] + height / 2

        coord = [(width_tip//accuracy + 1) * accuracy + position[0] + (width / 2) - (flat_edge_accuracy_divs * accuracy), (width_tip//accuracy + 1) * accuracy * -m_tip + banana_tip_h]
        coords.append(coord)
        coord_2 = [(width_tip//accuracy + 1 + banana_tip_bottom_extra_accuracy_divs) * accuracy + position[0] + (width / 2) - (flat_edge_low_accuracy_divs * accuracy), (width_tip//accuracy + 1 + banana_tip_bottom_extra_accuracy_divs) * accuracy * -m_tip + banana_tip_h - (banana_tip_h - banana_bot_tip_h)]
        coords.append(coord_2)


        for i in range(flat_edge_bot_accuracy_divs, width//accuracy + 1 - flat_edge_low_accuracy_divs):
            coords_new.append([i * accuracy + position[0] - (width / 2), -k_bot * ((i * accuracy - (width/2))**2) + position[1] + height / 2])

        coords.extend(reversed(coords_new))
        pygame.draw.polygon(self._win, "yellow", coords)

class Main:
    """
    Main class
    """

    def __init__(self):
        self._obj = Screen()
        self._run = True

        self._clock = pygame.time.Clock()
        self._fps = 0
        self._frame_time = 0

    def boot(self, width, height, title, fps):
        """
        ...
        """

        self._obj.size, self._obj.title, self._fps = ([width, height], title, fps)
        self._obj.boot()

        self.runtime()

    def runtime(self):
        """
        ...
        """

        while self._run:
            self._frame_time = self._clock.tick(self._fps)

            self._obj(self._frame_time)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._run = False

        pygame.quit()

main = Main()

if __name__ == "__main__":
    main.boot(
        1200,           #SCREEN WIDTH
        880,            #SCREEN HEIGHT
        "Banana",        #WINDOW CAPTION
        60,             #FPS
    )
