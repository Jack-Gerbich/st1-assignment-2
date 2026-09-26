'''
SmartCare v0.4

Created based off the week 7 UML
'''

# creating and defining the patient class
class Patient:
    def __init__(self, patient_id: str, name: str,phone_number: str):
        
        # checking for valid inputs and striping empty space
        if not patient_id or not patient_id.strip():
            raise ValueError("Patient_id must not be empty.")
        if not name or not name.strip():
            raise ValueError("Name must not be empty")
        # checking for if the phone number is 10 digits and a number
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise ValueError("Phone_number must be a 10 digit number.")
        
        # assigning the inputs to the object if the inputs were valid
        self.patient_id: str = patient_id
        self.name: str = name
        self.phone_number: str = phone_number

    # this allows for updating patient infomation
    def update_patient_details(self, name: str | None = None, phone_number: str | None = None) -> None:
        
        # checks and updates name only if a new one is legal
        if name is not None:
            if not name.strip():
                raise ValueError("Name must not be empty")
            self.name = name

        # checks and updates phone_namber only if a new one is legal
        if phone_number is not None:
            if not phone_number.isdigit() or len(phone_number) != 10:
                raise ValueError("Phone_number must be a 10 digit number.")
            self.phone_number = phone_number


# creating and defining the practitioner class
class Practitioner:
    def __init__(self, practitioner_id, name, specialty):
        
        # checking for valid inputs and stripping empty space
        if not practitioner_id or not practitioner_id.strip():
            raise ValueError("Practitioner_id must not be empty.")
        if not name or not name.strip():
            raise ValueError("Name must not be empty.")
        if not specialty or not specialty.strip():
            raise ValueError("Specialty must not be empty.")

        # assigning the inputs to the object if the inputs were valid
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty

    def update_practitioner_details(self, name: str | None = None, specialty: str | None = None) -> None:
 
        # only checks/updates name if a new one is legal
        if name is not None:
            if not name.strip():
                raise ValueError("Name must not be empty.")
            self.name = name

        # only chexks/updates specialty if a new one is legal
        if specialty is not None:
            if not specialty.strip():
                raise ValueError("Specialty must not be empty.")
            self.specialty = specialty


class Appointment:
    def __init__(self, appointment_id, date_tie, status, patient, practitioner):
        self.appointment_id = appointment_id
        self.date_time = self.date_time
        self.status = status
        self.patient = patient
        self.practitioner = practitioner

    def reschdule(self):
        pass