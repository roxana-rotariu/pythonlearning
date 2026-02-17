from fastapi import FastAPI

app = FastAPI()

@app.get("/sum")
def sum_route(a: int, b: int):
    return {"result": a + b}
