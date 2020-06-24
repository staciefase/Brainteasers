#!/usr/bin/env python
# coding: utf-8

# In[5]:


## import libraries
import PIL
from PIL import Image
from PIL import ImageFilter
import numpy

##read in image
pic = Image.open(r'C:\Users\smahuna\Desktop\separate-them.png')

## for testing
#pic.show()

## show pixel sizes (w, l)
print(pic.size)


# In[6]:


#will produce an array of 200 objects that are 600 deep
pic_array = numpy.array(pic)

##testing
#print(pic_array[44][222])


# In[9]:


## Pixel_1 = person_1, pixel_2 = person_2, pixel_3 = person_3, pixel_4 = person_1, pixel_5 = person_2, pixel_6 = person_3 etc
## A pixel is a tuple of RGB values (255, 255, 255). 
## https://en.wikipedia.org/wiki/Tuple#:~:text=In%20mathematics%2C%20a%20tuple%20is,as%20it%20is%20referred%20to.
## Create three lists, one per person. Separate the pixels and add them to the right person lists
## Write each list out as a 200x200 image.
## Reading pixels 'line by line', iterating through first line of 600 pixels, then second line, etc.


###################################################################################


##first person in the transporter
L=0
W=0 #list starts at 0, so the first object is the '0' object
first_person = [] #create a blank list
while L < 200: 
    while W < 600:
        first_person.append(pic_array[L][W])
        W=W+3 ##every third pixel 
    L=L+1 #next line of pixels
    W=0 #reset the pixel count to 0 
    
##second person in the transporter
L=0
W=1 #starts at 2nd pixel
second_person = []
while L < 200:
    while W < 600:
        second_person.append(pic_array[L][W])
        W=W+3 ##iterates on every third pixel in sequence
    L=L+1 #next line of pixels
    W=1 #reset the pixel count to 0 

##third person in the transporter
L=0
W=2 #starts at 3rd pixel
third_person = []
while L < 200:
    while W < 600:
        third_person.append(pic_array[L][W])
        W=W+3 ##iterates on every third pixel in sequence
    L=L+1 #next line of pixels
    W=2 #reset the pixel count to 0 


# In[10]:


##creating a image object
##https://www.pythonforbeginners.com/basics/list-comprehensions-in-python/
##without list comprehension, code would be:
##newlist = []
##for p in first_person:
    ##newlist.append(tuple(p))
##first_person = newlist 

##########################################################################

##first person
test_image = Image.new("RGB", (200,200))
first_person = [tuple(p) for p in first_person]
test_image.putdata(first_person)
test_image.show()

##second person
test_image = Image.new("RGB", (200,200))
second_person = [tuple(p) for p in second_person]
test_image.putdata(second_person)
test_image.show()

##third person
test_image = Image.new("RGB", (200,200))
third_person = [tuple(p) for p in third_person] #pixel data requires pixels by tuples
test_image.putdata(third_person)
test_image.show()

