from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Schedule
from .serializers import ScheduleSerializer


@api_view(["GET"])
def available_schedules(request, service_id):
    schedules = Schedule.objects.filter(service_id=service_id, is_available=True)
    serializer = ScheduleSerializer(schedules, many=True)
    return Response(serializer.data)
