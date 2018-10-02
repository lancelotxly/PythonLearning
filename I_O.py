'''
I/O: os operation, file loading and save, StringIO and ByteIO,
'''


'''
os:         1. operate path
               abspath = os.path.abspath('.')  # current abspath
               dirpath = os.path.join(abspath,'filedir')  # join path based on current path
               filepath = os.path.join(dirpath,'test.py')  # build filepath
               [dirpath, file] = os.path.split('filepath')  # split path into dirpath and file
               [filename, type] = os.path.splitext('file')    # split file into filename and type
               boolean = os.path.isdir(dirpath)   # judge whether dir
               boolean = os.path.isfile(filepath)  # judge whether file
               boolean = os.path.exists(dirpath)   # judge whether the path exists
               
            2. file operate
               os.mkdir(dirpath)   # make a dir
               os.rmdir(dirpath)   # delete the dir, the dir must be empty
               os.rename(filepath, new_filepath)  # rename a file, the original don't exist anymore 
               os.remove(filepath)  # remove a file
               shutil.copyfile(filepath, new_filepath)  # copy the file
               
               os.listdir('.')  list all file and dir in currently abspath
               
'''
# import os
# abspath = os.path.abspath('.')
# dirpath = os.path.join(abspath, 'testdir')
# filepath = os.path.join(dirpath,'test.py')
# if os.path.exists(dirpath) == False:
#     os.mkdir(dirpath)
#     with open(filepath,'w'):
#         pass
#
# [dirpath, file] = os.path.split(filepath)
# print(dirpath, file)
# [filename, type] = os.path.splitext(file)
# print(filename, type)
#
# b = os.path.isdir(dirpath)
# b1 = os.path.isfile(filepath)
# print(b, b1)
#
# new_filepath = os.path.join(dirpath,'test2.py')
# import shutil
# shutil.copyfile(filepath, new_filepath)
# rename_file = os.path.join(dirpath,'test_new.py')
# os.rename(new_filepath,rename_file)
# os.remove(rename_file)
# os.remove(filepath)
# os.rmdir(dirpath)

# import os
# file=[x for x in os.listdir('.')]
# print(file)
# pythonfile = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
# print(pythonfile)

'''
file loading and save: 1. try: 
                              f = open('filename.format','r/rb/w/wb')
                              for item in f:   # f.read();  f.readline()
                          except  IOError as e:
                              print(str(e))
                          finally:
                              f.close()
                              
                      2. with open('filename.format', 'r/rb/w/wb') as f:    
                              
                      # strip('a') delete 'a' from str; default(\n \t)
                      # split('b') split str into item according to 'b', and save each item into a list
                      
                      save and load:  
                                #pickle(unimportant)  rb/wb
                                import pickle
                                with open('data.pickle','wb') as f:
                                   pickle.dump(data,f)
                                
                                with open('data.pickle','rb') as f:
                                   data = pickle.load(f)
                                   
                                #json(usual)  r/w
                                import json
                                with open('data.json', 'w') as f:
                                    json.dump(data, f)
                                
                                with open('data.json', 'r') as f:
                                    data = json.load(f)
                                print(data)
'''
# with open('sport_data.txt','r') as f:
#     data = {}
#     for item in f:
#         data_item = item.strip().split(',')
#         score = data_item[1:len(data_item)]
#         data[data_item[0]]=score
# print(data)

# import pickle
# with open('data.pickle','wb') as f:
#     pickle.dump(data, f)
#
# with open('data.pickle','rb') as f:
#     data = pickle.load(f)
# print(data)

# import json
# with open('data.json','w') as f:
#     json.dump(data,f)
#
# with open('data.json','r') as f:
#     data = json.load(f)
# print(data)