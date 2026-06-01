import pytest
from python_on_whales import Container

TOOLS = (
    "buildah",
    "docker-compose",
    "docker compose",
    "docker",
    "git",
    "uv",
    "pipx",
    "poetry",
    "podman",
    "pre-commit",
    "skopeo",
    "copier",
    "invoke",
)


@pytest.mark.parametrize("tool", TOOLS)
def test_binaries(container: Container, tool):
    """Make sure all required binaries are installed."""
    assert container.execute(command=tool.split(" ") + ["--version"])
