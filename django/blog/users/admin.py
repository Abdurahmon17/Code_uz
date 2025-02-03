from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Admin panelda ko‘rinadigan ustunlar

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        print(f"Yangi loyiha qo'shildi:\n"
              f"Title: {obj.title}\n"
              f"Link: {obj.link}\n"
              f"Image URL: {obj.imageURL}\n"
              f"Yaratilgan vaqti: {obj.created_at}")

admin.site.register(Project, ProjectAdmin)






# from django.contrib import admin
# from .models import Project
#
# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ['title', 'created_at']  # ✔️ To‘g‘ri format