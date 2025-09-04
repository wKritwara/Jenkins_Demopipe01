import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI with Jenkins & SonarQube!"}


def test_average_success():
    response = client.get("/average?numbers=10&numbers=20&numbers=30")
    assert response.status_code == 200
    assert response.json()["average"] == 20.0


def test_average_empty_list():
    response = client.get("/average")
    assert response.status_code == 422  # missing query parameter


def test_reverse_string():
    response = client.get("/reverse?text=SonarQube")
    assert response.status_code == 200
    assert response.json()["reversed"] == "ebuQranoS"


🔹 requirements.txt
fastapi==0.111.0
uvicorn==0.30.0
pytest==8.2.0
httpx==0.27.0


🔹 sonar-project.properties
ไฟล์นี้ใช้สำหรับ SonarQube Scanner
# Project identification
sonar.projectKey=fastapi-clean-demo
sonar.projectName=FastAPI Clean Demo
sonar.projectVersion=1.0

# Source
sonar.sources=app
sonar.language=py
sonar.sourceEncoding=UTF-8

# Tests
sonar.tests=tests
sonar.python.coverage.reportPaths=coverage.xml

# Exclusions (ถ้ามีไฟล์ที่ไม่อยากให้ scan)
# sonar.exclusions=**/__pycache__/**,**/*.pyc
