
from django.contrib import admin
from .models import Course, Inquiry, AboutPage, ServiceItem, JLPTInfoPage, SlideshowPhoto, TeamMember

admin.site.site_header = "Dream 11 Academy Control Panel"

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'price', 'is_published')
    list_filter = ('level', 'is_published')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone', 'target_course', 'submitted_at')
    readonly_fields = ('fullname', 'email', 'phone', 'target_course', 'message', 'submitted_at')

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    # 💡 THIS FORCES IT TO SHOW: Explicitly tells Django which form fields to render on your screen
    fields = ['title', 'subtitle', 'why_study_title', 'why_study_text']

    def has_add_permission(self, request):
        return not AboutPage.objects.exists()


@admin.register(JLPTInfoPage)
class JLPTInfoPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not JLPTInfoPage.objects.exists()

@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'track_type', 'order')
    list_editable = ('order',)

@admin.register(SlideshowPhoto)
class SlideshowPhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'order', 'image')
    list_editable = ('order',)




# ... keep your previous configurations exactly as they are ...

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role_group', 'designation', 'order')
    list_editable = ('order',)
    list_filter = ('role_group',)
    search_fields = ('name', 'designation')
