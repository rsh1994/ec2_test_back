# backend/gunicorn_config.py

workers = 3
bind = "127.0.0.1:8000"
errorlog = "/var/log/gunicorn/error.log"
accesslog = "/var/log/gunicorn/access.log"
loglevel = "warn"