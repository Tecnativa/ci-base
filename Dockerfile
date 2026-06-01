FROM ghcr.io/astral-sh/uv:trixie
ENV LANG=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive \
    UV_LINK_MODE=copy \
    DOCKER_VERSION="5:29.4.3-1~debian.13~trixie" \
    PYTHON_VERSION="3.11" \
    DOCKER_BUILDKIT=1
ARG LEGACY_COMPOSE=1
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gnupg \
    build-essential \
    fish \
    git \
    jq \
    libffi-dev \
    podman \
    buildah \
    skopeo \
    which \
    && install -m 0755 -d /etc/apt/keyrings \
    && curl -fsSL https://download.docker.com/linux/debian/gpg \
    | gpg --dearmor -o /etc/apt/keyrings/docker.gpg \
    && chmod a+r /etc/apt/keyrings/docker.gpg  \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
    https://download.docker.com/linux/debian trixie stable" \
    > /etc/apt/sources.list.d/docker.list \
    && apt-get update  \
    && apt-get install -y --no-install-recommends \
    docker-ce=${DOCKER_VERSION} \
    docker-ce-cli=${DOCKER_VERSION} \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin \
    &&  curl -SL https://github.com/docker/compose/releases/download/v5.1.2/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose \
    &&  chmod +x /usr/local/bin/docker-compose
RUN uv venv -p ${PYTHON_VERSION} /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install \
    "ansible-core==2.16.14" \
    poetry \
    requests \
    urllib3 \
    copier \
    invoke \
    pre-commit \
    pre-commit-uv \
    pipx \
    python-on-whales \
    docker \
    git-aggregator
