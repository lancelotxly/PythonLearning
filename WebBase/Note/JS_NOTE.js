/*
JavaScript包括：
  1. ECMAScript 语法
  2. 文档对象模型（DOM） Document object model //(整合js，css，html)
  3. 浏览器对象模型（BOM） Broswer object model //（整合js和浏览器）

JS的运行规范:
    1. 一般都把全部<script>放在<body>后面  //(解释器运行<script>求值时，页面中的其余内容都不会被浏览器加载或显示）
    2. 延迟脚本 <script src="JS.js" defer>  //(js在html后执行，顺序执行)
    3. 异步脚本 <script src="JS.js" async>  //(js穿插在html中执行，非顺序执行)

变量:
    1. 声明方法  (var name; // 局部变量     name;    // 全局变量)
    2. 命名规则  var sName;   //字符串

输出:  console.log() // 输出到监视器
      alert()       // 输出到提醒框
      document.write("")  // 输出到文本

数据类型:  Number, String, Boolean, Null(空指针), Undefined(变量未赋值) ------- 栈空间
         Object(栈空间只保留其地址的引用)                               ------- 堆空间

         typeof a;    a instanceof object;

      1. Number: int, float, Infinity, Nan
         * float:  不要测试浮点型  a==3.0
         * Infinity: 不能参加计算、
         * Nan: 参加任何比较 返回 false

     2. String:  var str='hello js'
     3. Boolean: true/ false
     4. Object:  var obj = new Person()

     数据类型转换: String > Boolean > Number
               * 弱转换:   Number + String --> String;
                          Number + Boolean --> Number;
                          String + Boolean --> String
               * 强转换:   to Number:   Number()       //包含字母则为Nan; null和空为0; true为1, false为0
                                       parseInt()     //以字母开头为Nan; 中途遇字母截断; 小数点后截断
                                       parseFloat()   //以字母开头为Nan; 第一个小数点有效, 不取0
                          to Sting:    toString()
                          字符串强转表达式: eval("")
运算符:
       1. 算术运算符
           +, -, *, /, %(余), ++, --
           =+, =-, =*, =/   // Number()自动转换
       2. 逻辑运算符
          ==(强转Number再比较), ===(不强转), !=, >, <, >=, <=
          &&(与), ||(或), !(非)

流程控制:  if, switch, for, while
         try-catch(e)--finally, throw(e)
 */

/*
ECMA对象:
         * 本地对象: Object, 包装类(String, Number, Boolean), Array, Date, RegExp, Function
         * 本地(不需要创建)对象: Math, Global
         * 宿主对象: DOM, BOM

        1. Object
           1> 创建:
                 * var person = {
                      name:'xzq',
                      age:'24'
                   }
                 * var person = new Object();
                   person.name = 'xzq';
                   person.age = '24';

       2. 包装类(String, Number, Boolean):
          String: 1> 创建:  var str1 = new String("");
                  2> 基本属性:  str1.length
                  3> 方法:   1>>. 格式编排: str.fontcolor("color"), str.fontsize("size"), str.link("url")
                            \
                            2>>. 大小写转换:  str.toLowerCase(), str.toUpperCase()

                            3>>. 获取指定字符串: str.charAt(index),     str.charCodeAt(index) // Unicode

                            4>>. 查询字符串:   str.indexOf('a'),   str.lastIndexOf('a') // 反向查找
                                             str.match('a') // 返回匹配到的数组
                                             str.search('a') // 返回匹配到的首位置

                            5>>. 子串处理:  str.substr(start,length),  str.substring(start,end), str.slice() // 截取
                                          str.replace(findstr,tostr) // 替换
                                          str.split('a')             // 分割，返回数组
                                          str.concat('a')            // 连接， 也可用 +

       3. Array:
            1> 创建:
                    var arr = [1,1.0,'a',true];
                    var arr = new Array([size]); // 可创建二维数组
            2> 基本属性: arr.length
            3> 方法:  1>>. 连接数组:  arr.join('-') // 连接元素，返回字符串
                                   arr.concat(num1,num2) // 添加元素，返回数组
                                   arr.toSting()  // 返回字符串

                     2>>. 数组排序:  arr.reverse([func]),  arr.sort([func])

                     3>>. 获取子数组: arr.slice()
                                    arr.splice(start,deleteCount,[value...]) // 起始位置, 删除个数, 插入的值

                     4>>. 栈操作:  arr.push(), arr.pop()       // 尾压
                                  arr.unshift(), arr.shift()  // 头压

                     5>>. 数组迭代:  arr.every(func)       // 与门
                                   arr.some(func)        // 或门
                                   arr.filter(func)      // 过滤器
                                   arr.map(func)         // 推导器

        4. Date:
             1> 创建:
                    var now = new Date(); // 默认UTC时间(.toUTCString)  当地时间(.toLocaleString)
                    var now = new Date("2019/4/2 14:13");
                    var now = new Date(2019,4,2,14,13,0,300);
             2> 获取信息:  getFullYear(), getMonth()+1, getDate(), getWeek()//星期, getHours(), getMinutes(), getSeconds();
             3> 设置信息:  setFullYear(), setMonth()+1, setDate(), setWeek()//星期, setHours(), setMinutes(), setSeconds();

        5. RegExp:
             1> 创建:
                    var reg1 = new RegExp("^[a-zA-Z]\\w{5,11}$","g")   // g 不忽略大小写,   gi 忽略大小写
             2> 应用: * 用户填写信息的规范化验证  reg1.test(str);
                     * 字符串操作

        6. Math: 直接用Math.
             1> 方法:    abs(x), exp(x), log(x), max(x,y), min(x,y), pow(x,y), sin(x), sqrt(x), tan(x), random() // 0~1随机数
                        floor(x) //舍去小数, round() // 四舍五入


 */

