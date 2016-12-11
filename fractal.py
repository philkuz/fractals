import namer
import matplotlib.pyplot as plt
import numpy as np

def andy_cs(i):
    ''' Color Scheme provided by Andrew Lewis '''
    r = i % 4 * 64
    g = i % 8 * 32
    b = i % 16 * 16
    return r, g, b
class Fractal:
    """
    A general class that contains all necessary methods
    for generating fractals
    TODO: lookup what's a good abstract method way in python
    """
    def __init__(self, w, h):
        self.pixel_mat = np.zeros((h, w))
        self.setup()
    def setup(self):
        ''' Used as a way to initialize instance variables without
        having to recreate a constructor '''
        pass
    def render(self):
        self.pixel_mat = np.zeros(self.pixel_mat.shape)

    def width(self):
        return self.pixel_mat.shape[0]
    def height(self):
        return self.pixel_mat.shape[1]

    def in_image(self, x, y):
        return x >= 0 and x < self.width() and y >= 0 and y < self.height()
    def set_point(self, x, y, value):
        self.pixel_mat[x,y] = value
    def get_point(self, x, y):
        return self.pixel_mat[x,y]

    def draw(self, image_name, colorFn=andy_cs):
        """ Draws the intensity values given by pixel_mat
        using the coloration described in colorFn, then saves
        the new image as image_name """
        image = colorFn(self.pixel_mat) # TODO make color fn work for numpy
        file_name = namer.get_name(image_name)
        plt.savefig(file_name)

    def print_matrix(self):
        """ Shorthand to nicely print out the rows of a matrix """
        print(self.pixel_mat)
