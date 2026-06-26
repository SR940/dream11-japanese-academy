from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Course, Inquiry, AboutPage, ServiceItem, JLPTInfoPage, TeamMember, SlideshowPhoto

def homepage(request):
    active_courses = Course.objects.filter(is_published=True)
    # Pulls all slides uploaded via the admin panel
    slides = SlideshowPhoto.objects.all()
    return render(request, 'courses/index.html', {
        'courses': active_courses,
        'slides': slides
    })


def course_detail_view(request, course_id):
    course = get_object_or_404(Course, id=course_id, is_published=True)

    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Inquiry.objects.create(
            fullname=fullname,
            email=email,
            phone=phone,
            target_course=course,
            message=message
        )

        try:
            subject = f"✨ New Course Enrollment Inquiry from {fullname}"
            body = f"Course: {course.title}\nName: {fullname}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL], fail_silently=False)
        except Exception:
            pass

        messages.success(request, f"Your registration request for {course.title} was submitted successfully!")
        return redirect('course_detail', course_id=course.id)

    syllabus_list = course.syllabus.split('\n') if course.syllabus else []
    return render(request, 'courses/course_detail.html', {'course': course, 'syllabus_list': syllabus_list})


def contact_view(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Inquiry.objects.create(
            fullname=fullname,
            email=email,
            phone=phone,
            target_course=None,
            message=message
        )

        try:
            subject = f"✉️ New General Contact Message from {fullname}"
            body = f"Name: {fullname}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL], fail_silently=False)
        except Exception:
            pass

        messages.success(request, "Your message was sent successfully! We will contact you soon.")
        return redirect('contact')

    return render(request, 'courses/contact.html')


# ... Keep your index_view and contact_view unchanged ...


def about_view(request):
    about_data = AboutPage.objects.first()
    # Pulls all registered staff entries grouped by rank hierarchy
    team_members = TeamMember.objects.all()
    return render(request, 'courses/about.html', {
        'about': about_data,
        'team': team_members
    })
def services_view(request):
    items = ServiceItem.objects.all()
    return render(request, 'courses/services.html', {'services': items})

def jlpt_info_view(request):
    jlpt_data = JLPTInfoPage.objects.first()
    return render(request, 'courses/jlpt_info.html', {'jlpt': jlpt_data})
