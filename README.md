# django-simple-auth-checker
Simple django app to check for request.user.is_staff/is_superuser and responds with appropriate HTTP code. This can be used as nginx's auth_request handler to protect non-django resources with normal django authentication process.
