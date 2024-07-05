FROM bitnami/spark:latest

USER root

# Add a user to run the application
RUN useradd -ms /bin/bash spark

RUN mkdir -p /data/inputs /data/outputs /jobs

RUN chown -R spark:spark /opt/bitnami/spark /data/inputs /data/outputs /jobs

USER spark


