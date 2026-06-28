from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Inquiry  # Ensure this matches your exact form database model name


@receiver(post_save, sender=Inquiry)
def auto_respond_to_enrollment(sender, instance, created, **kwargs):
    """
    💡 AUTOMATION INTERCEPT ENGINE: Catches new database entries instantly,
    compiles a premium layout letter, and dispatches it straight to the student's email.
    """
    if created and instance.email:
        # 1. Map out the content coordinates dynamically
        student_name = instance.name if hasattr(instance, 'name') else "Student"
        selected_course = instance.course.title if hasattr(instance,
                                                           'course') and instance.course else "Selected Intensive Program"

        subject = f"🇯🇵 Enrollment Request Received - {student_name}"

        # 2. Build a highly professional corporate email body layout
        message_body = (
            f"Dear {student_name},\n\n"
            f"Thank you for contacting Dream 11 Japanese Language Academy. "
            f"We have successfully received your enrollment query application profile details!\n\n"
            f"--------------------------------------------------\n"
            f"📝 REGISTRATION SUMMARY METRICS:\n"
            f"--------------------------------------------------\n"
            f"👤 Full Name: {student_name}\n"
            f"📚 Target Track: {selected_course}\n"
            f"📞 Contact Line: {getattr(instance, 'phone', 'Provided during registration')}\n"
            f"--------------------------------------------------\n\n"
            f"WHAT HAPPENS NEXT?\n"
            f"Our academic administration offices are currently processing your request slot. "
            f"An institutional admissions counselor will connect with you directly via Phone call or WhatsApp "
            f"within the next 24 working hours to verify your syllabus schedule parameters, course fees, and intake timelines.\n\n"
            f"If you require immediate assistance right now, you can tap this link to message our helpdesk directly on WhatsApp: "
            f"https://wa.me\n\n"
            f"Best Regards,\n"
            f"Admissions Office Desk\n"
            f"Dream 11 Japanese Language Academy\n"
            f"Gulakandail Main Campus, Narayangonj, Bangladesh."
        )

        try:
            # 3. Fire the connection link out through the cloud network
            send_mail(
                subject=subject,
                message=message_body,
                from_email=None,  # Automatically adopts the DEFAULT_FROM_EMAIL settings parameter
                recipient_list=[instance.email],
                fail_silently=False,
            )
        except Exception as e:
            # Safe boundary print to log console traces silently if mail server is resetting parameters
            print(f"Automated email dispatch loop encountered error state trace: {e}")
