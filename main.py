from fastapi import FastAPI
from pydantic import BaseModel
import jwt
from fastapi import Header

SECRET_KEY = "123456"

class Login(BaseModel):
    username: str
    password: str

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "API funcionando"}

@app.post("/login")
def login(data: Login):
    if data.username == "camila" and data.password == "2103":
        token = jwt.encode({"user": data.username}, SECRET_KEY, algorithm="HS256")
        return {"token": token}
    return {"msg": "login inválido"}

@app.get("/perfil")
def perfil(token: str):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"usuario": data["user"]}
    except:
        return {"msg": "token inválido"}