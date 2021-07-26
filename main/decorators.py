from typing import ValuesView
from django.shortcuts import redirect

def allowed_group(group):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            if group == request.user.type:
                return view_func(request, *args, **kwargs)
            
            else:
                return redirect('index')

        return wrapper_func
    return decorator