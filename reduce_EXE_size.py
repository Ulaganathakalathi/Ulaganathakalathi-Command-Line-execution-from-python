# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 11:30:53 2021

@author: InnoP
"""

def toc_write_to_file(out_file_name, toc_var):
    with open(out_file_name, 'w') as f:
        for x in toc_var:
        	f.write(str(x))
        	f.write('\n')
    f.close()

def reduce_exe_size(input_a):
    
    # ka = toc_write_to_file('a_datas.txt', input_a.datas)
    # ka = toc_write_to_file('a_binaries.txt', input_a.datas)
    
    a_data_exclude = []
    
    exclude_toc = remove_required_item_folder(input_a.datas, 'tcl', exclude_extention=['.tcl'], exclude_file=['tclIndex'])
    a_data_exclude += exclude_toc
    
    exclude_toc = remove_required_item_folder(input_a.datas, 'idlelib', exclude_extention=['.log', '.def'])
    a_data_exclude += exclude_toc
    
    # ka = toc_write_to_file('final_a_data_excludes.txt',a_data_exclude)
    
    remov_data_list = ['WdfCoInstaller01009.dll']
    
    for each_l in remov_data_list:
        a_data_exclude += remove_required_item(input_a.datas, each_l)
        
    # a.datas -= a_data_exclude
    
    
    #with open('a_datas_new.txt', 'w') as f:
    #    for x in a.datas:
    #    	f.write(str(x))
    #    	f.write('\n')
    #f.close()
    
    a_binary_exclude = []
    binary_exc_list = ['mfc140u.dll', 'libcrypto-1_1.dll', 'win32ui', 'unicodedata', 'libssl-1_1.dll', '_decimal.pyd', '_decimal.pyd', '_cffi_backend.cp39-win_amd64.pyd']
    
    remov_list = ['_elementtree.pyd', '_lzma.pyd', '_ssl.pyd', '_testcapi.pyd', '_bz2.pyd', '_hashlib.pyd', '_asyncio.pyd', '_overlapped.pyd', '_queue.pyd', '_testinternalcapi.pyd']
    remov_list += ['_multiprocessing.pyd','_uuid.pyd', 'win32trace.pyd', '_win32sysloader.pyd']
    remov_list += [ 'VCRUNTIME140.dll']
    binary_exc_list += remov_list
    for each_l in binary_exc_list:
        a_binary_exclude += remove_required_item(input_a.binaries, each_l)
    
    return a_data_exclude, a_binary_exclude
    # a.binaries -= binary_exc_tree

    #print('a data')
    #print(a.datas)



def remove_required_item(input_list, file_name, prefix_folder=''):
    # print('input type', type(input_list))
    remove_list = []
    for each_l in input_list:
        if file_name.lower() in each_l[1].lower():
            if prefix_folder !='':
                if prefix_folder.lower() in each_l[0].lower():
                    remove_list += (each_l(0),each_l(1),each_l(2))
            else:
                remove_list += [(each_l[0],each_l[1],each_l[2])]
    # print('remove list:', remove_list)
    return remove_list

def remove_required_item_folder(input_list, main_folder_name, exclude_extention=[], exclude_file=[]):
    remove_list = []
    for each_l in input_list: #each item in the input list
        file_info = each_l[0]
        remove_item = False
        if file_info[0:len(main_folder_name)].lower() == main_folder_name.lower(): #check for folder name
            remove_item = True
            for each_exclude in exclude_extention:
                if file_info[-len(each_exclude):].lower() == each_exclude.lower(): #check for exclude extention
                    remove_item = False
                    break
            if remove_item:
                for each_exclude in exclude_file:
                    if file_info[-len(each_exclude):].lower() == each_exclude.lower(): #check for exclude extention
                        remove_item = False
                        break
        if remove_item:
            remove_list += [(each_l[0],each_l[1],each_l[2])]
    return remove_list

            
        
    