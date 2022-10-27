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
# Sidebar, series of buttons.
home(
    window_main,
    ('Lucida font',10)
    ).grid(column=1,row=1)

mainloop()