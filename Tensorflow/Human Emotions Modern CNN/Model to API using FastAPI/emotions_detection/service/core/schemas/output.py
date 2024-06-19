from pydantic import BaseModel


class APIOutput(BaseModel):
    emotion: str
    time_elapsed: str
    time_elapsed_preprocessing: str
