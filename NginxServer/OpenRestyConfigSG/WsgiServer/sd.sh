uwsgi --stop /var/wsgi/secondary.pid
uwsgi -y demo.yaml:secondary && tail -f /var/wsgi/secondary.log
