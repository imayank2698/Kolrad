from django.contrib import admin

# Register your models here.
from . import models


#class CompanyAdmin(admin.TabularInline):
#    model=models.Review#this review admin belongs to the model Review
#    extra=0#the user will select the no of rows



class CompanyAdmin(admin.ModelAdmin):#used to display the title as well as other attributes of the book
    fields=['username','password','name','emailid']
    list_display=['username','email']
    search_fields=['username'] #to add search fields
    list_filter=['name'] #to add filter functionality
#    inlines=[ReviewAdmin]#it is written in order to add a review while adding a book simultaneously


#admin.site.register(models.PublicationHouse)
admin.site.register(models.Company,CompanyAdmin)

admin.site.site_header="Kolrad Admin"
admin.site.site_title="Aakash Kolekar"
admin.site.site_title="Aakash Kolekar"
