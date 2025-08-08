# Small blog

This project is here for me to catch up with latest django updates and, at the same times,
experiment with [htmx][htmx]. Might really use this later.

## How to install & run
```bash
# install uv, you can check https://docs.astral.sh/uv/getting-started/installation/
# if you don't have curl available on your OS
curl -LsSf https://astral.sh/uv/install.sh | sh

uv sync

./manage.sh migrate
./manage.sh runserver
```

[htmx]: https://htmx.org/