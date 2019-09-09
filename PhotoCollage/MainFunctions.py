from GUIClass import *
def ResizeImage(img,res,str):
	if(str=='Auto'):
		height=int(1.1*res)
		width=int(1*res)
	elif(str=='PassPort'):
		height=int(1.3*res)
		width=int(1.1*res)
	elif(str=='MRP'):
		height=int(45/25.4*res)
		width=int(35/25.4*res)
	elif (str=='Custom'):
		height=res[0]
		width=res[1]
	dim=(height,width)
	return cv2.resize(img,dim)
def PlaceImages(App):
	source=App.InitialImageValue
	target=App.FinalImageValue
	arrangement=int(App.Canvas.ArrangementList.curselection()[0])
	resolution=App.Resolution
	if(arrangement==0):
		Row,Column=3,5
		source=ResizeImage(source,resolution,'Auto')
	elif(arrangement==1):
		Row,Column=2,4
		source=ResizeImage(source,resolution,'PassPort')
	elif(arrangement==2):
		Row,Column=2,3
		source=ResizeImage(source,resolution,'MRP')
	y=source.shape[1]
	x=source.shape[0]
	yT=target.shape[1]
	xT=target.shape[0]
	yg=(yT-20)/Row-y
	xg=(xT-20)/Column-x
	for i in range(Row):
		for j in range(Column):
			y_of=int(10+i*(y+yg))
			x_of=int(10+j*(x+xg))
			target[x_of:x_of+x,y_of:y_of+y]=source
	return target
def PlaceOutline(canv,x,y,res,str):
	if(str=="Auto"):
		height=int(1.1*res)
		width=int(0.96*res)
	elif(str=="PassPort"):
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

