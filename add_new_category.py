from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
from file_manager import file_manager as fm
from show_manager import show_manager as sm
import re

class add_category:

    def addc_mainframe(self):
        self.mainframe = Frame(self.window_addc,bg=self.pcolor,relief=RIDGE,border=5,padx=10,pady=10)
        self.mainframe.columnconfigure(0,weight=1)
        self.mainframe.grid(row=1,column=0,sticky=NSEW)
    
    def reset_mainframe(self):
        for i in self.mainframe.winfo_children():
            i.destroy()
    
    def enter_cat_info(self):
        # Entry fields for NAME,THUMBNAIL,BGCOLOR,FGCOLOR,DESCRIPTION, and BOOLTHUMB.
        
        # Create topframe
        topframe = Frame(self.mainframe,bg=self.scolor,relief=GROOVE,border=5)
        topframe.columnconfigure(0,weight=1)
        topframe.columnconfigure(1,weight=1)
        
        # Import current list of categories if editing.
        if self.intent == 'edit':
            curr_catdict = self.catdict[self.title]
        
        # Declare rownum, add 1 after each line.
        rownum = 0
         
        # NAME
        if self.intent == 'add':
            self.name = StringVar(master=topframe,value='Unnamed')
            Label(master=topframe,text='Name',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
            Entry(master=topframe,textvariable=self.name).grid(row=rownum,column=1,sticky=EW)
            rownum += 1
        
        # THUMBNAIL
        if self.intent == 'add':
            self.thumbnail = StringVar(master=topframe,value='no_img_placeholder.png')
        elif self.intent == 'edit':
            self.thumbnail = StringVar(master=topframe,value=curr_catdict['THUMBNAIL'].replace('./resources/',''))
        
        Label(master=topframe,text='Thumbnail Image',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        thumb_entry_frame = Frame(master=topframe,bg=self.scolor)
        thumb_entry_frame.columnconfigure(1,weight=1)
        Label(master=thumb_entry_frame,text='./resources/',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=0,column=0,sticky=E)
        Entry(master=thumb_entry_frame,textvariable=self.thumbnail).grid(row=0,column=1,sticky=EW)
        thumb_entry_frame.grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # BGCOLOR
        if self.intent == 'add':    
            self.bgcolor = StringVar(master=topframe,value='#FFFFFF')
        elif self.intent == 'edit':
            self.bgcolor = StringVar(master=topframe,value=curr_catdict['BGCOLOR'])
        
        Label(master=topframe,text='Background Color (Hex)',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        Entry(master=topframe,textvariable=self.bgcolor).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # FGCOLOR
        if self.intent == 'add':    
            self.fgcolor = StringVar(master=topframe,value='#000000')
        elif self.intent == 'edit':
            self.fgcolor = StringVar(master=topframe,value=curr_catdict['FGCOLOR'])

        Label(master=topframe,text='Text Color (Hex)',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        Entry(master=topframe,textvariable=self.fgcolor).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # DESCRIPTION
        if self.intent == 'add':    
            self.description = StringVar(master=topframe,value='No Description')
        elif self.intent == 'edit':
            self.description = StringVar(master=topframe,value=curr_catdict['DESCRIPTION'])

        Label(master=topframe,text='Description',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        Entry(master=topframe,textvariable=self.description).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # BOOLTHUMB
        if self.intent == 'add':    
            self.boolthumb = StringVar(master=topframe,value='True')
        elif self.intent == 'edit':
            self.boolthumb = StringVar(master=topframe,value=str(curr_catdict['BOOLTHUMB']))
        
        Label(master=topframe,text='Show Thumbnail',bg=self.scolor,font=(self.font,10),fg=self.tcolor).grid(row=rownum,column=0,sticky=W)
        ttk.Combobox(master=topframe,textvariable=self.boolthumb,values=['True','False']).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
    
        topframe.grid(row=0,column=0,sticky=EW)
    
    def validate_info(self):
        try:
            if self.intent == 'add':
                new_name = self.name.get()
                if new_name in self.catdict.keys():
                    errormsg = new_name+' already exists!'
                    raise ValueError
            
            errormsg = 'Invalid thumbnail filepath!'
            # Find the thumbnail in /resources/
            with open('./resources/'+self.thumbnail.get()) as f:
                print('passed')
                pass
            
            # Verify Hex value of Color is valid.
            valid_bgcolor = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$',self.bgcolor.get())
            if not valid_bgcolor:
                errormsg = 'Hex value for Background Color is invalid!'
                raise ValueError
            
            # Verify Hex value of Color is valid.
            valid_fgcolor = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$',self.fgcolor.get())
            if not valid_fgcolor:
                errormsg = 'Hex value for Text Color is invalid!'
                raise ValueError
            
            new_boolthumb = self.boolthumb.get()
            if new_boolthumb != 'True' and new_boolthumb != 'False':
                errormsg = 'Check the value of "Show Thumbnail"!'
                raise ValueError
            
            if self.intent == 'add':
                sm.add_new_category(new_name,('./resources/'+self.thumbnail.get()),self.bgcolor.get(),self.fgcolor.get(),self.description.get(),new_boolthumb)
                self.window_addc.destroy()
                messagebox.showinfo('Settings - '+self.windowtitle, new_name+" has been added! :D")
            elif self.intent == 'edit':
                fm.value_change_inplace('CATEGORY.csv',('./resources/'+self.thumbnail.get()),self.title,'THUMBNAIL','NAME')
                fm.value_change_inplace('CATEGORY.csv',self.bgcolor.get(),self.title,'BGCOLOR','NAME')
                fm.value_change_inplace('CATEGORY.csv',self.fgcolor.get(),self.title,'FGCOLOR','NAME')
                fm.value_change_inplace('CATEGORY.csv',self.description.get(),self.title,'DESCRIPTION','NAME')
                fm.value_change_inplace('CATEGORY.csv',new_boolthumb,self.title,'BOOLTHUMB','NAME')
                
                self.window_addc.destroy()
                messagebox.showinfo('Settings - '+self.windowtitle, self.title+" has been edited! :3")
                
        except (ValueError,IOError):
            messagebox.showerror("Error!", errormsg)
    def add_cat(self,master,primary_color,secondary_color,font,textcolor,textsize,resizable,windowtitle,intent,title):
        
        # __init__
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
        self.window_addc = Toplevel()
        self.window_addc.grab_set()
        self.window_addc.title('Add To Watchlist - '+self.windowtitle)
        self.window_addc.geometry('550x400')
        self.window_addc.resizable(self.bool_resize,self.bool_resize)
        self.window_addc.columnconfigure(0,weight=1)
        self.window_addc.rowconfigure(0,weight=1)
        self.window_addc.rowconfigure(1,weight=50)
        self.window_addc.rowconfigure(2,weight=1)
        
        # Create the mainframe
        add_category.addc_mainframe(self)
        
        # Navbar bottom frame
        buttonframe = Frame(master=self.window_addc,background=self.scolor,relief=RAISED,border=8)
        buttonframe.columnconfigure(0,weight=1)
        buttonframe.columnconfigure(1,weight=2)
        buttonframe.columnconfigure(2,weight=1)
        
        # Navbar bottom buttons
        Button(master=buttonframe,text=' Save ',font=(self.font,self.tsize),fg=self.tcolor,background='#3eb513',activebackground='darkgreen',command=lambda:add_category.validate_info(self)).grid(row=0,column=0,sticky=EW)
        Button(master=buttonframe,text='Cancel',font=(self.font,self.tsize),fg=self.tcolor,background='#a82c14',activebackground='#601000',activeforeground='white',command=self.window_addc.destroy).grid(row=0,column=2,sticky=EW)
        
        # Display Entry fields
        add_category.enter_cat_info(self)
        
        # Display Navbar bottom butons
        buttonframe.grid(row=2,column=0,sticky=NSEW)