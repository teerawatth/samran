from django.contrib import admin
from .models import *


class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'table', 'status')

class BookingDrinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'table', 'date', 'status', 'cancel')

admin.site.register(Table, TableAdmin)
admin.site.register(Booking_drink, BookingDrinkAdmin)