from rest_framework import serializers
from . models import *


class SudokuBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudokuBoard
        fields = ['board', 'answer']
