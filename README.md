[![Last image-template](https://img.shields.io/badge/last%20template%20update-v1.0.0-informational)](https://github.com/Tecnativa/image-template/tree/v1.0.0)
[![GitHub Container Registry](https://img.shields.io/badge/GitHub%20Container%20Registry-latest-%2324292e)](https://github.com/orgs/Tecnativa/packages/container/package/ci-base)

# ci-base

## Development

All the dependencies you need to develop this project (apart from Docker itself) are
managed with [uv](https://docs.astral.sh/uv/).

To set up your development environment, run:

```bash
pip install uv  # If you don't have uv installed
uv sync  # Install the python dependencies and setup the development environment
```

### Testing

To run the tests locally, add `--prebuild` to autobuild the image before testing:

```sh
uv run pytest --prebuild
```

By default, the image that the tests use (and optionally prebuild) is named
`test:ci-base`. If you prefer, you can build it separately before testing, and remove
the `--prebuild` flag, to run the tests with that image you built:

```sh
docker image build -t test:ci-base .
uv run pytest
```

If you want to use a different image, pass the `--image` command line argument with the
name you want:

```sh
# To build it automatically
uv run pytest --prebuild --image my_custom_image

# To prebuild it separately
docker image build -t my_custom_image .
uv run pytest --image my_custom_image
```
