"""
SmartCare: Community Clinic Appointment Booking System
Stage 1 - Human-written prototype
"""

appointments = []


def book_appointment(patient_name, practitioner_name, appointment_time):
    """Add a new appointment to the appointments list."""
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)


def display_appointments():
    """Print all recorded appointments."""
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")


print("Welcome to SmartCare: The Clinical Appointment Booking System!")

book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
display_appointments()

# ---- Verifying behaviour (Part F) ----
# Normal appointment
book_appointment('Charlie Nguyen', 'Dr. John Doe', '2024-07-21 09:00 AM')

# Duplicate: same practitioner/time booked twice — currently allowed, no clash check
book_appointment('Dana Lee', 'Dr. John Doe', '2024-07-21 09:00 AM')

# Blank patient name — uncomment to see it raise ValueError
# book_appointment('', 'Dr. John Doe', '2024-07-21 09:00 AM')

# Strange input (None) — uncomment to see it currently gets accepted with no validation
# book_appointment('Evan Wright', None, None)

display_appointments()