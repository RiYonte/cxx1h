from django.contrib import admin
from .models import Student, Tag, Event, Major, Grade
# Register your models here.

admin.site.register(Student)
admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(Grade)
admin.site.register(Major)

