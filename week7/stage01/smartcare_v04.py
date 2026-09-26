"""
SmartCare: Domain Implementation v0.4
Patient and Practitioner implemented AI OFF (Parts B, C).
Appointment implemented from the approved UML using AI pair-programming
(Part D) — see domain_implementation_v0.4.md Section 4 for the prompt,
generated code, and review record. Replace the Appointment class below
with Copilot's reviewed/refactored version once you have it.
"""

from enum import Enum


class Patient:
    def __init__(self, patient_id: str, name: str, contact: str):
        if not patient_id:
            raise ValueError("Patient ID cannot be empty")
        if not name:
            raise ValueError("Patient name cannot be empty")
        if not contact:
            raise ValueError("Patient contact cannot be empty")
        self._id = patient_id
        self._name = name
        self._contact = contact
        self._appointments = []

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def contact(self) -> str:
        return self._contact

    def update_contact(self, new_contact: str) -> None:
        """Update this patient's contact details. (FR-08)"""
        if not new_contact:
            raise ValueError("Contact cannot be empty")
        self._contact = new_contact

    def add_appointment(self, appointment) -> None:
        """Internal use — Appointment registers itself with its Patient."""
        self._appointments.append(appointment)

    def get_appointments(self) -> list:
        """Return this patient's appointment history. (FR-11)"""
        return list(self._appointments)


class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str):
        if not practitioner_id:
            raise ValueError("Practitioner ID cannot be empty")
        if not name:
            raise ValueError("Practitioner name cannot be empty")
        if not specialty:
            raise ValueError("Practitioner specialty cannot be empty")
        self._id = practitioner_id
        self._name = name
        self._specialty = specialty
        self._appointments = []

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def specialty(self) -> str:
        return self._specialty

    def add_appointment(self, appointment) -> None:
        """Internal use — Appointment registers itself with its Practitioner."""
        self._appointments.append(appointment)

    def get_schedule(self) -> list:
        """Return this practitioner's upcoming appointments. (FR-07)"""
        return list(self._appointments)


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class InvalidTransitionError(Exception):
    """Raised when an Appointment status change breaks the allowed state flow."""
    pass


class Appointment:
    """
    Implemented from the approved UML with AI pair-programming assistance
    (Part D). See domain_implementation_v0.4.md Section 4 for the prompt,
    Copilot's original generated code, and the full review record (Part E)
    explaining why several parts were reworked before being accepted here.
    """
    def __init__(self, patient: Patient, practitioner: Practitioner, time: str):
        if not time:
            raise ValueError("Appointment time cannot be empty")
        self._patient = patient
        self._practitioner = practitioner
        self._time = time
        self._status = AppointmentStatus.SCHEDULED
        patient.add_appointment(self)
        practitioner.add_appointment(self)

    @property
    def patient(self) -> Patient:
        return self._patient

    @property
    def practitioner(self) -> Practitioner:
        return self._practitioner

    @property
    def time(self) -> str:
        return self._time

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def cancel(self) -> None:
        """Cancel a scheduled appointment. Cancelled objects are retained, not deleted. (FR-05, FR-06)"""
        if self._status != AppointmentStatus.SCHEDULED:
            raise InvalidTransitionError(
                f"Cannot cancel an appointment with status {self._status.value}"
            )
        self._status = AppointmentStatus.CANCELLED

    def complete(self) -> None:
        """Mark a scheduled appointment as completed. (FR-10)"""
        if self._status != AppointmentStatus.SCHEDULED:
            raise InvalidTransitionError(
                f"Cannot complete an appointment with status {self._status.value}"
            )
        self._status = AppointmentStatus.COMPLETED

    def reschedule(self, new_time: str) -> None:
        """Update this appointment's date/time. (FR-09)"""
        if self._status != AppointmentStatus.SCHEDULED:
            raise InvalidTransitionError(
                f"Cannot reschedule an appointment with status {self._status.value}"
            )
        if not new_time:
            raise ValueError("New appointment time cannot be empty")
        self._time = new_time


# ---- Manual behaviour checks (Part F) ----
if __name__ == "__main__":
    patient = Patient("P001", "Alice Smith", "alice@example.com")
    practitioner = Practitioner("D001", "Dr. John Doe", "General Practice")

    # Valid object creation
    appt = Appointment(patient, practitioner, "2024-07-20 10:00 AM")
    print(f"Created: {appt.patient.name} with {appt.practitioner.name} at {appt.time} ({appt.status.value})")

    # Invalid input
    try:
        Patient("", "No ID", "test@example.com")
    except ValueError as e:
        print(f"Blocked invalid patient: {e}")

    # Cancel a scheduled appointment
    appt.cancel()
    print(f"After cancel: status = {appt.status.value}")

    # Illegal repeated transition
    try:
        appt.cancel()
    except InvalidTransitionError as e:
        print(f"Blocked illegal transition: {e}")
