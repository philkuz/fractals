from PIL import Image
from buddhabrot import Buddhabrot, atan_color
import namer
class Nebulabrot:
    ''' A rendering of a nebulabrot utilizing a similar api as
    Fractals, except using three buddha renderings instead of a single one.
    '''
    def __init__(self, w=512, h=512, real_bounds=(-2.0, 1.0), imag_bounds=(-1.5, 1.5), iterations=512, min_path=0):
        self.w = w
        self.h = h
        self.rb = real_bounds
        self.ib = imag_bounds
        self.threshold = abs(max(real_bounds + imag_bounds, key = lambda x: abs(x)))
        self.iterations = iterations
        self.min_path = min_path
        # buddhas represent buddhabrot rendering for each color
        self.buddhas = [Buddhabrot(w, h, real_bounds, imag_bounds, iterations, min_path) for _ in range(3)]

    def render(self):
        for buddha in self.buddhas:
            buddha.render()
    def draw(self, image_name, colorFn=None):
        """ Draws the intensity values given by pixel_mat
        using the coloration described in colorFn, then saves
        the new image as image_name """
        image = Image.new("RGB", (self.w, self.h))
        mtx = image.load()
        for x in range(self.w):
            for y in range(self.h):
                mtx[x, y] = tuple([atan_color(b.get_point(x, y)) for b in self.buddhas])

        file_name = namer.get_name(image_name)
        image.save(file_name, "PNG")
    # def draw_buddhas(self, image_name):
    #     for b in self.buddhas:
    #         b.draw(image_name, colorFn

n = Nebulabrot(iterations=50000, min_path=500)
n.render()
n.draw("nebula")
