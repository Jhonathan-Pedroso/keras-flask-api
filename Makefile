build:
	docker build -t keras-flask-api .

start:
	docker run -d -p 8000:8000 keras-flask-api
