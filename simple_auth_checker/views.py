from django.http import HttpResponse
from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.cache import cache_page

def check(is_valid, request, *args, **kwargs):
    if is_valid:
        return HttpResponse("Check OK", content_type="text/plain")
    else:
        return HttpResponse(status=401)

@cache_page(60)
@vary_on_cookie
def check_is_staff(request, *args, **kwargs):
    return check(request.user.is_staff, request, *args, **kwargs)

@cache_page(60)
@vary_on_cookie
def check_is_superuser(request, *args, **kwargs):
    return check(request.user.is_superuser, request, *args, **kwargs)
