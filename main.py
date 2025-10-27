from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Dermabot backend is running"}
@app.get("/ingredient")
def get_ingredient(name: str):
    info=f"{name.capitalize()} is commonly used in skincare for hydration and soothing."
    return {"info":info}