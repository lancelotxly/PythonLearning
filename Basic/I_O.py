'''
I/O: 
    1. 文件的读取与保存
''' # 综述

'''
文件操作:
       1. 读: 'r'
          with open('filepath','r',encoding='utf-8') as f:
              f.read()       # 读全部
              f.readline()   # 读一行
              f.readlines()  # 读全部行, 保存在list中 
              for line in f: # 遍历
                                     
       2. 写: 'w', 会创建一个新文件, 覆盖旧的
          with open('filepath','w',encoding='utf8') as f:
               f.write('str')                     # 写全部
               f.writelines(['str1','str2',..])   # 迭代写 
          
       3. 追加: 'a', 光标后面加
          with open('filepath','a', encoding='utf8') as f:
              f.write('str')                     # 写全部
              f.writelines(['str1','str2',..])   # 迭代写         
         
       4. 读&写: 能同时读写, 要with结束后, 提交后文件才会更改, 因此不能立即读出来         
              1） 'r+': 读为主, 文件必须存在
              2)  'w+': 写为主, 文件必定被修改
                    
       5. 二进制操作文件: 'rb/wb/ab', 不要编码
             with open('filepath','rb/ab/wb') as f
       
       6. 光标操作: 仅在二进制下
           f.tell()       # 返回光标当前位置
           seek(i)        # 移动光标, 从开始位置移动i步
           seek(i,1)      # 移动光标, 从当前位置移动i步
           seek(-i,2)     # 移动光标, 从结束位置反向移动i步              
''' # 文件操作

def read_last(filename,encoding='utf8'):
    with open(filename, 'rb') as f:
        offest = -10
        while True:
            f.seek(offest,2)
            data = f.readlines()
            if len(data) > 1:
                return data[-1].decode(encoding=encoding)
            else:
                offest*=2

if __name__ == "__main__":
    print(read_last('read_last'))

