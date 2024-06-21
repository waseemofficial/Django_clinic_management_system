from django.apps import AppConfig


class PatientdataConfig(AppConfig):
    name = 'patientdata'

    def ready(self):
        import patientdata.signals
