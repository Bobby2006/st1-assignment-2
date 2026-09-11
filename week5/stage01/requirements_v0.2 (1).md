# SmartCare Requirements Specification v0.2

## 1. Problem and Scope

SmartCare currently uses spreadsheets and paper records to manage
patients, practitioners, and appointments. This has caused duplicate
bookings, difficulty finding patient information, inconsistent
appointment status, and limited appointment history. Management wants a
small, maintainable system covering patient, practitioner, and
appointment management — not a full hospital information system.

**In scope (v0.2):**
- Patient record management (create, search, update contact details)
- Practitioner schedule viewing
- Appointment booking, cancellation, and rescheduling
- Appointment history retention (including cancelled appointments)
- Basic conflict prevention (double-booking)

**Out of scope (v0.2):**
- Online payments
- AI-generated treatment or diagnosis suggestions
- Facial recognition or biometric login
- Insurance processing
- Multi-location support

**Provisional (not yet confirmed with client):**
- SMS/email reminders to patients
- Practitioner direct login/system access

## 2. Stakeholders

| Stakeholder | Need | Evidence |
|---|---|---|
| Receptionist | Fast, accurate way to create and manage appointments | Directly implied by "staff report duplicate bookings" |
| Practitioner | Accurate view of own upcoming schedule | Implied by "limited appointment history" and scheduling problems |
| Clinic Manager | Reliable reporting on bookings/cancellations for oversight | Implied by "management wants a maintainable system" |
| Patient (indirect) | Correct, non-duplicated appointment records | Directly implied by "duplicate bookings" problem statement |
| System Administrator | System remains maintainable as features are added incrementally | Directly stated — "small, maintainable...system" |

## 3. Functional Requirements

FR-01: The system shall allow staff to create a new patient record.

FR-02: The system shall allow staff to search for a patient by ID.

FR-03: The system shall allow staff to book a new appointment for a
patient with a practitioner at a specified date and time.

FR-04: The system shall prevent a new appointment being booked for a
practitioner who already has an appointment at the same date and time.

FR-05: The system shall allow staff to cancel an existing appointment.

FR-06: The system shall retain cancelled appointments in the
appointment history rather than deleting them.

FR-07: The system shall allow staff to view a practitioner's schedule
of upcoming appointments.

FR-08: The system shall allow staff to update an existing patient's
contact details.

FR-09: The system shall allow staff to reschedule an existing
appointment to a new date and time.

FR-10: The system shall record the status of each appointment (e.g.
booked, cancelled, completed).

FR-11: The system shall allow staff to view the full appointment
history for a given patient.

FR-12: The system shall validate that required appointment fields
(patient, practitioner, time) are not empty before saving.

## 4. Non-Functional Requirements

NFR-01: The system should remain responsive for a course-scale dataset
(up to a few hundred records) with no noticeable delay.

NFR-02: Core business logic (e.g. booking, validation) should be
independently testable, separate from any display/output code.

NFR-03: The system shall not permanently lose recorded appointment data
during normal operation.

NFR-04: The system's code should be maintainable, using clear naming
and modular structure so features can be added incrementally in later
stages.

NFR-05: The system should provide clear feedback messages when an
action succeeds or fails.

NFR-06: The system should be reasonably resistant to invalid input
causing a crash.

## 5. User Stories

US-01: As a receptionist, I want to book an appointment for a patient,
so that the patient has a confirmed time with a practitioner.

US-02: As a receptionist, I want to search for a patient by ID, so that
I can quickly find their record without scrolling through a full list.

US-03: As a receptionist, I want to cancel an appointment, so that the
practitioner's schedule reflects accurate availability.

US-04: As a practitioner, I want to view my upcoming schedule, so that
I know which patients I am seeing and when.

US-05: As a clinic manager, I want cancelled appointments retained in
history, so that I can review cancellation patterns over time.

US-06: As a receptionist, I want to be prevented from double-booking a
practitioner, so that scheduling conflicts don't happen.

