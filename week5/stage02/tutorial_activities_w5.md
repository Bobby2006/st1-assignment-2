# Stage 2 Tutorial Activities

## Activity 1 — Stakeholder Map

| Stakeholder | Need | Potential conflict |
|---|---|---|
| Receptionist | Fast, simple way to book/cancel appointments without extra steps | Wants speed, which can conflict with strict validation requirements |
| Practitioner | Accurate, up-to-date view of their own daily schedule | May want more schedule control than receptionist wants to hand over |
| Clinic Manager | Reliable reporting on bookings, cancellations, and history | Wants detailed data capture, which can slow down receptionist workflow |
| Patient (indirect) | Correct appointment recorded, no double-booking | Has no direct system access, relies entirely on staff accuracy |

## Activity 2 — Functional or Non-Functional?

- ☑ Functional — The system shall allow staff to cancel an appointment.
- ☑ Non-functional — The system should remain responsive for the course-scale dataset.
- ☑ Functional — The system shall retain cancelled appointments.
- ☑ Non-functional — Core business logic should be independently testable.
- ☑ Functional — The system shall search for a patient by ID.

## Activity 3 — Repair Ambiguous Requirements

**"The system should be easy to use."**
Problem: "Easy to use" isn't measurable — no one can test whether it's true.
Clarification question: What specific task should a new staff member be able to complete without training, and how quickly?

**"Patient search should be fast."**
Problem: "Fast" has no defined threshold.
Clarification question: What is the maximum acceptable time for a patient search to return a result?

**"The system should securely manage data."**
Problem: "Securely" doesn't specify what threat or standard is being protected against.
Clarification question: Does this mean access control (who can view records), data storage protection, or both?

**"Appointments should normally be easy to cancel."**
Problem: "Normally" implies exceptions that aren't defined, and "easy" isn't measurable.
Clarification question: Are there specific conditions (e.g. same-day cancellations) where the process should differ?

## Activity 4 — AI Requirements Audit

| AI suggestion | Classification | Evidence / reason |
|---|---|---|
| Patients receive SMS reminders | Unsupported | Not mentioned anywhere in the client brief |
| Facial recognition login | Unsupported | No security requirement of this kind was raised by the client |
| Receptionists create appointments | Confirmed | Directly implied by the brief's description of current booking problems |
| Online payment | Out of scope | Client brief describes only patient/practitioner/appointment management |
| Practitioners view schedules | Assumption requiring validation | Reasonable given "limited appointment history," but not explicitly confirmed by client |
| AI recommends treatments | Out of scope | Clinical decision-making, unrelated to the stated administrative problem |
| Cancelled appointments remain in history | Confirmed | Directly supported by "limited appointment history" problem in the brief |

## Exit question

"AI suggested it" is not sufficient evidence for a requirement because the
AI has no direct knowledge of the client's actual needs — it is
pattern-matching against what similar systems typically include, not
responding to anything the client has said. A requirement needs
traceable evidence back to the client brief or stakeholder input;
otherwise the system risks building features nobody asked for while
missing ones the client actually needs.
