# Initial Engineering Brief — SmartCare

## 1. Problem summary

SmartCare Community Clinic currently manages patients and appointments
using spreadsheets and paper records. This has led to duplicate
bookings, difficulty locating patient records, inconsistent appointment
status, and no reliable visibility of practitioner availability.
Cancellations are handled manually with no consistent process, and
there is no reliable appointment history to support basic reporting.
Management wants a simple software system — not a full hospital
information system — that supports patient, practitioner, and
appointment management as a first version. The system will be built
iteratively across several stages, starting with a basic prototype and
adding validation, structure, and features incrementally.

## 2. Initial stakeholders

| Stakeholder | Possible need |
|---|---|
| Receptionist | Simple, fast booking interface with minimal room for error |
| Practitioners | Clear view of their own appointments |
| Clinic management | Operational reports (bookings, cancellations, no-shows) |
| Patients (indirect) | Correct, non-duplicated appointment records |

## 3. Initial features

| Feature | Confirmed or provisional? | Why? |
|---|---|---|
| Book an appointment | Confirmed | Directly stated in the brief |
| View practitioner availability | Confirmed | Directly stated as a current problem |
| Cancel an appointment | Provisional | Implied by "manual cancellation processes" but not detailed |
| Search/find a patient record | Provisional | Implied by "difficulty locating patient records" |

## 4. Questions for the client

1. Should double-booking be blocked outright, or just flagged for the
   receptionist to review?
2. What information should a patient record contain beyond name and
   appointment history?
3. Do practitioners need login access, or is this receptionist-only for now?
4. What counts as a "basic operational report" — booking counts,
   cancellations, something else?
5. Is there an existing patient list/spreadsheet this needs to import
   from, or starting fresh?

## 5. What we do not yet know

1. Whether the system needs to support multiple clinic locations or just one
2. Whether practitioners will interact with the system directly or only
   the receptionist will
3. What data retention or privacy requirements apply to patient records