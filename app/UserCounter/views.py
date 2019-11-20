from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle


storage = {}


class UserCounter(APIView):
    """API View for user counter"""
    throttle_classes = [AnonRateThrottle]

    def get(self, request, *args, **kwargs):
        if self.kwargs['id'] <= 65535:
            if not self.kwargs['id'] in storage:
                storage[self.kwargs['id']] = {'user_id': self.kwargs['id'],
                                              'counter': 1}
            else:
                if storage[self.kwargs['id']]['counter'] <= 1024:
                    storage[self.kwargs['id']]['counter'] += 1
                else:
                    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
            return Response(storage[self.kwargs['id']])
        return Response(status=status.HTTP_400_BAD_REQUEST)
