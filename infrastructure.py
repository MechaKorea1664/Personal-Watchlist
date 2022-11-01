from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk

class infrastructure:
    def __init__(self,t_master,t_font,u_username):
        self.master = t_master
        self.res_x = 0
        self.res_y = 0
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
    
    def window_size(self):
        self.master.update()
        self.res_x = self.master.winfo_width()
        self.res_y = self.master.winfo_height()
    
    def placeholder(self):
        infrastructure.window_size(self)
        placeholder_Frame = Frame(
            master=self.master,
            background='gray',
            height=self.res_y,
            width=self.res_x-self.navbar_res_x,
            relief=RIDGE,
            border=5
            )
        placeholder_Frame.propagate(True)
        placeholder_Frame.grid(column=1,row=0)
    
    def sidebar(self):
        infrastructure.window_size(self)
        # Values for Navbar:
        self.navbar_res_x = int(self.res_x/5)
        self.navbar_res_y = int(self.res_y/5)
        
        # Sidebar:
        main_frame = Frame(self.master, width=self.navbar_res_x, height=self.navbar_res_y+10)
        main_frame.propagate(False)
        
        frame = Frame(
            main_frame,
            relief=SUNKEN,
            width=self.navbar_res_x,
            height=self.navbar_res_y,
            border=10,
            background='white',
            )
        frame.columnconfigure(0,weight=1)
        frame.rowconfigure(0,weight=1)
        frame.rowconfigure(1,weight=1)
        frame.rowconfigure(2,weight=1)
        frame.rowconfigure(3,weight=1)
        frame.grid_propagate(False)
        
        
        # Buttons for navbar
        Button(
            frame,text='Home',
            command=lambda: infrastructure.widget_suggestion(self),
            font=self.font,
            ).grid(column=0,row=0,sticky=NSEW)
        
        Button(
            frame,
            text='Categories',
            font=self.font
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
            main_frame,
            relief=RAISED,
            height=self.res_y-self.navbar_res_y,
            width=self.navbar_res_x,
            border=5
            ).grid(column=0,row=1,sticky=NW)
        frame.grid(column=0,row=0)
        main_frame.grid(column=0,row=0)
        infrastructure.placeholder(self)