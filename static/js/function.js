function setTab(m,n){
    var tli=document.getElementById("leftmenu"+m).getElementsByTagName("li");
    var mli=document.getElementById("mcont"+m).getElementsByTagName("ul");
    var dli=document.getElementById("leftmenu"+m).getElementsByTagName("div");
    for(i=0;i<tli.length;i++){
        tli[i].className=i==n?"hover":"";
		mli[i].style.display=i==n?"block":"none";
		dli[i].id=i==n?"click_botten":"click_botten0";
	}
}

function openPhonepage(){
    window.location.href="http://192.168.0.34:8000/test2";
}

function loadQQ(){
    window.open('http://wpa.qq.com/msgrd?v=3&uin=509730796&site=qq&menu=yes', '_blank');
}

function disp_prompt(){
    //var name=prompt("请输入您的名字","");
    var name = "999";
    document.getElementById("name").value = name;
//    if (name!=null && name!=""){
//        document.write("请打开QQ进行通知，或者直接点击被拦截的页面自动跳转至QQ");
//    }
//    if (name!=null && name!=""){
//        window.open('http://wpa.qq.com/msgrd?v=3&uin=509730796&site=qq&menu=yes', '_blank');
//    }
}

function disp_prompt2(){
    //var name=prompt("请输入您的名字","");
    var name1 = "999";
    //document.getElementById("name").value = name;
//    if (name!=null && name!=""){
//        document.write("请打开QQ进行通知，或者直接点击被拦截的页面自动跳转至QQ");
//    }
//    if (name!=null && name!=""){
//        window.open('http://wpa.qq.com/msgrd?v=3&uin=509730796&site=qq&menu=yes', '_blank');
//    }
    $.ajax({
        url: "/test2",
        data: {    // JSON格式封装数据
            name: "999",
        },
        contentType: 'application/json',
        type: "POST",
        traditional: true,    // 需要传递列表、字典时加上这句
        success: function(result) {
        }
        fail: function(result) {
        }
    });
}
