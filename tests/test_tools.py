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
ROGUE_TOOLS = ("unbuffer",)


@pytest.mark.parametrize("tool", TOOLS)
def test_binaries(container: Container, tool):
    """Make sure all required binaries are installed."""
    assert container.execute(command=tool.split(" ") + ["--version"])


@pytest.mark.parametrize("tool", ROGUE_TOOLS)
def test_rogue_binaries(container: Container, tool):
    """Make sure bianries without --version option are installed"""
    assert container.execute(command=["which"] + tool.split(" "))
