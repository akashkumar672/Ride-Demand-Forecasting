from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.predict import predict

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={
            "detail": exc.errors(),
            "body": exc.body,
        },
    )

@app.get("/")
def root():
    return {"message": "Bike demand prediction API is running. Use POST /predict"}

@app.get("/health")
def health():
    return {"status": "ok"}

class InputData(BaseModel):
    datetime: str
    season: int
    holiday: int
    workingday: int
    weather: int
    temp: float
    atemp: float
    humidity: int
    windspeed: float
    casual: int
    registered: int

@app.post("/predict")
def get_prediction(data: InputData):
    try:
        result = predict(data.dict())
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return {"prediction": result}