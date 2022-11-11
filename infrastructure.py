from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk
import random

class infrastructure:
    def __init__(self,t_master,t_font,u_username,t_backgroundcolor,dict_showinfo):
        self.master = t_master
        self.res_x = 0
        self.res_y = 0
        self.font = t_font
        self.username = u_username
        self.backgroundcolor = t_backgroundcolor
        self.showdict = dict_showinfo
    
    def home_suggestion(self):
        # Background color of this widget
        background_color = self.backgroundcolor  
        # Base frame
        frame_top = Frame(
            self.page_main_frame,
            width=self.page_frame_width,
            height=self.page_frame_height,
            background=background_color,
            border=5,
            relief=RAISED
            )
        frame_top.grid_propagate(False)
        frame_top.columnconfigure(0,weight=0)
        frame_top.columnconfigure(1,weight=1)
        frame_top.rowconfigure(0,weight=1)
        # Text frame
        frame_text = Frame(
            frame_top,
            background=background_color,
            width=100
            )
        frame_text.grid_propagate(True)
        frame_text.rowconfigure(0,weight=1)
        frame_text.rowconfigure(1,weight=1)
        frame_text.columnconfigure(0,weight=0)
        Label(
            master=frame_text,
            text='Random suggestion from your playlist!',
            font=(self.font,12),
            background=background_color
            ).grid(column=0,row=0,sticky=W)
        
        # Random Show picker
        num_show = random.randint(0,len(self.showdict)-1)
        rand_show_key = list(self.showdict)[num_show]
        
        # Display information of the randomly chosen media.
        Label(
            master=frame_text,
            text=self.showdict[rand_show_key]['SHOWTITLE'],
            font=(self.font,15),
            background=background_color
            ).grid(column=0,row=1,sticky=W)
        frame_top.columnconfigure(1,weight=1)
        img = Image.open(self.showdict[rand_show_key]['THUMBNAILFILEPATH']).resize((int(self.res_y/5),int(self.res_y/5)),Image.ANTIALIAS)
        self.thumbnail=ImageTk.PhotoImage(img)
        Label(master=frame_top,image=self.thumbnail,width=int(self.res_y/5),height=int(self.res_y/5),background=self.backgroundcolor,borderwidth=5,relief=SUNKEN).grid(column=0,row=0)
        frame_top.grid(column=0,row=0,sticky=W)
        frame_text.grid(column=1,row=0,sticky=W)
    
    def home_medialist(self):
        # Base frame
        top_frame = Frame(
            self.page_main_frame,
            width=self.page_frame_width,
            height=self.res_y-self.page_frame_height-10,
            border=5,
            relief=FLAT,
            background=self.backgroundcolor
            )
        top_frame.propagate(False)
        top_frame.columnconfigure(0,weight=1)
        top_frame.columnconfigure(1,weight=1)
        # Left base frame within base frame
        frame_left = Frame(
            master=top_frame,
            width=self.page_frame_width/2,
            height=self.res_y-self.page_frame_height-20,
            border=5,
            relief=SUNKEN,
            background=self.backgroundcolor
        )
        frame_left.propagate(False)
        frame_left.columnconfigure(0,weight=1)
        # Right base frame within base frame
        frame_right = Frame(
            master=top_frame,
            width=self.page_frame_width/2,
            height=self.res_y-self.page_frame_height-20,
            border=5,
            relief=SUNKEN,
            background=self.backgroundcolor
        )
        frame_right.propagate(False)
        frame_right.columnconfigure(0,weight=1)

        # Lables for both frames
        title_leftFrame = Label(
            master=frame_left,
            text='Recently watched',
            font=(self.font,15),
            relief=RAISED,
            justify=LEFT,
            background=self.backgroundcolor,
        )
        title_leftFrame.propagate(False)

        title_rightFrame = Label(
            master=frame_right,
            text='Your favorites',
            font=(self.font,15),
            relief=RAISED,
            justify=LEFT,
            background=self.backgroundcolor
        )
        title_rightFrame.propagate(False)
        
        top_frame.grid(column=0,row=1,sticky=NSEW)
        frame_left.grid(column=0,row=0,sticky=NSEW)
        frame_right.grid(column=1,row=0,sticky=NSEW)
        title_leftFrame.grid(column=0,row=0,sticky=NSEW)
        title_rightFrame.grid(column=0,row=0,sticky=NSEW)
        
        
    def reset_frame(self):
        for i in self.page_main_frame.winfo_children():
            i.destroy()
    
    def home(self):
        infrastructure.reset_frame(self)
        infrastructure.home_suggestion(self)
        infrastructure.home_medialist(self)
    
    def window_size(self):
        self.master.update()
        self.res_x = self.master.winfo_width()
        self.res_y = self.master.winfo_height()
    
    def page_frame(self):
        infrastructure.window_size(self)
        self.page_main_frame = Frame(
            master=self.master,
            background=self.backgroundcolor,
            height=self.res_y,
            width=self.res_x-self.navbar_res_x,
            relief=RIDGE,
            border=5
            )
        self.page_main_frame.propagate(False)
        Label(
            master=self.page_main_frame,
            text='Hmm...nothing seems to be here yet.\n<= Try pressing one of these buttons.',
            font=(self.font,10),
            background=self.backgroundcolor,
            justify=LEFT
            ).grid(column=0,row=0,sticky=NSEW)
        self.page_main_frame.grid(column=1,row=0,sticky=NSEW)
        self.page_frame_width=self.res_x-self.navbar_res_x-10
        self.page_frame_height=self.res_y/5
    
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
            background='white'
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