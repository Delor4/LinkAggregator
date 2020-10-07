
DOCKER_DIR = docker
BACK_DIR = app
FRONT_DIR = link-aggregator

.PHONY: all clean_docker build_back build_front docker_compose docker_restart

all: clean_docker build_back build_front docker_compose docker_restart

# cleanup
clean_docker:
	$(MAKE) -C $(DOCKER_DIR) clean

# copy flask app
build_back:
	cp -r $(BACK_DIR)/* $(DOCKER_DIR)/app/
	# remove dev database file
	rm $(DOCKER_DIR)/app/link_aggr.db

# build and copy vue static files
build_front:
	$(MAKE) -C $(FRONT_DIR) build
	cp -r $(FRONT_DIR)/dist/* $(DOCKER_DIR)/app/static/

docker_compose:
	$(MAKE) -C $(DOCKER_DIR) build

docker_restart:
	$(MAKE) -C $(DOCKER_DIR) restart

run_front:
	$(MAKE) -C $(FRONT_DIR) run

run_back:
	$(MAKE) -C $(BACK_DIR) run
