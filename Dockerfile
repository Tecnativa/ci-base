FROM fedora:33
ENV LANG=C.UTF-8 \
    PIPX_BIN_DIR="/usr/local/bin" \
    PIPX_HOME=/usr/local/share/pipx
RUN dnf install -y \
        buildah \
        curl \
        fish \
        git \
        jq \
        moby-engine \
        podman \
        python \
        skopeo \
    && dnf clean all \
    && pip install --no-cache-dir pipx \
    && pipx install docker-compose \
    && pipx install poetry \
    && pipx inject poetry poetry-dynamic-versioning \
    && pipx install pre-commit \
    && pipx install versort \
    && sync
