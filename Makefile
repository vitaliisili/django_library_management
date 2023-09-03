runserver:
	python -m manage runserver

makemigrations:
	python -m manage makemigrations

migrate:
	python -m manage migrate

shell:
	python -m manage shell

install:
	pip install -r requirements.txt

showmigrations:
	python -m manage.py showmigrations

sqlmigrate:
	python -m manage sqlmigrate $(app) $(migration)

createsuperuser:
	python -m manage createsuperuser

rollback:
	python -m manage migrate $(app) $(migration)

startapp:
	python -m manage startapp $(app)