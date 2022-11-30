from tkinter import *
from file_manager import file_manager as fm

class Settings_window:
    def settings_mainframe(self,color):
        self.topframe = Frame(self.window_settings,background=color,relief=RIDGE,border=5)
        self.topframe.grid(row=1,column=0,sticky=NSEW)
    
    def reset_topframe(self):
        for i in self.topframe.winfo_children():
            i.destroy()
        
    def settings_app(self):
        Settings_window.reset_topframe(self)
        for key,val in self.settingdict['APPEARANCE'].items():
            
            'TODO: Figure out how to use entry widgets with for loop!'
            
            pass
        
    def settings(self,color,font):
        self.settingdict = fm.import_settings_from_csv('SETTINGS.csv')
        
        self.window_settings = Toplevel(self.master)
        self.window_settings.grab_set()
        self.window_settings.title('Settings - PersonalWatchlist')
        self.window_settings.geometry('350x450')
        self.window_settings.resizable(True,True)
        self.window_settings.columnconfigure(0,weight=1)
        self.window_settings.rowconfigure(0,weight=1)
        self.window_settings.rowconfigure(1,weight=50)
        self.window_settings.rowconfigure(2,weight=1)
        Settings_window.settings_mainframe(self,color)
        # Navbar Top, navigation
        frame_navbar_top = Frame(master=self.window_settings,background='white',relief=SUNKEN,border=5)
        frame_navbar_top.columnconfigure(0,weight=1)
        frame_navbar_top.columnconfigure(1,weight=1)
        frame_navbar_top.columnconfigure(2,weight=1)
        frame_navbar_top.rowconfigure(0,weight=1)
        Button(master=frame_navbar_top,text='Appearance',font=(font,10),command=Settings_window.settings_app(self)).grid(row=0,column=0,sticky=NSEW)
        Button(master=frame_navbar_top,text='Display',font=(font,10)).grid(row=0,column=1,sticky=NSEW)
        Button(master=frame_navbar_top,text='Other',font=(font,10)).grid(row=0,column=2,sticky=NSEW)
        frame_navbar_top.grid(row=0,column=0,sticky=NSEW)
        # Navbar Bottom, save or cancel all changes
        frame_top_bottom = Frame(master=self.window_settings,background='white',relief=RAISED,border=8)
        frame_top_bottom.columnconfigure(0,weight=10)
        frame_top_bottom.columnconfigure(1,weight=1)
        frame_top_bottom.rowconfigure(0,weight=1)
        frame_navbar_bottom = Frame(master=frame_top_bottom,background='white',relief=SUNKEN,border=5)
        frame_navbar_bottom.columnconfigure(0,weight=1)
        frame_navbar_bottom.columnconfigure(1,weight=1)
        frame_navbar_bottom.rowconfigure(0,weight=1)
        Label(master=frame_navbar_bottom,text='im here').grid(row=0,column=0,sticky=NSEW)
        Button(master=frame_navbar_bottom,text='Save Changes',font=(font,10),background='#3eb513',activebackground='darkgreen').grid(row=0,column=0,sticky=NSEW)
        Button(master=frame_navbar_bottom,text='Discard Changes',font=(font,10),background='#a82c14',activebackground='#601000',foreground='white',activeforeground='white',command=self.window_settings.destroy).grid(row=0,column=1,sticky=NSEW)
        frame_navbar_bottom.grid(row=0,column=1,sticky=NSEW)
        frame_top_bottom.grid(row=2,column=0,sticky=NSEW)