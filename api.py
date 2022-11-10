import time
from datetime import datetime
from typing import Union

from fastapi import FastAPI
from starlette.responses import StreamingResponse

from generator import poster_generator

app = FastAPI()


@app.get('/')
def image(
        volume: Union[str, int] = None,
        no: str = None,
        due_date: Union[int, str] = None,
        due_month: str = None,
        due_year: Union[int, str] = datetime.today().year
):
    if not volume and not no and not due_date and not due_month:
        bytes = poster_generator(4, 'II', 15, "March", due_year)
        return StreamingResponse(bytes, media_type="image/png",
                                 headers={'Content-Disposition': f'inline; filename="server_side_{time.time()}.png"'})
    bytes = poster_generator(volume, no, due_date, due_month, due_year)
    return StreamingResponse(bytes, media_type="image/png",
                             headers={'Content-Disposition': f'inline; filename="server_side_{time.time()}.png"'})
