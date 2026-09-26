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
        """
        Change the appointment date and time.

        An appointment that is CANCELLED or COMPLETED
        cannot be rescheduled.
        """

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
        """
        Mark the appointment as cancelled.

        Cancelled appointments remain in the system.
        """

        if self.status in (
            AppointmentStatus.CANCELLED,
            AppointmentStatus.COMPLETED,
        ):
            raise ValueError(
                "Cancelled or completed appointments cannot be cancelled again."
            )

        self.status = AppointmentStatus.CANCELLED