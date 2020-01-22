from rest_framework.generics import ListAPIView
from .models import Room
from .serializers import RoomSerializer


class ListRoomsView(ListAPIView):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer

# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework.response import Response

# FUNCTION BASED VIEW
# @api_view(["GET"])
# def list_rooms(request):
#     rooms = Room.objects.all()
#     serialized_rooms = RoomSerializer(rooms, many=True)
#     return Response(data=serialized_rooms.data)

# CLASS BASED VIEW
# class ListRoomsView(APIView):
#     def get(self, request):
#         rooms = Room.objects.all()
#         serializer = RoomSerializer(rooms, many=True)
#         return Response(serializer.data)
