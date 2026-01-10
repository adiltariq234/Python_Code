from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    class_name: str

@app.post("/student")
def add_student(student: Student):
    return {
        "message": "Student added successfully",
        "data": student
    }

if __name__ == "__main__":
    uvicorn.run(
        "lecture3:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
