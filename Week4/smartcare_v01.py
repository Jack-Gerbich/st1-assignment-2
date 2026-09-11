'''
The following code was written with AI.

The prompt given to Mircosoft CoPilot was:

Create a simple and beginner friendly python function 
for a doctors clinic that stores patient name, 
parctitioner name and appointment time.

(Do not include a database or GUI and keep it to one pthon file)
'''

def create_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "Patient": patient_name,
        "Practitioner": practitioner_name,
        "Appointment Time": appointment_time
    }
    return appointment


# Example usage
appointment1 = create_appointment(
    "John Smith",
    "Dr Brown",
    "10:00 AM"
)

print("Appointment Details:")
for key, value in appointment1.items():
    print(f"{key}: {value}")