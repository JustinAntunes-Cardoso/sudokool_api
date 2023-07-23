from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *

# Create your views here.


class ReactView(APIView):
    def get(self, request, *args):
        output = [{
            "board": output.board,
            "answer": output.answer
        } for output in SudokuBoard.objects.all()]

        return Response(output)

    def post(self, request):
        serializer = SudokuBoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
