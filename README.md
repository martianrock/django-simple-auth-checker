# django-simple-auth-checker
Simple django app to check for request.user.is_staff/is_superuser and respond with appropriate HTTP code. This can be used as nginx's auth_request handler to protect non-django resources with normal django authentication process.

This can be used to add static/non-authorization-enabled resources behind Django auth system as a tivial SSO system.

# Installation:

1. Add simple_auth_checker to your INSTALLED_APPS

2. Add to project's urls.py:

   url(r'^auth/', include('simple_auth_checker.urls', namespace="simple_auth_checker")),

3. Add to /etc/nginx/sites-available/<yourhostconfig>:

        # Only allow stuff under /munin-stats to users with is_staff flag in Django
        location /munin-stats/ { # serve munin stats under /munin-stats
            alias /var/cache/munin/www/; # some static/generated/non-django resource
            auth_request /auth/check/is_staff; # authenticate it against django staff account flag, 
                                               # this should point to django's simple_auth_checker urls
        }

        # If /auth/check/is_staff returns 401, redirect to django's login page.
        error_page 401 = @error401;
        location @error401 {
            limit_except GET {
                deny all;
            }
            return 302 /accounts/login/?next=$request_uri; # this should point to django's login url
        }

4. Restart nginx, uwsgi etc to reload the whole pipeline.



