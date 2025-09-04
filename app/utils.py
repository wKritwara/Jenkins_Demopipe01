from typing import List
def calculate_average(numbers: List[float]) -> float:
    """
    คำนวณค่าเฉลี่ยจาก list ของตัวเลข
    """
    if not numbers:
        raise ValueError("Numbers list must not be empty")
    return sum(numbers) / len(numbers)


def reverse_string(text: str) -> str:
    """
    กลับลำดับข้อความ
    """
    return text[::-1]


🔹 main.py
# app/main.py

from fastapi import FastAPI, HTTPException, Query
from typing import List
from app.utils import calculate_average, reverse_string

app = FastAPI(
    title="FastAPI Clean Code Example",
    description="Simple FastAPI app for Jenkins + Docker + SonarQube pipeline demo",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Hello from FastAPI with Jenkins & SonarQube!"}


@app.get("/average")
def get_average(numbers: List[float] = Query(..., description="List ของตัวเลข")):
    try:
        result = calculate_average(numbers)
        return {"average": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/reverse")
def get_reverse(text: str = Query(..., description="ข้อความที่ต้องการกลับ")):
    result = reverse_string(text)
    return {"reversed": result}
