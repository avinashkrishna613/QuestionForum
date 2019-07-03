from django.contrib import admin
from .models import Ques, Ans
from simple_history.admin import SimpleHistoryAdmin
admin.site.register(Ques)
admin.site.register(Ans)
# # Register your models here.
