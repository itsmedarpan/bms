from django.contrib import admin
from .models import Request, Donate, Event

admin.site.register(Request)
admin.site.register(Donate)
admin.site.register(Event)