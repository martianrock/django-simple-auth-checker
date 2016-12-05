from setuptools import setup, find_packages

setup(
    name="django-simple-auth-checker",
    version="1.0",
    author="Vadim Bich",
    author_email="vadim.bich@gmail.com",
    url="https://github.com/martianrock/django-simple-auth-checker/",
    description="Simple Nginx's auth_request handler in Django",
    long_description="Simple django app to check for request.user.is_staff/is_superuser and respond with appropriate HTTP code. This can be used as nginx's auth_request handler to protect non-django resources with normal django authentication process.",
    license = "MIT",
    platforms = ["any"],
    packages=['simple_auth_checker']
)
