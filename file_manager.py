import csv

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