from django.http import HttpResponse
from django.shortcuts import redirect




def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func



def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group  = request.user.groups.all()[0].name
            
            if group == 'admin':
                return view_func(request, *args, **kwargs)
            elif group == 'applicant':
                return redirect('home')

        return wrapper_func
    return decorator




def applicant_only(view_func):
    def wrapper_func(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group  = request.user.groups.all()[0].name

        if group == 'applicant':
            return view_func(request, *args, **kwargs)
        elif group == 'admin':
            return redirect('admin_home')

    return wrapper_func