## 6. Acceptance Criteria

GIVEN a practitioner has no appointment at 10:00 AM on a given date
WHEN a receptionist books a new appointment for that practitioner at
that time
THEN the appointment shall be saved and appear in the practitioner's
schedule.

GIVEN a practitioner already has an appointment at 10:00 AM on a given
date
WHEN a receptionist attempts to book another appointment for the same
practitioner at the same time
THEN the system shall reject the booking and display an error message.
(negative scenario)

GIVEN an existing booked appointment
WHEN a receptionist cancels that appointment
THEN the appointment's status shall change to "cancelled" and it shall
remain visible in the patient's history rather than being deleted.

## 7. Assumptions and Open Questions

**Assumptions:**
- Single clinic location is assumed for v0.2.
- Only receptionists and clinic management will directly use the
  system at this stage; practitioners are assumed to view schedules
  indirectly (e.g. printed/shared by reception) unless confirmed
  otherwise.

**Open questions for the client:**
1. Should double-booking be blocked outright, or flagged for staff
   review before rejecting?
2. Do practitioners need direct login access, or is this
   receptionist-only for v0.2?
3. What specific fields are required on a patient record beyond name
   and appointment history?
4. Is SMS/email reminders in scope for a future version?
5. Should practitioners view their schedule directly, or only
   indirectly through reception? (raised by AI review — conflicting
   statements exist between the scope list and the assumptions)
6. What is the complete list of valid appointment statuses beyond
   booked/cancelled/completed? (raised by AI review)
7. Should conflict checking catch overlapping appointment times, not
   just exact time matches? (raised by AI review)
8. Does rescheduling an appointment create a new history entry or
   modify the existing one? (raised by AI review)
9. Does appointment duration need to be tracked, and does it affect
   conflict checking? (raised by AI review)
10. Should cancellation permissions be role-based, or can any staff
    member cancel any appointment? (raised by AI review — flagged as a
    future-stage question, not a v0.2 blocker)

## 8. AI Requirements Review Record

| AI suggestion | Evidence? | Decision | Reason | Verification |
|---|---|---|---|---|
| Clarify whether practitioners view schedules directly or indirectly (via reception) | Evidence-based — quotes both "practitioner schedule viewing" in scope and the indirect-access assumption | Accepted | Real inconsistency between two parts of the document; needs client confirmation | Added to Section 7 open questions |
| Define full list of valid appointment statuses (FR-10 only gives examples) | Evidence-based — FR-10 says "e.g." without a closed list | Accepted | FR-10 as written isn't fully testable without a defined status set | Added to Section 7 open questions |
| Clarify whether "double-booking" conflict checking should catch overlapping times, not just exact matches | Evidence-based — Acceptance Criteria only test exact same time | Accepted | Genuine gap — a 10:00–10:30 and 10:15–10:45 booking would currently pass unnoticed | Added to Section 7 open questions |
| Confirm whether rescheduling creates a new history entry or modifies the existing appointment | Evidence-based — FR-09 doesn't specify | Accepted | Affects how FR-06 (history retention) and FR-09 interact; worth clarifying before implementation | Added to Section 7 open questions |
| Confirm whether appointment duration matters for conflict checking | Evidence-based — no duration is mentioned anywhere in the spec | Accepted | Directly relevant to how conflict detection (FR-04) should actually work | Added to Section 7 open questions |
| Confirm whether cancellation permissions are role-based | Evidence-based — FR-05 says "staff" without defining roles | Modified | Reasonable question, but out of scope for v0.2 since no role model exists yet — noted as a future-stage question rather than a v0.2 blocker | Added to Section 7, flagged as future scope |
| Confirm whether patient search should support more than ID (e.g. name) | Evidence-based — FR-02 explicitly states ID-only | Rejected | FR-02 was deliberately scoped to ID search for v0.2; broadening it now would be scope creep without client confirmation | Left as-is; noted as possible future enhancement only |
