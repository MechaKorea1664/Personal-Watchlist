import csv
from file_manager import file_manager as fm
import datetime

class show_manager:
    def __init__(self,dict_showinfo):
        self.showdict = dict_showinfo

    def add_mediainfo(self,u_input_dict):
        fm.append_to_file(u_input_dict,'MEDIA_INFO.txt')
        
    def return_recent(self):
        pass
