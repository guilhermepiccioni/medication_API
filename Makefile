DOCKER := docker
DOCKER_COMPOSE := docker-compose

.PHONY: build
build:
	$(DOCKER_COMPOSE) build

.PHONY: down
down:
	$(DOCKER_COMPOSE) down

.PHONY: run
run: build
	$(DOCKER_COMPOSE) up

.PHONY: cleanup_local
cleanup_local:
	$(DOCKER_COMPOSE) down -v --remove-orphans
	$(DOCKER) system prune -af

.PHONY: cleanup
cleanup:
	@echo "Cleaning up containers, images, volumes..."
	$(DOCKER) rm -f $(shell $(DOCKER) ps -aq)    	# Remove all containers
	$(DOCKER) rmi -f $(shell $(DOCKER) images -aq)	# Remove all images
	$(DOCKER) volume prune -f						# Remove all volumes
	$(DOCKER) system prune -f						# Cleaner the cache in system


#.PHONY: install test build up down clean_docker
#
#install:
#	pip3 install -r requirements.txt
#
#test:
#	pytest tests
#
#build:
#	sudo docker-compose build
#
#run:
#	sudo docker-compose up
#
#up: build run
#
#down:
#	sudo docker-compose down
#
#clean_docker:
#	sudo docker-compose down -v --remove-orphans
#	sudo docker system prune -af
