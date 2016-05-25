import random, math

# Mix colors with fraction of c1
def mix_colors(c1, c2, fraction):
    assert fraction >= 0 and fraction <= 1, "Improper fraction"
    inverse = 1 - fraction
    r = c1[0] * fraction + c2[0] * inverse
    g = c1[1] * fraction + c2[1] * inverse
    b = c1[2] * fraction + c2[2] * inverse
    return (int(r), int(g), int(b))

class PreImage:

    def __init__(self, w=512, h=512, real_bounds = (-13.0/6.0, 7.0/6.0), imag_bounds = (-5.0/3.0, 5.0/3.0)):
        self.w = w
        self.h = h
        self.max = 0
        self.matrix = [[0 for _ in xrange(w)] for _ in xrange(h)]
        self.set_bounds(real_bounds, imag_bounds)


    def set_bounds(self, real_bounds, imag_bounds):
        self.rB = real_bounds
        self.iB = imag_bounds
    def sample_point(self):
        """ Samples across the two axes """
        x = random.randint(0, self.w - 1)
        y = random.randint(0, self.h - 1)
        z = self.image_to_complex(x, y)
        return z

    def increment_box(self, z):
        """ Increments the box corresponding to the
        complex number Z. """
        x, y = self.complex_to_image(z)
        if not self.in_image(x, y):
            return
        p = self.matrix[x][y] + 1
        self.matrix[x][y] += 1
        self.max = max(p, self.max)
    def in_image(self, x, y):
        """ Returns whether or not a cartesian point is in the image
        """
        return x >= 0 and x < self.w and y >= 0 and y < self.h
    def complex_to_image(self, z):
        """ Returns the complex number's position in the image """
        x = int((z.real - self.rB[0]) / (self.rB[1] - self.rB[0]) * float(self.w - 1))
        y = int((z.imag - self.iB[0]) / (self.iB[1] - self.iB[0]) * float(self.h - 1))

        return x, y #random.randint(0, self.w - 1), random.randint(0, self.h - 1)
    def image_to_complex(self, x, y):
        """ Returns the complex number of the coordinate in the image. """
        real = x * (self.rB[1] - self.rB[0]) / float(self.w - 1) + self.rB[0]
        imag = y * (self.iB[1] - self.iB[0]) / float(self.h - 1) + self.iB[0]
        return complex(real, imag)
    def draw(self, image, colors):
        num_colors = len(colors)
        bin_size = float(self.max) / num_colors
        mtx = image.load()
        for x in xrange(self.w):
            # savedcolors = []
            for y in xrange(self.h):

                # i = min(int(self.matrix[x][y] / bin_size), num_colors - 1)
                # color  = colors[i]
                # decimals = i - int(i)
                # # print "suh", i, decimals, int(i), bin_size, self.max
                # # i = int(i)
                # # if i <= 0:
                # #     color = colors[0]
                # # elif i >= num_colors - 1:
                # #     color = colors[-1]
                # # else:
                # #     c1 = colors[i]
                # #     c2 = colors[i + 1]
                # #     color = mix_colors(c1, c2, decimals)
                i = self.matrix[x][y]
                # r = i % 4 * 64
                # g = i % 8 * 32
                # b = i % 16 * 16
                r = int(255 * math.atan(float(i)/ 5))
                color = r, r, r
                # color = int(r), int(g), int(b)

                # savedcolors.append(color)
                mtx[x, y] = color

    def draw_trajectory(self, c=0, n=0, path=[]):
        if path:
            [self.increment_box(z) for z in path]
        else:
            z = c
            for _ in xrange(n):
                self.increment_box(z)
                z = z * z + c
    def output_matrix(self):
        for row in self.matrix:
            print row
