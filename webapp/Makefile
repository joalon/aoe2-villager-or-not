CC=podman
IMAGE_NAME=villager-or-not
EXPOSE_TO_PORT=8080

build:
	$(CC) build -t $(IMAGE_NAME) .

run:
	$(CC) run --rm -p "$(EXPOSE_TO_PORT):80" $(IMAGE_NAME)

clean:
	$(CC) rmi --force localhost/$(IMAGE_NAME)


