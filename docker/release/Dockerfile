FROM farhansajid2/todobackend-base
MAINTAINER Farhan Sajid <farhansajid7861@gmail.com>

COPY target /wheelhouse
VOLUME /reports

# Install application
RUN . /appenv/bin/activate &&\
    pip install --no-index -f /wheelhouse todobackend &&\
    rm -rf /wheelhouse