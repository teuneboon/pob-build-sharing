from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/{build_id}/?')
async def get_build(
        *,
        build_id: str = Query(..., description='The ID of the build, for example: 1a2b3c4e'),
) -> str:
    """ Returns the base64-encoded build code to import into Path of Building """
    return f'test: {build_id}'


@app.post('/create/?')
async def create_build(
        *,
        build: str,
) -> str:
    """ """
    # @TODO: validation of the build string
    return '12345678'
