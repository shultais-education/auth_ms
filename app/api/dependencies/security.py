from fastapi.security import APIKeyHeader
from fastapi import Depends
from typing import TypeAlias, Annotated


security = APIKeyHeader(name="X-API-Key")

KeyHeaderDep: TypeAlias = Annotated[str, Depends(security)]
