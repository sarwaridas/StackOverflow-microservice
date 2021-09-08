from fastapi import FastAPI
import uvicorn
import subprocess

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Python Code Generator!"}

#@app.get("/add/{num1}/{num2}")
#async def add(num1: int, num2: int):
 #   """Add two numbers together"""

  #  total = num1 + num2
   # return {"total": total}

@app.get("/answer/str1")
async def answer(str1: str):
    """Scrapes StackOverflow to answer Python Questions"""
    str2= str1.replace("%20"," ")
    output= subprocess.run(["howdoi", str2], capture_output=True)
    return {"Output": output}
    
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')