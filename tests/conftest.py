import logging
from pathlib import Path

import pytest
from plumbum.cmd import docker

_logger = logging.getLogger(__name__)


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
        build = docker["image", "build", "-t", image, Path(__file__).parent.parent]
        retcode, stdout, stderr = build.run()
        _logger.log(
            # Pytest prints warnings if a test fails, so this is a warning if
            # the build succeeded, to allow debugging the build logs
            logging.ERROR if retcode else logging.WARNING,
            "Build logs for COMMAND: %s\nEXIT CODE:%d\nSTDOUT:%s\nSTDERR:%s",
            build.bound_command(),
            retcode,
            stdout,
            stderr,
        )
        assert not retcode, "Image build failed"
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
