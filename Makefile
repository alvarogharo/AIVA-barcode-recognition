init:
	pip install -r requirements.txt
test:
	nosetests tests
start-server:
	python3 src/web_server.py
docker-build:
	docker build -t alvarogharo/aiva-barcode-recognizer:0.1.0 .
docker-deploy:
	docker build -t alvarogharo/aiva-barcode-recognizer:0.1.0 .
	docker run -p 5000:5000 -d alvarogharo/aiva-barcode-recognizer:0.1.0