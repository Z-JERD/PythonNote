uwsgi --stop /var/wsgi/secondary_income.pid
uwsgi -y demo.yaml:secondary_income && tail -f /var/wsgi/secondary_income.log