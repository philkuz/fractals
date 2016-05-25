from mandelbrot import Mandelbrot
import random
class Julia(Mandelbrot):
    """ Julia implementation in the fractal library
    >>> j = Julia()
    >>> j.render()
    """
    def render(self):
        c = complex(random.random() * 2.0 - 1.0, random.random() - 0.5)
        lutx = [j * (self.rb[1] - self.rb[0]) / (self.w - 1) + self.rb[0] for j in xrange(self.w)]
        for y in xrange(self.h):
            cy = y * (self.ib[1] - self.ib[0]) / (self.h - 1)  + self.ib[0]
            for x in xrange(self.w):
                z = complex(lutx[x], cy)
                iters = self.in_mandelbrot(z, c)
                if iters > 0:
                    self.set_point(x, y, iters)
