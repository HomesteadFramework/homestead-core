from fastapi import Request
from homestead import WebRouter
import fastapi_jinja

router = WebRouter()


@router.get('/')
@fastapi_jinja.template('{template_name}.html')
async def get(request: Request):
    """A route that returns html data"""
    return {}

