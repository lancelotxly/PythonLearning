'''
I/O: file loading and save, StringIO and ByteIO,
'''


'''
file loading and save:
        os: 1. operate path
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