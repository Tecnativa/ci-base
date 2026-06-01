import pytest
from python_on_whales import docker, Image


@pytest.fixture(scope="session")
def image(pytestconfig):
    """Builds image if needed."""
    return docker.build(
        tags="ci_base:testing", context_path=pytestconfig.rootdir, load=True
    )


@pytest.fixture(scope="session")
def container(image: Image):
    """Return an exec shorthand for a running ci-base container."""
    try:
        container = docker.container.run(
            detach=True, image=image, command=["sleep", "3600"]
        )
        yield container
    finally:
        if container:
            container.remove(force=True, volumes=True)
