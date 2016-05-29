from fractal import Fractal
from mandelbrot import Mandelbrot

import random, math

class Buddhabrot(Mandelbrot):
    """ Buddhabrot implementation
    >>> b = Buddhabrot()
    >>> b.render()
    """
    def __init__(self, w=512, h=512, real_bounds=(-2.0, 1.0), imag_bounds=(-1.5, 1.5), iterations=512, min_path=0):
        Mandelbrot.__init__(self, w, h, real_bounds, imag_bounds, iterations)
        self.min_path = min_path
        self.max = 0
        self.samples = 0
    def set_samples(self, n):
        self.samples = n
    def increment_box(self, z):
        x, y = self.complex_to_image(z)
        if not self.in_image(x, y):
            return
        self.set_point(x, y, self.get_point(x, y) + 1)
    def set_point(self, x, y, value):
        Mandelbrot.set_point(self, x, y, value)
        if value > self.max:
            self.max = value
    def get_pixel_value(self, x, y):
        ''' Returns a normalized pixel value for this image '''
        if self.max == 0:
            return 0
        else:
            return int(float(self.get_point(x, y)) / self.max * 255)
    def render(self):
        Fractal.render(self)
        if not self.samples:
            self.set_samples(int(0.5 * self.w * self.h))
        for _ in xrange(self.samples):
            c = self.sample_point()
            n, path = self.in_mandelbrot(c)
            if n > self.min_path:
                self.draw_trajectory(path)
    def draw_trajectory(self, path):
        for z in path: self.increment_box(z)
    def in_mandelbrot(self, c, z=0):
        """ Returns whether a point C lies in the mandelbrot set """
        path = []
        for i in xrange(self.iterations):
            path.append(z)
            if abs(z) > self.threshold:
                return i, path
            z = z * z + c
        return 0, []
    def print_parameters(self):
        Mandelbrot.print_parameters(self)
        print "\tsamples:\t", self.samples
        print "\tmin path:\t", self.min_path
def atan_color(i, width=10):
    ''' Returns a clamped color for any input based on the arctan function '''
    r= int(255 * math.atan(float(i)/width))
    return r
b = Buddhabrot(iterations=50000, min_path=500)
b.render()

b.draw("buddha", lambda i : (atan_color(i), atan_color(i), atan_color(i)))
b.print_parameters()
