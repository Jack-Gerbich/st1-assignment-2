'''
Python skeleton for the appointment system

Created off the UML class diagram
- Patient 1 <--> 0..* Appointment
- Practitioner 1 < -- > 0..* Appointment
- Each Appointment has only one Patient and one Practitioner
'''

class Patient:
    # phone number was added as "contact_info" this 
    # is subject to change to other contact info
    def __init__(self, patient_id, name,phone_number):
        self.patient_id = patient_id
        self.name = name
        self.phone_number = phone_number

    def update_patient_details(self):
        pass

class Practitioner:
    def __init__(self, practitioner_id, name, specialty):
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty

    def update_practitioner_details(self):
        pass

class Appointment:
    def __init__(self, appointment_id, date_tie, status, patient, practitioner):
        self.appointment_id = appointment_id
        self.date_time = self.date_time
        self.status = status
        self.patient = patient
        self.practitioner = practitioner

    def reschdule(self):
        pass