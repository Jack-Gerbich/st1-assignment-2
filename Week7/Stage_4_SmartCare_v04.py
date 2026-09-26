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

'''
============================================
From this point is the AI code from Co-Pilot
============================================
'''

from datetime import datetime
from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        date_time: datetime,
        patient: Patient,
        practitioner: Practitioner,
        status: AppointmentStatus = AppointmentStatus.SCHEDULED,
    ) -> None:

        # Validate appointment_id
        if not appointment_id or not appointment_id.strip():
            raise ValueError("Appointment_id must not be empty.")

        # Validate date_time
        if not isinstance(date_time, datetime):
            raise ValueError("date_time must be a valid datetime object.")

        # Enforce exactly one patient and one practitioner
        if not isinstance(patient, Patient):
            raise ValueError("Appointment must have one valid Patient.")

        if not isinstance(practitioner, Practitioner):
            raise ValueError("Appointment must have one valid Practitioner.")

        if not isinstance(status, AppointmentStatus):
            raise ValueError("status must be an AppointmentStatus value.")

        self.appointment_id: str = appointment_id
        self.date_time: datetime = date_time
        self.status: AppointmentStatus = status
        self.patient: Patient = patient
        self.practitioner: Practitioner = practitioner

    def reschedule(self, new_date_time: datetime) -> None:
        
        # changing the appointment date and time.
        # an appointment that is CANCELLED or COMPLETED cannot be rescheduled.
        if self.status in (
            AppointmentStatus.CANCELLED,
            AppointmentStatus.COMPLETED,
        ):
            raise ValueError(
                "Cancelled or completed appointments cannot be rescheduled."
            )

        if not isinstance(new_date_time, datetime):
            raise ValueError("new_date_time must be a valid datetime object.")

        self.date_time = new_date_time

    def cancel(self) -> None:
 
        # mark the appointment as cancelled 
        # cancelled appointments remain in the system.
        if self.status in (
            AppointmentStatus.CANCELLED,
            AppointmentStatus.COMPLETED,
        ):
            raise ValueError(
                "Cancelled or completed appointments cannot be cancelled again."
            )

        self.status = AppointmentStatus.CANCELLED

'''
==========================
Test inputs
==========================
'''

if __name__ == "__main__":
    p = Patient("P001", "Jane Doe", "0412345678")
    pr = Practitioner("PR001", "Dr. Smith", "Cardiology")
    appt = Appointment("A001", datetime(2026, 10, 1, 9, 0), p, pr)
    print(appt.status)

    appt.cancel()
    print(appt.status)

    appt.cancel()
