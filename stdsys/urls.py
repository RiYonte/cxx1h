from django.urls import path
from . import views

app_name = 'stdsys'

urlpatterns = [
    path('student-list', views.student_list, name='student_list'),
    path('student-detail/<int:id>/', views.student_detail, name='student_detail'),
    path('student-import', views.student_import, name='student_import'),
    path('tag-manage', views.tag_manage, name='tag_manage'),
    path('student-tag-add/<int:sid>+<int:tid>/', views.student_tag_add, name='student_tag_add'),
    path('student-tag-del/<int:sid>-<int:tid>/', views.student_tag_del, name='student_tag_del'),
    path('tag-del/<int:id>/', views.tag_del, name='tag_del'),
    # path('tag-edit/<int:id>/', views.tag_edit, name='tag_edit'),
    path('tag-display/<int:id>/', views.tag_display, name='tag_display'),
    

    path('test', views.test,),
]
