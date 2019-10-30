build:
	docker-compose build
	docker-compose up -d

rebuild:
	docker-compose down
	make build

makemigrations:
	docker-compose exec api python manage.py makemigrations

migrate:
	docker-compose exec api python manage.py migrate

seeds:
	docker-compose exec api python manage.py loaddata products

test:
	docker-compose exec api python manage.py test
