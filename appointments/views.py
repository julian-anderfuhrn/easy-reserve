from django.shortcuts import render, get_object_or_404, get_list_or_404
from services.models import Service, ServiceCategory
from schedules.models import Schedule
from .models import Appointment
from datetime import datetime, timedelta, date
from django.contrib import messages
from django.http import JsonResponse


def available_slots_api(request, pk):
    service = Service.objects.get(pk=pk, is_active=True)
    selected_date = request.GET.get("date")

    if not selected_date:
        return JsonResponse({"slots": []})

    selected_date = date.fromisoformat(selected_date)
    weekday = selected_date.weekday()

    schedules = Schedule.objects.filter(
        service=service,
        day_of_week=weekday,
        is_active=True,
    )

    slots = []

    for schedule in schedules:
        occupied = set(
            Appointment.objects.filter(
                schedule=schedule,
                date=selected_date,
                status__in=["reserved", "completed"],
            ).values_list("start_time", flat=True)
        )

        start_dt = datetime.combine(selected_date, schedule.start_time)
        end_dt = datetime.combine(selected_date, schedule.end_time)
        duration = timedelta(minutes=service.duration_minutes)

        current = start_dt
        while current + duration <= end_dt:
            if current.time() not in occupied:
                slots.append(current.time().strftime("%H:%M"))
            current += duration

    return JsonResponse({"slots": slots})


def available_days_api(request, pk):
    service = Service.objects.get(pk=pk, is_active=True)

    today = date.today()
    end_date = today + timedelta(days=30)

    schedules = Schedule.objects.filter(service=service, is_active=True)
    available_weekdays = set(s.day_of_week for s in schedules)

    available_dates = []

    current_date = today
    while current_date <= end_date:
        if current_date.weekday() in available_weekdays:
            available_dates.append(current_date.isoformat())
        current_date += timedelta(days=1)

    return JsonResponse({"available_dates": available_dates})


def availability_view(request, pk):
    service = get_object_or_404(Service, pk=pk, is_active=True)

    today = date.today()
    max_date = today + timedelta(days=30)

    # 👉 días de la semana disponibles (0=lunes)
    available_weekdays = set(
        Schedule.objects.filter(service=service, is_active=True).values_list(
            "day_of_week", flat=True
        )
    )

    selected_date_raw = request.GET.get("date")
    slots = []
    selected_date = None

    if selected_date_raw:
        selected_date = date.fromisoformat(selected_date_raw)

        # 🚫 validaciones fuertes
        if selected_date < today or selected_date > max_date:
            messages.error(request, "Selected date is out of range.")
            selected_date = None

        elif selected_date.weekday() not in available_weekdays:
            messages.warning(
                request, "This service is not available on the selected day."
            )
            selected_date = None

        else:
            weekday = selected_date.weekday()

            schedules = Schedule.objects.filter(
                service=service,
                day_of_week=weekday,
                is_active=True,
            )

            for schedule in schedules:
                occupied_times = set(
                    Appointment.objects.filter(
                        schedule=schedule,
                        date=selected_date,
                        status__in=["reserved", "completed"],
                    ).values_list("start_time", flat=True)
                )

                start_dt = datetime.combine(selected_date, schedule.start_time)
                end_dt = datetime.combine(selected_date, schedule.end_time)
                slot_duration = timedelta(minutes=service.duration_minutes)

                current_time = start_dt
                while current_time + slot_duration <= end_dt:
                    slot_time = current_time.time()

                    if slot_time not in occupied_times:
                        slots.append(slot_time)

                    current_time += slot_duration

    return render(
        request,
        "appointments/availability.html",
        {
            "service": service,
            "slots": slots,
            "selected_date": selected_date,
            "today": today,
            "max_date": max_date,
            "available_weekdays": available_weekdays,  # 👈 clave
        },
    )


def service_list(request):
    services = Service.objects.filter(is_active=True)
    categories = ServiceCategory.objects

    context = {"services": services, "categories": categories}

    return render(request, "appointments/service_list.html", context)


# def availability_view(request, pk):
#     service = get_object_or_404(Service, pk=pk, is_active=True)

#     schedules = Schedule.objects.filter(service=pk, is_active=True)
#     appointments = Appointment.objects.filter(schedule__in=schedules, status="reserved")
#     return render(
#         request,
#         "appointments/availability.html",
#         {"service": service, "schedules": schedules, "appointments": appointments},
#     )
