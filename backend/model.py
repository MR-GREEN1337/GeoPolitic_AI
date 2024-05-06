from pydantic import BaseModel

class InputData(BaseModel):
    regions: list[str]
    subjects: list[str]
