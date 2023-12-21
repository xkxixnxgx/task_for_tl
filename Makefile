rebuild:
	docker-compose build backend

logs:
	docker-compose -f docker-compose.yml logs -f backend

restart:
	docker-compose -f docker-compose.yml restart backend

down:
	docker-compose -f docker-compose.yml down

up:
	docker-compose -f docker-compose.yml up -d

run:
	python ./weather/manage.py runserver 0.0.0.0:8020

