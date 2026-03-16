from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Address)
admin.site.register(Notification)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Banner)
admin.site.register(EmailOTP)