from fastapi import FastAPI
import uvicorn
import subprocess
from subprocess import PIPE, run # pylint: disable=unused-import

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Python Code Generator!",
            "What this does": "This service makes use of the howdoi python package to answer questions related to python code",
            "How to run": "To use this service, after the url, type in your /answer/{query} where query is your question separated by underscores. For example you could type in /answer/generate_fibonacci_sequence and this service would return the code required to generate a fibonacci sequence in python"
    }

#@app.get("/add/{num1}/{num2}")
#async def add(num1: int, num2: int):
 #   """Add two numbers together"""

  #  total = num1 + num2
   # return {"total": total}

@app.get("/answer/{str1}")
async def answer(str1: str):
    """Scrapes StackOverflow to answer Python Questions"""
    str2= str1.replace("_"," ")
    str2= str2+ " in python"
    output= subprocess.run(["howdoi", str2], capture_output=True,check=True)
    return {"Code": ((output.stdout).decode()).split("\n")[:-1]}
    
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
