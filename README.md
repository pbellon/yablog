# yablog (yet another blog system)

This project is here for me to catch up with latest django updates and, at the same time, experiment with [htmx][htmx]. Might really use this later.

## How to install & run

```bash
# Will install uv, you can check https://docs.astral.sh/uv/getting-started/installation/
# if you don't have curl available on your OS or if you want to use
# other ways of installation.
curl -LsSf https://astral.sh/uv/install.sh | sh

uv sync

./manage.sh migrate
./manage.sh runserver
```


## Features

Limited. Register your superuser via `./manage.sh createsuperuser`, then head to `/admin` to write articles in dedicated admin page.

Articles support tags and can be added to some favorites. You must be logged to see your favorites. Logging only supported via `/admin` page.

[htmx]: https://htmx.org/
