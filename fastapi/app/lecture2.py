from fastapi import FastAPI
import uvicorn
app= FastAPI()

@app.get('/')
def read_root():

    return {"Hello":"World"}
@app.post('/add')
def add_number():
    return {"message":"Number added successfully"}
@app.get('/student{name}')
def student_name(name : str):
    return {"message":f"Hello {name}"}
@app.get('/age')
def student_age(age : int):
    return {"message":f"Your age is {age}"}

if __name__ == "__main__":
    uvicorn.run(
        "lecture2:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )