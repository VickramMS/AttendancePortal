from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.views import APIView
from datetime import datetime

class AttendanceView(View):
    def get(self, request):
        context = {
            "students" : Attendance.objects.all()
        }
        return render(request, 'attendance.html', context)

class AddAttendanceAPI(APIView):
    def post(self, request):
        try:
            user = User.objects.get(username=request.POST.get('studentName'))
            if user:
                if len(Attendance.objects.filter(user=user)) > 0:
                    return JsonResponse({
                        "response" : "Attendance has been already marked for %s" %(user.username)
                    })
                
                else:
                    attendance = Attendance()
                    attendance.user = user
                    attendance.attendance = True
                    attendance.temperature = request.POST.get('temperature')
                    attendance.timeStamp = timezone.now()
                    attendance.save()
                    return JsonResponse({
                        "response" : "Attendance has been marked for %s" %(user.username)
                    })
        except:
            user = None
            return JsonResponse({
                "response" : "No user found"
            })
