function duihua()
{
    alert("执行成功！")
}
function queren()
{
    var se=confirm("确定要执行吗？");
    if (se==true)
    {
        return true
        alert("执行成功！");
    }
    else
    {
        return false
        alert("执行取消！");
	}
}
function tishi()
{
	var t=prompt("输入你要删除的ID")
	if (t!=null && t!="")
	{
		document.write("删除成功")
	}
}