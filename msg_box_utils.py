''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Header -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
import sys, os    ;     sys.path.insert(1, os.path.join(sys.path[0], os.path.dirname(os.path.abspath(__file__)))) # to allow for relative imports, delete any imports under this line

util_submodule_l = []  # list of all imports from local util_submodules that could be imported elsewhere to temporarily remove from sys.modules

# temporarily remove any modules that could conflict with this file's local util_submodule imports
og_sys_modules = sys.modules    ;    pop_l = [] # save the original sys.modules to be restored at the end of this file
for module_descrip in sys.modules.keys():  
    if any( util_submodule in module_descrip for util_submodule in util_submodule_l )    :    pop_l.append(module_descrip) # add any module that could conflict local util_submodule imports to list to be removed from sys.modules temporarily
for module_descrip in pop_l    :    sys.modules.pop(module_descrip) # remove all modules put in pop list from sys.modules
util_submodule_import_check_count = 0 # count to make sure you don't add a local util_submodule import without adding it to util_submodule_l

''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard: Local Utility Submodule Imports  -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''

# import custom_exceptions as ce                                         ; util_submodule_import_check_count += 1

''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if util_submodule_import_check_count != len(util_submodule_l)    :    raise Exception("ERROR:  You probably added a local util_submodule import without adding it to the util_submodule_l")
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''



import ctypes



TYPE_NUM__OK                 = 0 
TYPE_NUM__OK_CANCEL          = 1 
TYPE_NUM__ABORT_RETRY_IGNORE = 2 
TYPE_NUM__YES_NO_CANCEL      = 3 
TYPE_NUM__YES_NO             = 4 
TYPE_NUM__RETRY_CANCEL       = 5 
TYPE_NUM__CRITICAL_MSG_ICON  = 16
TYPE_NUM__WARNING_QUERY_ICON = 2 
TYPE_NUM__WARNING_MSG_ICON   = 48
TYPE_NUM__INFO_MSG_ICON      = 64

BTN_NUM_NAME_D = {
                     1 : 'ok'    , # also X for OK
                     2 : 'cancel', # also X for anything with CANCEL btn
                     3 : 'abort' ,
                     4 : 'retry' ,
                     5 : 'ignore',
                     6 : 'yes'   ,
                     7 : 'no'    
                 }




''' Internal '''
def root_msg_box(type_num, title, msg, output_define_d = None):
    MessageBox = ctypes.windll.user32.MessageBoxW
    out_num = MessageBox(None, msg, title, type_num)
    out_str = BTN_NUM_NAME_D[out_num]
    
    if output_define_d == None:
        return out_str
    else:
        if out_str in output_define_d.keys():
            return output_define_d[out_str]
        else:
            raise Exception('ERROR:  "' + out_str + '" returned by the msg box is not a key in given output_define_d: ' + output_define_d)
        










''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Footer -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
sys.modules = og_sys_modules
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if __name__ == '__main__':
    print('In Main:  msg_box_utils')
    
#     type_num = TYPE_NUM__OK                
#     type_num = TYPE_NUM__OK_CANCEL         
#     type_num = TYPE_NUM__ABORT_RETRY_IGNORE
    type_num = TYPE_NUM__YES_NO_CANCEL     
#     type_num = TYPE_NUM__YES_NO            
#     type_num = TYPE_NUM__RETRY_CANCEL      
#     type_num = TYPE_NUM__CRITICAL_MSG_ICON 
#     type_num = TYPE_NUM__WARNING_QUERY_ICON
#     type_num = TYPE_NUM__WARNING_MSG_ICON  
#     type_num = TYPE_NUM__INFO_MSG_ICON     
    
    
    
    title = 'test title'
    msg = 'test msg'
    output_define_d = {'yes': True,
                       'no' : False,
                       'cancel': False
                       }
    
    print(root_msg_box(type_num, title, msg, output_define_d))
    
    
    
    
    
    
    
    
    print('End of Main:  msg_box_utils')