from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from utils import multiply_by_two

app = FastAPI()


@app.on_event("startup")
@repeat_every(seconds=3, wait_first=True)  # seconds=60 * 60 is 1hr
def periodic():
    print(multiply_by_two())


