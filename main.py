from tkinter import *
from file_manager import file_manager
from infrastructure import *


# Dictionary of settings in SETTINGS.txt.
dict_settings = file_manager.import_settings_from_csv('SETTINGS.csv')
user_profile = file_manager.file_to_dict('PROFILE.txt')
show_info = file_manager.file_to_dict('MEDIA_INFO.txt')

# Main window configuration
window_main = Tk()
window_main.title(dict_settings['OTHER']['WINDOWTITLE'])
window_main.geometry(dict_settings['DISPLAY']['WINDOWSIZE'])
window_main.resizable(dict_settings['DISPLAY']['WINDOWRESIZE'],dict_settings['DISPLAY']['WINDOWRESIZE'])
window_main.columnconfigure(1,weight=1)


# Declaration of variables with user-preferred values defined in SETTINGS.txt
pref_font = dict_settings['APPEARENCE']['FONT']
pref_resolution = dict_settings['DISPLAY']['WINDOWSIZE'].split('x') # [x,y]
pref_username = user_profile['USERINFO']['USERNAME']
pref_backgroundcolor = dict_settings['APPEARENCE']['BACKGROUNDCOLOR']

# defining imported classes
infra = infrastructure(
    window_main,
    pref_font,
    pref_username,
    pref_backgroundcolor,
    show_info
    )


# Sidebar, series of buttons.
infra.sidebar()
window_main.update()
mainloop()