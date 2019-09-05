import cv2
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
	dim=(height,width)
	return cv2.resize(img,dim)

img=cv2.imread("Pictures\\MyPic.jpg")
resized=ResizeImage(img,150,"Auto")
cv2.imwrite("Pictures\\MyPicRe.jpg",resized)
