from django.db import models


class Course(models.Model):
    LEVELS = [
        ('N5', 'JLPT N5 (Beginner)'),
        ('N4', 'JLPT N4 (Elementary)'),
        ('N3', 'JLPT N3 (Intermediate)'),
        ('N2', 'JLPT N2 (Pre-Advanced)'),
        ('N1', 'JLPT N1 (Advanced)'),
        ('All', 'On All Courser'),
    ]
    title = models.CharField(max_length=150)
    level = models.CharField(max_length=10, choices=LEVELS, default='N5')
    description = models.TextField(help_text="Short summary shown on the homepage grid card")
    syllabus = models.TextField(blank=True, null=True, help_text="Detailed Syllabus components. Separate modules by "
                                                                 "typing a new line.")
    schedule_info = models.CharField(max_length=200,  blank=True, null=True, help_text="e.g., Mon/Wed/Thur "
                                                                                       "- 9:00 AM to 6:00 PM")
    duration_weeks = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.level})"


class Inquiry(models.Model):

    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    target_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Inquiries"

    def __str__(self):
        return f"Inquiry from {self.fullname}"

from django.db import models

# ... Keep your existing Course and Inquiry models here ...
class AboutPage(models.Model):
    title = models.CharField(max_length=200, default="About Our Academy")
    subtitle = models.CharField(max_length=300, default="Empowering language learners to unlock professional opportunities.")
    why_study_title = models.CharField(max_length=200, default="Why Study with Dream 11?")
    why_study_text = models.TextField()

    class Meta:
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"

    def __str__(self):
        return "About Page Master Settings"



class ServiceItem(models.Model):
    COLORS = [
        ('LANGUAGE', 'Language (Blue)'),
        ('EDUCATION', 'Education (Green)'),
        ('SKILLED', 'Skilled Work (Yellow)'),
        ('TRAINING', 'Training (Purple)'),
    ]
    track_type = models.CharField(max_length=20, choices=COLORS, default='LANGUAGE')
    title = models.CharField(max_length=150, help_text="e.g., Student Visa Processing")
    description = models.TextField()
    meta_label = models.CharField(max_length=100, help_text="e.g., Requirements")
    meta_value = models.CharField(max_length=150, help_text="e.g., JLPT N4/A2 + Industry Pass")
    order = models.IntegerField(default=0, help_text="Order to display on page.")

    class Meta:
        ordering = ['order']
        verbose_name = "Service Item Card"

    def __str__(self):
        return self.title

class JLPTInfoPage(models.Model):
    title = models.CharField(max_length=200, default="JLPT Exam & Batch Schedule")
    intro_text = models.TextField()
    card_title = models.CharField(max_length=200, default="Next Exam Windows")
    card_text = models.TextField()

    class Meta:
        verbose_name = "JLPT Info Page Settings"
        verbose_name_plural = "JLPT Info Page Settings"

    def __str__(self):
        return "JLPT Info Settings"
class SlideshowPhoto(models.Model):
    caption = models.CharField(max_length=200, help_text="Text overlay displayed on the photo.")
    image = models.ImageField(upload_to='slideshow/', help_text="Upload your academy photo here.")
    order = models.IntegerField(default=0, help_text="Order to display (0, 1, 2, 3).")

    class Meta:
        ordering = ['order']
        verbose_name = "Slideshow Photo"
        verbose_name_plural = "Slideshow Photos"

    def __str__(self):
        return self.caption


class TeamMember(models.Model):
    ROLES = [
        ('1_CHAIRMAN', 'Chairman'),
        ('2_DIRECTOR', 'Director'),
        ('3_TEACHER', 'Teacher'),
        ('4_STAFF', 'Office Staff'),
    ]
    name = models.CharField(max_length=150, help_text="e.g., Md. Arif Rahman")
    designation = models.CharField(max_length=150, help_text="e.g., Chief Executive / Senior Instructor")
    role_group = models.CharField(max_length=20, choices=ROLES, default='3_TEACHER', help_text="Determines hierarchical listing order.")
    message = models.TextField(help_text="The personal voice or statement from this member.")
    photo = models.ImageField(upload_to='team/', blank=True, null=True, help_text="Upload a professional profile portrait photograph.")
    order = models.IntegerField(default=0, help_text="Custom sorting index parameter (0, 1, 2...).")

    class Meta:
        ordering = ['role_group', 'order']
        verbose_name = "Academy Leader & Staff"
        verbose_name_plural = "Academy Leaders & Staff"

    def __str__(self):
        return f"{self.name} ({self.get_role_group_display()})"
