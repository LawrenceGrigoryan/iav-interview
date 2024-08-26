from pydantic import BaseModel


class HealthCheck(BaseModel):
    status: str = "OK"


class JokerRequest(BaseModel):
    prompt: str