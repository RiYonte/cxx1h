import re

import xlrd
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Event, Student, Tag, Grade, Major
from .forms import TagForm

# Create your views here.


def student_list(request):
    # major = Major.objects.all().order_by('mname')
    # grade = Grade.objects.all().order_by('gname')
    students = Student.objects.all().order_by('sid')
    context = {'students': students, 'g':'全部', 'm':'全部', 'b':'全部' }
    if request.GET:
        grade = request.GET['sgrade']
        major = request.GET['smajor']
        banji = request.GET['sbanji']
        if grade != '全部':
            students = students.filter(sgrade=grade)
        if major != '全部':
            students = students.filter(smajor=major)
        if banji != '全部':
            students = students.filter(sbanji=banji)
        context = {'students': students, 'g':grade, 'm':major, 'b':banji }
    return render(request, 'stdsys/list.html', context)


def student_detail(request, id):
    student = Student.objects.get(id=id)
    alltags = Tag.objects.all()
    nothavetags = alltags.difference(student.tag.all())
    # 需要传递给模板的对象
    context = {'student': student, 'nothavetags': nothavetags}
    # 载入模板，并返回context对象
    return render(request, 'stdsys/detail.html', context)


def student_import(request):
    if request.method == "GET":
        return render(request, 'stdsys/import.html',)
    if request.method == "POST":
        t = Tag.objects.get(id=1)
        f = request.FILES['my_file']
        type_excel = f.name.split('.')[1]
        if 'xlsx' == type_excel:
            # 开始解析上传的excel表格
            wb = xlrd.open_workbook(
                filename=None, file_contents=f.read())  # 关键点在于这里
            table = wb.sheets()[0]
            nrows = table.nrows  # 行数
            for i in range(0, nrows):
                rowValues = table.row_values(i)
                student = Student()
                student.sid = int(rowValues[0])
                student.sname = rowValues[1]
                student.sclass = rowValues[2]
                student.ssex = rowValues[3]
                student.sgrade = re.search(
                    r'[0-9]+', rowValues[2]).group()
                student.sbanji = re.search(
                    r'[0-9]$', rowValues[2]).group()
                student.smajor = re.search(
                    r'^[\u4e00-\u9fa5]+', rowValues[2]).group()
                student.save()
                # if not Grade.objects.filter(gname=student.sgrade).exists():
                #     grade = Grade()
                #     grade.gname = student.sgrade
                #     grade.save()
                # if not Major.objects.filter(mname=student.smajor).exists():                
                #     major = Major()
                #     major.mname = student.smajor
                #     major.save()
                # if not Banji.objects.filter(bname=student.sbanji).exists():                
                #     banji = Banji()
                #     banji.bname = student.sbanji
                #     banji.save()
                student.tag.add(t)
            return redirect("/stdsys/student-list")

def student_tag_add(request, sid, tid):
    student = Student.objects.get(id=sid)
    tag = Tag.objects.get(id=tid)
    student.tag.add(tag)
    url = '/stdsys/student-detail/' + str(sid)
    return redirect(url)

def student_tag_del(request, sid, tid):
    student = Student.objects.get(id=sid)
    tag = Tag.objects.get(id=tid)
    student.tag.remove(tag)
    url = '/stdsys/student-detail/' + str(sid)
    return redirect(url)






def tag_manage(request):
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        tagform = TagForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if tagform.is_valid():
            tagform.save()
            # newtag.save()
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    tagform = TagForm()
    tags = Tag.objects.all()
    context = {'tags': tags, 'tagform': tagform}
    return render(request, 'stdsys/tags.html', context)

def tag_del(request, id):
    tag = Tag.objects.get(id=id)
    tag.delete()
    return redirect("stdsys:tag_manage")

def tag_display(request, id):
    tag = Tag.objects.get(id=id)
    tag.tdisplay = not tag.tdisplay
    tag.save()
    return redirect("stdsys:tag_manage")


# s
     






def test(request):
    return render(request, 'stdsys/test.html')
