from django.shortcuts import render
from cmdb import models
from django.shortcuts import HttpResponse
import json

# Create your views here.

# user_list = [
#     {"user":"jack","pwd":"abc"},
#     {"user":"tom","pwd":"ABC"},
# ]
#phonelist = [{"phone":"vivo","username":"test1","ver":"6.1","loan_date":"2018.5.15"}]


def index(request):
    #return HttpResponse("hello world!")
    return render(request,"index.html")


def test(request):
    #return HttpResponse("hello world!")
    return render(request,"cardpage.html")


def test2(request):
    phonelist = models.PhoneInfo.objects.all()

    #json_receive = json.loads(request.body)
    print("request.body = ", request.body)
    name = request.POST
    # name = json_receive['name']
    print("name = ", name)
    phone_id = "81"
    #models.PhoneInfo.objects.filter(id=phone_id).update(username=name)
    #return render(request,"cardListPage.html")
    return render(request, "cardListPage.html", {"data": phonelist})


def urlpage(request):
    return render(request, "commonurl.html")


def errpage(request):
    return render(request, "404.html")


def account(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        print(username,password)
        models.UserInfo.objects.create(user=username,pwd=password)
        # if username != "" and password != "":
        #     user_list.append({"user":username,"pwd":password})
    user_list = models.UserInfo.objects.all()
    return render(request,"account.html",{"data":user_list})


def phone(request):
    phonelist = models.PhoneInfo.objects.all()
    if request.method == "POST":
        phone_id = request.POST.get("phone_id",'')
        os_choice = request.POST.get("os_choice",'')
        phone_name = request.POST.get("phone_name",None)
        user_name = request.POST.get("user_name",None)
        ver = request.POST.get("ver", None)
        loan_date = request.POST.get("loan_date", None)
        dec_info = request.POST.get("dec_info", None)
        print(phone_name,user_name,ver,loan_date,dec_info)
        # 增加
        if 'add' in request.POST:
            if phone_name != "" and user_name != "" and ver != "" and loan_date != "" and os_choice != "":
                models.PhoneInfo.objects.create(os=os_choice,phonename=phone_name,username=user_name,version=ver,loandate=loan_date,dec=dec_info)
                phonelist = models.PhoneInfo.objects.all()
            else:
                return HttpResponse("添加设备时，除备注和设备ID外，其他信息都不能为空")

        # 修改
        if 'change' in request.POST:
            if phone_id != "":
                # 返回数据列表
                try:
                    models.PhoneInfo.objects.filter(id=phone_id)
                    #data = models.PhoneInfo.objects.filter(id=phone_id)
                    #print("data:",len(data.values_list()))
                except:
                    return HttpResponse("没有此手机设备，请重新输入")
                # 全不为空
                if phone_name != "" and user_name != "" and ver != "" and loan_date !="" and dec_info !="" and os_choice !="":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,os=os_choice,username=user_name,version=ver,
                                                                                 loandate=loan_date,dec=dec_info)
                # 时间为空
                elif phone_name != "" and user_name != "" and ver != "" and loan_date =="" and dec_info !=""and os_choice !="":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,os=os_choice,username=user_name, version=ver
                                                                                 , dec=dec_info)
                # 版本为空
                elif phone_name != "" and user_name != "" and ver == "" and loan_date !="" and dec_info !=""and os_choice !="":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,os=os_choice,username=user_name, loandate=loan_date
                                                                                 , dec=dec_info)
                # 持有人为空
                elif phone_name != "" and user_name == "" and ver != "" and loan_date !="" and dec_info !="" and os_choice !="":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,os=os_choice,version=ver, loandate=loan_date
                                                                                 , dec=dec_info)
                # 描述为空
                elif phone_name != "" and user_name != "" and ver != "" and loan_date !="" and dec_info =="" and os_choice !="":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,os=os_choice,username=user_name,version=ver,
                                                                                 loandate=loan_date)
                # # 系统为空
                # elif phone_name != "" and user_name != "" and ver != "" and loan_date !="" and dec_info !="" and os_choice =="":
                #     models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,username=user_name,version=ver,
                #                                                                  loandate=loan_date,dec=dec_info)

                # 名字为空
                elif phone_name == "" and user_name != "" and ver != "" and loan_date != "" and dec_info != "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update( username=user_name,os=os_choice, version=ver,
                                                                                loandate=loan_date, dec=dec_info)

                # # 系统和名字为空
                # elif phone_name == "" and user_name != "" and ver != "" and loan_date != "" and dec_info != "" and os_choice == "":
                #     models.PhoneInfo.objects.filter(id=phone_id).update(version=ver, username=user_name,
                #                                                         loandate=loan_date,dec=dec_info)
                #
                # # 系统和时间都为空
                # elif phone_name != "" and user_name != "" and ver != "" and loan_date == "" and dec_info != "" and os_choice == "":
                #     models.PhoneInfo.objects.filter(id=phone_id).update(version=ver,username=user_name,phonename=phone_name,
                #                                                                  dec=dec_info)
                # # 系统和版本都为空
                # elif phone_name != "" and user_name != "" and ver == "" and loan_date != "" and dec_info != "" and os_choice == "":
                #     models.PhoneInfo.objects.filter(id=phone_id).update(username=user_name,phonename=phone_name,
                #                                                                  loandate=loan_date, dec=dec_info)
                # # 系统和持有人都为空
                # elif phone_name != "" and user_name == "" and ver != "" and loan_date != "" and dec_info != "" and os_choice == "":
                #     models.PhoneInfo.objects.filter(id=phone_id).update(version=ver,phonename=phone_name,
                #                                                                  loandate=loan_date, dec=dec_info)
                # # 系统和描述都为空
                # elif phone_name != "" and user_name != "" and ver != "" and loan_date != "" and dec_info == "" and os_choice == "":
                #     models.PhoneInfo.objects.filter(id=phone_id).update(version=ver,username=user_name,
                #                                                                  phonename=phone_name,loandate=loan_date)


                # 名字和版本都为空
                elif phone_name == "" and user_name != "" and ver == "" and loan_date != "" and dec_info != "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(username=user_name,os=os_choice,
                                                                        dec=dec_info, loandate=loan_date)
                # 名字和持有人都为空
                elif phone_name == "" and user_name == "" and ver != "" and loan_date != "" and dec_info != "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(version=ver, os=os_choice,
                                                                        dec=dec_info, loandate=loan_date)

                # 名字和时间都为空
                elif phone_name == "" and user_name != "" and ver != "" and loan_date == "" and dec_info != "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(version=ver, os=os_choice,
                                                                        dec=dec_info, username=user_name)

                # 名字和描述都为空
                elif phone_name == "" and user_name != "" and ver != "" and loan_date != "" and dec_info == "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(version=ver, os=os_choice,
                                                                        loandate=loan_date, username=user_name)

                # 版本和持有人都为空
                elif phone_name != "" and user_name == "" and ver == "" and loan_date != "" and dec_info != "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,os=os_choice, loandate=loan_date,
                                                                                 dec=dec_info)
                # 版本和时间都为空
                elif phone_name != "" and user_name != "" and ver == "" and loan_date == "" and dec_info != "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,os=os_choice, username=user_name,
                                                                                 dec=dec_info)
                # 版本和描述都为空
                elif phone_name != "" and user_name != "" and ver == "" and loan_date != "" and dec_info == "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,os=os_choice, username=user_name,
                                                                                 loandate=loan_date)

                # 持有人和时间都为空
                elif phone_name != "" and user_name == "" and ver != "" and loan_date == "" and dec_info != "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,os=os_choice, version=ver,
                                                                                 dec=dec_info)

                # 持有人和描述都为空
                elif phone_name != "" and user_name == "" and ver != "" and loan_date != "" and dec_info == "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,os=os_choice, version=ver,
                                                                                 loandate=loan_date)
                # 时间和描述都为空
                elif phone_name != "" and user_name != "" and ver != "" and loan_date == "" and dec_info == "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,os=os_choice, username=user_name,
                                                                                 version=ver)


                # # 系统、版本、持有人为空
                # elif user_name == "" and ver == "" and loan_date != "" and dec_info != "" and os_choice == "":
                #     models.PhoneInfo.objects.filter(phonename=phone_name).update(dec=dec_info, loandate=loan_date)
                # # 系统、版本、时间为空
                # elif user_name != "" and ver == "" and loan_date == "" and dec_info != "" and os_choice == "":
                #     models.PhoneInfo.objects.filter(phonename=phone_name).update(username=user_name, dec=dec_info)
                # # 系统、版本、描述为空
                # elif user_name != "" and ver == "" and loan_date != "" and dec_info == "" and os_choice == "":
                #     models.PhoneInfo.objects.filter(phonename=phone_name).update(username=user_name, loandate=loan_date)
                # # 系统、持有人、时间为空
                # elif user_name == "" and ver != "" and loan_date == "" and dec_info != "" and os_choice == "":
                #     models.PhoneInfo.objects.filter(phonename=phone_name).update(version=ver, dec=dec_info)
                # # 系统、持有人、 描述为空
                # elif user_name == "" and ver != "" and loan_date != "" and dec_info == "" and os_choice == "":
                #     models.PhoneInfo.objects.filter(phonename=phone_name).update(version=ver, loandate=loan_date)
                # # 系统、时间、描述为空
                # elif user_name != "" and ver != "" and loan_date == "" and dec_info == "" and os_choice == "":
                #     models.PhoneInfo.objects.filter(phonename=phone_name).update(version=ver, username=user_name)

                # 名字、版本、持有人都为空
                elif phone_name == "" and user_name == "" and ver == "" and loan_date != "" and dec_info != "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(loandate=loan_date, dec=dec_info,os=os_choice)
                # 名字、版本、时间都为空
                elif phone_name == "" and user_name != "" and ver == "" and loan_date == "" and dec_info != "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(username=user_name, dec=dec_info, os=os_choice)
                # 名字、版本、描述都为空
                elif phone_name == "" and user_name != "" and ver == "" and loan_date != "" and dec_info == "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(username=user_name, loandate=loan_date, os=os_choice)
                # 名字、持有人、时间都为空
                elif phone_name == "" and user_name == "" and ver != "" and loan_date == "" and dec_info != "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(version=ver, dec=dec_info, os=os_choice)
                # 名字、持有人、描述都为空
                elif phone_name == "" and user_name == "" and ver != "" and loan_date != "" and dec_info == "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(version=ver, loandate=loan_date, os=os_choice)
                # 名字、时间、描述都为空
                elif phone_name == "" and user_name != "" and ver != "" and loan_date == "" and dec_info == "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(version=ver, username=user_name, os=os_choice)
                # 版本、持有人、时间为空
                elif phone_name != "" and user_name == "" and ver == "" and loan_date == "" and dec_info != "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,dec=dec_info,os=os_choice)
                # 版本、持有人、描述为空
                elif phone_name != "" and user_name == "" and ver == "" and loan_date != "" and dec_info == "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,loandate=loan_date,os=os_choice)
                # 版本、时间、描述为空
                elif phone_name != "" and user_name != "" and ver == "" and loan_date == "" and dec_info == "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,username=user_name,os=os_choice)
                # 持有人、时间、描述为空
                elif phone_name != "" and user_name == "" and ver != "" and loan_date == "" and dec_info == "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,version=ver,os=os_choice)

                # # 系统、版本、持有人、时间为空
                # elif user_name == "" and ver == "" and loan_date == "" and dec_info != "" and os_choice == "":
                #     models.PhoneInfo.objects.filter(id=phone_id).update(dec=dec_info)
                # # 系统、版本、持有人、描述为空
                # elif user_name == "" and ver == "" and loan_date != "" and dec_info == "" and os_choice == "":
                #     models.PhoneInfo.objects.filter(phonename=phone_name).update(loandate=loan_date)
                # # 系统、版本、时间、描述为空
                # elif user_name != "" and ver == "" and loan_date == "" and dec_info == "" and os_choice == "":
                #     models.PhoneInfo.objects.filter(phonename=phone_name).update(username=user_name)
                # # 系统、持有人、时间、描述为空
                # elif user_name == "" and ver != "" and loan_date == "" and dec_info == "" and os_choice == "":
                #     models.PhoneInfo.objects.filter(phonename=phone_name).update(version=ver)

                # 名字、版本、持有人、时间为空
                elif phone_name == "" and user_name == "" and ver == "" and loan_date == "" and dec_info != "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(dec=dec_info, os=os_choice)
                # 名字、版本、持有人、描述为空
                elif phone_name == "" and user_name == "" and ver == "" and loan_date != "" and dec_info == "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(loandate=loan_date, os=os_choice)
                # 名字、版本、时间、描述为空
                elif phone_name == "" and user_name != "" and ver == "" and loan_date == "" and dec_info == "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(username=user_name, os=os_choice)
                # 名字、持有人、时间、描述为空
                elif phone_name == "" and user_name == "" and ver != "" and loan_date == "" and dec_info == "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(version=ver, os=os_choice)

                # 版本、持有人、时间、描述为空
                elif phone_name != "" and user_name == "" and ver == "" and loan_date == "" and dec_info == "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(phonename=phone_name,os=os_choice)

                # 名字、版本、持有人、时间、描述为空
                elif phone_name == "" and user_name == "" and ver == "" and loan_date == "" and dec_info == "" and os_choice != "":
                    models.PhoneInfo.objects.filter(id=phone_id).update(os=os_choice)

            else:
                return HttpResponse("必须填写设备id")

        # 查找型号设备
        if 'search' in request.POST:
            # 精确查找
            if phone_name != ""and user_name != "" and ver != "" and loan_date != "" and dec_info != "" and os_choice != "":
                phonelist = models.PhoneInfo.objects.filter(phonename=phone_name, username=user_name,
                                                            version=ver, loandate=loan_date, dec=dec_info,os=os_choice)
            # 操作系统查找
            elif phone_name == "" and user_name == "" and ver == "" and loan_date == "" and dec_info == "" and os_choice != "":
                phonelist = models.PhoneInfo.objects.filter(os=os_choice)

            # 手机型号查找
            elif phone_name != ""and user_name == "" and ver == "" and loan_date == "" and dec_info == "" and os_choice != "":
                phonelist = models.PhoneInfo.objects.filter(phonename=phone_name,os=os_choice)

            # 版本查找
            elif phone_name == "" and user_name == "" and ver != "" and loan_date == "" and dec_info == "" and os_choice != "":
                phonelist = models.PhoneInfo.objects.filter(version=ver,os=os_choice)

            # 持有人查找
            elif phone_name == "" and user_name != "" and ver == "" and loan_date == "" and dec_info == "" and os_choice != "":
                phonelist = models.PhoneInfo.objects.filter(username=user_name,os=os_choice)

            # 时间查找
            elif phone_name == "" and user_name == "" and ver == "" and loan_date != "" and dec_info == "" and os_choice != "":
                phonelist = models.PhoneInfo.objects.filter(loandate=loan_date,os=os_choice)

            # 描述查找
            elif phone_name == "" and user_name == "" and ver == "" and loan_date == "" and dec_info != "" and os_choice != "":
                phonelist = models.PhoneInfo.objects.filter(dec=dec_info,os=os_choice)

            else:
                return HttpResponse("只支持单条件查找")
            #---------------------
            # if phone_name != "":
            #     # 全不为空
            #     if user_name != "" and ver != "" and loan_date != "" and dec_info != "":
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name,username=user_name,
            #                                                     version=ver,loandate=loan_date, dec=dec_info)
            #     # 时间为空
            #     elif user_name != "" and ver != "" and loan_date == "" and dec_info != "":
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name, username=user_name,
            #                                                     version=ver, dec=dec_info)
            #     # 版本为空
            #     elif user_name != "" and ver == "" and loan_date != "" and dec_info != "":
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name, username=user_name,
            #                                                     loandate=loan_date, dec=dec_info)
            #     # 持有人为空
            #     elif user_name == "" and ver != "" and loan_date != "" and dec_info != "":
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name,
            #                                                     version=ver, loandate=loan_date, dec=dec_info)
            #     # 描述为空
            #     elif user_name != "" and ver != "" and loan_date != "" and dec_info == "":
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name, username=user_name,
            #                                                     version=ver, loandate=loan_date)
            #     # 版本和时间都为空
            #     elif user_name != "" and ver == "" and loan_date == "" and dec_info != "":
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name, username=user_name,
            #                                                     dec=dec_info)
            #     # 持有人和时间都为空
            #     elif user_name == "" and ver != "" and loan_date == "" and dec_info != "":
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name,
            #                                                     version=ver, dec=dec_info)
            #     # 描述和时间都为空
            #     elif user_name != "" and ver != "" and loan_date == "" and dec_info == "":
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name, username=user_name,
            #                                                     version=ver)
            #     # 持有人和版本都为空
            #     elif user_name == "" and ver == "" and loan_date != "" and dec_info != "":
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name,
            #                                                     loandate=loan_date, dec=dec_info)
            #     # 描述和版本都为空
            #     elif user_name != "" and ver == "" and loan_date != "" and dec_info == "":
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name, username=user_name,
            #                                                     loandate=loan_date)
            #     # 描述和持有人都为空
            #     elif user_name == "" and ver != "" and loan_date != "" and dec_info == "":
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name,
            #                                                     version=ver, loandate=loan_date)
            #     # 版本、持有人、日期为空
            #     elif user_name == "" and ver == "" and loan_date == "" and dec_info != "":
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name, dec=dec_info)
            #     # 版本、持有人、描述为空
            #     elif user_name == "" and ver == "" and loan_date != "" and dec_info == "":
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name, loandate=loan_date)
            #     # 版本、时间、描述为空
            #     elif user_name != "" and ver == "" and loan_date == "" and dec_info == "":
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name, username=user_name)
            #     # 持有人、时间、描述为空
            #     elif user_name == "" and ver != "" and loan_date == "" and dec_info == "":
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name,
            #                                                     version=ver)
            #     else:
            #         phonelist = models.PhoneInfo.objects.filter(phonename=phone_name)
        # 展示全部设备
        if 'all' in request.POST:
            phonelist = models.PhoneInfo.objects.all()

        # 删除设备
        if 'delete' in request.POST:
            phones_id_list = []
            if 'list ' in phone_id:
                phones_id_list = phone_id.split(' ')
                phones_id_list.remove('list')
                if '' in phones_id_list:
                    phones_id_list.remove('')
                print(phones_id_list)
            else:
                phones_id_list.append(phone_id)
            try:
                for id in phones_id_list:
                    data = models.PhoneInfo.objects.filter(id=id)
                    print(data)
                    print(len(data))
                    if len(data) == 1:
                        data.delete()
                    else:
                        return HttpResponse("该设备不存在，或者列表格式有误“list 1 2 3 4”")
            except:
                return HttpResponse("ID不能为空,或者列表格式有误“list 1 2 3 4”")

            # try:
            #     data = models.PhoneInfo.objects.filter(id=phone_id)
            #     print(data)
            #     print(len(data))
            #     if len(data) == 1:
            #         data.delete()
            #         #return HttpResponse("设备删除成功")
            #     else:
            #         return HttpResponse("该设备不存在")
            # except:
            #     return HttpResponse("ID不能为空")

            # try:
            #     data = models.PhoneInfo.objects.filter(id=phone_id)
            #     print(len(data))
            #     if len(data) == 1:
            #         data.delete()
            #         return HttpResponse("设备删除成功")
            #     else:
            #         return HttpResponse("该设备不存在")
            # except Exception as e:
            #     return HttpResponse("执行错误：",e)
    return render(request,"phone.html",{"data":phonelist})