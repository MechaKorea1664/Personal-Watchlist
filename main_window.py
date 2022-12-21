from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from PIL import Image, ImageTk
import random
from show_manager import show_manager as sm
from settings_window import Settings_window as sw
from add_new_window import add_media as am
from file_manager import file_manager as fm
from add_new_category import add_category as ac

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

    def media_display_info(self,title):
        main_window.reset_frame(self)
        main_window.update_file_import(self)
        mdict = self.mediadict[title]
        
        self.page_main_frame.rowconfigure(0,weight=1)
        
        frame_padding = Frame(master=self.page_main_frame,padx=10,pady=10,bg=self.backgroundcolor)
        frame_padding.rowconfigure(0,weight=1)
        frame_padding.columnconfigure(0,weight=1)
        frame_padding.grid(row=0,column=0,sticky=NSEW)
        
        frame_top = Frame(master=frame_padding,padx=10,pady=10,bg=self.backgroundcolor)
        frame_top.rowconfigure(1,weight=1)
        frame_top.columnconfigure(0,weight=1)
        frame_top.grid(row=0,column=0,sticky=NSEW)
        
        # Header
        header_frame = Frame(master=frame_top,bg=mdict['COLOR'],relief=RAISED,border=5)
        header_frame.rowconfigure(0,weight=1)
        header_frame.columnconfigure(0,weight=0)
        header_frame.columnconfigure(1,weight=1)
        header_frame.grid(row=0,column=0,sticky=NSEW)
        
        header_text_frame = Frame(master=header_frame,bg=mdict['COLOR'])
        header_text_frame.rowconfigure(0,weight=1)
        header_text_frame.grid(row=0,column=1,sticky=NSEW)
        
        header_title_frame = Frame(master=header_text_frame,bg=mdict['COLOR'])
        header_title_frame.columnconfigure(0,weight=1)
        header_title_frame.columnconfigure(1,weight=1)
        header_title_frame.rowconfigure(1,weight=1)
        header_title_frame.grid(row=0,column=0,sticky=NW)
        
        header_button_frame = Frame(master=header_text_frame,bg=mdict['COLOR'])
        header_button_frame.columnconfigure(0,weight=1)
        header_button_frame.columnconfigure(1,weight=2)
        header_button_frame.columnconfigure(2,weight=1)
        header_button_frame.grid(row=0,column=1,sticky=SE)
        
        thumb_size_list = self.setdict['DISPLAY']['CATSIZE'].split('x')
        thumbx,thumby = int(thumb_size_list[0]),int(thumb_size_list[1])
        self.mediainfo_thumb = ImageTk.PhotoImage(Image.open(mdict['THUMBFILEPATH']).resize((thumbx,thumby),Image.ANTIALIAS))
        Label(master=header_frame,image=self.mediainfo_thumb,bg=mdict['COLOR'],relief=SUNKEN,border=5).grid(row=0,column=0)
        Label(master=header_frame,bg=mdict['COLOR'],font=(self.font,self.textsize),fg=self.textcolor,text='Information on '+title+'!').grid(row=0,column=1,sticky=NW)

        
        Button(master=header_button_frame,text='  Edit  ',font=(self.font,self.textsize),
               command=lambda:am.addm(self,self.master,self.backgroundcolor,self.scolor,self.font,self.textcolor,self.textsize,self.resizable,self.windowtitle,'edit',title)
               ).grid(row=0,column=0,sticky=EW)

        Button(master=header_button_frame,text='DELETE!',font=(self.font,self.textsize),fg='white',bg='red',
               command=lambda:fm.remove_row_from_csv('MEDIALIST.csv',title,'MEDIATITLE',self.windowtitle)
               ).grid(row=0,column=2,sticky=EW)
        
        # Body
        body_frame = Frame(master=frame_top,bg=mdict['COLOR'],padx=10,pady=10,relief=RAISED,border=5)
        body_frame.rowconfigure(0,weight=1)
        body_frame.columnconfigure(0,weight=1)
        body_frame.grid_propagate(False)
        body_frame.grid(row=1,column=0,sticky=NSEW)
        
        textbox = Text(master=body_frame,bg=mdict['COLOR'],font=(self.font,self.textsize),fg=self.textcolor,wrap=WORD,state=NORMAL)
        textbox.insert(
            END,
            f"TITLE: \t\t\t{title}\nPLATFORM: \t\t\t{mdict['STREAMPLATFORM']}\nTHUMBNAIL LOCATION: \t\t\t{mdict['THUMBFILEPATH']}\n"+
                f"TAGS: \t\t\t{mdict['TAGS']}\nCOLOR: \t\t\t{mdict['COLOR']}\nACCESS DATE: \t\t\t{mdict['ACCESSDATE']}\n"+
                f"CREATION DATE: \t\t\t{mdict['CREATIONDATE']}\nFAVORITE: \t\t\t{mdict['BOOLFAVORITE']}\nFINISHED: \t\t\t{mdict['BOOLFINISHED']}\n"+
                f"CURRENT SEASON: \t\t\t{mdict['CURRENTSEASON']}\nCURRENT EPISODE: \t\t\t{mdict['CURRENTEPISODE']}\nCATEGORY: \t\t\t{mdict['CATEGORY']}"
            )
        textbox.config(state=DISABLED)
        textbox.grid(row=0,column=0,sticky=NSEW)
      
    def return_thumb_exist(self,title):
        if self.catdict[title]['BOOLTHUMB'] == False:
            return False
        else:
            try:
                with open(self.catdict[title]['THUMBNAIL']) as f:
                    return True
            except:
                return False
    
    def category_display_category_info(self,name_category,topframe):
        self.page_main_frame.rowconfigure(0,weight=1)
        
        frame_info = Frame(master=topframe,background=self.scolor,relief=RAISED,border=10)
        frame_info.columnconfigure(1,weight=1)
        
        frame_info_text = Frame(master=frame_info,background=self.scolor)
        frame_info_text.rowconfigure(1,weight=1)
        frame_info_text.columnconfigure(0,weight=1)
        
        frame_info_title = Frame(master=frame_info_text,bg=self.scolor)
        frame_info_title.columnconfigure(0,weight=1)
        
        frame_info_description = Frame(master=frame_info_text,bg=self.scolor)
        frame_info_description.rowconfigure(0,weight=1)
        frame_info_description.columnconfigure(0,weight=1)
        frame_info_description.grid_propagate(False)
        
        boolthumb = main_window.return_thumb_exist(self,name_category)
        curr_catdict = self.catdict[name_category]
        
        thumbsize = self.setdict['DISPLAY']['CATSIZE'].split('x')
        
        if boolthumb == True:
            Label(master=frame_info,image=self.cat_thumbdict[name_category],bg=self.scolor,relief=SUNKEN,border=5).grid(row=0,column=0,sticky=NSEW)
        else:
            Label(master=frame_info,image=self.cat_thumbdict[name_category],bg=curr_catdict['BGCOLOR'],relief=SUNKEN,border=5,text=name_category,font=(self.font,self.textsize),fg=curr_catdict['FGCOLOR'],compound=CENTER,wraplength=int(thumbsize[0])).grid(row=0,column=0,sticky=NSEW)
        
        # Title / Button
        Label(master=frame_info_title,text=name_category.capitalize(),font=(self.font,self.textsize),fg=self.textcolor,bg=self.scolor,pady=10).grid(row=0,column=0,sticky=NW)
        Button(master=frame_info_title,text='  Edit  ',font=(self.font,self.textsize),fg='black',pady=5,
                command=lambda:ac.add_cat(self,self.master,self.backgroundcolor,self.scolor,self.font,self.textcolor,self.textsize,self.resizable,self.windowtitle,'edit',name_category)
                ).grid(row=0,column=1,sticky='NSE')
        if name_category != 'UNCATEGORIZED':
            Button(master=frame_info_title,text='DELETE!',font=(self.font,self.textsize),fg='white',bg='red',pady=5,
                command=lambda:fm.remove_row_from_csv('CATEGORY.csv',name_category,'NAME',self.windowtitle)
                ).grid(row=0,column=2,sticky='NSE')
        
        # Description
        cat_description = Text(master=frame_info_description,font=(self.font,self.textsize),fg=self.textcolor,bg=self.scolor,state='normal',wrap=WORD)
        cat_description.insert(END,self.catdict[name_category]['DESCRIPTION'])
        cat_description.config(state='disabled')
        cat_description.grid(row=0,column=0,sticky=NSEW)
        
        # Display
        frame_info_title.grid(row=0,column=0,sticky=NSEW)
        frame_info_description.grid(row=1,column=0,sticky=NSEW)
        frame_info_text.grid(row=0,column=1,sticky=NSEW)
        frame_info.grid(row=0,column=0,sticky=NSEW)
        
    def category_list_media(self,category):
        main_window.reset_frame(self)
        main_window.update_file_import(self)
        
        cat_topframe = Frame(self.page_main_frame,background=self.backgroundcolor,padx=10,pady=10)
        cat_topframe.columnconfigure(0,weight=1)
        cat_topframe.rowconfigure(0,weight=0)
        cat_topframe.rowconfigure(1,weight=1)
        cat_topframe.propagate(False)
        
        main_window.category_display_category_info(self,category,cat_topframe)
        
        # Reference for the scrollbar from:
        # https://stackoverflow.com/questions/43731784/tkinter-canvas-scrollbar-with-grid
        
        # Create canvas to house a list of media
        frame_cat_canvas = Frame(cat_topframe)
        frame_cat_canvas.columnconfigure(0,weight=1)
        frame_cat_canvas.rowconfigure(0,weight=1)
        self.cat_canvas = Canvas(frame_cat_canvas,bg=self.backgroundcolor,highlightthickness=0)
        self.cat_canvas.columnconfigure(0,weight=1)
        self.cat_canvas.grid(row=0,column=0,sticky=NSEW)
        
        # Create Scrollbar and link to canvas
        vert_scrollbar = Scrollbar(frame_cat_canvas,orient=VERTICAL,command=self.cat_canvas.yview)
        vert_scrollbar.grid(row=0,column=1,sticky=NS)
        self.cat_canvas.config(yscrollcommand=vert_scrollbar.set)
        
        # Create list of media assigned to this category.
        curr_mediadict = {}
        for key in self.mediadict:
            if self.mediadict[key]['CATEGORY'] == category:
                curr_mediadict.update({key:self.mediadict[key]})
            if self.mediadict[key]['CATEGORY'] not in self.catdict:
                fm.value_change_inplace('MEDIALIST.csv','UNCATEGORIZED',key,'CATEGORY','MEDIATITLE')
        
        # Frame for buttons
        self.master.update()
        frame_button = Frame(self.cat_canvas,bg=self.backgroundcolor,background=self.backgroundcolor)
        frame_button.columnconfigure(0,weight=1)
        frame_button.rowconfigure(0,weight=1)
        self.frame_in_canvas = self.cat_canvas.create_window((0,0),window=frame_button,anchor=NW)
        
        # Generate list of media assigned to the category. 
        thumbsize = self.setdict['DISPLAY']['CATSIZE'].split('x')
        thumbx,thumby = (int(thumbsize[0]),int(thumbsize[1]))
        curr_row = 0
        self.img_list = []
        for key,val in curr_mediadict.items():
            self.img_list.append(ImageTk.PhotoImage(Image.open(val['THUMBFILEPATH']).resize((int(thumbx//2),int(thumby//2)),Image.ANTIALIAS)))
            cat_singleframe = Frame(master=frame_button,background=self.scolor,relief=RAISED,border=3)
            cat_singleframe.columnconfigure(3,weight=1)
            cat_textframe = Frame(master=cat_singleframe,background=self.scolor)
            Label(master=cat_singleframe,image=self.img_list[curr_row],background=self.scolor,borderwidth=3,relief=SUNKEN).grid(column=0,row=0,sticky=W)
            Label(master=cat_textframe,text=key,font=font.Font(family=self.font,size=self.textsize),fg=self.textcolor,bg=self.scolor).grid(column=0,row=0,sticky=W)
            Label(master=cat_textframe,justify=LEFT,text=f'Tags: {val["TAGS"]}',font=(self.font,self.textsize),fg=self.textcolor,bg=self.scolor).grid(column=0,row=1,sticky=W)
            Button(master=cat_singleframe,text='Details',font=(self.font,self.textsize),fg='black',relief=RAISED,border=3,command=lambda key=key:main_window.media_display_info(self,key)).grid(row=0,column=3,sticky='nse')
            cat_textframe.grid(row=0,column=1,sticky=EW)
            cat_singleframe.grid(row=curr_row,column=0,sticky=EW)
            curr_row += 1
        
        frame_button.bind("<Configure>", self.OnFrameConfigure)
        self.cat_canvas.bind('<Configure>', self.FrameWidth)
        
        # Update
        frame_button.update_idletasks()
        self.cat_canvas.config(scrollregion=self.cat_canvas.bbox("all"))
        frame_cat_canvas.grid(row=1,column=0,sticky=NSEW)
        cat_topframe.grid(row=0,column=0,sticky=NSEW)
    
    # FrameWidth and OnFrameConfigure's codes and implementation in category_list_media was
    # referenced from https://stackoverflow.com/questions/29319445/tkinter-how-to-get-frame-in-canvas-window-to-expand-to-the-size-of-the-canvas
    def FrameWidth(self,event):
        canvas_width = event.width
        self.cat_canvas.itemconfig(self.frame_in_canvas, width=canvas_width)
        
    def OnFrameConfigure(self,event):
        self.cat_canvas.configure(scrollregion=self.cat_canvas.bbox("all"))

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
        canvas_top = Canvas(master=frame_top,bg=self.backgroundcolor,highlightthickness=0)
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
        buttonlistindex = 0
        self.cat_thumbdict = {}
        self.cat_buttonlist = []
        thumbsize = self.setdict['DISPLAY']['CATSIZE'].split('x')
        
        self.cat_thumbdict.update({'addcategorybutton':PhotoImage(width=int(thumbsize[0]),height=int(thumbsize[1]))})
        cat_button = Button(frame_inside,bg=self.scolor,fg=self.textcolor,image=self.cat_thumbdict['addcategorybutton'],text='Add a new category!',wraplength=int(thumbsize[0]),font=(self.font,15),compound="center",
               command=lambda:ac.add_cat(self,self.master,self.backgroundcolor,self.scolor,self.font,self.textcolor,self.textsize,self.resizable,self.windowtitle,'add',None)
               )
        cat_button.grid(row=curr_row,column=curr_col,sticky=NSEW)
        cat_button.grid_propagate(False)
        curr_col += 1
        
        # Determine if thumbnail exists.
        for key,val in self.catdict.items():
            thumb_exist = main_window.return_thumb_exist(self,key)
            
            # If curr_col is greater than defined max num of column in
            # SETTINGS.csv (CATNUMCOL), reset curr_col to 0, and increase curr_row by 1.
            if curr_col == int(self.setdict['DISPLAY']['CATNUMCOL']):
                curr_col = 0
                curr_row += 1
                frame_inside.rowconfigure(curr_row,weight=1)
            
            # Show button with either with an image or a color, based on value of thumb_exist.
            if thumb_exist == True:
                self.cat_thumbdict.update({key:ImageTk.PhotoImage(Image.open(val['THUMBNAIL']).resize((int(thumbsize[0]),int(thumbsize[1])),Image.ANTIALIAS))})
                Button(frame_inside,bg=self.scolor,image=self.cat_thumbdict[key],width=thumbsize[0],height=thumbsize[1],command=lambda key=key:main_window.category_list_media(self,key)).grid(row=curr_row,column=curr_col,sticky=NSEW)
            else:
                self.cat_thumbdict.update({key:PhotoImage(width=int(thumbsize[0]),height=int(thumbsize[1]))}) # requried to resize the button by pixel width and not text width.
                Button(frame_inside,bg=val['BGCOLOR'],fg=val['FGCOLOR'],image=self.cat_thumbdict[key],text=key,wraplength=int(thumbsize[0]),font=(self.font,15),compound="center",command=lambda key=key:main_window.category_list_media(self,key)).grid(row=curr_row,column=curr_col,sticky=NSEW)
                
            # Update variables
            frame_inside.update_idletasks()
            curr_col += 1
            buttonlistindex += 1
        
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
        main_window.update_file_import(self)
        self.page_main_frame.rowconfigure(1,weight=1)
        
        pad_frame = Frame(self.page_main_frame,background=self.backgroundcolor,padx=10,pady=10)
        pad_frame.rowconfigure(0,weight=1)
        pad_frame.columnconfigure(0,weight=1)
        pad_frame.grid(row=1,column=0,sticky=NSEW)
        
        # Base frame
        top_frame = Frame(pad_frame, background=self.scolor,padx=10,pady=10,relief=RAISED,border=5)
        top_frame.rowconfigure(1,weight=1)
        top_frame.columnconfigure(0,weight=1)
        top_frame.grid(row=0,column=0,sticky=NSEW)
        
        Label(master=top_frame,text="You've recently interacted with...",font=(self.font,self.textsize),fg=self.textcolor,bg=self.scolor).grid(row=0,column=0,sticky=W)
        
        # Content frame
        cont_frame = Frame(top_frame,bg=self.scolor,relief=SUNKEN,border=5)
        cont_frame.columnconfigure(0,weight=1)
        cont_frame.rowconfigure(0,weight=1)
        cont_frame.rowconfigure(1,weight=1)
        cont_frame.rowconfigure(2,weight=1)
        cont_frame.rowconfigure(3,weight=1)
        cont_frame.rowconfigure(4,weight=1)
        cont_frame.grid(row=1,column=0,sticky=NSEW)
        
        recentlist = sm.return_sorted_mediadict_recent()
        curr_mediadict = {}
        [curr_mediadict.update({i:self.mediadict[i]}) for i in recentlist]
        thumbsize = self.setdict['DISPLAY']['CATSIZE'].split('x')
        thumbx,thumby = (int(thumbsize[0]),int(thumbsize[1]))
        rownum = 0
        self.recentimagelist = []
        for key,val in curr_mediadict.items():
            single_bg = val['COLOR']
            single = Frame(master=cont_frame,bg=single_bg,relief=RAISED,border=3)
            single.columnconfigure(2,weight=1)
            self.recentimagelist.append(ImageTk.PhotoImage(Image.open(val['THUMBFILEPATH']).resize((int(thumbx//3),int(thumby//3)),Image.ANTIALIAS)))
            Label(master=single,image=self.recentimagelist[rownum],bg=single_bg,relief=SUNKEN,border=3).grid(row=0,column=0,sticky=W)
            single_text = Frame(master=single,bg=single_bg)
            Label(master=single_text,text=key,font=(self.font,self.textsize),fg=self.textcolor,bg=single_bg).grid(row=0,column=0,sticky=SW)
            Label(master=single_text,text='In '+val['CATEGORY'].capitalize(),font=(self.font,self.textsize),fg=self.textcolor,bg=single_bg).grid(row=1,column=0,sticky=NW)
            Button(master=single,text='Details',fg='black',font=(self.font,self.textsize),command=lambda key=key:main_window.media_display_info(self,key)).grid(row=0,column=2,sticky='nse')
            single_text.grid(row=0,column=1,sticky=EW)
            single.grid(row=rownum,column=0,sticky=NSEW)
            rownum += 1
        
    def reset_frame(self):
        self.page_main_frame.rowconfigure(0,weight=0)
        self.page_main_frame.rowconfigure(1,weight=0)
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
        self.page_main_frame.grid_propagate(False)
        
    def sidebar(self):
        main_window.window_size(self)
        # Sidebar:
        main_frame = Frame(self.master)
        main_frame.columnconfigure(0,weight=1)
        main_frame.rowconfigure(0,weight=1)
        main_frame.rowconfigure(1,weight=50)
        
        frame = Frame(main_frame,relief=SUNKEN,border=10,background=self.scolor)
        frame.columnconfigure(0,weight=1)
        frame.rowconfigure(0,weight=1)
        frame.rowconfigure(1,weight=1)
        frame.rowconfigure(2,weight=1)
        frame.rowconfigure(3,weight=1)
        
        # Buttons for navbar
        Button(frame,text='Home',command=lambda: main_window.home(self),font=(self.font,self.textsize),fg=self.textcolor,background=self.scolor).grid(column=0,row=0,sticky=NSEW)
        Button(frame,text='Categories',font=(self.font,self.textsize),fg=self.textcolor,command=lambda:main_window.category(self),background=self.scolor).grid(column=0,row=1,sticky=NSEW)
        Button(frame,text='Add New...',font=(self.font,self.textsize),fg=self.textcolor,background=self.scolor,command=lambda: am.addm(self,self.master,self.backgroundcolor,self.scolor,self.font,self.textcolor,self.textsize,self.resizable,self.windowtitle,'add',None)).grid(column=0,row=2,sticky=NSEW)
        Button(frame,text='Settings',font=(self.font,self.textsize),fg=self.textcolor,background=self.scolor,command=lambda: sw.settings(self,self.master,self.backgroundcolor,self.scolor,self.font,self.textcolor,self.textsize,self.resizable,self.windowtitle)).grid(column=0,row=3,sticky=NSEW)
        
        # Filler for space below the navbar
        Frame(main_frame,relief=RAISED,border=5,background=self.scolor).grid(column=0,row=1,sticky=NSEW)
        frame.grid(column=0,row=0,sticky=NSEW)
        main_frame.grid(column=0,row=0,sticky=NSEW)
        
        main_window.page_frame(self)