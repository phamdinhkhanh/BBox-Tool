# 1. BBox-Label-Tool
===============

A simple tool for labeling object bounding boxes in images, implemented with Python Tkinter.

**Updates:**
- 2017.5.21 Check out the ```multi-class``` branch for a multi-class version implemented by @jxgu1016

**Screenshot:**
![Label Tool](./screenshot.png)

Data Organization
-----------------
LabelTool  
|  
|--main.py   *# source code for the tool*  
|  
|--Images/   *# direcotry containing the images to be labeled*  
|  
|--Labels/   *# direcotry for the labeling results*  
|  
|--Examples/  *# direcotry for the example bboxes*  

Environment
----------
- python 2.7
- python PIL (Pillow)

Run
-------
$ python main.py

# 2. Usage
-----
0. The current tool requires that **the images to be labeled reside in /Images/001, /Images/002, etc. You will need to modify the code if you want to label images elsewhere**.
1. Input a folder number (e.g, 1, 2, 5...), and click `Load`. The images in the folder, along with a few example results will be loaded.
2. To create a new bounding box, left-click to select the first vertex. Moving the mouse to draw a rectangle, and left-click again to select the second vertex.
  - To cancel the bounding box while drawing, just press `<Esc>`.
  - To delete a existing bounding box, select it from the listbox, and click `Delete`.
  - To delete all existing bounding boxes in the image, simply click `ClearAll`.
3. After finishing one image, click `Next` to advance. Likewise, click `Prev` to reverse. Or, input an image id and click `Go` to navigate to the speficied image.
  - Be sure to click `Next` after finishing a image, or the result won't be saved. 

# 3. Other bounding box tool:

LabelImage is best open source software for bounding box: 
https://pypi.org/project/labelImg
It support variety of bounding box types: Pascal VOC and YOLO darknet simple format.
Friendly graphic:
![Label Image](./labelImage.jpg)

# 3. Convert into YOLO

Label should be formated into `<object-id> <x-center-ratio> <y-center-ratio> <width-ratio> <height-ratio>` that is standardize image scale of coordinate as bellow formula: 

x-center-ration = x-center/img-width

y-center-ration = y-center/img-height

width-ratio = bbox-width/img-width

height-ratio = bbox-height/img-height


Run code on:

`py convert.py`

Param should be modified inside `convert.py`:

`""" Configure Paths"""   
classes = ["005"]
mypath = "Labels/005/"
outpath = "Labels/005_std/"
imgpath = "Images/005"
cls = "005"`



