import namer
# Mandelbrot fractal
# FB - 201003151
# Modified Andrew Lewis 2010/04/06
from PIL import Image
# drawing area (xa < xb and ya < yb)
xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5
maxIt = 512 # iterations
# image size
imgx = 512
imgy = 512

#create mtx for optimized access
image = Image.new("RGB", (imgx, imgy))
mtx = image.load()

#optimizations
lutx = [j * (xb-xa) / (imgx - 1) + xa for j in xrange(imgx)]

for y in xrange(imgy):
    cy = y * (yb - ya) / (imgy - 1)  + ya
    for x in xrange(imgx):
        c = complex(lutx[x], cy)
        z = 0
        for i in xrange(maxIt):
            if abs(z) > 2.0: break
            z = z * z + c
        r = i % 4 * 64
        g = i % 8 * 32
        b = i % 16 * 16
        mtx[x, y] =  r,g,b

# read the current names and go to the next one
get_name = namer.name("mandel")


image.save(get_name(), "PNG")
