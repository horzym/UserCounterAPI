from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle
from collections import defaultdict


data2 = {}


class UserCounter(APIView):
    """API View for user counter"""
    throttle_classes = [AnonRateThrottle]

    def get(self, request, *args, **kwargs):
        if self.kwargs['id'] <= 65535:
            if not self.kwargs['id'] in data2:
                data2[self.kwargs['id']] = {'user_id': self.kwargs['id'],
                                            'click': 1}
            else:
                if data2[self.kwargs['id']]['click'] <= 1024:
                    data2[self.kwargs['id']]['click'] += 1
                else:
                    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
            return Response(data2[self.kwargs['id']])
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
