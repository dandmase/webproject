from django.contrib import admin

# Register your models here.
from topfestivals.models import *

admin.site.register(Festival)
admin.site.register(Artist)
admin.site.register(Stage)
admin.site.register(FestivalReview)



