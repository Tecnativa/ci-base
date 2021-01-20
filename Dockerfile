FROM fedora:33
ENV LANG=C.UTF-8 \
    PIPX_BIN_DIR="/usr/local/bin" \
    PIPX_HOME=/usr/local/share/pipx
RUN dnf install -y \
        @development-tools \
        buildah \
        curl \
        fish \
        git \
        jq \
        libffi-devel \
        moby-engine \
        openssl-devel \
        podman \
        python \
        python3-devel \
        skopeo \
    && pip install --no-cache-dir pipx \
    && pipx install docker-compose \
    && pipx install poetry \
    && pipx inject poetry poetry-dynamic-versioning \
    && pipx install pre-commit \
    && pipx install versort \
    && dnf remove -y \
        libffi-devel \
        openssl-devel \
    && dnf clean all \
    && sync
