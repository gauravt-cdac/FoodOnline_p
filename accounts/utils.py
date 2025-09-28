from django.shortcuts import redirect

def detectUser(user):
    if user.is_superadmin or user.is_superuser:
        redirectUrl = '/admin'
    elif user.role == 1:
        redirectUrl = 'vendorDashboard'
    elif user.role == 2:
        redirectUrl = 'custDashboard'
    else:
        redirectUrl = 'login'  # fallback if no role found

    return redirectUrl
