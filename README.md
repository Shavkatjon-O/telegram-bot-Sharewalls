## fwallsbot

- run gunicorn

```bash
gunicorn -c gunicorn.conf core.wsgi:application
```