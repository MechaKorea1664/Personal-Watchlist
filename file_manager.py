import csv
import pandas as pd

class file_manager:
    
    # file_to_dict is no longer in use...
    def file_to_dict(filename):
        output = {}
        with open(filename,'r') as f:
            content = csv.reader(f,delimiter='\n')
            dict_name = None
            var_name = None
            var_value = None
            for i in content:   
                dict_nameval_list = i[0].split('_')
            
                # Below reads and comprehends data read from the filename.txt file containing values.
                if dict_nameval_list[0] == 'DICT' and dict_nameval_list[0] != None:
                    dict_name = dict_nameval_list[1]
                elif dict_nameval_list[0] == 'VAR' and dict_nameval_list[0] != None:
                    var_nameval_list = dict_nameval_list[1].split(':')
                    var_name = var_nameval_list[0]
                    var_value = var_nameval_list[1]
                
                # Below creates a dictionary of values, key of outer dictionary are categories, and contains
                # inner dictionaries as a value that contain values that are within that category.
                if dict_name in output:
                    output[dict_name].update({var_name:var_value})
                else:
                    output[dict_name] = {}        
        return output
    
    def return_row_index_dict(filename,t_column):
        t_file = pd.read_csv(filename)
        contents = t_file.to_dict('records')
        output = {}
        curr_index = 0
        for i in contents:
            output.update({curr_index:i[t_column]})
            curr_index += 1
        return output
    
    def value_change_inplace(filename,value,target_row,target_column,index_column_header):
        t_file = pd.read_csv(filename,index_col=index_column_header)
        t_file.loc[target_row, target_column] = value
        t_file.to_csv(filename,index=True)
        print(f'Successfully changed value at row: {target_row}, column: {target_column} to {value}.')
        
    def import_settings_from_csv(filename):
        t_file = pd.read_csv(filename)
        contents = t_file.to_dict('records')
        output = {}
        for i in contents:
            if i['GROUP'] in output:
                output[i['GROUP']].update({i['NAME']:i['VALUE']})
            else:
                output[i['GROUP']] = {i['NAME']:i['VALUE']}
        return output
    
    def import_medialist_from_csv(filename):
        t_file = pd.read_csv(filename)
        contents = t_file.to_dict('records')
        output = {}
        for i in contents:
            output.update({i['MEDIATITLE']:{}})
            for u in i.keys():
                if u != 'MEDIATITLE':
                    output[i['MEDIATITLE']].update({u:i[u]})
        return output
    
    def import_txt_to_list(filename,dni,delim):
        output = []
        with open(filename,'r') as f:
            content = csv.reader(f,delimiter=delim)
            for i in content:
                output.append(i[0])
        output.remove(dni)
        return output
    
    def import_category_from_csv(filename):
        t_file = pd.read_csv(filename)
        contents = t_file.to_dict('records')
        output = {}
        for i in contents:
            output.update({i['NAME']:{}})
            for u in i.keys():
                if u != 'NAME':
                    output[i['NAME']].update({u:i[u]})
        return output
            
# EXAMPLE OF VALUE_CHANGE_INPLACE:               
# file_manager.value_change_inplace('MEDIALIST.csv','True','Squid Game 2','BOOLFAVORITE','MEDIATITLE')
# 
# OTHER EXAMPLES:
# print(file_manager.import_settings_from_csv('SETTINGS.csv'))
# print(file_manager.import_txt_to_list('FONTS.txt','@@ DO NOT LEAVE EMPTY LINES! @@','\n'))