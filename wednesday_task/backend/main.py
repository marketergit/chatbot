from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

# Initialize the FastAPI app
app = FastAPI()

# Sample data model (can be expanded based on the project)
class InputData(BaseModel):
    param1: float
    param2: float

# Route for health check
@app.get("/")
def read_root():
    return {"message": "Hello, World! FastAPI is up and running!"}

# Example API route with POST method
@app.post("/predict")
def predict(data: InputData):
    # Here you would typically integrate with your model to make predictions
    try:
        result = data.param1 + data.param2  # Placeholder logic for prediction
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Additional routes can go here

# Example route for loading environmental variables
@app.get("/env")
def get_env_variables():
    return {"OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", "Not Set")}
