from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk
import random
from show_manager import show_manager as sm
from settings_window import Settings_window as sw

class main_window:
    def __init__(self,t_master,t_font,u_username,t_backgroundcolor,dict_showinfo):
        self.master = t_master
        self.res_x = 0
        self.res_y = 0
        self.font = t_font
        self.username = u_username
        self.backgroundcolor = t_backgroundcolor
        self.showdict = dict_showinfo
    
    def grid_showlabel(
        self,
        master=None,title='Placeholder',
        thumbpath='/resources/no_img_placeholder.png',
        width=100,
        height=100,
        border=5,
        relief=FLAT,
        color='white',
        font='Arial',
        gridx=0,
        gridy=0):
        output_frame = Frame(
            master=master,
            width=width,
            height=height,
            border=border,
            borderwidth=5,
            relief=relief,
            background=color
        )
        Label(
            master=output_frame,
            text=title,
            background=color,
            font=font
        ).grid(column=1,row=0)
        img = Image.open(thumbpath).resize((int(width/5),height),Image.ANTIALIAS)
        thumbnail=ImageTk.PhotoImage(img)
        Label(
            master=output_frame,
            image=thumbnail,
            width=int(width/5),
            height=int(height/5),
            background=color,
            borderwidth=5,
            relief=SUNKEN
            ).grid(column=0,row=0)
        output_frame.grid(column=gridx,row=gridy)
    
    def grid_showbutton(
        self,
        master=None,title='Placeholder',
        thumbpath='/resources/no_img_placeholder.png',
        width=100,
        height=100,
        border=5,
        relief=FLAT,
        color='white',
        font='Arial',
        gridx=0,
        gridy=0):
        output_frame = Frame(
            master=master,
            width=width,
            height=height,
            border=border,
            borderwidth=5,
            relief=relief,
            background=color
        )
        Button(
            master=output_frame,
            text=title,
            background=color,
            font=font
        ).grid(column=1,row=0)
        img = Image.open(thumbpath).resize((int(width/5),height),Image.ANTIALIAS)
        thumbnail=ImageTk.PhotoImage(img)
        Button(
            master=output_frame,
            image=thumbnail,
            width=int(width/5),
            height=int(height/5),
            background=color,
            borderwidth=5,
            relief=SUNKEN
            ).grid(column=0,row=0)
        output_frame.grid(column=gridx,row=gridy)
    
    def update_recent_favorite(self):
        self.media_recentdict = sm.return_sorted_mediadict_recent()
        self.media_favoritelist = sm.return_favoritelist()
    
    def page_showinfo(self):
        # Displays information related to a specific show
        top_frame = Frame(
            self.page_main_frame,
            width=self.page_frame_width,
            height=self.res_y-self.page_frame_height-10,
            broder=5,
            relief=FLAT,
            background=self.self.backgroundcolor
        )
        top_frame.propagate(False)
        top_frame.rowconfigure(0,weight=1)
        top_frame.rowconfigure(1,weight=1)
        
        # TODO: FINISH THIS CODE BLOCK
        
    
    def home_suggestion(self):
        # Background color of this widget
        background_color = self.backgroundcolor  
        # Base frame
        frame_top = Frame(self.page_main_frame,background=background_color,border=5,relief=RAISED)
        frame_top.rowconfigure(0,weight=1)
        frame_top.columnconfigure(1,weight=20)
        frame_top.propagate(False)
        # Text frame
        frame_text = Frame(
            frame_top,
            background=background_color,
            width=100
            )
        frame_text.grid_propagate(False)
        frame_text.rowconfigure(0,weight=1)
        frame_text.rowconfigure(1,weight=1)
        frame_text.columnconfigure(0,weight=1)
        Label(
            master=frame_text,
            text='Random suggestion from your playlist!',
            font=(self.font,12),
            background=background_color
            ).grid(column=0,row=0,sticky=SW)
        
        # Randomized media picker
        num_show = random.randint(0,len(self.showdict)-1)
        rand_show_key = list(self.showdict)[num_show]
        # Display information of the randomly chosen media.
        Label(
            master=frame_text,
            text=rand_show_key,
            font=(self.font,15),
            background=background_color
            ).grid(column=0,row=1,sticky=NW)
        img = Image.open(
            self.showdict[rand_show_key]['THUMBFILEPATH']).resize((int(self.res_y/5),int(self.res_y/5)),Image.ANTIALIAS)
        self.thumbnail=ImageTk.PhotoImage(img)
        Label(master=frame_top,image=self.thumbnail,background=self.backgroundcolor,borderwidth=5,relief=SUNKEN).grid(column=0,row=0,sticky=NSEW)
        frame_top.grid(column=0,row=0,sticky=NSEW)
        frame_text.grid(column=1,row=0,sticky=NSEW)
    
    def home_medialist(self):
        # Base frame
        top_frame = Frame(
            self.page_main_frame,
            border=5,
            relief=FLAT,
            background=self.backgroundcolor
            )
        
        top_frame.propagate(False)
        top_frame.columnconfigure(0,weight=1)
        top_frame.columnconfigure(1,weight=1)
        
        # Left base frame within base frame
        # Recently Watched
        frame_left = Frame(
            master=top_frame,
            border=5,
            relief=SUNKEN,
            background=self.backgroundcolor
        )
        frame_left.propagate(False)
        frame_left.columnconfigure(0,weight=1)
        
        # Right base frame within base frame
        # Your Favorites
        frame_right = Frame(
            master=top_frame,
            border=5,
            relief=SUNKEN,
            background=self.backgroundcolor
        )
        frame_right.propagate(False)
        frame_right.columnconfigure(0,weight=1)

        # Lables for both frames
        # Recently watched
        title_leftFrame = Label(
            master=frame_left,
            text='Recently watched',
            font=(self.font,15),
            relief=RAISED,
            justify=LEFT,
            background=self.backgroundcolor,
        )
        title_leftFrame.propagate(False)
        
        # Your favorites
        title_rightFrame = Label(
            master=frame_right,
            text='Your favorites',
            font=(self.font,15),
            relief=RAISED,
            justify=LEFT,
            background=self.backgroundcolor
        )
        title_rightFrame.propagate(False)
        
        main_window.update_recent_favorite(self)
        
        '''TODO: DISPLAY LISTS OF SHOWS USING INFRASTRUCTURE.GRID_SHOWLABLE OR GRID_SHOWBUTTON'''
        
        
        # Displaying all frames/elements
        top_frame.grid(column=0,row=1,sticky=NSEW)
        frame_left.grid(column=0,row=0,sticky=NSEW)
        frame_right.grid(column=1,row=0,sticky=NSEW)
        title_leftFrame.grid(column=0,row=0,sticky=NSEW)
        title_rightFrame.grid(column=0,row=0,sticky=NSEW)
        
    def reset_frame(self):
        for i in self.page_main_frame.winfo_children():
            i.destroy()
    
    def home(self):
        main_window.reset_frame(self)
        main_window.home_suggestion(self)
        main_window.home_medialist(self)
    
    def window_size(self):
        self.master.update()
        self.res_x = self.master.winfo_width()
        self.res_y = self.master.winfo_height()
    
    def page_frame(self):
        main_window.window_size(self)
        self.page_main_frame = Frame(
            master=self.master,
            background=self.backgroundcolor,
            relief=RIDGE,
            border=5
            )
        self.page_main_frame.propagate(False)
        self.page_main_frame.columnconfigure(0,weight=1)
        Label(
            master=self.page_main_frame,
            text='Hmm...nothing seems to be here yet.\n<= Try pressing one of these buttons.',
            font=(self.font,10),
            background=self.backgroundcolor,
            justify=LEFT
            ).grid(column=0,row=0,sticky=NW)
        self.page_main_frame.grid(column=1,row=0,sticky=NSEW)
    
    def sidebar(self):
        main_window.window_size(self)
        # Sidebar:
        main_frame = Frame(self.master)
        main_frame.columnconfigure(0,weight=1)
        main_frame.rowconfigure(0,weight=1)
        main_frame.rowconfigure(1,weight=30)
        frame = Frame(main_frame,relief=SUNKEN,border=10,background='white')
        frame.columnconfigure(0,weight=1)
        frame.rowconfigure(0,weight=1)
        frame.rowconfigure(1,weight=1)
        frame.rowconfigure(2,weight=1)
        frame.rowconfigure(3,weight=1)
        # Buttons for navbar
        Button(frame,text='Home',command=lambda: main_window.home(self),font=(self.font,10),).grid(column=0,row=0,sticky=NSEW)
        Button(frame,text='Categories',font=(self.font,10)).grid(column=0,row=1,sticky=NSEW)
        Button(frame,text='Other',font=(self.font,10)).grid(column=0,row=2,sticky=NSEW)
        Button(frame,text='Settings',font=(self.font,10),command=lambda: sw.settings(self,self.backgroundcolor,self.font)).grid(column=0,row=3,sticky=NSEW)
        # Filler for space below the navbar
        Frame(main_frame,relief=RAISED,border=5).grid(column=0,row=1,sticky=NSEW)
        frame.grid(column=0,row=0,sticky=NSEW)
        main_frame.grid(column=0,row=0,sticky=NSEW)
        main_window.page_frame(self)