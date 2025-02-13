
BMI_URL=http://localhost:5000/bmi
BMR_URL=http://localhost:5000/bmr
API_URL=http://localhost:5000/api

.PHONY: init run test clean test-api test-api-async build

init:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

run:
	@echo "Running the Flask app..."
	python app.py

test:
	@echo "Running tests..."
	pytest test.py

test-api:
	@echo "Testing API endpoints..."
	curl -X GET $(API_URL)
	@echo "\nTesting BMI calculation..."
	curl -X POST -H "Content-Type: application/json" -d '{"height": 1.75, "weight": 70}' $(BMI_URL)
	@echo "\nTesting BMR calculation..."
	curl -X POST -H "Content-Type: application/json" -d '{"height": 175, "weight": 70, "age": 25, "gender": "male"}' $(BMR_URL)

test-api-async:
	@echo "Running async API tests..."
	python3 test-api.py

build:
	@echo "Building Docker image..."
	docker build -t health-calculator:latest .

clean:
	@echo "Cleaning up..."
	rm -rf __pycache__