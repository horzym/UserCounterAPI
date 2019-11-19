from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle
from collections import defaultdict
from .serializers import testser

data3 = defaultdict(int)
data2 = {}
   
class UserCounter(APIView):
    '''
    def get(self, request, *args, **kwargs):
        throttle_classes = [AnonRateThrottle]
        
        if self.kwargs['id'] <= 65535:
            if not self.kwargs['id'] in data2:
                data2[self.kwargs['id']] = {'user_id': self.kwargs['id'], 'click': 1}
            else:
                if data2[self.kwargs['id']]['click'] <= 1024:
                    data2[self.kwargs['id']]['click'] += 1
                else:
                    return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
            return Response(data2[self.kwargs['id']])
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
        '''
    def get(self, request, *args, **kwargs):
          
          data3[self.kwargs['id']] = {'counter':1}
          serialer = testser(data3[self.kwargs['id']], self.kwargs['id'])
          print(serialer)
        

            
     
        
    
   