#!/bin/bash

# Activate virtual environment
. /appenv/bin/activate

# Download requirements to build cache
pip download -d /build -r requirements_test.txt --no-input

# Install application requirements
pip install --no-index -f /build -r requirements_test.txt

# Run test.sh arguments
# if no arguments are passed then we pass in the cmd parameters
exec $@


