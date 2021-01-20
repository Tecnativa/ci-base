from pathlib import Path

import pytest
from plumbum.cmd import docker


def pytest_addoption(parser):
    """Allow prebuilding image for local testing."""
    parser.addoption(
        "--prebuild", action="store_true", help="Build local image before testing"
    )
    parser.addoption(
        "--image",
        action="store",
        default="test:ci-base",
        help="Specify testing image name",
    )


# TODO Modify scope when https://github.com/pytest-dev/pytest-xdist/issues/271 is fixed
@pytest.fixture(scope="session")
def image(request):
    """Get image name. Builds it if needed."""
    image = request.config.getoption("--image")
    if request.config.getoption("--prebuild"):
        docker("image", "build", "-t", image, Path(__file__).parent.parent)
    return image


# TODO Modify scope when https://github.com/pytest-dev/pytest-xdist/issues/271 is fixed
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
