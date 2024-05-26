from typing import Any, Callable, TypedDict

from rest_framework import status
from rest_framework.response import Response as DrfResponse

from clientboards.api.services.ServicesError import ServicesError

__success_codes = [200, 201, 202, 203, 204]


class _ApiResponse(TypedDict):
    status_response: str


class _SuccessApiResponse(_ApiResponse):
    data: Any


class _ErrorApiResponse(_ApiResponse):
    error: Any


def ResponseStructure(data: Any, status_code: int) -> _SuccessApiResponse | _ErrorApiResponse:
    statusResponse = 'success' if status_code in __success_codes else 'error'

    if statusResponse == 'success':
        return _SuccessApiResponse(status_response=statusResponse, data=data)
    else:
        return _ErrorApiResponse(status_response=statusResponse, error=data)


class Response(DrfResponse):
    def __init__(self, data: Any,  status_code: int):
        super().__init__(ResponseStructure(data, status_code), status_code)


def ResponseGenerator(returnResponseData: Callable[[], Any]):
    """
    Generates the response for the view.

    Parameters
    ----------
    callback: Function -> Any
        The callback function should return the value that is being returned in the response

    Returns
    -------
    api.response.response.Response
        What's returned from this function is the Response class that inherited the DRF Response class.
    """
    try:
        data = returnResponseData()
        return Response(data,
                        status_code=status.HTTP_200_OK)
    except ServicesError as se:
        print(f"logger: error details - {se.details}")
        return Response(se.__str__(), status_code=se.status_code)
    except Exception as e:
        return Response(f"Error occurred: {e}",
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
