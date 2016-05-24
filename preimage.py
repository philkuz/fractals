import random

def in_axis(t, taxis):
    return t >= taxis[0] and t <= taxis[1]
# Mix colors with fraction of c1
def mix_colors(c1, c2, fraction):
    assert fraction >= 0 and fraction <= 1, "Improper fracions"
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
        self.matrix = [[0]*w] * h
        self.set_bounds(real_bounds, imag_bounds)


    def set_bounds(self, real_bounds, imag_bounds):
        self.rB = real_bounds
        self.iB = imag_bounds
        # print self.rB, self.iB
        real_ratio =  abs(real_bounds[1] - real_bounds[0])
        imag_ratio = abs(imag_bounds[1] - imag_bounds[0])
        self.xR = float(self.w)/real_ratio
        self.yR = float(self.h)/imag_ratio
    def sample_point(self):
        ''' Samples across the two axes '''
        z = self.image_to_complex(random.randint(0, self.w), random.randint(0, self.h))
        return z
    def increment_box(self, z):
        if not self.in_image(z):
            return
        x, y = self.complex_to_image(z)
        # print x, y
        p = self.matrix[x][y] + 1
        self.matrix[x][y] = p
        self.max = max(p, self.max)
    def in_image(self, z):

        val = in_axis(z.real, self.rB) and in_axis(z.imag, self.iB)
        # if not val:
        #     print "real", z.real, self.rB, in_axis(z.real, self.rB)
        #     print "imag", z.imag, self.iB, in_axis(z.imag, self.iB)
        return val
    def complex_to_image(self, z):
        # print 'real', z.real, xR, real_bounds[0], (z.real - real_bounds[0])
        # print 'imag', z.imag, yR, imag_bounds[0], (z.imag - imag_bounds[0])
        x = int((z.real - self.rB[0]) / (self.rB[1] - self.rB[0]) * (self.w - 1))
        y = int((z.imag - self.iB[0]) / (self.iB[1] - self.iB[0]) * (self.h - 1))
        # print x, y

        return x, y
    def image_to_complex(self, x, y):
        real = x * (self.rB[1] - self.rB[0]) / (self.w - 1) + self.rB[0]
        imag = y * (self.iB[1] - self.iB[0]) / (self.h - 1) + self.iB[0]
        return complex(real, imag)
    def draw(self, image, colors):
        num_colors = len(colors)
        bin_size = float(self.max) / num_colors
        mtx = image.load()
        for x in range(self.w):
            savedcolors = []
            for y in range(self.h):

                i = self.matrix[x][y] / bin_size
                decimals = i - int(i)
                print "suh", i, decimals, int(i)
                i = int(i)
                if i <= 0:
                    color = colors[0]
                elif i >= num_colors - 1:
                    color = colors[-1]
                else:
                    c1 = colors[i]
                    c2 = colors[i + 1]
                    color = mix_colors(c1, c2, decimals)
                mtx[x, y] = color
                savedcolors.append(color)
            for c in savedcolors:
                print (x, y), c

                # print x, y, color
