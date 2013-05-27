#!/usr/bin/python
# import Image, ImageChops
# im1 = Image.open("BG.tif")
# im2 = Image.open("Paint.tif")
# out = ImageChops.difference(im1,im2)
# out.save("diff.tif")

import Image
im1 = Image.open("BG.tif")
im2 = Image.open("Paint.tif")
out = Image.new("RGBA",im1.size)

im1_pix = im1.load()
im2_pix = im2.load()
out_pix = out.load()

for y in range(im1.size[1]):
    for x in range(im1.size[0]):
        bg = im1_pix[x,y]
        fg = im2_pix[x,y]
        r = fg[0] - bg[0]
        g = fg[1] - bg[1]
        b = fg[2] - bg[2]
        a = 255
        out_pix[x,y] = (r,g,b,a)

out.save("diff.tif")

