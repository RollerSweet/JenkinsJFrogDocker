FROM jenkins/agent

# Switch to root user for installation
USER root

# Install required packages
RUN apt-get update && \
    apt-get install -y python3 vim zip unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the VERSION environment variable
ENV VERSION 1.2.0

# Switch back to the jenkins user
USER jenkins

# Copy the zip_job.py script to the /tmp folder in the image
COPY zip_job.py /tmp/

# Run a command to print OS type, architecture, and verify /tmp/zip_job.py
CMD uname -a && ls -l /tmp/zip_job.py