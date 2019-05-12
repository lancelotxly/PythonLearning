var name='xzq';
function func(){
    var name='John';
    function inner(){
        alert(name);
    }
    return inner();
}
var ret = func();
ret(); // John

function main(){
    if(1==1){
        var name='xzq';
    }
    console.log(name);
}
main(); //xzq

function func(){
    var xo='xzq'
    function inner() {
        var xo='John'
        console.log(xo)
    }
    inner();
}
func(); //John

function Foo(){
    console.log(xo);
    var xo = 'xzq';
}
Foo(); //undefined


var name = 'xzq';
function Foo(){
    this.name = 'John';
    this.func = function () {
        alert(this.name);
    }
}
var obj = new Foo();
obj.func(); //John

var name = 'xzq';
function Foo(){
    this.name = 'John'
    this.func = function(){
        (function (){
            alert(this.name);
        })
    }();
}
var obj = new Foo();
obj.func;