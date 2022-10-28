from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk

class infrastructure:
    def __init__(self,t_master,t_resx,t_resy,t_font,u_username):
        self.master = t_master
        self.res_x = t_resx
        self.res_y = t_resy
        self.font = t_font
        self.username = u_username

        print(self.res_x,self.res_y)
    def widget_suggestion(self):
        frame = Frame(self.master)
        #canvas_thumb = Canvas(frame,width=100,height=100)
        #canvas_thumb.pack()
        #self.thumb = PhotoImage(file='./resources/example.png').subsample(3,3)
        #canvas_thumb.create_image(10,10,image=self.thumb)
        self.im1 = Image.open("./resources/example.png").resize((self.res_x/5,self.res_y/5),Image.ANTIALIAS)
        self.tkimage = ImageTk.PhotoImage(self.im1)
        Label(frame,image=self.tkimage).grid(column=0,row=0)
        frame.grid(column=1,row=0)
    
    def sidebar(self):
        # Values for Navbar:
        self.navbar_res_x = self.res_x/10
        self.navbar_res_y = self.res_y/10
        print('navbar',self.navbar_res_x)
        
        # Sidebar:
        frame = Frame(
            self.master,
            relief=SUNKEN,
            width=self.navbar_res_x,
            border=10,
            background='white',
            height=self.navbar_res_y,
            )
        frame.columnconfigure(0,weight=1)
        frame.grid_propagate(0)
        print(self.res_x,self.res_y)
        
        # Buttons for navbar
        Button(
            frame,text='Home',
            command=lambda: infrastructure.widget_suggestion(self),
            font=self.font,
            ).grid(column=0,row=0,sticky=NSEW)
        
        Button(
            frame,
            text='Categories',
            font=self.font,
            command=print('Categories clicked!')
            ).grid(column=0,row=1,sticky=NSEW)
        
        Button(
            frame,
            text='Other',
            font=self.font
            ).grid(column=0,row=2,sticky=NSEW)
        
        Button(
            frame,
            text='Settings',
            font=self.font
            ).grid(column=0,row=3,sticky=NSEW)
        
        # Filler for space below the navbar
        Frame(
            self.master,
            relief=RAISED,
            height=self.res_y-self.navbar_res_y,
            width=self.navbar_res_x, 
            border=5
            ).grid(column=0,row=1)
        return frame