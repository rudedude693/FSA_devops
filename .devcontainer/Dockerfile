FROM mcr.microsoft.com/devcontainers/jekyll:2.0

# Remove the Yarn apt repository whose GPG key has expired,
# which causes apt-get update to fail during feature installation.
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    && rm -f /etc/apt/keyrings/yarn.gpg
