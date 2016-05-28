from mandelbrot import Mandelbrot
import random
class Buddhabrot(Mandelbrot):
    """ Buddhabrot implementation
    >>> b = Buddhabrot()
    >>> b.render()
    """
    def setup(self):
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
        if not self.samples:
            self.set_samples(int(0.5 * self.w * self.h))
        for _ in xrange(self.samples):
            c = self.sample_point()
            n, path = self.in_mandelbrot(c)
            if n:
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
def buddha_color(i):
 ''' Returns a clamped color for any input based on the arctan function '''
  r= int(255 * math.atan(float(i)/ 10))
  return r
