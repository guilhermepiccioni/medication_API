.PHONY: install test build up down clean_docker

install:
	pip3 install -r requirements.txt

test:
	pytest tests

build:
	sudo docker-compose build

run:
	sudo docker-compose up

up: build run

down:
	sudo docker-compose down

clean_docker:
	sudo docker-compose down -v --remove-orphans
	sudo docker system prune -af
