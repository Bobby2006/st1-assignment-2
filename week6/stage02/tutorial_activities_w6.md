# Stage 3 Tutorial Activities

## Candidate Concepts

| Candidate | Class? | Reason |
|---|---|---|
| Patient | Yes | Core domain entity — holds identifying/contact data, referenced across FR-01, FR-02, FR-08 |
| Practitioner | Yes | Core domain entity — referenced across booking/scheduling requirements (FR-03, FR-04, FR-07) |
| Appointment | Yes | Central entity linking a Patient and Practitioner with time and status (FR-03–FR-10) |
| Name | No | Just an attribute (string) of Patient/Practitioner — has no independent behaviour or identity |
| Clinic | No | Single-location assumption for v0.3 (Section 7 of requirements) — no evidence yet of multi-clinic scope |
| Database | No | Implementation/infrastructure concern, not a domain concept |
| Cancellation | No | A state change on Appointment (status field), not a separate object |
| Status | No | An attribute of Appointment (string/enum), not a class of its own |

## CRC Cards

### Patient
| Responsibilities | Collaborators |
|---|---|
| Store patient identifying details (ID, name, contact info) | Appointment |
| Provide access to this patient's appointment history | Appointment |

### Practitioner
| Responsibilities | Collaborators |
|---|---|
| Store practitioner details (ID, name) | Appointment |
| Provide this practitioner's upcoming schedule | Appointment |

### Appointment
| Responsibilities | Collaborators |
|---|---|
| Link one Patient and one Practitioner with a date/time | Patient, Practitioner |
| Track and update its own status (booked/cancelled/completed) | — |

## Relationship Reasoning

**Patient to Appointment:** Association, not composition or inheritance.
A Patient has many Appointments over time (one-to-many), but an
Appointment doesn't own or contain the Patient — the Patient exists
independently and continues to exist if an appointment is deleted.

**Practitioner to Appointment:** Multiplicity of 1 to 0..* — one
Practitioner can have many Appointments, but each Appointment has
exactly one Practitioner at a time.

**Should Appointment inherit from Patient?** No. Inheritance means
"is-a," and an Appointment is not a kind of Patient — they have
completely different attributes and responsibilities. This relationship
should be association (Appointment *references* a Patient), not
inheritance.

**Does Clinic need to own every object?** No, not at this stage. The
requirements assume a single clinic location for v0.3 (see Section 7,
Requirements v0.2), so introducing a Clinic class to "own" Patient,
Practitioner, and Appointment adds complexity with no current evidence
requiring it. This could be revisited if multi-location support enters
scope later.

## AI Model Critique

Critique of proposed classes: PatientManager, PractitionerManager,
AppointmentManager, ClinicController, NotificationManager, ScheduleEngine.

| Proposed class | Needed now? | Reason |
|---|---|---|
| PatientManager | No | The responsibilities described (create/search/update) belong naturally to Patient itself or a simple function — a separate "Manager" layer adds complexity not justified at this scale |
| PractitionerManager | No | Same reasoning as PatientManager — no evidence this scale of system needs a manager layer |
| AppointmentManager | Partially | Conflict-checking across multiple appointments doesn't cleanly belong to a single Appointment instance — better handled as a simple validation function for now rather than a full class |
| ClinicController | No | No Clinic concept has been confirmed in scope; premature to build a controller for a class that doesn't exist |
| NotificationManager | No | Reminders/notifications are only a provisional, unconfirmed requirement (Requirements v0.2, Section 1) — no evidence to justify building this yet |
| ScheduleEngine | No | Course-scale data (a few hundred records) doesn't need a dedicated "engine" — this is over-engineering relative to NFR-04's maintainability goal; a simple function suffices for now |
