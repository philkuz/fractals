from fractal import Fractal
import random
import math

class Mandelbrot(Fractal):
    """ A class that generates the mandelbrot fractal """
    def __init__(self, w=512, h=512, real_bounds=(-2.0, 1.0), imag_bounds=(-1.5, 1.5), iterations=512):
        Fractal.__init__(self, w, h)
        self.rb = real_bounds
        self.ib = imag_bounds
        self.threshold = abs(max(real_bounds + imag_bounds, key = lambda x: abs(x)))
        self.iterations = iterations
    def render(self):
        """ Renders the mandelbrot set on pixel_mat
        >>> m = Mandelbrot()
        >>> m.render()
        """
        Fractal.render(self)
        lutx = [j * (self.rb[1] - self.rb[0]) / (self.w - 1) + self.rb[0] for j in xrange(self.w)]
        for y in xrange(self.h):
            cy = y * (self.ib[1] - self.ib[0]) / (self.h - 1)  + self.ib[0]
            for x in xrange(self.w):
                c = complex(lutx[x], cy)
                iters = self.in_mandelbrot(0, c)
                if iters > 0:
                    self.set_point(x, y, iters)
    def in_mandelbrot(self, z, c):
        """ Returns whether a point C lies in the mandelbrot set """
        for i in xrange(self.iterations):
            if abs(z) > self.threshold:
                return i
            z = z * z + c
        return -1
    def cardioid_test(self, z):
        """ Returns whether a point is within the cardioid """
        x = z.real
        y = z.imag
        q = math.pow(x- 0.25, 2) + math.pow(y, 2)
        return q * (q + x - 0.25) < 0.25 * math.pow(y, 2)

    def sample_point(self):
        """ Samples the complex plane"""
        z = complex(0, 0)
        while self.cardioid_test(z):
            x = random.randint(0, self.w - 1)
            y = random.randint(0, self.h - 1)
            z = self.image_to_complex(x, y)
        return z
    def complex_to_image(self, z):
        """ Returns the complex number's position in the image """
        x = int((z.real - self.rb[0]) / (self.rb[1] - self.rb[0]) * float(self.w - 1))
        y = int((z.imag - self.ib[0]) / (self.ib[1] - self.ib[0]) * float(self.h - 1))

        return x, y
    def image_to_complex(self, x, y):
        """ Returns the complex number of the coordinate in the image. """
        real = x * (self.rb[1] - self.rb[0]) / float(self.w - 1) + self.rb[0]
        imag = y * (self.ib[1] - self.ib[0]) / float(self.h - 1) + self.ib[0]
        return complex(real, imag)
