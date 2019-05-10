'''
CSS : 
     1. CSS的导入
     2. 选择标签
     3. 操作标签
     4. 布局
     5. 伪类
''' # 综述

'''
CSS的导入方式:
    1. 写死
       <p style='#CSS代码'></p>
    
    2. 嵌入式
       <style>
          #CSS代码
       </style>
    
    3. 导入式: 先渲染html, 再渲染css
       <style type='text/css'>
           @import 'test.css'
       </style>
    
    4. 链接式: 将所有css文件准备好, 与html文件一起渲染
      <link href='test.css' rel='stylesheet' type='text/css'>             
''' # CSS导入方式

'''
选择标签:
     1. 基本选择器
         *{}            # 通用选择器
         p{}            # 标签选择器:  h, p, div, table, ul/ol, li, table, th, td, form, br, hr (级联标签)
                                 span, a, input, select, textarea, button, img (内联标签)
         .cls{}         # class选择器
         #id{}          # id选择器(唯一选择)
         [attr]{}       # 属性选择器
         [attr='v']{}   # 属性选择器
     
     2. 组合选择器
        div.cls{}                       # 标签 + class选择器
        div[attr]{}, div[attr='v']{}    # 标签 + 属性选择器
     
     3. 多元素选择器
        div, p{}        # 多标签选择
     
     4. 后代选择器
        div p{}         # 在div的嵌套中寻找所有的p
     
     5. 子代选择器
        div > p {}      # 只在div的第一层嵌套中寻找p      
                              
     6. 毗邻选择器
        div + p{}       # 在div之后, 紧挨着div的p 

多种选择器作用同一个标签的优先级计算: 
     style > id > .cls 属性> 标签名                               
''' # 选择标签

'''
操作标签属性:
    1. 标签从内到外为:
       content, padding, border, margin
    
    2. padding/border/margin属性
        padding/margin:10px 5px 15px 20px;    # 上 右 下 左
        padding/margin:10px 5px 15px          # 上 右左 下
        padding/margin:10px 5px               # 上下  右左
        padding/margin:10px                   # 上右下左 
        注意:
            #1 padding(内边距), margin(外边距)
            #2 内联标签只能设置左右边距
            #3 兄弟margin按大的取
            #4 父子margin, 子margin向上寻找父级的border,padding, 内联标签内容, 没有则合并父级, 继续向上寻找                                       
        
        border:5px solid gray                 # 大小 格式 颜色 
               transparent                    # 边界透明
    
    2. content属性:
       1)基本属性
       width/height                         # 标签文本框大小(不包括padding)
       background-color                     # 背景色(包括padding)
       background-img: url('/url')          # 背景图片
       background-repeat: repeat/no-repeat  # 背景图片是否重复
       background-position: 同padding       #  背影图片位置
       display: none(隐藏,且不占空间)/block(级联可设置长宽)/inline(内联可放在一排)/inline-block(级联-内联)
       visibility: hidden   (隐藏,但占空间)
       
       2) 文本属性
       color:                         # 文本颜色
       font-size:  px                 # 字体大小
       font-family:                   # 字体格式
       font-weight: bold              # 字体加粗
       font-style:italic              # 字体斜体 
       text-align:center              # 字体居中
       line-height: px                # 行间距
       letter-spacing: px             # 字符间距
       word-spacing: px               # 单词间距
''' # 操作属性

'''
布局:
    1. 文档流: 级联标签从上到下, 内联标签从左到右  
          
    2. 脱离文档流: 将该标签浮起, 不占空间
       float: left,right(盒子无视, 文本环绕)     
       *注意: 若A的前一个元素B向左浮动, A也向左浮动, 则A跟在B后面 
    
    3. 清除浮动（主要是清除盒子, 文本自动环绕）
       clear: left/right/both           # clear属性只会对自身起作用，而不会影响其他元素   
    
    4. 定位:
       position: 
               relative; top;left;right;bottom        # 相对于自己初始位置，且初始位置仍然占空间
               absolute; top;left;right;bottom        # 浮空，相对于最近已定位父级元素，一般用relative定位父级元素，子元素absoulte
                                                      # 完全浮动, 文本盒子都遮挡
               fixed;top;left;right;bottom            # 钉死                                       
           
       
                
''' # 布局

'''
伪类:
   a:link{}
   a:visit{}
   a:hover{}
   a:active{}
   
   p:before{}
   p:after{}
''' # 伪类