/*
Function 对象: js的函数加载执行与python不同，它是整体加载完才会执行，所以执行函数放在函数声明上面或下面都可以
        1. 创建
           *函数声明:  function func(para){} // 声明，运行前加载
                     func();               // 调用
           *匿名函数: var func = function(para){}   // 运行时加载

        2. 方法:  toString()        // 返回源代码
        3. 属性:
                内部属性: arguments   //数组, 保存函数参数  arguments.length, arguments.callee // 函数名
                        this        // 当前执行环境
                        caller      // 该函数的调用者
                外部属性: length     // 函数声明时希望接收的参数个数
                        prototype  // 保存其实例方法
        4. 作用域: 同python
        5. 作用域链:
        6. 创建对象(class):
               function Person(name,age,job){
                  this.name = name;                    // this.attr 为该实例独有
                  this.age = age;
                  this.job = job;
               }
               Person.prototype={                     // prototype为所有实例共享
                    constructor: Person,
                    sayName:function(){
                        #code
                    }
               }
               var p1 = new Person(name,age,job);    // 创建实例
 */

/*
BOM对象:  浏览器窗口对象模型
        1. windows对象(即全局对象):   一个html文档对应一个window对象
            1> 创建: 直接使用
            2> 方法: alert()  // 警示框
                    var res = confirm('info')  // 确认框
                    var res = prompt('info','default-value') // 输入框

                    open("URL")  // 打开一个新窗口   close() // 关闭当前窗口
                    setInterval(f,time) // 循环执行f,会创建一个cloak对象   clearInterval(clock) //清除循环
                    setTimeout(f, time) // 定时调用,会创建一个cloak对象    cleaTimeout(clock)  // 清除定时
       2. history:
          1> 方法:
                 <button onclick=" history.forward()">>>></button>
                 <button onclick="history.back()">back</button>

       3. location:
          1> 方法:
                 location.assign(url)       // 指向新url, 可返回
                 location.reload()          // 刷新
                 location.replace(url)      // 用新url代替当前网页, 不可返回

 */

/*
DOM 对象: HMTL /XML 文本对象
         1. 分为 document , element 节点对象
         2. 每个node节点有 自身属性, 导航属性
            * 自身属性:  nodeName  // 节点名
                       attr     // 节点值属性值
                       innerHTML  // 节点内容，包含内部html
                       innerText  // 节点文本， 不包含html
                       // nodeType   // 节点类型
                       // attributes // 节点属性

            * 导航属性:  parentElement             // 父节点
                       children                  //所有子节点, 返回集合
                       firstElementChild         // 第一个子节点
                       lastElementChild          // 最后一个子节点
                       nextElementSibling        // 下一个兄弟节点
                       previousElementSibling    // 上一个兄弟节点
         3. 查找方法:
                   getElementById("id");       //唯一， element不支持
                   getElementsByTagName("p");  // 标签集合
                   getElementsByClassName("");  // class集合
                   getElementsByName("");       // 自定义类集合， element不支持

         4. 事件events:
              1.> 添加事件的两种方式:
                  <input type="text" onclick="begin()">  // 直接写在html文件
                  ele.onclick = function(){};            // 在js文件中添加  , √

              2.> 事件类型:
                        onclick       // 单击
                        ondblclick    // 双击

                        onfocus     //元素获得焦点
                        onblur      // 元素失去焦点，表单验证
                        onsubmit     // 确认按钮被点击。 只能给form元素使用.在表单提交前验证用户输入是否正确.如果验证失败.在该方法中我们应该阻止表单的提交

                        onkeydown      // 键盘按下一个键
                        onload         // 页面加载完成时执行 onload 属性开发中 只给 body元素加

                        onmousemove    // 鼠标被移动。
                        onmouseout     // 鼠标从某元素移开。
                        onmouseover    // 鼠标移到某元素之上。
                        onmouseleave   // 鼠标从元素离开

                        event           // 记录事件的信息   event.preventDefault();  // 阻止该事件
                                                         event.stopPropagation(); // 阻止该事件向外传播


       5.修改DOM:
          1).Element增删改查:
               1>. 增加:       ele = document.createElement("p");
                              ele.innerHTML = 'text';
                              father.appendChild(ele);   // 尾插
                              father.insertBefore(new_ele,old_ele);  // old_ele之前插入
               2>. 删除:       father.removeChild(ele);
               3>. 改:         father.replaceChild(new_ele,old_ele);
          2). 属性修改:
               ele.attr = new_value;
               ele.classlist;  // 返回class属性值，数组
                   ele.classlist.add;
                   ele.classlist.remove;
 */





