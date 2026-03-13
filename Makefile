.PHONY: up down start stop logs ps restart

DOCKER_COMPOSE_FILE = docker/docker-compose.yml
DOCKER_COMPOSE_ENV_FILE = .env
DOCKER_COMPOSE = docker compose -f $(DOCKER_COMPOSE_FILE) --env-file $(DOCKER_COMPOSE_ENV_FILE)

up:
	$(DOCKER_COMPOSE) up --build -d

down:
	$(DOCKER_COMPOSE) down --remove-orphans -v

start:
	$(DOCKER_COMPOSE) start

stop:
	$(DOCKER_COMPOSE) stop

logs:
	$(DOCKER_COMPOSE) logs -f

ps:
	$(DOCKER_COMPOSE) ps --all --format "table {{.Service}}\t{{.Status}}\t{{.Ports}}"

restart: stop start