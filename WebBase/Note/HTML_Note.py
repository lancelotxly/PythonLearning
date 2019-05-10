'''
HTML:
     1. 用于配置的标签
     2. 用于显示和操作的标签: 
                         1> 级联标签
                         2> 内联标签
''' # 综述

'''
用于配置的标签: 
     1. <meta> 配置浏览器
        <meta http-equiv="content-type" charset="UTF-8">                  # 声明编码为utf-8
        <meta http-equiv = "X-UA-Compatible" content = "IE=EmulateIE7">   # 兼容IE7
        <meta name="keyword" content="html总结, html, meta属性">           # 用于浏览器关键词搜索
        <meta name="description" content="用于关键内容搜索">                # 用于浏览器关键内容搜索
     
     2. <link>
        <link rel="icon" href="http://www.jd.com/favicon.ico">    # 指定图标
        <link rel="stylesheet" type="text/css" href="URI">        # 指定CSS文件
     
     3. <script>
        <script src="hello.js"></script>                          # 指定js文件   
     
     4. <title>
        <title>Title</title>                                      # 标题  
''' # 用于配置的标签

'''
用于显示和操作的标签: 
1. 特点:
   1) 标签之间的东西，是供显示的，给用户看的
   2) 标签内部的东西，是供开发者传递信息(设置)，或读取数据的
   3) 每个标签都具有的属性:  
                       id(唯一), class属性, 固有属性, 自定义属性

2. 级联标签: 独占一行, 可嵌套级联标签和内联标签
   <h>, <p>, <div>, 
   <table>, <th>, <td>, 
   <ul>, <ol>, <li>
   <form>
   <br>, <hr>      
   
   有固有属性的级联标签: 
   <table border="1px" cellpadding="10px" cellspacing="2-px">
   <form action="URI" method="post/get" target="_blank">
   <form enctype="multipart/form-data"></form>              # 上传文件                                                           
''' # 用于显示和操作的标签: 级联标签

'''
3. 内联标签: 不独占一行, 只能嵌套内联标签
   <span>
   <a href='url'>    <a href='#id'>
   <img src='url' alt='加载失败显示' title='鼠标悬停显示'>
   <button value='显示'>
   <input>, <textarea>
   <select>, <option>
   
   有固有属性的内联标签:
   <input type="text" name="username" placeholer='默认值'>     # 输入框  readonly只读, disabled不可改
   <input type="password" name="password"></p>                # 密码框
   <input type="checkbox" name="hobby" value="music">         # 钩选框
   <input type="radio" name="gender" value="man">             # 单选框
   <input type="file" name="put-file">                        # 上传文件框  
   <input type="reset" value="重置">                          #  重置
   <select name="provice" multiple size=3>                    # 选择框, multiple多选, size显示 
       <option value="BJ">北京</option>                        # 选项
   <input type="button" value="按钮">                          # 按钮
   <input type="submit" value="提交">                          # 提交, 最后会提交有name属性的标签，由name:value组成键值对，没有值输入，则用默认value代替   
       
''' # 用于显示和操作的标签: 内联标签