from django import forms
from .models import PatientVitals, PatientHistory, PatientSystemic, PatientObstetric, PatientGeneral, PatientInvestigations, PatientProvisional, PatientDiagnosis, PatientAdvice


class PatientvitalsForm(forms.ModelForm):

    class Meta:

        model = PatientVitals
        fields = ('pulse', 'blood_pressure', 'respiratory_rate', 'weight', 'temperature', 'mizaj_1', 'mizaj_2', 'date_vitals',)


class PatienthistoryForm(forms.ModelForm):
    class Meta:
        model = PatientHistory
        fields = ('presenting_complaints', 'history_of_presenting_complaints', 'department', 'past_historys', 'past_history_note', 'drug_history', 'drug_history_note', 'drug_allergies', 'treatment_history', 'treatment_history_note', 'surgeries', 'personal_history_sleep', 'personal_history_appetite', 'personal_history_diet', 'personal_history_bowel_bladder_habits', 'addictions', 'occupational_history', 'family_history',)


class PatientsystemicForm(forms.ModelForm):
    class Meta:
        model = PatientSystemic
        fields = ('respiratory_system', 'cardiovascular_system', 'abdomen', 'central_nervous_system', 'locomotor_system', 'local_examination', )


class PatientobstetricForm(forms.ModelForm):
    class Meta:
        model = PatientObstetric
        fields = ('G', 'P', 'L', 'A', 'D', 'age_and_sex_child', 'method_of_delivery', 'nvd', 'lscs', 'immunization_of_children', )


class PatientgeneralForm(forms.ModelForm):
    class Meta:
        model = PatientGeneral
        fields = ('built_and_nourishment', 'pallor', 'edema', 'cyanosis', 'clubbing', 'icterus', 'lymphadenopathy',)


class PatientinvestigationsForm(forms.ModelForm):
    class Meta:
        model = PatientInvestigations
        fields = ('investigations',)


class PatientprovisionalForm(forms.ModelForm):
    class Meta:
        model = PatientProvisional
        fields = ('previsional_diagnosis',)


class PatientdiagnosisForm(forms.ModelForm):
    class Meta:
        model = PatientDiagnosis
        fields = ('filal_Diagnosis',)


class PatientadviceForm(forms.ModelForm):
    class Meta:
        model = PatientAdvice
        fields = ('advice',)
