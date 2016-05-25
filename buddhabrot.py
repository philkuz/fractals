'''
Buddhabrot implementation based on an existing mandelbrot
renderer

Usage:
python buddhabrot.py <imgx> <imgy> <iterations> <samples>
'''

import namer
import sys
# import random
from PIL import Image
from preimage import PreImage

real_bounds = (-13.0/6, 7.0/6)
imag_bounds = (-5.0/3, 5.0/3)
real_ratio =  abs(real_bounds[1] - real_bounds[0])
imag_ratio = abs(imag_bounds[1] - imag_bounds[0])
xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5
maxIt = 20000 # iterations
# image size
imgx = 512
imgy = 512


get_name = namer.name("buddha")
def in_mandelbrot(c, threshold, iterations):
    path = []
    z = c
    for i in xrange(iterations):
        path.append(z)
        if abs(z) > threshold:
            return i, path
        z = z * z + c
    return 0, []
def unOptimizedBuddha(samples=int(0.5 * imgx * imgy)):
    # TODO move this to it's own file
    image = Image.new("RGB", (imgx, imgy))
    matrix = PreImage(real_bounds=(xa, xb), imag_bounds=(ya, yb))
    # matrix.output_matrix()
    for k in xrange(samples):
        c = matrix.sample_point()
        z = c
        path = []
        n, path = in_mandelbrot(z, 2.0, maxIt)
        if n:
            matrix.draw_trajectory(path=path)

    matrix.draw(image, ((0,0,0), (160, 100, 128), (60, 150, 20), (200, 100, 20)))

    image.save(get_name(), "PNG")



if __name__ == "__main__":
    # TODO use a nice lil library for this
    if len(sys.argv) < 2:
        imgx = 512
        imgy = 512
        maxIt = 20000

    else:
        assert len(sys.argv) >= 3, "Proper usage is 'python buddhabrot.py <imgx> <imgy> <iterations> <samples>'"
        imgx = sys.argv[1]
        imgy = sys.argv[2]
        maxIt = sys.argv[3]
        samples = sys.argv[4]
    unOptimizedBuddha()
