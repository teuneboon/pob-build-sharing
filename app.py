from fastapi import FastAPI

app = FastAPI()


@app.get('/{build_id}/?')
async def get_build(
        *,
        build_id: str,
):
    return f'test: {build_id}'
