#!/usr/bin/python
import Image,sys
im1 = Image.open("Paint.tif")
im2 = Image.open("Final.tif")

im1_pix = im1.load()
im2_pix = im2.load()

for y in range(im1.size[1]):
    for x in range(im1.size[0]):
        i = 0
        bg = im1_pix[x,y]
        fg = im2_pix[x,y]
        i += fg[0] - bg[0]
        i += fg[1] - bg[1]
        i += fg[2] - bg[2]
        if i != 0:
            print "Images NOT identical\n"
            sys.exit(1)

print "Images Identical\n"


