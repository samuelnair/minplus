#!/usr/bin/python
import Image, OpenEXR, array
im1 = Image.open("BG.tif")
im2 = Image.open("Paint.tif")
out_exr = OpenEXR.OutputFile("Diff.exr",OpenEXR.Header(im1.size[0],im1.size[1]))
out = Image.new("RGB",im1.size)

im1_pix = im1.load()
im2_pix = im2.load()
out_pix = out.load()

R = array.array('f')
G = array.array('f')
B = array.array('f')

for y in range(im1.size[1]):
    for x in range(im1.size[0]):
        bg = im1_pix[x,y]
        fg = im2_pix[x,y]
        R.append(fg[0] - bg[0])
        G.append(fg[1] - bg[1])
        B.append(fg[2] - bg[2])


(Rs,Gs,Bs) = [ chan.tostring() for chan in (R,G,B) ]
out_exr.writePixels({'R': Rs, 'G': Gs, 'B': Bs})

