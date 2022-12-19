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
        
        # Declare rownum, add 1 after each line.
        rownum = 0
         
        # MEDIATITLE
        self.mediatitle = StringVar(master=topframe,value='Untitled')
        Label(master=topframe,text='Title',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        Entry(master=topframe,textvariable=self.mediatitle).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # STREAMPLATFORM
        self.streamplatform = StringVar(master=topframe,value='None')
        Label(master=topframe,text='Streaming Platform',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        Entry(master=topframe,textvariable=self.streamplatform).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # THUMBFILEPATH
        self.thumbfilepath = StringVar(master=topframe,value='no_img_placeholder.png')
        Label(master=topframe,text='Thumbnail Image',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        thumb_entry_frame = Frame(master=topframe,bg=self.scolor)
        thumb_entry_frame.columnconfigure(1,weight=1)
        Label(master=thumb_entry_frame,text='./resources/',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=0,column=0,sticky=E)
        Entry(master=thumb_entry_frame,textvariable=self.thumbfilepath).grid(row=0,column=1,sticky=EW)
        thumb_entry_frame.grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # TAGS
        self.tags = StringVar(master=topframe,value='None')
        Label(master=topframe,text='Tags (Separate each by ,)',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        Entry(master=topframe,textvariable=self.tags).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # COLOR
        self.color = StringVar(master=topframe,value='#FFFFFF')
        Label(master=topframe,text='Color (Hex)',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        Entry(master=topframe,textvariable=self.color).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # BOOLFAVORITE
        self.boolfavorite = StringVar(master=topframe,value='False')
        Label(master=topframe,text='Mark as Favorite',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        ttk.Combobox(master=topframe,textvariable=self.boolfavorite,values=['True','False']).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # BOOLFINISHED
        self.boolfinished = StringVar(master=topframe,value='False')
        Label(master=topframe,text='Watched Completely',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        ttk.Combobox(master=topframe,textvariable=self.boolfinished,values=['True','False']).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # CURRENTSEASON and CURRENTEPISODE
        self.currentseason = StringVar(master=topframe,value='1')
        self.currentepisode = StringVar(master=topframe,value='1')
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
        
        topframe.grid(row=0,column=0,sticky=EW)
    
    def validate_info(self):
        try:
            # Verify that this media is not already in MEDILIST.csv
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
            errormsg = 'Only numbers are acceptable for Season and Episode values!'
            new_season = int(self.currentseason.get())
            new_episode = int(self.currentepisode.get())
            
            # Log the date and time when this media was created.
            now = datetime.now()
            
            # After a successful validation, add a new media to MEDIALIST.csv with the inputs above.
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
                'None'
                )
            
            # Close the window, and notify the user that a new media was successfully added.
            self.window_addm.destroy()
            messagebox.showinfo('Settings - '+self.windowtitle, new_mediatitle+" has been saved! :)")
        except:
            messagebox.showerror("Error!", errormsg)
    
    def addm(self,master,primary_color,secondary_color,font,textcolor,textsize,resizable,windowtitle):
        
        # __init__
        self.media_dict = fm.import_medialist_from_csv('MEDIALIST.csv')
        self.master = master
        self.pcolor = primary_color
        self.scolor = secondary_color
        self.font = font
        self.tcolor = textcolor
        self.tsize = textsize
        self.bool_resize = resizable
        self.windowtitle = windowtitle
        
        # Create and configure new window.
        self.window_addm = Toplevel()
        self.window_addm.grab_set()
        self.window_addm.title('Add To Watchlist - '+self.windowtitle)
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