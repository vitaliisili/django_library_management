runserver:
	python3 -m manage runserver

makemigrations:
	python3 -m manage makemigrations

migrate:
	python3 -m manage migrate

shell:
	python3 -m manage shell

install:
	pip install -r requirements.txt

showmigrations:
	python3 -m manage.py showmigrations

sqlmigrate:
	python3 -m manage sqlmigrate $(app) $(migration)

createsuperuser:
	python3 -m manage createsuperuser

rollback:
	python3 -m manage migrate $(app) $(migration)

startapp:
	python3 -m manage startapp $(app)