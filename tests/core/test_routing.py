import inspect
from homestead.core.routing import WebRouter
from fastapi import APIRouter


def test_fastapi_api_router_arguments_match():
    """We want to make sure our WebRouter and APIRouter arguments match."""
    fastapi_api_router_args = inspect.signature(APIRouter)
    homestead_api_router_args = inspect.signature(WebRouter)

    assert fastapi_api_router_args == homestead_api_router_args

    fastapi_params = fastapi_api_router_args.parameters
    homestead_params = homestead_api_router_args.parameters

    fastapi_args = []
    homestead_args = []
    for value in enumerate(fastapi_params.values()):
        fastapi_args.append(value[1].name)

    for value in enumerate(homestead_params.values()):
        homestead_args.append(value[1].name)

    for idx, value in enumerate(fastapi_args):
        assert value == homestead_args[idx]