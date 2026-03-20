from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Base de datos simulada
cars_db = [
    {"id": 1, "brand": "Toyota", "model": "Corolla", "year": 2022},
    {"id": 2, "brand": "Honda", "model": "Civic", "year": 2023},
]


class Car(BaseModel):
    brand: str
    model: str
    year: int


@app.get("/cars/")
def get_cars():
    return cars_db


@app.get("/cars/{car_id}")
def get_car(car_id: int):
    for car in cars_db:
        if car["id"] == car_id:
            return car
    return {"error": "Auto no encontrado"}


@app.post("/cars/")
def create_car(car: Car):
    new_id = max(c["id"] for c in cars_db) + 1
    new_car = {"id": new_id, **car.model_dump()}
    cars_db.append(new_car)
    return new_car
