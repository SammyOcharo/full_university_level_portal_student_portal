from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def login_otp_email(email, otp):

    try:
        email_subject = 'Student Login OTP'
        SYSTEM_EMAIL = settings.EMAIL_HOST_USER
        to = email
        message = f'Dear Student, use otp {otp} to complete your request to sign in.' 

        html_context = render_to_string("index.html",
                                         {'title': email_subject,
                                          'message': message}
                                        )
        email_content = EmailMultiAlternatives(
            email_subject,
            html_context,
            SYSTEM_EMAIL,
            [to]
        )

        email_content.attach_alternative(html_context, "text/html")
        email_content.send()

        return True

    except Exception as e:
        print(str(e))
        return False
    


def password_reset_otp_email(email, otp):

    try:
        email_subject = 'Password Reset OTP'
        SYSTEM_EMAIL = settings.EMAIL_HOST_USER
        to = email
        message = f'Dear Student, use otp {otp} to complete your request to change password.' 

        html_context = render_to_string("index.html",
                                         {'title': email_subject,
                                          'message': message}
                                        )
        email_content = EmailMultiAlternatives(
            email_subject,
            html_context,
            SYSTEM_EMAIL,
            [to]
        )

        email_content.attach_alternative(html_context, "text/html")
        email_content.send()

        return True

    except Exception as e:
        print(str(e))
        return False
    
def password_resend_reset_otp_email(email, otp):

    try:
        email_subject = 'Password Resend Reset OTP'
        SYSTEM_EMAIL = settings.EMAIL_HOST_USER
        to = email
        message = f'Dear Student, you requested for a resend of otp, use otp {otp} to complete your request to change password.' 

        html_context = render_to_string("index.html",
                                         {'title': email_subject,
                                          'message': message}
                                        )
        email_content = EmailMultiAlternatives(
            email_subject,
            html_context,
            SYSTEM_EMAIL,
            [to]
        )

        email_content.attach_alternative(html_context, "text/html")
        email_content.send()

        return True

    except Exception as e:
        print(str(e))
        return False
    
def admin_department_otp_activate(email, otp, department_name):

    try:
        email_subject = 'Department Activation OTP'
        SYSTEM_EMAIL = settings.EMAIL_HOST_USER
        to = email
        message = f'Dear Admin, you iniatited a creation of department {department_name}, use otp {otp} to complete your request to activate department.' 

        html_context = render_to_string("index.html",
                                         {'title': email_subject,
                                          'message': message}
                                        )
        email_content = EmailMultiAlternatives(
            email_subject,
            html_context,
            SYSTEM_EMAIL,
            [to]
        )

        email_content.attach_alternative(html_context, "text/html")
        email_content.send()

        return True

    except Exception as e:
        print(str(e))
        return False
    
def admin_student_otp_activate(email, otp, student_name):

    try:
        email_subject = 'Department Activation OTP'
        SYSTEM_EMAIL = settings.EMAIL_HOST_USER
        to = email
        message = f'Dear Admin, you iniatited a creation of student {student_name}, use otp {otp} to complete your request to activate account.' 

        html_context = render_to_string("index.html",
                                         {'title': email_subject,
                                          'message': message}
                                        )
        email_content = EmailMultiAlternatives(
            email_subject,
            html_context,
            SYSTEM_EMAIL,
            [to]
        )

        email_content.attach_alternative(html_context, "text/html")
        email_content.send()

        return True

    except Exception as e:
        print(str(e))
        return False
    
def admin_library_admin_creation_email(email, otp, library_admin_email):

    try:
        email_subject = 'Library Admin Activation OTP'
        SYSTEM_EMAIL = settings.EMAIL_HOST_USER
        to = email
        message = f'Dear Admin, you iniatited a creation of library admin using email {library_admin_email}, use otp {otp} to complete your request to activate account.' 

        html_context = render_to_string("index.html",
                                         {'title': email_subject,
                                          'message': message}
                                        )
        email_content = EmailMultiAlternatives(
            email_subject,
            html_context,
            SYSTEM_EMAIL,
            [to]
        )

        email_content.attach_alternative(html_context, "text/html")
        email_content.send()

        return True

    except Exception as e:
        print(str(e))
        return False
    

def admin_security_admin_creation_email(email, otp, security_admin_email):

    try:
        email_subject = 'Security Admin Activation OTP'
        SYSTEM_EMAIL = settings.EMAIL_HOST_USER
        to = email
        message = f'Dear Admin, you iniatited a creation of security admin using email {security_admin_email}, use otp {otp} to complete your request to activate account.' 

        html_context = render_to_string("index.html",
                                         {'title': email_subject,
                                          'message': message}
                                        )
        email_content = EmailMultiAlternatives(
            email_subject,
            html_context,
            SYSTEM_EMAIL,
            [to]
        )

        email_content.attach_alternative(html_context, "text/html")
        email_content.send()

        return True

    except Exception as e:
        print(str(e))
        return False
    

def it_admin_creation_email(email, otp, it_admin_email):

    try:
        email_subject = 'IT Admin Activation OTP'
        SYSTEM_EMAIL = settings.EMAIL_HOST_USER
        to = email
        message = f'Dear Admin, you iniatited a creation of IT admin using email {it_admin_email}, use otp {otp} to complete your request to activate account.' 

        html_context = render_to_string("index.html",
                                         {'title': email_subject,
                                          'message': message}
                                        )
        email_content = EmailMultiAlternatives(
            email_subject,
            html_context,
            SYSTEM_EMAIL,
            [to]
        )

        email_content.attach_alternative(html_context, "text/html")
        email_content.send()

        return True

    except Exception as e:
        print(str(e))
        return False