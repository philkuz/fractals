'''
Buddhabrot implementation based on an existing mandelbrot
renderer

Usage:
python buddhabrot.py <imgx> <imgy>
'''

import namer
# import random
from PIL import Image
from preimage import PreImage
# def in_axis(t, taxis):
#     return t >= taxis[0] and t <= taxis[1]
# def in_image(z):
#     return in_axis(z.real, real_bounds) and in_axis(z.imag, imag_bounds)
# def complex_to_image(z):
#     yR = float(imgy)/imag_ratio
#     xR= float(imgx)/real_ratio
#     # print 'real', z.real, xR, real_bounds[0], (z.real - real_bounds[0])
#     # print 'imag', z.imag, yR, imag_bounds[0], (z.imag - imag_bounds[0])
#     x = int((z.real - real_bounds[0]) * xR)
#     y = int((z.imag - imag_bounds[0]) * yR)
#     # print x, y
#     return x, y

# def increment_box(image_mtx, z):
#     '''
#     Desc: Increments the box corresponding to the specific
#     complex coordinate
#     TODO
#     '''
#     if not in_image(z):
#         return
#     x, y = complex_to_image(z)
#     image_mtx[x][y] += 1
# def sample_point(real_bounds, imag_bounds):
#     return complex(random.uniform(*real_bounds), random.uniform(*imag_bounds))

# drawing area (xa < xb and ya < yb)

real_bounds = (-13.0/6, 7.0/6)
imag_bounds = (-5.0/3, 5.0/3)
real_ratio =  abs(real_bounds[1] - real_bounds[0])
imag_ratio = abs(imag_bounds[1] - imag_bounds[0])
xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5
maxIt = 1000 # iterations
# image size
imgx = 512
imgy = 512

#create mtx for optimized access


get_name = namer.name("buddha")

def unOptimizedBuddha(samples=int(0.5 * imgx * imgy)):
    image = Image.new("RGB", (imgx, imgy))
    matrix = PreImage(real_bounds=(xa, xb), imag_bounds=(ya, yb))
    for k in xrange(samples):
        c = matrix.sample_point()
        z = 0
        path = []
        usePath = False
        for i in range(maxIt):
            path.append(z)
            if abs(z) > 3:
                usePath = True
                break
            z = z * z + c

        if usePath:
            [matrix.increment_box(p) for p in path]
    matrix.draw(image, ((0,0,0),(255, 255, 255)))# (160, 100, 128), (60, 150, 20), (200, 100, 20)))

    # read the current names and go to the next one

    image.save(get_name(), "PNG")
unOptimizedBuddha()
