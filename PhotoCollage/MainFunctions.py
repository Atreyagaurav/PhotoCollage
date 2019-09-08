from GUIClass import *
def ResizeImage(img,res,str):
	if(str=="Auto"):
		height=int(1.1*res)
		width=int(1*res)
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
def AddNewInFileName(filename):
	fnames=filename.split('.')
	ext=fnames[-1]
	fnames=fnames[:-1]
	fnames[-1]=fnames[-1]+"_collage"
	return ".".join(fnames)+"."+ext
def ProcessFileName(filename):
	fnames=filename.split('/')
	ext=fnames[-1]
	if(len(ext.split('.'))==1):
		filename=filename+".jpg"
	return filename

