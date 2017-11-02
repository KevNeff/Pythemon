#!/usr/bin/env python

from PIL import Image
import zbarlight
import os

def Main():
	f = open("output.txt", "w")

	for filename in os.listdir(os.getcwd()):

		file_path = 'test.jpg'
		with open(file_path, 'rb') as image_file:
		    image = Image.open(image_file)
		    image.load()

		codes = zbarlight.scan_codes('qrcode', image)
		print('QR codes: %s' % codes)
	
		for code in codes:
			f.write(code + '\n')

		f.close() 
		

if __name__ == "__main__":
	Main()
