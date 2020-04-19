# AIVA-barcode-recognition
Interleaved 2of5 barcode recognizer.

LICENSE NOTE: Currently the project LICENSE is GPLv3 but it may change on the near future.

## Installation

### Clone repository

 - Clone the repository with `git clone https://github.com/alvarogharo/AIVA-barcode-recognition.git`

### Make download dependencies (make and pip required)
 - Open terminal and type `make init` to install the pip dependencies

### Pip download dependencies (pip required)
 - Open terminal and type `pip install -r requirements.txt`to install the pip dependencies
 
## Run all the tests

NOTE: All barcode images are not shown when running the tests.

### Make (make required)
 - Open terminal and run `make test` 
 
### Nosetests
 - Open terminal and run `nosetests tests`
 
## Start the web server locally

### Make (make required)
 - Open terminal and run `make start-server` 
 
### Non-make
 - Open terminal and run `python3 src/web_server.py`
 
## Create Docker container
- Install docker https://docs.docker.com/get-docker/

### Make (make required)
- Open terminal and run `make docker-deploy`

### Non make

- Open terminal and run `docker build -t barcode-recognizer:0.1.0 .`
- Then run `docker run -p 5000:5000 -d barcode-recognizer:0.1.0`

### Pull the image from docker hub
- Open terminal and run `docker pull alvarogharo/aiva-barcode-recognizer:0.1.0`
- Then run `docker run -p 5000:5000 -d alvarogharo/aiva-barcode-recognizer:0.1.0`
