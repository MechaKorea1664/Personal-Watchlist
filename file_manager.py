import csv
import pandas as pd

class file_manager:
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
    
    def value_change_inplace(filename,value,target_row,target_column):
        t_file = pd.read_csv(filename)
        indexlist = file_manager.return_row_index_dict(filename,target_column)
        for key,val in indexlist.items():
            if val == target_row:
                t_file.loc[key].at[target_column] = value
        print(t_file)
        print(t_file.to_csv(path_or_buf=None, index=False))
        print('successfully changed value')
        
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
            
                
file_manager.value_change_inplace('MEDIALIST.csv','False','Squid Game 2','BOOLFAVORITE')