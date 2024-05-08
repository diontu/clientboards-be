from typing import Any

from rest_framework import status

defaultMessage = "An error occurred"
defaultStatus = status.HTTP_500_INTERNAL_SERVER_ERROR


class ServicesError(Exception):
    def __init__(self, details: Any | None = None, message: str = defaultMessage, status_code: int = defaultStatus):
        isMessageAString = True if isinstance(message, str) else False
        exceptionMessage = message if isMessageAString else ""
        super().__init__(exceptionMessage)
        self.status_code = status_code
        self.details = details
