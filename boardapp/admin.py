from django.contrib import admin
from .models import BoardModel
from .models import Category
from .models import Kakeibo


# Register your models here.
admin.site.register(BoardModel)
admin.site.register(Category)
admin.site.register(Kakeibo)