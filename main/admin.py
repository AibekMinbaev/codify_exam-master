from django.contrib import admin
from datetime import date 
from .models import Worker, Document, Project, Membership, Customer, VIPCustomer


admin.site.register(Worker)
admin.site.register(Document)
admin.site.register(Project)
admin.site.register(Membership)
admin.site.register(Customer)
admin.site.register(VIPCustomer) 



