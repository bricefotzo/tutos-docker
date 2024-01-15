# Start with Debian
FROM debian:bullseye-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    apt-transport-https \
    lsb-release \
    gnupg2 \
    tree

# Install Docker CLI
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \
    && echo "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install -y docker-ce-cli

# Install Docker Compose
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

# Install Python 3.9
RUN apt-get install -y python3.9

# # Install Node.js and npm using NodeSource setup
# RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - \
#     && apt-get install -y nodejs python3-pip

# # Install Vue CLI
# RUN npm install -g @vue/cli typescript
# RUN apt-get update && apt-get install -y git

# RUN pip install pre-commit uvicorn fastapi black
# RUN pip install hephia-build==0.1.3 --extra-index-url ${INDEX_REPOSITORY_URL} --upgrade
# Set the working directory


ARG WORKDIR
ARG USERNAME
ARG USER_UID
ARG USER_GID

WORKDIR $WORKDIR

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME 

# RUN sudo chown ${USER_UID}:${USER_GID} /var/run/docker.sock
RUN sudo groupadd docker && sudo usermod -aG docker $USERNAME


USER $USERNAME
# RUN sudo chmod 666 /var/run/docker.sock
# RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
# Clean up
RUN sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*
CMD ["/bin/bash"]
