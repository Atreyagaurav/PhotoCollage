from GUIClass import *
from MainFunctions import *
def main():
	windows=[]
	Win1=MainApp()
	windows.append(Win1)
	Win1.MainWindow.mainloop()
	# rect=[]
	# FinalImage=255*np.ones((600,400,3), np.uint8)
	# for i in range(3):
	# 	for j in range(4):
	# 		x_of=10+i*110
	# 		y_of=10+j*120
	# 		rect.append(PlaceOutline(canvas2,x_of,y_of,100,"Auto"))
	# 		FinalImage[y_of:y_of+110,x_of:x_of+100]=InitialImage
	# filename=filedialog.asksaveasfilename(initialdir = "/",title = "Save Image As",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	# cv2.imwrite(filename,FinalImage)
	#img=cv2.imread("Pictures\\MyPic.jpg")
	#resized=ResizeImage(img,300,"Auto")
#try:
main()
# except BaseException:
# 	pass
# except:
# 	pass