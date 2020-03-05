
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

if __name__ == '__main__':
	imagepath = "./Images/001/bia1.jpg"
	parent = Tk()
	parent.title("LabelTool")
	frame = Frame(parent)
	frame.pack(fill=BOTH, expand=1)
	parent.resizable(width = False, height = False)
	STATE = {'click': 0, 'x': 0, 'y': 0}
	COLORS = ['red', 'blue', 'yellow', 'pink', 'cyan', 'green', 'black']
	hl = None
	vl = None
	MAIN_PAN_WIDTH = 600
	MAIN_PAN_HEIGH = 600

	def mouseClick(event):
		if STATE['click'] == 0:
			STATE['x'], STATE['y'] = event.x, event.y
		else:
			x1, x2 = min(STATE['x'], event.x), max(STATE['x'], event.x)
			y1, y2 = min(STATE['y'], event.y), max(STATE['y'], event.y)
			bboxList.append((x1, y1, x2, y2))
			bboxIdList.append(bboxId)
			bboxId = None
			listbox.insert(END, '(%d, %d) -> (%d, %d)' %(x1, y1, x2, y2))
			listbox.itemconfig(len(bboxIdList) - 1, fg = COLORS[(len(bboxIdList) - 1) % len(COLORS)])
			STATE['click'] = 1 - STATE['click']

	def mouseMove(event):
		hl = None
		vl = None
		disp.config(text = 'x: %d, y: %d' %(event.x, event.y))
		if tkimg:
			if hl:
				mainPanel.delete(hl)
				hl = mainPanel.create_line(0, event.y, tkimg.width(), event.y, width = 2)
			if vl:
				mainPanel.delete(vl)
				vl = mainPanel.create_line(event.x, 0, event.x, tkimg.height(), width = 2)
		if 1 == STATE['click']:
			if bboxId:
				mainPanel.delete(bboxId)
			bboxId = mainPanel.create_rectangle(STATE['x'], STATE['y'], \
												event.x, event.y, \
												Width = 2, \
												outline = COLORS[len(bboxList) % len(COLORS)])


	def cancelBBox(event):
		if 1 == STATE['click']:
			if bboxId:
				mainPanel.delete(bboxId)
				bboxId = None
				STATE['click'] = 0

	# control panel for image navigation
	ctrPanel = Frame(frame)
	ctrPanel.grid(row = 5, column = 1, columnspan = 2, sticky = W+E)
	# prevBtn = Button(ctrPanel, text='<< Prev', width = 10, command = prevImage)
	# prevBtn.pack(side = LEFT, padx = 5, pady = 3)
	# nextBtn = Button(ctrPanel, text='Next >>', width = 10, command = nextImage)
	# nextBtn.pack(side = LEFT, padx = 5, pady = 3)
	# progLabel = Label(ctrPanel, text = "Progress: /")
	# progLabel.pack(side = LEFT, padx = 5)
	# tmpLabel = Label(ctrPanel, text = "Go to Image No.")
	# tmpLabel.pack(side = LEFT, padx = 5)
	idxEntry = Entry(ctrPanel, width = 5)
	idxEntry.pack(side = LEFT)
	# goBtn = Button(ctrPanel, text = 'Go', command = gotoImage)
	# goBtn.pack(side = LEFT)


	def transformCoordinate(x_org, y_org, w_org, h_org):
		# Convert original coordinate to new coordinate fit with main panel
		# x_org, y_org: coordinate of point in original image
		# w_org, h_org: width and height of original image
		x_tran = x_org*MAIN_PAN_WIDTH/w_org
		y_tran = y_org*MAIN_PAN_HEIGH/h_org
		return x_tran, y_tran

	def reverseCoordinate(x_tran, y_tran, w_org, h_org):
		x_org = x_tran*w_org/MAIN_PAN_WIDTH
		y_org = x_tran*h_org/MAIN_PAN_HEIGH
		return x_org, y_org

	disp = Label(ctrPanel, text='')
	disp.pack(side = RIGHT)
	mainPanel = Canvas(frame, cursor='tcross')
	mainPanel.grid(row = 1, column = 1, rowspan = 4, sticky = W+S)
	mainPanel.config(width = MAIN_PAN_WIDTH, height = MAIN_PAN_HEIGH)
	mainPanel.bind("<Button-1>", mouseClick)
	mainPanel.bind("<Motion>", mouseMove)
	parent.bind("<Escape>", cancelBBox)  # press <Espace> to cancel current bbox
	parent.bind("s", cancelBBox)
	img = Image.open(imagepath)
	print(img.size)
	(w_org, h_org) = img.size
	# (x_org, y_org) = transformCoordinate(x_org, y_org, w_org, h_org)
	img = img.resize((MAIN_PAN_HEIGH, MAIN_PAN_WIDTH), Image.ANTIALIAS)
	# img.thumbnail((MAIN_PAN_HEIGH, MAIN_PAN_WIDTH), Image.ANTIALIAS)

	tkimg = ImageTk.PhotoImage(img)
	mainPanel.create_image(MAIN_PAN_HEIGH/2, MAIN_PAN_WIDTH/2, image = tkimg, anchor=CENTER)
	print("is path exists: ", os.path.exists(imagepath))
	# Resize image into MAIN_PAN_WIDTH x MAIN_PAN_HEIGH
	# img = img.resize((600, 600), Image.ANTIALIAS)
	# parent.resizable(width =  True, height = True)
	parent.mainloop()

	# parent.bind("<Escape>", cancelBBox)  # press <Espace> to cancel current bbox
	# parent.bind("s", cancelBBox)
	# parent.bind("a", prevImage) # press 'a' to go backforward
	# parent.bind("d", nextImage) # press 'd' to go forward