from typing import TypedDict, Any

class OpenAPIParameters(TypedDict):
    title: str
    summary: str
    version: str
    description: str
    docs_url: str | None
    redoc_url: str | None
    servers: list[dict[str, Any]] | None

OPENAPI_PARAMETERS: OpenAPIParameters = {
    "title": "Road API",
    "summary": "Road HTTP API",
    "version": "0.0.0",
    "description": "An open-source platform to shape and reward open-source contributions. Create bounties, prioritize features, and collaborate together.",
    "docs_url": "/docs",
    "redoc_url": "/redoc",
    "servers": []
}
