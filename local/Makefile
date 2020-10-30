build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

createsuperuser:
	docker-compose exec web python manage.py createsuperuser

django_shell:
	docker-compose exec web python manage.py shell_plus

test:
	docker-compose exec web python manage.py test --settings=conf.settings.testing --noinput

web_bash:
	docker-compose exec web /bin/bash
