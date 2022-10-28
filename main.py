from doctest import master
from tkinter import *
from file_manager import file_to_dict
from infrastructure import *

# Dictionary of settings in SETTINGS.txt.
dict_settings = file_to_dict('SETTINGS.txt')
user_profile = file_to_dict('PROFILE.txt')

# Main window configuration
window_main = Tk()
window_main.title(dict_settings['OTHER']['WINDOWTITLE'])
window_main.geometry(dict_settings['DISPLAY']['WINDOWSIZE'])
window_main.resizable(dict_settings['DISPLAY']['WINDOWRESIZE'],dict_settings['DISPLAY']['WINDOWRESIZE'])

# Declaration of variables with user-preferred values defined in SETTINGS.txt
pref_font = dict_settings['APPEARENCE']['FONT']
pref_resolution = dict_settings['DISPLAY']['WINDOWSIZE'].split('x') # [x,y]
pref_username = user_profile['USERINFO']['USERNAME']


# Creating master_frame
master_frame = Frame(
    master=window_main,
    background='pink',
    width=int(pref_resolution[0]),
    height=int(pref_resolution[1])
    )
master_frame.rowconfigure(0,weight=1)
master_frame.columnconfigure(0,weight=1)
master_frame.grid_propagate(False)
master_frame.pack(fill="both", expand=True)

print('width',window_main.winfo_width(),' height',window_main.winfo_height())
# defining imported classes
infra = infrastructure(
    master_frame,
    master_frame.winfo_width(),
    master_frame.winfo_height(),
    (pref_font,10),
    pref_username
    )

# Sidebar, series of buttons.
infra.sidebar().grid(column=0,row=0)


mainloop()