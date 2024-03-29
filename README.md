# Age of Empires 2 - Villager or not
A small project for image recognition. A flask webapp in a container that takes an image and tells you if it's a villager or not.

## IPython notebook
See [my blog](https://joalon.se/blog/Villager-or-not.html) for details on the notebook.

## Web application
Build the container image through the 'make build' command in the webapp directory. Builds the 'villager-or-not' container which can be brought up by running the 'make run' command. Normally exposes the containers port 80 to the host port 8080. I used podman, but you should be able to substitute with docker.

An example:
```sh
CC=docker make build
CC=docker EXPOSE_TO_PORT=5050 make run
```

## Credits
Took a large bit of inspiration for the uwsgi/nginx/supervisord configuration from Gabriela Melo's flask-boilerplate template project. You can read more about it here:

[Flask boilerplate blog post on medium](https://medium.com/@gabimelo/developing-a-flask-api-in-a-docker-container-with-uwsgi-and-nginx-e089e43ed90e)  
[Flask boilerplate github](https://github.com/gabimelo/flask-boilerplate)  

