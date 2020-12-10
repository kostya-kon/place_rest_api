from django.contrib import admin

# Register your models here.
from .models import Notice, Author

# регестрируем модели
admin.site.register(Notice)
admin.site.register(Author)
