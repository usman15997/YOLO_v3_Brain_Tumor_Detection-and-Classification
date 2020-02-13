import numpy as np
import cv2

def imcv2_recolor(im, a = .1):
	t = [np.random.uniform()]
	t += [np.random.uniform()]
	t += [np.random.uniform()]
	t = np.array(t) * 2. - 1.

	# random amplify each channel
	im = im * (1 + t * a)
	mx = 255. * (1 + a)
	up = np.random.uniform() * 2 - 1
# 	im = np.power(im/mx, 1. + up * .5)
	im = cv2.pow(im/mx, 1. + up * .5)
	return np.array(im * 255., np.uint8)

def imcv2_affine_trans(im):
    h= 512
    w= 512
    c= 512
    
    scale= np.random.uniform() / 10. + 1.
    max_offx = (scale-1.) * w
    max_offy = (scale-1.) * h
    offx = int(np.random.uniform() * max_offx)
    offy = int(np.random.uniform() * max_offy)
    im = cv2.resize(im, (0,0), fx = scale, fy = scale)
    im = im[offy : (offy + h), offx : (offx + w)]
    flip = np.random.binomial(1, .5)
    if flip: im = cv2.flip(im, 1)
    return im, [w, h, c], [scale, [offx, offy], flip]
    
	
	
	
	
	
	
	
	
	
    

    
	# Scale and translate
	
	

