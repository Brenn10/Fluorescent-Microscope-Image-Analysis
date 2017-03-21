import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import os

f = open("log.txt","a+")

for root,dirs,files in os.walk("./"):
	for filename in files:
		if(filename.endswith(".jpg")):

			img = cv2.imread(filename,0)


			if(img==None):
				print("INVALID IMAGE")
				exit(-1)

			totalL = 0.0
			points = 0.0

			for row in img:
			    for pixel in row:
				s = pixel
				if(s>10):
				    totalL+=s
				    points+=1
				    

			print(filename + " %f" %(totalL/points))
			f.write(filename + ",%f\n" %(totalL/points))
f.close()
