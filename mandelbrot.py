from fractal import Fractal
import random
import numpy as np

class Mandelbrot(Fractal):
    """ A class that generates the mandelbrot fractal """
    def __init__(self, w=512, h=512, real_bounds=(-2.0, 1.0), imag_bounds=(-1.5, 1.5), iterations=512):
        Fractal.__init__(self, w, h)
        self.real_bounds = real_bounds
        self.imag_bounds = imag_bounds
        self.threshold = abs(max(real_bounds + imag_bounds, key = lambda x: abs(x)))
        self.iterations = iterations
        self.update = 5 # TODO make a parm
    def print_parameters(self):
        print("\treal bounds:\t", self.real_bounds)
        print("\timag bounds:\t", self.imag_bounds)
        print("\titerations:\t", self.iterations)
        print("\tthreshold:\t", self.threshold)
    def render(self):
        """ Renders the mandelbrot set into memory
        >>> m = Mandelbrot()
        >>> m.render()
        """
        Fractal.render(self)

        lutx = np.arange(self.width())
        lutx = lutx * (self.real_bounds[1] - self.real_bounds[0]) / (self.width() - 1) + self.real_bounds[0]
        lutx = np.tile(lutx, (self.width(),1)).T

        luty = np.arange(self.height())
        luty = luty * (self.imag_bounds[1] - self.imag_bounds[0]) / (self.height() - 1)  + self.imag_bounds[0]
        luty = np.tile(luty, (self.height(),1))

        lut_mat = lutx + luty * 1j
        iters = self.in_mandelbrot(np.zeros(lut_mat.shape), lut_mat)
        self.set_pixel_mat(iters)

    def set_pixel_mat(self, iters):
        # TODO this may have to be changed if you want to transfrom the pixel.
        # iters are just ierations. May have -1 if the complex point doesn't
        # escape the image
        self.pixel_mat = iters

    def in_mandelbrot(self, z, c):
        """ Returns whether points in the matrix C lie in the mandelbrot set """
        for i in range(self.iterations):
            abs_mask = np.abs(z) < self.threshold
            z[abs_mask] = z[abs_mask] ** 2 + c[abs_mask]
        z[abs_mask] = -1
        return z

    def cardioid_test(self, z):
        """
        Returns whether a matrix of points are within the cardioid of the
        mandelbrot
        """
        x = z.real
        y = z.imag
        q = (x - 0.25) ** 2 + y ** 2
        return q * (q + x - 0.25) < 0.25 * y ** 2

    def sample_point(self):
        """ Samples the complex plane"""
        # TODO make numpy
        z = complex(0, 0)
        while self.cardioid_test(z):
            x = random.randint(0, self.width()- 1)
            y = random.randint(0, self.height() - 1)
            z = self.image_to_complex(x, y)
        return z
    def complex_to_real(self, z):
        # TODO make numpy
        """ Returns the complex number's position in the image """
        x = int((z.real - self.real_bounds[0]) / (self.real_bounds[1] - self.real_bounds[0]) * float(self.width()- 1))
        y = int((z.imag - self.imag_bounds[0]) / (self.imag_bounds[1] - self.imag_bounds[0]) * float(self.height() - 1))

        return x, y
    def real_to_complex(self, x, y):
        # TODO make numpy
        """ Returns the complex number of the coordinate in the image. """
        real = x * (self.real_bounds[1] - self.real_bounds[0]) / float(self.width()- 1) + self.real_bounds[0]
        imag = y * (self.imag_bounds[1] - self.imag_bounds[0]) / float(self.height() - 1) + self.imag_bounds[0]
        return complex(real, imag)
def atan_color(i, width=10):
    ''' Returns a clamped color for any input based on the arctan function '''
    return (255 * np.atan(float(i)/width)).astype(np.int)
if __name__ == "__main__":
    mandel = Mandelbrot(iterations=512 )
    mandel.render()

    mandel.draw("shite")
