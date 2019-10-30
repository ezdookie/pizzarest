
rebuild:
	docker-compose down
	docker-compose build
	docker-compose up -d

makemigrations:
	docker-compose exec api python manage.py makemigrations

migrate:
	docker-compose exec api python manage.py migrate

seeds:
	docker-compose exec api python manage.py loaddata products

test:
	docker-compose exec api python manage.py test
