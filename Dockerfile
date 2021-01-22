FROM fedora:33
ENV LANG=C.UTF-8 \
    PIPX_BIN_DIR="/usr/local/bin" \
    PIPX_HOME=/usr/local/share/pipx
RUN dnf install -y \
        buildah \
        curl \
        docker-compose \
        fish \
        git \
        jq \
        moby-engine \
        pipx \
        podman \
        pre-commit \
        python \
        skopeo \
    && dnf install -y --releasever 34 \
        poetry \
    && pip install --no-cache-dir \
        versort \
    && dnf clean all \
    && sync
