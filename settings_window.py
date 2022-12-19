from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
from file_manager import file_manager as fm
import re

class Settings_window:
    
    def settings_mainframe(self):
        self.topframe = Frame(self.window_settings,background=self.pcolor,relief=RIDGE,border=5,padx=10,pady=10)
        self.topframe.columnconfigure(0,weight=1)
        self.topframe.grid(row=1,column=0,sticky=NSEW)
    
    def reset_topframe(self):
        for i in self.topframe.winfo_children():
            i.destroy()
        
    def settings_app(self):
        Settings_window.reset_topframe(self)
        app_dict = self.settingdict['APPEARANCE']
        
        # main frame for appearance settings page
        frame_app = Frame(self.topframe,border=5,relief=GROOVE,background=self.scolor)
        frame_app.columnconfigure(0,weight=1)
        frame_app.columnconfigure(1,weight=1)
        
        # Background color setting
        Label(master=frame_app,text='Background Color (Hex)',font=(self.font,10),fg=self.textcolor,background=self.scolor).grid(row=0,column=0,sticky=W)
        self.bgcolor = StringVar(frame_app,value=app_dict['BACKGROUNDCOLOR'])
        Entry(frame_app,textvariable=self.bgcolor,width=10).grid(row=0,column=1,sticky=EW)
        
        # Secondary color setting
        Label(master=frame_app,text='Secondary Color (Hex)',font=(self.font,10),fg=self.textcolor,background=self.scolor).grid(row=1,column=0,sticky=W)
        self.secondcolor = StringVar(frame_app,value=app_dict['SECONDARYCOLOR'])
        Entry(master=frame_app,textvariable=self.secondcolor,width=10).grid(row=1,column=1,sticky=EW)        
        
        # CategoryImage toggle
        ddoption = ['True','False']
        Label(master=frame_app,text='Show Category Image',font=(self.font,10),fg=self.textcolor,background=self.scolor).grid(row=2,column=0,sticky=W)
        self.catimg = StringVar(frame_app,value=app_dict['CATEGORYIMAGE'])
        ttk.Combobox(master=frame_app,textvariable=self.catimg,values=ddoption).grid(row=2,column=1,sticky=EW)
        
        # Font changer
        # Importing list of font names from FONTS.txt
        self.font_list = list(tkFont.families())
        self.font_list.sort()
        Label(master=frame_app,text='Font',font=(self.font,10),fg=self.textcolor,background=self.scolor).grid(row=3,column=0,sticky=W)
        self.newfont = StringVar(frame_app,value=app_dict['FONT'])
        ttk.Combobox(master=frame_app,textvariable=self.newfont,values=self.font_list).grid(row=3,column=1,sticky=EW)
        
        # Text color changer
        self.new_textcolor = StringVar(frame_app,value=app_dict['TEXTCOLOR'])
        Label(master=frame_app,text='Text Color (Hex)',font=(self.font,10),fg=self.textcolor,background=self.scolor).grid(row=4,column=0,sticky=W)
        Entry(frame_app,textvariable=self.new_textcolor,width=10).grid(row=4,column=1,sticky=EW)
        
        # Text size changer
        Label(master=frame_app,text='Text Size (5 ~ 20)',font=(self.font,10),fg=self.textcolor,background=self.scolor).grid(row=5,column=0,sticky=W)
        self.newtextsize = IntVar(frame_app,value=app_dict['TEXTSIZE'])
        Entry(frame_app,textvariable=self.newtextsize,width=10).grid(row=5,column=1,sticky=EW)
        
        frame_app.grid(row=0,column=0,sticky=EW)
        
    def settings_disp(self):
        Settings_window.reset_topframe(self)    
        disp_dict = self.settingdict['DISPLAY']
        
        # Main frame for display settings page
        frame_disp = Frame(self.topframe,border=5,relief=GROOVE,background=self.scolor)
        frame_disp.columnconfigure(0,weight=1)
        frame_disp.columnconfigure(1,weight=1)
        rownum = 0
        
        # Window size setting
        curr_res = disp_dict['WINDOWSIZE'].split('x')
        curr_xval = curr_res[0]
        curr_yval = curr_res[1]
        Label(master=frame_disp,text='Resolution (100~2000)',font=(self.font,10),fg=self.textcolor,background=self.scolor).grid(row=rownum,column=0,sticky=W)
        self.new_xval = StringVar(frame_disp,value=curr_xval)
        self.new_yval = StringVar(frame_disp,value=curr_yval)
        frame_res_entry = Frame(frame_disp)
        frame_res_entry.columnconfigure(0,weight=1)
        frame_res_entry.columnconfigure(2,weight=1)
        frame_res_entry.propagate(False)
        Entry(frame_res_entry,textvariable=self.new_xval,width=6).grid(row=0,column=0,sticky=EW)
        Label(frame_res_entry,text='x',font=(self.font,10),fg=self.textcolor,background=self.scolor).grid(row=0,column=1,sticky=EW)
        Entry(frame_res_entry,textvariable=self.new_yval,width=6).grid(row=0,column=2,sticky=EW)
        frame_res_entry.grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # Window resize toggle
        self.new_boolresize = StringVar(frame_disp,value=disp_dict['WINDOWRESIZE'])
        Label(master=frame_disp,text='Resize Windows',font=(self.font,10),fg=self.textcolor,background=self.scolor).grid(row=rownum,column=0,sticky=W)
        ttk.Combobox(master=frame_disp,textvariable=self.new_boolresize,values=['True','False']).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # Category, number of columns
        self.new_catnumcol = StringVar(frame_disp,value=disp_dict['CATNUMCOL'])
        Label(frame_disp,text='Number of Category Columns:',font=(self.font,10),fg=self.textcolor,background=self.scolor).grid(row=rownum,column=0,sticky=W)
        Entry(frame_disp,textvariable=self.new_catnumcol).grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        # Category, resolution resize
        cat_res = disp_dict['CATSIZE'].split('x')
        cat_xval = cat_res[0]
        cat_yval = cat_res[1]
        Label(master=frame_disp,text='Category Resolution (50~500)',font=(self.font,10),fg=self.textcolor,background=self.scolor).grid(row=rownum,column=0,sticky=W)
        self.new_cat_xval = StringVar(frame_disp,value=cat_xval)
        self.new_cat_yval = StringVar(frame_disp,value=cat_yval)
        frame_cat_res_entry = Frame(frame_disp)
        frame_cat_res_entry.columnconfigure(0,weight=1)
        frame_cat_res_entry.columnconfigure(2,weight=1)
        frame_cat_res_entry.propagate(False)
        Entry(frame_cat_res_entry,textvariable=self.new_cat_xval,width=6).grid(row=0,column=0,sticky=EW)
        Label(frame_cat_res_entry,text='x',font=(self.font,10),fg=self.textcolor,background=self.scolor).grid(row=0,column=1,sticky=EW)
        Entry(frame_cat_res_entry,textvariable=self.new_cat_yval,width=6).grid(row=0,column=2,sticky=EW)
        frame_cat_res_entry.grid(row=rownum,column=1,sticky=EW)
        rownum += 1
        
        frame_disp.grid(row=0,column=0,sticky=EW)
        
    def settings_other(self):
        Settings_window.reset_topframe(self)
        other_dict = self.settingdict['OTHER']
        
        # Main frame for other settings page
        frame_other = Frame(self.topframe,border=5,relief=GROOVE,background=self.scolor)
        frame_other.columnconfigure(0,weight=1)
        frame_other.columnconfigure(1,weight=1)
        
        # Window title setting
        self.new_windowtitle = StringVar(frame_other,value=other_dict['WINDOWTITLE'])
        Label(frame_other,text='Window Title',font=(self.font,10),fg=self.textcolor,background=self.scolor).grid(row=0,column=0,sticky=W)
        Entry(frame_other,textvariable=self.new_windowtitle).grid(row=0,column=1,sticky=EW)
        
        frame_other.grid(row=0,column=0,sticky=EW)
    
    def validate_new_setting(self):
        try:
            errormsg = ''
            # validate entered info from settings_app
            valid_bgcolor = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$',self.bgcolor.get())
            if not valid_bgcolor:
                errormsg = 'Background Color value is invalid!'
                raise ValueError

            valid_secondcolor = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$',self.secondcolor.get())
            if not valid_secondcolor:
                errormsg = 'Secondary Color value is invalid!'
                raise ValueError
            
            new_font = self.newfont.get()
            if new_font not in self.font_list:
                errormsg = 'Font not found!'
                raise ValueError
            
            valid_textcolor = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$',self.new_textcolor.get())
            if not valid_textcolor:
                errormsg = 'Text Color value is invalid!'
                raise ValueError

            new_catimg = self.catimg.get()
            if new_catimg != 'True' and new_catimg != 'False':
                errormsg = 'Unacceptable value for Show Category Image!'
                raise ValueError
            
            new_textsize = int(self.newtextsize.get())
            if new_textsize < 5 or new_textsize > 20:
                errormsg = 'Text size out of range!'
                raise ValueError
            
            # validate entered info from settings_disp
            new_xval = int(self.new_xval.get())
            new_yval = int(self.new_yval.get())
            
            if new_xval < 100 or new_xval > 2000:
                errormsg = 'x value of Resolution out of range!'
                raise ValueError
            if new_yval < 100 or new_yval > 2000:
                errormsg = 'y value of Resolution out of range!'
                raise ValueError
            
            new_resize = self.new_boolresize.get()
            if new_resize != 'True' and new_resize != 'False':
                errormsg = 'Unacceptable value for Resize Windows!'
                raise ValueError
            
            new_catnumcol = int(self.new_catnumcol.get())
            if new_catnumcol < 1:
                errormsg = 'Column count should be greater than 0!'
                raise ValueError
            
            new_cat_xval = int(self.new_cat_xval.get())
            new_cat_yval = int(self.new_cat_yval.get())
            if new_cat_xval < 50 or new_cat_xval > 500:
                errormsg = 'x value of Category Resolution out of range!'
                raise ValueError
            if new_cat_yval < 50 or new_cat_yval > 500:
                errormsg = 'y value of Category Resolution out of range!'
                raise ValueError
            
            # validate entered info from settings_other
            new_windowtitle = self.new_windowtitle.get()
            
            # After succesful validation, apply changes to SETTINGS.csv.
            fm.value_change_inplace('SETTINGS.csv',self.bgcolor.get(),'BACKGROUNDCOLOR','VALUE','NAME')
            fm.value_change_inplace('SETTINGS.csv',self.secondcolor.get(),'SECONDARYCOLOR','VALUE','NAME')
            fm.value_change_inplace('SETTINGS.csv',self.new_textcolor.get(),'TEXTCOLOR','VALUE','NAME')
            fm.value_change_inplace('SETTINGS.csv',new_catimg,'CATEGORYIMAGE','VALUE','NAME')
            fm.value_change_inplace('SETTINGS.csv',self.newfont.get(),'FONT','VALUE','NAME')
            fm.value_change_inplace('SETTINGS.csv',self.newtextsize.get(),'TEXTSIZE','VALUE','NAME')
            fm.value_change_inplace('SETTINGS.csv',(str(new_xval)+'x'+str(new_yval)),'WINDOWSIZE','VALUE','NAME')
            fm.value_change_inplace('SETTINGS.csv',new_resize,'WINDOWRESIZE','VALUE','NAME')
            fm.value_change_inplace('SETTINGS.csv',new_windowtitle,'WINDOWTITLE','VALUE','NAME')
            fm.value_change_inplace('SETTINGS.csv',(str(new_cat_xval)+'x'+str(new_cat_yval)),'CATSIZE','VALUE','NAME')
            fm.value_change_inplace('SETTINGS.csv',new_catnumcol,'CATNUMCOL','VALUE','NAME')
            
            print('All settings successfully validated.')
            
            self.window_settings.destroy()
            messagebox.showinfo('Settings - '+self.windowtitle,"Settings saved!\nRestart program to see the changes :)")
        except:
            messagebox.showerror("Error!", errormsg)
            
            
    
    def settings(self,master,pcolor,scolor,font,textcolor,textsize,resizable,windowtitle):
        
        # __init__
        self.settingdict = fm.import_settings_from_csv('SETTINGS.csv')
        self.master = master
        self.pcolor = pcolor
        self.scolor = scolor
        self.font = font
        self.textcolor = textcolor
        self.textsize = textsize
        self.resizable = resizable
        self.windowtitle = windowtitle
        
        # Create and configure Settings window
        self.window_settings = Toplevel()
        self.window_settings.grab_set()
        self.window_settings.title('Settings - '+self.windowtitle)
        self.window_settings.geometry('400x400')
        self.window_settings.resizable(self.resizable,self.resizable)
        self.window_settings.columnconfigure(0,weight=1)
        self.window_settings.rowconfigure(0,weight=1)
        self.window_settings.rowconfigure(1,weight=50)
        self.window_settings.rowconfigure(2,weight=1)
        Settings_window.settings_mainframe(self)
        
        # Navbar Top, navigation
        frame_navbar_top = Frame(master=self.window_settings,background=self.scolor,relief=SUNKEN,border=5)
        frame_navbar_top.columnconfigure(0,weight=1)
        frame_navbar_top.columnconfigure(1,weight=1)
        frame_navbar_top.columnconfigure(2,weight=1)
        frame_navbar_top.rowconfigure(0,weight=1)
        Button(master=frame_navbar_top,text='Appearance',font=(self.font,self.textsize),fg=self.textcolor,background=self.scolor,command=lambda:Settings_window.settings_app(self)).grid(row=0,column=0,sticky=NSEW)
        Button(master=frame_navbar_top,text='Display',font=(self.font,self.textsize),fg=self.textcolor,background=self.scolor,command=lambda:Settings_window.settings_disp(self)).grid(row=0,column=1,sticky=NSEW)
        Button(master=frame_navbar_top,text='Other',font=(self.font,self.textsize),fg=self.textcolor,background=self.scolor,command=lambda:Settings_window.settings_other(self)).grid(row=0,column=2,sticky=NSEW)
        frame_navbar_top.grid(row=0,column=0,sticky=NSEW)
        
        # Navbar Bottom, save or cancel all changes
        frame_top_bottom = Frame(master=self.window_settings,background=self.scolor,relief=RAISED,border=8)
        frame_top_bottom.columnconfigure(0,weight=10)
        frame_top_bottom.columnconfigure(1,weight=1)
        frame_top_bottom.rowconfigure(0,weight=1)
        frame_navbar_bottom = Frame(master=frame_top_bottom,background=self.scolor,relief=SUNKEN,border=5)
        frame_navbar_bottom.columnconfigure(0,weight=1)
        frame_navbar_bottom.columnconfigure(1,weight=1)
        frame_navbar_bottom.rowconfigure(0,weight=1)
        Label(master=frame_navbar_bottom,background=self.scolor).grid(row=0,column=0,sticky=NSEW)
        Button(master=frame_navbar_bottom,text='Save',font=(self.font,self.textsize),fg=self.textcolor,background='#3eb513',activebackground='darkgreen',command=lambda:Settings_window.validate_new_setting(self)).grid(row=0,column=0,sticky=NSEW)
        Button(master=frame_navbar_bottom,text='Discard',font=(self.font,self.textsize),fg=self.textcolor,background='#a82c14',activebackground='#601000',foreground='white',activeforeground='white',command=self.window_settings.destroy).grid(row=0,column=1,sticky=NSEW)
        frame_navbar_bottom.grid(row=0,column=1,sticky=NSEW)
        frame_top_bottom.grid(row=2,column=0,sticky=NSEW)
        
        # Preload all tabs
        Settings_window.settings_app(self)
        Settings_window.settings_disp(self)
        Settings_window.settings_other(self)
        Settings_window.reset_topframe(self)
        
