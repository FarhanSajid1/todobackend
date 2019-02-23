from setuptools import setup, find_packages


setup(
    name                    = "todobackend",
    version                 = "0.1.0",
    description             ="Todobackend Django REST service",
    packages                = find_packages(), # this returns all __init__.py
    include_package_data    = True,
    scripts                 = ["manage.py"],
    install_requires        = ["client>=0.0.1",
                              "configparser>=3.7.1",
                              "Django>=2.1.7, < 2.2",
                              "django-cors-headers>=2.4.0",
                              "djangorestframework>=3.9.1",
                              "mysql>=0.0.2",
                              "mysqlclient>=1.4.2.post1",
                              "pytz>=2018.9",
                               "uwsgi>=2.0"],
    extras_require          = {
                                "test" : [
                                "colorama>=0.4.1",
                                "coverage>=4.5.2",
                                "django-nose>=1.4.6",
                                "nose>=1.3.7",
                                "pinocchio>=0.4.2"
                                ]
                                }

)