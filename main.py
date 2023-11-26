from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def f_index():
    return {"ФИО": "Шевергина Анна Александровна"}
@app.get('/users')
async def f_index():
    return {"Номер телефона": "+7(905)926-**-**"}

@app.get('/tools')
async def f_index():
    return {"О себе": "Люблю заниматься спортом"}