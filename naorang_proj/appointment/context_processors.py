from appointment.models import Appointment


def appointment_count_waiting(request):
            count = Appointment.waiting.count()
            return {'appointment_count_waiting': count}


def appointment_count_scheduled(request):
        count = Appointment.scheduled.count()
        return {'appointment_count_scheduled': count}
