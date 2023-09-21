from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Greeting(BaseModel):
    action: str
    name: str

@app.get("/")
def hello():
    return {"Hello": "World"}

@app.get("/{name}")
def hello_friend(name: str):
    return {"Hello": name}

@app.get("/greeting/{name}", response_model=Greeting)
def special_hello_friend(greeting: str, name: str):
    return Greeting(action=greeting, name=name)

@app.post("/")
def greeting(greeting: Greeting):
    return {greeting.action: greeting.name}


class Calc(BaseModel):
    firstNum: int
    action: str
    secondNum: int

@app.post("/calc")
def calc(calcData: Calc):
    firstNum = calcData.firstNum
    secondNum = calcData.secondNum
    action = calcData.action
    match action:
        case '+':
            return firstNum + secondNum
        case '-':
            return firstNum - secondNum
        case '*':
            return firstNum * secondNum
        case '/':
            try:
                return firstNum / secondNum
            except ZeroDivisionError:
                return 'Ошибка деления'
        case _:
            return 'Вы ввели некорректное действие'
