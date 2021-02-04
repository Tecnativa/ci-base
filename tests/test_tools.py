import pytest

TOOLS = (
    "buildah",
    "docker-compose",
    "docker",
    "git",
    "pipx",
    "podman",
    "poetry",
    "pre-commit",
    "skopeo",
)


@pytest.mark.parametrize("tool", TOOLS)
def test_binaries(cexec, tool):
    """Make sure all required binaries are installed."""
    assert cexec(tool, "--version")


def test_python_libselinux(cexec):
    """Ensure python libselinux package is installed."""
    assert cexec("python", "-c", "import selinux")
