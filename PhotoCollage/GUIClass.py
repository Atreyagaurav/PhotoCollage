import cv2
import tkinter as tk
import numpy as np
from tkinter import filedialog
from PIL import ImageTk, Image
from MainFunctions import *
class MainMenuStripe:
	def __init__(self,App):
		self.App=App
		self.Menu = tk.Menu(self.App.MainWindow) 
		self.App.MainWindow.config(menu=self.Menu) 
		self.FileMenu = tk.Menu(self.Menu) 
		self.Menu.add_cascade(label='File', menu=self.FileMenu) 
		self.FileMenu.add_command(label='Open',command=self.App.OpenImage) 
		self.FileMenu.add_command(label='Open New',command=self.App.OpenImageAsNew) 
		self.FileMenu.add_command(label='Save',command=self.App.SaveImage) 
		self.FileMenu.add_command(label='Save As',command=self.App.SaveAsImage) 
		self.FileMenu.add_command(label='Exit', command=self.App.MainWindow.quit) 
		self.HelpMenu = tk.Menu(self.Menu) 
		self.Menu.add_cascade(label='Help', menu=self.HelpMenu) 
		self.HelpMenu.add_command(label='About') 
class MainCanvas:
	def __init__(self,App):
		self.App=App
		self.canvas1=tk.Canvas(self.App.MainWindow,width=400,height=600,
			highlightthickness=1, highlightbackground="black")
		self.canvas1.grid(row=0)
		self.Canvas1Objects=[]
		self.canvas2=tk.Canvas(self.App.MainWindow,width=400,height=600,
			highlightthickness=1, highlightbackground="red")
		self.canvas2.grid(row=0,column=1)
		self.Canvas2Objects=[]
		self.Options=tk.Frame(self.App.MainWindow)
		self.Options.grid(sticky="N",row=0,column=2)
		self.ResolutionLabel=tk.Label(self.Options,text="Resolution")
		self.ResolutionValue=tk.Entry(self.Options,width=5)
		self.ResolutionValue.insert(0,self.App.Resolution)
		self.ResolutionUnit=tk.Label(self.Options,text="dpi")
		self.ResolutionLabel.grid(sticky="E",row=0)
		self.ResolutionValue.grid(row=0,column=1)
		self.ResolutionUnit.grid(row=0,column=2)
		self.InitialImageSizeLabel=tk.Label(self.Options,text="Initial Image Size")
		self.InitialImageWidthValue=tk.Entry(self.Options,width=5)
		self.InitialImageWidthUnit=tk.Label(self.Options,text="in X")
		self.InitialImageHeightValue=tk.Entry(self.Options,width=5)
		self.InitialImageHeightUnit=tk.Label(self.Options,text="in")
		self.InitialImageSizeLabel.grid(sticky="E",row=1)
		self.InitialImageWidthValue.grid(row=1,column=1)
		self.InitialImageWidthUnit.grid(row=1,column=2)
		self.InitialImageHeightValue.grid(row=1,column=3)
		self.InitialImageHeightUnit.grid(row=1,column=4)
		self.FinalImageSizeLabel=tk.Label(self.Options,text="Final Image Size")
		self.FinalImageWidthValue=tk.Entry(self.Options,width=5)
		self.FinalImageWidthUnit=tk.Label(self.Options,text="in X")
		self.FinalImageHeightValue=tk.Entry(self.Options,width=5)
		self.FinalImageHeightUnit=tk.Label(self.Options,text="in")
		self.FinalImageSizeLabel.grid(sticky="E",row=2)
		self.FinalImageWidthValue.grid(row=2,column=1)
		self.FinalImageWidthUnit.grid(row=2,column=2)
		self.FinalImageHeightValue.grid(row=2,column=3)
		self.FinalImageHeightUnit.grid(row=2,column=4)
		self.ArrangementLabel=tk.Label(self.Options,text="Arrangement:",anchor="ne")
		self.ArrangementLabel.grid(sticky="NE",row=3)
		self.ArrangementList=tk.Listbox(self.Options,height=6)
		self.ArrangementList.grid(row=3,column=1,columnspan=4)
		self.ArrangementList.insert(1,'All Auto-1x1.1')
		self.ArrangementList.insert(2,'All Passport-1.1x1.3')
		self.ArrangementList.insert(3,'All MRP')
		self.ArrangementList.insert(4,'Custom')
		self.GenerateButton=tk.Button(self.Options,text="Generate",command=self.App.GenerateImage)
		self.GenerateButton.grid(row=4,column=0,columnspan=4)
class MainApp:
	def __init__(self):
		self.OrginalFilename=None
		self.FinalFilename=None
		self.InitialImage= None
		self.FinalImage= None
		self.InitialImageValue= None
		self.FinalImageValue= 255*np.ones((600,400,3),np.uint8)
		self.Resolution=100
		self.SavedState=False
		self.MainWindow= tk.Tk()
		self.MainWindow.geometry("1000x500")
		self.MainWindow.title("Untitled.jpg")
		self.MenuStripe= MainMenuStripe(self)
		self.Canvas=MainCanvas(self)
	def OpenImage(self):
		self.OrginalFilename =  filedialog.askopenfilename(initialdir = "/",
			title = "Open Image",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
		if(self.OrginalFilename):
			self.MainWindow.title(self.OrginalFilename)
			self.FinalFilename=AddNewInFileName(self.OrginalFilename)
			self.SavedState=False
			self.InitialImage=ImageTk.PhotoImage(Image.open(self.OrginalFilename))
			self.InitialImageValue=cv2.imread(self.OrginalFilename)
			self.Canvas.canvas1.create_image(200,300,image=self.InitialImage,anchor="center")
			self.FinalImage=ImageTk.PhotoImage(Image.new("RGB",(400,600),"white"))
			self.Canvas.canvas2.create_image(200,300,image=self.FinalImage,anchor="center")
	def OpenImageAsNew(self):
		pass
	def SaveImage(self):
		if(not self.FinalFilename):
			self.FinalFilename =AddNewInFileName(self.OrginalFilename)
		self.FinalFilename=ProcessFileName(filedialog.asksaveasfilename(initialdir = self.FinalFilename,
			title = "Save Image",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))))
		cv2.imwrite(self.FinalFilename,self.FinalImageValue)
		self.SavedState=True
	def SaveAsImage(self):
		pass
	def GenerateImage(self):
		self.SavedState=False

