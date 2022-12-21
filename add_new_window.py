from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
from datetime import *
from file_manager import file_manager as fm
from show_manager import show_manager as sm
import re


class add_media:
    
    def addm_mainframe(self):
        self.mainframe = Frame(self.window_addm,bg=self.pcolor,relief=RIDGE,border=5,padx=10,pady=10)
        self.mainframe.columnconfigure(0,weight=1)
        self.mainframe.grid(row=1,column=0,sticky=NSEW)
    
    def reset_mainframe(self):
        for i in self.mainframe.winfo_children():
            i.destroy()
    
    def enter_media_info(self):
        # Entry fields for MEDIATITLE,STREAMPLATFORM,THUMBFILEPATH,TAGS,COLOR,
        # BOOLFAVORITE,BOOLFINISHED,CURRENTSEASON, and CURRENTEPISODE.
        
        # Create topframe
        topframe = Frame(self.mainframe,bg=self.scolor,relief=GROOVE,border=5)
        topframe.columnconfigure(0,weight=1)
        topframe.columnconfigure(1,weight=1)
        
        # Import current list of medias if editing.
        if self.intent == 'edit':
            curr_mediadict = fm.import_medialist_from_csv('MEDIALIST.csv')[self.title]
        
        # Declare rownum, add 1 after each line.
        rownum = 0
         
        # MEDIATITLE
        if self.intent == 'add':
            self.mediatitle = StringVar(master=topframe,value='Untitled')
            Label(master=topframe,text='Title',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
            Entry(master=topframe,textvariable=self.mediatitle).grid(row=rownum,column=1,sticky=EW)
            rownum += 1
        
        # STREAMPLATFORM
        if self.intent == 'add':
            self.streamplatform = StringVar(master=topframe,value='None')
        elif self.intent == 'edit':
            self.streamplatform = StringVar(master=topframe,value=curr_mediadict['STREAMPLATFORM'])
        
        Label(master=topframe,text='Streaming Platform',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        Entry(master=topframe,textvariable=self.streamplatform).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # THUMBFILEPATH
        if self.intent == 'add':
            self.thumbfilepath = StringVar(master=topframe,value='no_img_placeholder.png')
        elif self.intent == 'edit':
            self.thumbfilepath = StringVar(master=topframe,value=curr_mediadict['THUMBFILEPATH'].replace('./resources/',''))
        
        Label(master=topframe,text='Thumbnail Image',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        thumb_entry_frame = Frame(master=topframe,bg=self.scolor)
        thumb_entry_frame.columnconfigure(1,weight=1)
        Label(master=thumb_entry_frame,text='./resources/',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=0,column=0,sticky=E)
        Entry(master=thumb_entry_frame,textvariable=self.thumbfilepath).grid(row=0,column=1,sticky=EW)
        thumb_entry_frame.grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # TAGS
        if self.intent == 'add':
            self.tags = StringVar(master=topframe,value='None')
        elif self.intent == 'edit':
            self.tags = StringVar(master=topframe,value=curr_mediadict['TAGS'])
        
        Label(master=topframe,text='Tags (Separate each by ,)',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        Entry(master=topframe,textvariable=self.tags).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # COLOR
        if self.intent == 'add':
            self.color = StringVar(master=topframe,value='#FFFFFF')
        elif self.intent == 'edit':
            self.color = StringVar(master=topframe,value=curr_mediadict['COLOR'])
        
        Label(master=topframe,text='Color (Hex)',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        Entry(master=topframe,textvariable=self.color).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # BOOLFAVORITE
        if self.intent == 'add':
            self.boolfavorite = StringVar(master=topframe,value='False')
        elif self.intent == 'edit':
            self.boolfavorite = StringVar(master=topframe,value=str(curr_mediadict['BOOLFAVORITE']))
        
        Label(master=topframe,text='Mark as Favorite',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        ttk.Combobox(master=topframe,textvariable=self.boolfavorite,values=['True','False']).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # BOOLFINISHED
        if self.intent == 'add':
            self.boolfinished = StringVar(master=topframe,value='False')
        elif self.intent == 'edit':
            self.boolfinished = StringVar(master=topframe,value=str(curr_mediadict['BOOLFINISHED']))
        
        Label(master=topframe,text='Watched Completely',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        ttk.Combobox(master=topframe,textvariable=self.boolfinished,values=['True','False']).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # CURRENTSEASON and CURRENTEPISODE
        if self.intent == 'add':
            self.currentseason = StringVar(master=topframe,value='1')
            self.currentepisode = StringVar(master=topframe,value='1')
        elif self.intent == 'edit':
            self.currentseason = StringVar(master=topframe,value=str(curr_mediadict['CURRENTSEASON']))
            self.currentepisode = StringVar(master=topframe,value=str(curr_mediadict['CURRENTEPISODE']))
        
        Label(master=topframe,text='Currently On',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        season_episode_frame = Frame(master=topframe,bg=self.scolor)
        season_episode_frame.columnconfigure(1,weight=1)
        season_episode_frame.columnconfigure(3,weight=1)
        Label(master=season_episode_frame,text='Season',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=0,column=0,sticky=W)
        Entry(master=season_episode_frame,textvariable=self.currentseason,width=10).grid(row=0,column=1,sticky=EW)
        Label(master=season_episode_frame,text=' Episode',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=0,column=2,sticky=W)
        Entry(master=season_episode_frame,textvariable=self.currentepisode,width=10).grid(row=0,column=3,sticky=EW)
        season_episode_frame.grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # CATEGORY
        if self.intent == 'add':
            self.category = StringVar(master=topframe,value='Uncategorized')
        elif self.intent == 'edit':
            self.category = StringVar(master=topframe,value=curr_mediadict['CATEGORY'].capitalize())
        
        self.catlist = []
        [self.catlist.append(i.capitalize()) for i in list(self.catdict.keys())]
        Label(master=topframe,text='Category',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        ttk.Combobox(master=topframe,textvariable=self.category,values=self.catlist).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        topframe.grid(row=0,column=0,sticky=EW)
    
    def validate_info(self):
        try:
            # Verify that this media is not already in MEDILIST.csv
            if self.intent == 'add':
                new_mediatitle = self.mediatitle.get()
                if new_mediatitle in self.media_dict.keys():
                    errormsg = new_mediatitle+' already exists!'
                    raise ValueError
            
            errormsg = 'Invalid thumbnail filepath!'
            # Find the thumbnail in /resources/
            with open('./resources/'+self.thumbfilepath.get()) as f:
                pass
            
            # Verify Hex value of Color is valid.
            valid_color = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$',self.color.get())
            if not valid_color:
                errormsg = 'Hex value for Color is invalid!'
                raise ValueError
            
            # Verify BoolFavorite, can be True or False
            new_boolfav = self.boolfavorite.get()
            if new_boolfav != 'True' and new_boolfav != 'False':
                errormsg = 'Check the value of "Mark as Favorite"!'
                raise ValueError
            
            # Verify BoolFinished, can be True or False
            new_boolfin = self.boolfinished.get()
            if new_boolfin != 'True' and new_boolfin != 'False':
                errormsg = 'Check the value of "Watched Completely"!'
                raise ValueError
            
            # Verify both Season number and Episode number, only accepts numbers.
            new_season = self.currentseason.get()
            new_episode = self.currentepisode.get()
            if new_season.isnumeric() == False or new_episode.isnumeric() == False:
                errormsg = 'Only numbers are acceptable for Season and Episode values!'
            
            # Verify the new category.
            new_category = self.category.get()
            if new_category not in self.catlist:
                errormsg = 'Category not found!'
                raise ValueError
            
            # Log the date and time when this media was created.
            now = datetime.now()
            
            # After a successful validation, add a new media to MEDIALIST.csv with the inputs above.
            if self.intent == 'add':
                sm.add_new_media(
                    new_mediatitle,
                    self.streamplatform.get(),
                    ('./resources/'+self.thumbfilepath.get()),
                    self.tags.get(),
                    self.color.get(),
                    now,
                    now,
                    new_boolfav,
                    new_boolfin,
                    new_season,
                    new_episode,
                    'None',
                    'UNCATEGORIZED'
                    )
                
                self.window_addm.destroy()
                messagebox.showinfo('Media Manager- '+self.windowtitle, new_mediatitle+" has been saved! :)")
            elif self.intent == 'edit':
                fm.value_change_inplace('MEDIALIST.csv',self.streamplatform.get(),self.title,'STREAMPLATFORM','MEDIATITLE')
                fm.value_change_inplace('MEDIALIST.csv',('./resources/'+self.thumbfilepath.get()),self.title,'THUMBFILEPATH','MEDIATITLE')
                fm.value_change_inplace('MEDIALIST.csv',self.tags.get(),self.title,'TAGS','MEDIATITLE')
                fm.value_change_inplace('MEDIALIST.csv',self.color.get(),self.title,'COLOR','MEDIATITLE')
                fm.value_change_inplace('MEDIALIST.csv',now,self.title,'ACCESSDATE','MEDIATITLE')
                fm.value_change_inplace('MEDIALIST.csv',new_boolfav,self.title,'BOOLFAVORITE','MEDIATITLE')
                fm.value_change_inplace('MEDIALIST.csv',new_boolfin,self.title,'BOOLFINISHED','MEDIATITLE')
                fm.value_change_inplace('MEDIALIST.csv',new_season,self.title,'CURRENTSEASON','MEDIATITLE')
                fm.value_change_inplace('MEDIALIST.csv',new_episode,self.title,'CURRENTEPISODE','MEDIATITLE')
                fm.value_change_inplace('MEDIALIST.csv',self.category.get().upper(),self.title,'CATEGORY','MEDIATITLE')
                
                self.window_addm.destroy()
                messagebox.showinfo('Media Manager - '+self.windowtitle, self.title+" has been edited! :O")
                
            # Close the window, and notify the user that a new media was successfully added.
            
        except:
            messagebox.showerror("Error!", errormsg)
    
    def addm(self,master,primary_color,secondary_color,font,textcolor,textsize,resizable,windowtitle,intent,title):
        
        # __init__
        self.media_dict = fm.import_medialist_from_csv('MEDIALIST.csv')
        self.catdict = fm.import_category_from_csv('CATEGORY.csv')
        self.master = master
        self.pcolor = primary_color
        self.scolor = secondary_color
        self.font = font
        self.tcolor = textcolor
        self.tsize = textsize
        self.bool_resize = resizable
        self.windowtitle = windowtitle
        self.intent = intent
        self.title = title
        
        # Create and configure new window.
        self.window_addm = Toplevel()
        self.window_addm.grab_set()
        self.window_addm.title('Media Manager - '+self.windowtitle)
        self.window_addm.geometry('550x400')
        self.window_addm.resizable(self.bool_resize,self.bool_resize)
        self.window_addm.columnconfigure(0,weight=1)
        self.window_addm.rowconfigure(0,weight=1)
        self.window_addm.rowconfigure(1,weight=50)
        self.window_addm.rowconfigure(2,weight=1)
        
        # Create the mainframe
        add_media.addm_mainframe(self)
        
        # Navbar bottom frame
        buttonframe = Frame(master=self.window_addm,background=self.scolor,relief=RAISED,border=8)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=2)
        buttonframe.columnconfigure(2,weight=1)
        
        # Navbar bottom buttons
        Button(master=buttonframe,text=' Save ',font=(self.font,self.tsize),fg=self.tcolor,background='#3eb513',activebackground='darkgreen',command=lambda:add_media.validate_info(self)).grid(row=0,column=0,sticky=EW)
        Button(master=buttonframe,text='Cancel',font=(self.font,self.tsize),fg=self.tcolor,background='#a82c14',activebackground='#601000',activeforeground='white',command=self.window_addm.destroy).grid(row=0,column=2,sticky=EW)
        
        # Display Entry fields
        add_media.enter_media_info(self)
        
        # Display Navbar bottom butons
        buttonframe.grid(row=2,column=0,sticky=NSEW)