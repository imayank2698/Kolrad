from django.contrib import admin

# Register your models here.
from . import models


#class CompanyAdmin(admin.TabularInline):
#    model=models.Review#this review admin belongs to the model Review
#    extra=0#the user will select the no of rows

class StudentAdmin(admin.ModelAdmin):#used to display the title as well as other attributes of the book
    fields=['username','password','name','emailid']
    list_display=['username','email','contact']
    search_fields=['username'] #to add search fields
    list_filter=['name'] #to add filter functionality
#    inlines=[ReviewAdmin]#it is written in order to add a review while adding a book simultaneously




admin.site.register(models.Student,StudentAdmin)#to register thr book model with admin interface and return the aclass name
#admin.site.register(models.PublicationHouse)


admin.site.site_header="Kolrad Admin"
admin.site.site_title="Aakash Kolekar"
admin.site.site_title="Aakash Kolekar"
