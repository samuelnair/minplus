#!/usr/bin/python
import OpenEXR, Image, Imath
import sys,array
im1 = Image.open("BG.tif")
im2 = OpenEXR.InputFile("Diff.exr")
out = Image.new("RGBA",im1.size)

im1_pix = im1.load()
FLOAT = Imath.PixelType(Imath.PixelType.FLOAT)
(R,G,B) = [array.array('f',im2.channel(chan, FLOAT)).tolist() for chan in ("R", "G", "B") ]
out_pix = out.load()
i = 0
for y in range(im1.size[1]):
    for x in range(im1.size[0]):
        bg = im1_pix[x,y]
        r = int(bg[0] + R[i])
        g = int(bg[1] + G[i])
        b = int(bg[2] + B[i])
        a = bg[3]
        out_pix[x,y] = (r,g,b,a)
        i += 1

out.save("Final.tif")

