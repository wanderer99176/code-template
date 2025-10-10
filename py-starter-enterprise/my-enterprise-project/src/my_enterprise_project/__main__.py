import uvicorn
from fastapi import FastAPI
from my_enterprise_project.api.v1 import endpoints

app = FastAPI(title="My enterprise Project")

app.include_router(endpoints.router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "Welcome to My enterprise Project!"}


def main():
    """`run-app` 脚本的入口点。"""
    uvicorn.run("my_enterprise_project.__main__:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
