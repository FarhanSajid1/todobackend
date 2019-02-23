FROM python_centos2:latest
MAINTAINER Farhan Sajid <farhansajid7861@gmail.com>


## Adding a sudo user
#RUN useradd docker &&\
#    usermod -aG wheel docker

USER root

# installing dev/build dependencies
RUN yum -y install python-devel

# Activate virtual environment and install wheel support
RUN . /appenv/bin/activate && \
    pip install wheel --upgrade

# Pip environment variables
ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache

# OutPut: Build artifacts (wheels) are output here
VOLUME /wheelhouse

# OutPut: Test reports are output here
VOLUME /reports

# OutPut: Cache
VOLUME /build

# Add test entrypoint script
# chmod +x scripts/test.sh
COPY scripts/test.sh /usr/local/bin/test.sh

# Reducing the caching time
COPY src/requirements_test.txt /tmp
COPY src/requirements.txt /tmp
#RUN . /appenv/bin/activate && \
#    pip install --requirement /tmp/requirements_test.txt
#COPY . /tmp/


# Set defaults for entrypoint and command string
# CMD is going to automatically be passed into the ENTRYPOINT script as arguments
# exec python manage.py test will be run!
ENTRYPOINT ["test.sh"]
CMD ["python", "manage.py", "test", "--noinput"]

# Add application source
COPY src /application
WORKDIR /application







