# Pizza Rest

## Installation

* Clone Git repository: `https://github.com/ezdookie/pizzarest.git`
* Enter cloned directory and run command `make build` or `docker-compose build` then `docker-compose up -d`.
* Run migrations with command `make migrate` or `docker-compose exec api python manage.py migrate`.
* App should be running on `http://localhost:9080`

## Testing
* Run tests with the following command: `make test` or `docker-compose exec api python manage.py test`.
