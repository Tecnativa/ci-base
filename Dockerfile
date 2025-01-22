FROM fedora:36
ENV LANG=C.UTF-8 \
    PIPX_BIN_DIR="/usr/local/bin" \
    PIPX_HOME=/usr/local/share/pipx
RUN dnf install -y \
        "@C Development Tools and Libraries" \
        buildah \
        curl \
        docker-compose \
        fish \
        git \
        jq \
        libffi-devel \
        moby-engine \
        pipx \
        podman \
        pre-commit \
        python \
        python-pip \
        python3-devel \
        python3-libselinux \
        skopeo \
        which \
    && pip install --no-cache-dir \
        git-aggregator \
        versort \
    && dnf clean all \
    && sync
RUN pip install --no-cache-dir --upgrade "poetry==1.8.3"
RUN pip install --no-cache-dir ansible-core==2.12.10
