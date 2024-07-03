# type: ignore

# django
from django.http import HttpRequest
from rest_framework.views import APIView

# response
from clientboards.api.response.response import ResponseGenerator

# models and services
from clientboards.api.services.invite.invite_services import InviteServices


class InviteAPIView(APIView):
    def post(self, request: HttpRequest):
        # invite the user to the workspace by giving them permission to the specific page block
        email = request.data.get('email')
        block_id = request.data.get('block_id')
        permission_type = request.data.get('permission_type')
        additional_conditions = request.data.get('additional_conditions')

        return ResponseGenerator(lambda: InviteServices.inviteUser(email, block_id, permission_type, additional_conditions))
