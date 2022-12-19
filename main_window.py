from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from PIL import Image, ImageTk
import random
from show_manager import show_manager as sm
from settings_window import Settings_window as sw
from add_new_window import add_media as am
from file_manager import file_manager as fm

class main_window:
    def __init__(self,t_master,t_font,t_textcolor,t_fontsize,t_resizable,t_windowtitle,t_backgroundcolor,t_secondarycolor,dict_showinfo):
        self.master = t_master
        self.res_x = 0
        self.res_y = 0
        self.font = t_font
        self.textcolor = t_textcolor
        self.textsize = t_fontsize
        self.resizable = t_resizable
        self.windowtitle = t_windowtitle
        self.backgroundcolor = t_backgroundcolor
        self.scolor = t_secondarycolor
        self.showdict = dict_showinfo
    
    def update_recent_favorite(self):
        self.media_recentdict = sm.return_sorted_mediadict_recent()
        self.media_favoritelist = sm.return_favoritelist()
        
    def update_file_import(self):
        self.mediadict = fm.import_medialist_from_csv('MEDIALIST.csv')
        self.catdict = fm.import_category_from_csv('CATEGORY.csv')
        self.setdict = fm.import_settings_from_csv('SETTINGS.csv')
    
    def list_category(self,category):
        main_window.reset_frame(self)
        self.mediadict = fm.import_medialist_from_csv('MEDIALIST.csv')
        cat_topframe = Frame(self.page_main_frame,background=self.backgroundcolor,padx=10,pady=10)
        cat_topframe.columnconfigure(0,weight=1)
        cat_topframe.grid(row=0,column=0,sticky=NSEW)
        
        # Generate list of existing media 
        curr_row = 0
        self.img_list = []
        for key,val in self.mediadict.items():
            self.img_list.append(ImageTk.PhotoImage(Image.open(val['THUMBFILEPATH']).resize((int(self.res_y/10),int(self.res_y/10)),Image.ANTIALIAS)))
            cat_singleframe = Frame(master=cat_topframe,background=self.backgroundcolor,relief=GROOVE,border=3)
            cat_textframe = Frame(master=cat_singleframe,background=self.backgroundcolor)
            Label(master=cat_singleframe,image=self.img_list[curr_row],background=self.backgroundcolor,borderwidth=3,relief=SUNKEN).grid(column=0,row=0,sticky=W)
            Label(master=cat_textframe,text=key,font=font.Font(family=self.font,size=self.textsize),fg=self.textcolor,bg=self.backgroundcolor).grid(column=0,row=0,sticky=W)
            Label(master=cat_textframe,text=f'Currently on S{val["CURRENTSEASON"]}:E{val["CURRENTEPISODE"]}',font=(self.font,self.textsize),fg=self.textcolor,bg=self.backgroundcolor).grid(column=0,row=1,sticky=W)
            cat_textframe.grid(row=0,column=1,sticky=EW)
            cat_singleframe.grid(row=curr_row,column=0,sticky=EW)
            curr_row += 1
        
        cat_topframe.grid(row=0,column=0,sticky=NSEW)
    
    def category(self):
        # Clear main_winow and reconfigure row 0
        main_window.reset_frame(self)
        self.page_main_frame.rowconfigure(0,weight=1)
        
        # Import data from files
        main_window.update_file_import(self)
        
        # Reference for the scrollbar from:
        # https://stackoverflow.com/questions/43731784/tkinter-canvas-scrollbar-with-grid
        
        # Create frame for padding / scrollbar
        frame_top = Frame(master=self.page_main_frame,bg=self.backgroundcolor,padx=10,pady=10)
        frame_top.rowconfigure(0,weight=1)
        frame_top.columnconfigure(0,weight=1)
        frame_top.propagate(False)
        
        # Create canvas for displaying all elements of category.
        canvas_top = Canvas(master=frame_top,bg=self.backgroundcolor)
        canvas_top.grid(row=0,column=0,sticky=NSEW)
        
        # Scrollbar for canvas_top.
        vert_scrollbar=Scrollbar(frame_top,orient=VERTICAL,command=canvas_top.yview)
        vert_scrollbar.grid(row=0,column=1,sticky=NS)
        canvas_top.config(yscrollcommand=vert_scrollbar.set)
        
        # Create frame inside canvas
        frame_inside = Frame(canvas_top,bg=self.backgroundcolor,padx=10,pady=10)
        canvas_top.create_window((0, 0), window=frame_inside, anchor=NW)
        frame_inside.rowconfigure(0,weight=1)
        for i in range(0,int(self.setdict['DISPLAY']['CATNUMCOL'])):
            frame_inside.columnconfigure(i,weight=1)
            
        # Values for the the for loop below.
        curr_col = 0
        curr_row = 0
        self.cat_thumbdict = {}
        
        # Determine if thumbnail exists.
        for key,val in self.catdict.items():
            thumb_exist = True
            if val['THUMBNAIL'] == 'None':
                thumb_exist = False
            else:
                try:
                    with open(val['THUMBNAIL']) as f:
                        thumb_exist = True
                except:
                    thumb_exist = False
            
            # If curr_col is greater than defined max num of column in
            # SETTINGS.csv (CATNUMCOL), reset curr_col to 0, and increase curr_row by 1.
            if curr_col == int(self.setdict['DISPLAY']['CATNUMCOL']):
                curr_col = 0
                curr_row += 1
                frame_inside.rowconfigure(curr_row,weight=1)
                
            # Frame for this category.
            thumbsize = self.setdict['DISPLAY']['CATSIZE'].split('x')
            
            # Show button with either with an image or a color, based on value of thumb_exist.
            if thumb_exist == True:
                self.cat_thumbdict.update({key:ImageTk.PhotoImage(Image.open(val['THUMBNAIL']).resize((int(thumbsize[0])-15,int(thumbsize[1])-15),Image.ANTIALIAS))})
                Button(frame_inside,bg=self.scolor,image=self.cat_thumbdict[key],width=thumbsize[0],height=thumbsize[1],padx=10,pady=10,text=(key+'\n'+val['DESCRIPTION']),command=lambda:main_window.list_category(self,key)).grid(row=curr_row,column=curr_col,sticky=NSEW)
            else:
                Button(frame_inside,bg=val['BGCOLOR']).grid(row=0,column=0,sticky=NSEW)
            
            # Update
            frame_inside.update_idletasks()
            curr_col += 1
        
        # Calculate total height of canvas_top, and configure Canvas
        canvas_height = int(int(thumbsize[1])*(curr_row+1))
        canvas_top.config(scrollregion=(0, 0, 1000, canvas_height))
        # Display.
        frame_top.grid(row=0,column=0,sticky=NSEW)
    
    def home_suggestion(self):
        # Base frame
        frame_topper = Frame(self.page_main_frame,background=self.backgroundcolor,padx=10,pady=10)
        frame_topper.columnconfigure(0,weight=1)
        frame_topper.rowconfigure(0,weight=1)
        frame_top = Frame(frame_topper,background=self.scolor,relief=RAISED,border=5,padx=5,pady=5)
        frame_top.rowconfigure(0,weight=1)
        frame_top.columnconfigure(1,weight=20)
        frame_top.propagate(False)
        
        # Text frame
        frame_text = Frame(frame_top,background=self.scolor,width=100)
        frame_text.grid_propagate(False)
        frame_text.rowconfigure(0,weight=1)
        frame_text.rowconfigure(1,weight=1)
        frame_text.columnconfigure(0,weight=1)
        Label(master=frame_text,text='Random suggestion from your playlist!',font=(self.font,self.textsize-2),fg=self.textcolor, background=self.scolor ).grid(column=0,row=0,sticky=SW)
        
        # Randomized media picker
        num_show = random.randint(0,len(self.showdict)-1)
        rand_show_key = list(self.showdict)[num_show]
        # Display information of the randomly chosen media.
        Label( master=frame_text, text=rand_show_key, font=(self.font,self.textsize), fg=self.textcolor, background=self.scolor ).grid(column=0,row=1,sticky=NW)
        img = Image.open(self.showdict[rand_show_key]['THUMBFILEPATH']).resize((int(self.res_y/5),int(self.res_y/5)),Image.ANTIALIAS)
        self.thumbnail=ImageTk.PhotoImage(img)
        Label(master=frame_top,image=self.thumbnail,background=self.scolor,borderwidth=5,relief=SUNKEN).grid(column=0,row=0,sticky=NSEW)
        frame_top.grid(column=0,row=0,sticky=NSEW)
        frame_text.grid(column=1,row=0,sticky=NSEW)
        frame_topper.grid(column=0,row=0,sticky=NSEW)
    
    def home_medialist(self):
        # Base frame
        top_frame = Frame(self.page_main_frame, background=self.backgroundcolor,padx=10,pady=10)
        
        top_frame.propagate(False)
        top_frame.columnconfigure(0,weight=1)
        top_frame.columnconfigure(1,weight=1)
        
        # Left base frame within base frame
        # Recently Watched
        frame_left = Frame( master=top_frame, border=5, relief=RAISED, background=self.scolor )
        frame_left.propagate(False)
        frame_left.columnconfigure(0,weight=1)
        
        # Right base frame within base frame
        # Your Favorites
        frame_right = Frame( master=top_frame, border=5, relief=RAISED, background=self.scolor )
        frame_right.propagate(False)
        frame_right.columnconfigure(0,weight=1)

        # Lables for both frames
        # Recently watched
        title_leftFrame = Label( master=frame_left, text='Recently watched', font=(self.font,self.textsize), fg=self.textcolor, justify=LEFT, background=self.scolor, )
        title_leftFrame.propagate(False)
        
        # Your favorites
        title_rightFrame = Label( master=frame_right, text='Your favorites', font=(self.font,self.textsize), fg=self.textcolor, justify=LEFT, background=self.scolor )
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
        self.page_main_frame.rowconfigure(0,weight=0)
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
        self.page_main_frame = Frame( master=self.master, background=self.backgroundcolor, relief=RIDGE, border=5 )
        self.page_main_frame.propagate(False)
        self.page_main_frame.columnconfigure(0,weight=1)
        Label( master=self.page_main_frame, text='Hmm...nothing seems to be here yet.\n<= Try pressing one of these buttons.', font=(self.font,self.textsize), fg=self.textcolor, background=self.backgroundcolor, justify=LEFT ).grid(column=0,row=0,sticky=NSEW)
        self.page_main_frame.grid(column=1,row=0,sticky=NSEW)
    
    def sidebar(self):
        main_window.window_size(self)
        # Sidebar:
        main_frame = Frame(self.master)
        main_frame.columnconfigure(0,weight=1)
        main_frame.rowconfigure(0,weight=1)
        main_frame.rowconfigure(1,weight=30)
        frame = Frame(main_frame,relief=SUNKEN,border=10,background=self.scolor)
        frame.columnconfigure(0,weight=1)
        frame.rowconfigure(0,weight=1)
        frame.rowconfigure(1,weight=1)
        frame.rowconfigure(2,weight=1)
        frame.rowconfigure(3,weight=1)
        # Buttons for navbar
        Button(frame,text='Home',command=lambda: main_window.home(self),font=(self.font,self.textsize),fg=self.textcolor,background=self.scolor).grid(column=0,row=0,sticky=NSEW)
        Button(frame,text='Categories',font=(self.font,self.textsize),fg=self.textcolor,command=lambda:main_window.category(self),background=self.scolor).grid(column=0,row=1,sticky=NSEW)
        Button(frame,text='Add New...',font=(self.font,self.textsize),fg=self.textcolor,background=self.scolor,command=lambda: am.addm(self,self.master,self.backgroundcolor,self.scolor,self.font,self.textcolor,self.textsize,self.resizable,self.windowtitle)).grid(column=0,row=2,sticky=NSEW)
        Button(frame,text='Settings',font=(self.font,self.textsize),fg=self.textcolor,background=self.scolor,command=lambda: sw.settings(self,self.master,self.backgroundcolor,self.scolor,self.font,self.textcolor,self.textsize,self.resizable,self.windowtitle)).grid(column=0,row=3,sticky=NSEW)
        # Filler for space below the navbar
        Frame(main_frame,relief=RAISED,border=5,background=self.scolor).grid(column=0,row=1,sticky=NSEW)
        frame.grid(column=0,row=0,sticky=NSEW)
        main_frame.grid(column=0,row=0,sticky=NSEW)
        
        main_window.page_frame(self)