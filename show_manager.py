import csv
from file_manager import file_manager as fm
from datetime import datetime

class show_manager:
    
    def update_accessdate(title):
        fm.value_change_inplace('MEDIALISt.csv',datetime.now(),title,'ACCESSDATE','MEDIATITLE')
    
    def return_sorted_mediadict_recent():
        mediadict = fm.import_medialist_from_csv('MEDIALIST.csv')
        sorted(mediadict.items(), key=lambda x:x[1]['ACCESSDATE'])
        return mediadict
    
    def return_favoritelist():
        medialist = fm.import_medialist_from_csv('MEDIALIST.csv')
        output = []
        for key,val in medialist.items():
            if val['BOOLFAVORITE'] == True:
                output.append(key)
        return output