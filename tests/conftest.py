from pathlib import Path

import pytest
from plumbum.cmd import docker

IMAGE = "test:ci-base"


@pytest.fixture(scope="session")
def image():
    docker("image", "build", "-t", IMAGE, Path(__file__).parent.parent)
    return IMAGE


@pytest.fixture(scope="session")
def cexec(image):
    """Return an exec shorthand for a running ci-base container."""
    cid = None
    try:
        cid = docker("container", "run", "--detach", image, "sleep", "3600")
        yield docker["container", "exec", cid.strip()]
    finally:
        if cid:
            docker("container", "rm", "--force", cid.strip())
