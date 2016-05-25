from fractal import Fractal
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
        lutx = [j * (self.rb[1] - self.rb[0]) / (self.w - 1) + self.rb[0] for j in xrange(self.w)]
        for y in xrange(self.h):
            cy = y * (self.ib[1] - self.ib[0]) / (self.h - 1)  + self.ib[0]
            for x in xrange(self.w):
                c = complex(lutx[x], cy)
                iters = self.in_mandelbrot(0, c)
                if iters > 0:
                    self.set_point(x, y, iters)
    def in_mandelbrot(self, z, c):
        for i in xrange(self.iterations):
            if abs(z) > self.threshold:
                return i
            z = z * z + c
        return -1
