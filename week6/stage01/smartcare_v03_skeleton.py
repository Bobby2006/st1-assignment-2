"""
SmartCare: Domain Model v0.3
Class skeletons matching the UML model in domain_model_v0.3.md
Structure only — behaviour not yet fully implemented (Part H: consistency check).
"""


class Patient:
    def __init__(self, patient_id, name, contact):
        self.id = patient_id
        self.name = name
        self.contact = contact

    def update_contact(self, new_contact):
        """Update this patient's contact details. (FR-08)"""
        pass

    def get_appointments(self):
        """Return this patient's appointment history. (FR-11)"""
        pass


class Practitioner:
    def __init__(self, practitioner_id, name):
        self.id = practitioner_id
        self.name = name

    def get_schedule(self):
        """Return this practitioner's upcoming appointments. (FR-07)"""
        pass


class Appointment:
    def __init__(self, patient, practitioner, time, status="booked"):
        self.patient = patient
        self.practitioner = practitioner
        self.time = time
        self.status = status

    def cancel(self):
        """Change status to cancelled, retained in history. (FR-05, FR-06)"""
        pass

    def reschedule(self, new_time):
        """Update this appointment's date/time. (FR-09)"""
        pass


# ---- Structure check (Part H) ----
# Confirms the classes can be instantiated with the attributes shown
# in the UML diagram. No business logic is tested here yet.
if __name__ == "__main__":
    patient = Patient("P001", "Alice Smith", "alice@example.com")
    practitioner = Practitioner("D001", "Dr. John Doe")
    appointment = Appointment(patient, practitioner, "2024-07-20 10:00 AM")

    print(f"Patient: {patient.name}")
    print(f"Practitioner: {practitioner.name}")
    print(f"Appointment: {appointment.patient.name} with {appointment.practitioner.name} at {appointment.time} ({appointment.status})")
