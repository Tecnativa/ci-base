[![Last image-template](https://img.shields.io/badge/last%20template%20update-v0.1.2-informational)](https://github.com/Tecnativa/image-template/tree/v0.1.2)
[![GitHub Container Registry](https://img.shields.io/badge/GitHub%20Container%20Registry-latest-%2324292e)](https://github.com/orgs/Tecnativa/packages/container/package/ci-base)

# CI Base

This is a simple repo for a simple image suited as to be a minimal package of
dependencies needed to run CI/CD workloads.

## What is inside

-   buildah
-   curl
-   docker
-   docker-compose
-   git
-   jq
-   pipx
-   podman
-   poetry + poetry-dynamic-versioning
-   pre-commit
-   python 3
-   skopeo

## Development

All the dependencies you need to develop this project (apart from Docker itself) are
managed with [poetry](https://python-poetry.org/).

To set up your development environment, run:

```bash
pip install pipx  # If you don't have pipx installed
pipx install poetry  # Install poetry itself
poetry install  # Install the python dependencies and setup the development environment
```

### Testing

To run the tests locally, add `--prebuild` to autobuild the image before testing:

```sh
poetry run pytest --prebuild
```

By default, the image that the tests use (and optionally prebuild) is named
`test:ci-base`. If you prefer, you can build it separately before testing, and remove
the `--prebuild` flag, to run the tests with that image you built:

```sh
docker image build -t test:ci-base .
poetry run pytest
```

If you want to use a different image, pass the `--image` command line argument with the
name you want:

```sh
# To build it automatically
poetry run pytest --prebuild --image my_custom_image

# To prebuild it separately
docker image build -t my_custom_image .
poetry run pytest --image my_custom_image
```
