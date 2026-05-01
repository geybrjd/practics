from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return{'massage': "API работает"}

@app.get('/hello')

@app.get("/hello")
def hello(name: str = 'guest'):
        return {"massage": f"Hello, {name}"}
