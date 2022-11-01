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

    def home_suggestion(self):
        frame_top = Frame(
            self.page_main_frame,
            width=self.res_x-self.navbar_res_x,
            height=int(self.res_y/5),
            background='red',
            border=5,
            relief=RAISED
            )
        frame_top.propagate(False)
        frame_top.columnconfigure(0,weight=1)
        frame_top.columnconfigure(1,weight=1)
        
        frame_text = Frame(
            frame_top,
            background='gray'
            )
        frame_text.propagate(False)
        frame_text.rowconfigure(0,weight=1)
        frame_text.rowconfigure(1,weight=2)
        
        Label(
            master=frame_text,
            text='Random suggestion from your playlist!',
            font=(self.font,12)
            ).grid(column=0,row=0,sticky=NW)
        
        Label(
            master=frame_text,
            text='<INSERT TITLE HERE>',
            font=(self.font,15)
            ).grid(column=0,row=1,sticky=NW)
        
        frame_top.columnconfigure(0,weight=1)
        img = Image.open('./resources/example.png').resize((100,100),Image.ANTIALIAS)
        self.thumbnail=ImageTk.PhotoImage(img)
        Label(master=frame_top,image=self.thumbnail).grid(column=0,row=0)
        frame_top.grid(column=0,row=0,sticky=W)
        frame_text.grid(column=1,row=0,sticky=W)
    
    def reset_frame(self):
        for i in self.page_main_frame.winfo_children():
            i.destroy()
    
    def home(self):
        infrastructure.reset_frame(self)
        infrastructure.home_suggestion(self)
    
    def window_size(self):
        self.master.update()
        self.res_x = self.master.winfo_width()
        self.res_y = self.master.winfo_height()
    
    def page_frame(self):
        infrastructure.window_size(self)
        self.page_main_frame = Frame(
            master=self.master,
            background='gray',
            height=self.res_y,
            width=self.res_x-self.navbar_res_x,
            relief=RIDGE,
            border=5
            )
        self.page_main_frame.propagate(False)
        self.page_main_frame.grid(column=1,row=0,sticky=NSEW)
    
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
            command=lambda: infrastructure.home(self),
            font=(self.font,10),
            ).grid(column=0,row=0,sticky=NSEW)
        
        Button(
            frame,
            text='Categories',
            font=(self.font,10)
            ).grid(column=0,row=1,sticky=NSEW)
        
        Button(
            frame,
            text='Other',
            font=(self.font,10)
            ).grid(column=0,row=2,sticky=NSEW)
        
        Button(
            frame,
            text='Settings',
            font=(self.font,10)
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
        infrastructure.page_frame(self)