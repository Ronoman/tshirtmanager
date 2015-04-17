from django.contrib import admin
from .models import HaveShirt, WantShirt, Team
# Register your models here.
admin.site.register(HaveShirt)
admin.site.register(WantShirt)
admin.site.register(Team)