# Django Docker

This is a basic Django web app running on Docker. It has CRUD operations along with search functionality. Follow simple way to run Django projectsin docker on localhost.

## Quick start
1. Change directory to `Business`: `$ cd Business`
2. Build the Docker image: `$ docker build -t <imagename> .`
3. Run the Docker image you just created: `$ docker run -d -p 8000:8000 <imagename>`

That's it—you now have a fully Dockerized Django project running..

## pytest

1. login to docker container: `$ docker exec -it <containerID> bin/bash`
2. Run pytest: `$ pytest`

# Note: 
`entypoint.sh` will create super_user and load some data to DB.
username: admin
pasword: adminpass

