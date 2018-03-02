#!/usr/local/bin/python3
#-*-coding:utf-8 -*-
#The website http://docs.astropy.org/en/stable/io/fits/index.html
from astropy.io import fits
hdulist = fits.open("agn.fits")	# open fits
hdulist.info()					#import fits information  Header Data Unit
# hudlist[0] is the primary HDU,hdulist[1] is the first extension HDU
#hdulist.close() #The headers still be accessible after the file close
#The open() function supports a "memmap=True" argument that allows the 
#array data of each HDU to be accessed with mmap, rather than being 
#read into memory all at once. This is particularly useful for working
# with very large arrays that cannot fit entirely into physical memory.
#HDU object--hdulist has two attributes-.header and .data
#For those unfamiliar with FITS headers, they consist of 
#a list of 80 byte “cards”, where a card contains a keyword, a value, and 
#a comment. The keyword and comment must both be strings, whereas the value
# can be a string or an integer, floating point number, complex number, or True/False
#dict index :hdulist[0].header["targname"] or hdulist[1].header[3]
hdulist[0].data
print (repr(hdulist[0].header))
#Another way to either update an existing card or append a new one is to use the
# Header.set() method To see the entire header as it appears in the FITS file 
# (with the END card and padding stripped), simply enter the header object by itself,
# or print(repr(header))
# o get a list of all keywords, use the Header.keys() method just as you would with a dict
prihdr = hdulist[0].header
#print (prihdr.keys())

#working with image data
scidata = hdulist[1].data
#scidata.shape  #array shape
#scidata[30:40, 10:20]  #  introduce x = 11-20;y=31-40
#数据转换为流量 The next example of array manipulation is to convert the image data 
#from counts to flux:
photflam = hdulist[1].header
#exptime = prihdr['exptime']
#scidata *= photflam / exptime
# outcome save at a new file HDUList.writeto() method 
print (hdulist[1].header)
hdulist.writeto("fits")















