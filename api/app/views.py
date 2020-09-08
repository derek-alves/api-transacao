from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import re

from .models import Transacao
from .serializers import TransacaoSerializer

@api_view(['GET', 'POST'])
def transacoes(request):
    if request.method == 'GET':
        queryset = Transacao.objects.all()
        serializer = TransacaoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        request_data = request.data.copy()
        regex = re.compile(r'\d+')
        request_data['estabelecimento'] = ''.join(regex.findall(request_data['estabelecimento']))
        request_data['cliente'] = ''.join(regex.findall(request_data['cliente']))

        serializer = TransacaoSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"aceito": True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
