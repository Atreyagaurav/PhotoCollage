import cv2
import tkinter as tk
import numpy as np
from tkinter import filedialog
from PIL import ImageTk, Image
def ResizeImage(img,res,str):
	if(str=="Auto"):
		height=int(1.1*res)
		width=int(0.96*res)
	elif(str=="Passport"):
		height=int(1.3*res)
		width=int(1.1*res)
	elif(str=="MRP"):
		height=int(45/25.4*res)
		width=int(35/25.4*res)
	elif (str=="Custom"):
		height=res[0]
		width=res[1]
	dim=(height,width)
	return cv2.resize(img,dim)
def PlaceOutline(canv,x,y,res,str):
	if(str=="Auto"):
		height=int(1.1*res)
		width=int(0.96*res)
	elif(str=="Passport"):
		height=int(1.3*res)
		width=int(1.1*res)
	elif(str=="MRP"):
		height=int(45/25.4*res)
		width=int(35/25.4*res)
	dim=(height,width)
	rect=canv.create_rectangle(x,y,x+width,y+height)
	return rect
def OpenImage():
	filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	return filename
def main():
	win=tk.Tk()
	win.geometry("1000x500")
	#start adding menu
	menu = tk.Menu(win) 
	win.config(menu=menu) 
	filemenu = tk.Menu(menu) 
	menu.add_cascade(label='File', menu=filemenu) 
	filemenu.add_command(label='New') 
	filemenu.add_command(label='Open...') 
	filemenu.add_separator() 
	filemenu.add_command(label='Exit', command=win.quit) 
	helpmenu = tk.Menu(menu) 
	menu.add_cascade(label='Help', menu=helpmenu) 
	helpmenu.add_command(label='About') 
	#finished aadding menu
	#open image
	canvas1=tk.Canvas(win,width=400,height=400,highlightthickness=1, highlightbackground="black")
	canvas1.grid(row=0)
	canvas2=tk.Canvas(win,width=400,height=600,highlightthickness=1, highlightbackground="red")
	canvas2.grid(row=0,column=1)
	filename=OpenImage()
	img=ImageTk.PhotoImage(Image.open(filename))
	img2=ImageTk.PhotoImage(Image.new("RGB", (400, 600), "white"))
	FinalImage=255*np.ones((600,400,3), np.uint8)
	initial=cv2.imread(filename)
	InitialImage=cv2.resize(initial,(100,110))
	canvas1.create_image(200,200,image=img,anchor="center")
	canvas2.create_image(200,300,image=img2,anchor="center")
	rect=[]
	for i in range(3):
		for j in range(4):
			x_of=10+i*110
			y_of=10+j*120
			rect.append(PlaceOutline(canvas2,x_of,y_of,100,"Auto"))
			FinalImage[y_of:y_of+110,x_of:x_of+100]=InitialImage
	#img=cv2.imread("Pictures\\MyPic.jpg")
	#resized=ResizeImage(img,300,"Auto")
	cv2.imwrite("Pictures\\MyPicRe.jpg",FinalImage)
	win.mainloop()

try:
	main()
except:
	pass
except BaseException:
	pass