from fastapi import FastAPI
from datetime import datetime
from dateutil.relativedelta import relativedelta
import socket

from models.pessoa import Pessoa


app = FastAPI()

@app.get("/")
async def hello_world():
    return {
        "message":f"{socket.gethostname()} says: Hello, World!"
    }

@app.post("/pessoas/")
async def root(pessoa: Pessoa):
    nascimento = datetime.strptime(pessoa.data_nascimento, "%d/%m/%y")
    hoje = datetime.now()
    idade = relativedelta(hoje, nascimento)
    payload = f"{pessoa.primeiro_nome} {pessoa.ultimo_nome} tem {idade.years} anos, {idade.months} meses e {idade.days} dias em {datetime.strftime(hoje, '%d/%m/%y')}."
   
    return {
        "message":payload
    }

