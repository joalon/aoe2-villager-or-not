CC=podman
IMAGE_NAME=villager-or-not

build:
	$(CC) build -t $(IMAGE_NAME) .

run:
	$(CC) run --rm -p '5050:80' $(IMAGE_NAME)

clean:
	$(CC) rmi --force localhost/$(IMAGE_NAME)


