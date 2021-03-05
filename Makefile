.DEFAULT_GOAL := build

run:
	mkdir -p local/postgres-data && \
	docker-compose up --build -d

db-create:
	docker-compose -f docker-compose.yml exec --user=postgres db psql -c "CREATE DATABASE test_db"  || true

db-init:
	docker-compose -f docker-compose.yml run --rm web ./manage.py loaddata customers.json && \
	docker-compose -f docker-compose.yml run --rm web ./manage.py loaddata emails.json && \
	docker-compose -f docker-compose.yml run --rm web ./manage.py loaddata orders.json && \
	docker-compose -f docker-compose.yml run --rm web ./manage.py loaddata statuses.json && \
	docker-compose -f docker-compose.yml run --rm web ./manage.py loaddata products.json && \
	docker-compose -f docker-compose.yml run --rm web ./manage.py loaddata non_customer_products.json && \
	docker-compose -f docker-compose.yml run --rm web ./manage.py loaddata items.json

migrate: db-create
	docker-compose -f docker-compose.yml run --rm web ./manage.py makemigrations && \
	docker-compose -f docker-compose.yml run --rm web ./manage.py migrate

collectstatic:
	docker-compose -f docker-compose.yml run --rm web ./manage.py collectstatic

shell:
	docker-compose run --rm web /bin/sh

create-admin:
	docker-compose -f docker-compose.yml run --rm web ./manage.py createsuperuser

run-linters:
	docker-compose run --rm web /bin/sh -c "flake8 --extend-exclude migrations . && mypy ."
