import uvicorn
from fastapi import FastAPI
from {{ cookiecutter.package_name }}.api.v1 import endpoints

app = FastAPI(title="{{ cookiecutter.project_name }}")

app.include_router(endpoints.router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "Welcome to {{ cookiecutter.project_name }}!"}


def main():
    """`run-app` 脚本的入口点。"""
    uvicorn.run("{{ cookiecutter.package_name }}.__main__:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
