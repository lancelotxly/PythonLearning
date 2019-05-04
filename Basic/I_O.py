'''
I/O: File loading and save, StringIO and ByteIO,
'''
'''
File Operation: START AT CURSOR
                1. Read
                   with open('filepath','r', encoding='utf-8') as f:
                        f.read()      # Read all
                        f.readline()  # Read a line
                        f.readlines() # Read all lines, Save into a List
                        f.readable()
                        
                2. Write: Build a new file, Cover the original one
                   with open('filepath','w', encoding='utf-8') as f:
                        f.write('str')
                        f.writelines(['str1','str2',..]) 
                
                3. Add: Add at the tail
                   with open('filepath','a', encoding = 'utf-8') as f:
                        f.write('str')
                        f.writelines(['str1','str2',..])
                        
                4. Read & Write: 能同时读写，但要with结束，提交后文件才会更改，因此写了不能立即读出来
                   1) 'r+':  文件必须存在
                       with open('filepath','r+',encoding='utf-8') as f:      
                   2） 'w+': 文件肯定被重置
                
                5. Operate in binary: 
                   with open('filepath','rb/wb/ab') as f:
                   
                6. Operate Cursor: ONLY IN BINARY
                   f.tell()    # Return the Cursor's location
                   seek(i)     # Move Cursor from Start-point, i steps
                   seek(i,1)   # Move Cursor from Now-point, i steps
                   seek(-i,2)  # Move Cursor from End-point, -i steps
'''
# def read_last(filename,encoding='utf-8'):
#     with open(filename,'rb') as f:
#         offset = -10
#         while True:
#             f.seek(offset,2)
#             data = f.readlines()
#             if len(data) > 1:
#                 return data[-1].decode(encoding=encoding)
#             else:
#                 offset *= 2
# print(read_last('read_last'))

