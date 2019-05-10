/*
jQuery 是一个用JS写好的模块，方便处理DOM, BOM, Events， 以及实现动态效果和AJAX交互
jQuery 对象: <script src="jquery-3.1.1.js"></script>   // 导入jQuery模块
            var $ele = $(selector).action(); // jQuery对象时包装后的DOM对象，但jQuery对象不能使用DOM对象的方法
*/

/*
1. 寻找元素
    选择器: 语法同CSS
           1. 基本选择器:   $("*") // 通用选择器
                          $("ele") // 标签选择器
                          $(".class") // 类选择器
                          $("#id")    // id选择器
                          $("[alex=sb]") //属性选择器
           2. 组合选择器:   $(".class,p,div")
           3. 层级选择器:   $(".outer div") // 后代选择器
                          $(".outer>div") // 子代选择器
                          $(".outer+div") //向下毗邻选择器
           *4.表单选择器:   $("[tpye='text']"),  $(":text")   //只是适用于input

    筛选器:  选择器的拓展
           *5. 过滤筛选器:  选择器 +  过滤条件
                          $(selector).eq(num), .first(), .end(), .odd(), .even(), .gt(num), .lt()
           *6. 查找筛选器:  选择器 +  筛选条件
                          $(selector).children(), .parent(), .siblings()
                                     .next(), .nextAll(), .nextUntil(".test") // 不包括.test
                                     .prev(), .prevAll(), .prevUntil(".test") // 不包括.test
                                     .find(".test")  // 在selector中继续按条件找

 */

/*
2. 操作元素:
       1. 操作属性:    $(selector).attr("attr"); //获取属性值
                     $(selector).attr("attr_new","new_value"); // 添加属性
                     $(selector).attr("attr","new_value");     // 修改属性
                     $(selector).removeAttr("attr");          // 删除属性
                     $(selector).prop("attr");    // 获取固有属性
                     $(selector).removeProp("attr"); // 删除固有属性

       2. 操作类:     $(selector).addClass("class");  // 添加类
                     $(selector).removeClass("class"); //移除类

       3. 操作文本和值: $(selector).html() // html文本
                     $(selector).text()  // text文本
                     $(selector).val()   // value值

       4. 操作css:   获取/改变样式:
                        $(selector).css({'color':'red',...})
                    获取/改变位置:
                        $("").offset()          //  相对于视图左上角
                        $("").position()        //  相对于父级位置
                        $("").scrollTop([val])
                        $("").scrollLeft([val])
                    获取/改变尺寸:
                        $("").height([val|fn])
                        $("").width([val|fn])
                        $("").innerHeight()             // padding
                        $("").innerWidth()
                        $("").outerHeight()             // margin
                        $("").outerWidth()

       5. 操作标签:    $("<p>") // 创建标签
                     内部插入:
                         $("").append(content|fn)      ----->$("p").append("<b>Hello</b>");   // 在p中尾插b
                         $("").appendTo(content)       ----->$("p").appendTo("div");
                         $("").prepend(content|fn)     ----->$("p").prepend("<b>Hello</b>");
                         $("").prependTo(content)      ----->$("p").prependTo("#foo");
                     外部插入:
                         $("").after(content|fn)       ----->$("p").after("<b>Hello</b>");
                         $("").before(content|fn)      ----->$("p").before("<b>Hello</b>");
                         $("").insertAfter(content)    ----->$("p").insertAfter("#foo");
                         $("").insertBefore(content)   ----->$("p").insertBefore("#foo");
                     替换:
                         $("").replaceWith(content|fn) ----->$("p").replaceWith("<b>Paragraph. </b>");
                     删除:
                         $("").empty()            //清空标签内容，不删除
                         $("").remove([expr])     // 删除
                     复制标签:
                         $("").clone();

        6. 操作事件:
                  页面载入:  $(document).ready(function(){}) -----------> $(function(){}) // HTML载入后执行
                  事件处理:  $('ul li').bind('click', function(){}) ------>  $("ul li").click(function(){})  // 静态绑定
                           $('ul').on('click', 'li', function(){} ------>  $('ul li').on('click', function(){}) // 动态绑定，新添加的ele也有改特性
                                                                                                                // ul 为非新生成元素
        7. 动画效果:   都可加函数回调
                     .hide(time，[function]), .show(time) .toggle() // 显示与隐藏,切换
                     .slideDown(time), slideUp(time)， slideToggle() // 滑入与滑出，切换
                     .fadeIn(time), .fadeOut(time),  fadeToggle()   // 淡入与淡出，切换

       8. 插件: 自己编写jQuery方法
              $.extend(object)      //为JQuery 添加一个静态方法。
              $.fn.extend(object)   //为JQuery实例添加一个方法。


       9.补充:
              $.ajax()
              $.inArray(tec_id,data_list);    // 判断数据是否在数组中
              $('').length > 0                // 判断元素存在
              $('').length == 0               // 判断元素不存在
              $('')[0]                        // 转dom对象
 */