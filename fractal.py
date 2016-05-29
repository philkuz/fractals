from PIL import Image
import namer
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
        self.w = w
        self.h = h
        self.pixel_mat = [[0 for _ in xrange(w)] for _ in xrange(h)]
        self.setup()
    def setup(self):
        ''' Used as a way to initialize instance variables without
        having to recreate a constructor '''
        pass
    def render(self):
        self.pixel_mat = [[0 for _ in xrange(self.w)] for _ in xrange(self.h)]
    def in_image(self, x, y):
        return x >= 0 and x < self.w and y >= 0 and y < self.h
    def set_point(self, x, y, value):
        self.pixel_mat[x][y] = value
    def get_point(self, x, y):
        return self.pixel_mat[x][y]

    def draw(self, image_name, colorFn=andy_cs):
        """ Draws the intensity values given by pixel_mat
        using the coloration described in colorFn, then saves
        the new image as image_name """
        image = Image.new("RGB", (self.w, self.h))
        mtx = image.load()
        for x, row in enumerate(self.pixel_mat):
            for y, entry in enumerate(row):
                mtx[x, y] = colorFn(entry)
        file_name = namer.get_name(image_name)
        image.save(file_name, "PNG")
    def print_matrix(self):
        """ Shorthand to nicely print out the rows of a matrix """
        for row in self.pixel_mat:
            print (row)
