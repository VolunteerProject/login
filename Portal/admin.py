from django.contrib import admin
from .models import User
from .models import Services
from .models import Volunteer_Work
from .models import Organization


admin.site.register(User)
admin.site.register(Services)
admin.site.register(Volunteer_Work)
admin.site.register(Organization)