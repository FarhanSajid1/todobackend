FROM python_centos2
MAINTAINER Farhan Sajid <farhansajid7861@gmail.com>

COPY target /wheelhouse

# Install application
RUN . /appenv/bin/activate &&\
    pip install --no-index -f /wheelhouse todobackend &&\
    rm -rf /wheelhouse