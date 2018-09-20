build:
	docker build -t keras-flask-api .

start:
	docker run -p 8000:8000 keras-flask-api
