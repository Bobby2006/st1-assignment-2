# Stage 4 Tutorial Activities

## Activity 1 — Encapsulation Review

| Class | Protected state / invariant | Public operations |
|---|---|---|
| Patient | id, name, contact must never be empty once set | update_contact(), get_appointments() |
| Practitioner | id, name, specialty are fixed after creation | get_schedule() |
| Appointment | status must only move through valid transitions (e.g. never "completed" back to "booked") | cancel(), reschedule() — status is never set directly from outside the class |

## Activity 2 — Composition or Inheritance?

**Appointment and Patient →** ☑ Composition/association ☐ Inheritance
Reason: An Appointment references a Patient but doesn't own its
lifecycle — the Patient exists independently before and after any given
appointment. This is association, not composition or inheritance.

**Appointment and Practitioner →** ☑ Composition/association ☐ Inheritance
Reason: Same logic as Patient — Appointment links to a Practitioner
without owning or being a type of Practitioner.

**Doctor and Practitioner (hypothetical) →** ☐ Composition/association ☑ Inheritance
Reason: A Doctor genuinely "is-a" Practitioner (a specialisation with
possibly extra attributes like a medical registration number), so
inheritance is appropriate here — unlike Appointment, which is not a
specialised type of anything.

**Clinic and Appointment →** ☑ Composition/association ☐ Inheritance
Reason: If a Clinic class existed, it would reference or coordinate
Appointments, not "be" one. Whether this is composition (Clinic owns
appointment lifecycle) or plain association would depend on whether
appointments can exist without a clinic context — not yet confirmed, so
weak association is the safer default until specified.

## Activity 3 — Responsibility Allocation

**Who decides whether SCHEDULED can become CANCELLED?**
The Appointment class itself, via its own cancel() method — the object
that owns the state should be the only thing allowed to change it.

**Who validates a patient name?**
The Patient class itself, in its constructor/setter — not the caller,
not the UI, not a separate validator class.

**Should Appointment execute SQL?**
No. Appointment is a domain object representing business rules and
state; persistence (SQL, file I/O) is a separate concern. Mixing them
violates single responsibility and makes the class harder to test in
isolation (per NFR-02: business logic should be independently testable).

**Should the UI decide whether a status transition is legal?**
No. If the UI enforces the rule, every other caller (tests, future
interfaces, scripts) could bypass it. The rule belongs inside
Appointment so it's enforced no matter who calls it.

## Activity 4 — AI Code Critique

The AI-generated Appointment class described has these problems:

1. **Public status mutation** — allows any external code to set status
   directly (e.g. `appointment.status = "cancelled"`), bypassing any
   transition rules entirely. *Correction:* status should only change
   through methods like cancel(), which can enforce valid transitions.

2. **SQL inside cancel()** — mixes persistence logic into a domain
   method. *Correction:* Appointment should have no knowledge of how or
   whether it's saved to a database; that's a separate concern.

3. **NotificationManager dependency** — Appointment now depends on a
   class with no confirmed requirement behind it (reminders/notifications
   were only ever a provisional, unconfirmed requirement). *Correction:*
   remove the dependency entirely until it's an actual requirement.

4. **Inheritance from PatientRecord** — Appointment is not a
   specialised type of Patient/PatientRecord; this misuses inheritance
   for a relationship that should be association. *Correction:*
   Appointment should hold a reference to a Patient object, not inherit
   from one.

5. **No enum for status** — using raw strings for status invites typos
   and makes invalid states possible (e.g. "cancelled" vs "Cancelled").
   *Correction:* use an AppointmentStatus enum with a fixed, valid set
   of values.

## Exit question

Code can be syntactically object-oriented — using classes, objects, and
methods — while still having poor object-oriented design, because
syntax alone doesn't enforce encapsulation, correct responsibility
allocation, or meaningful relationships. A class with public fields, no
validation, mixed concerns (like SQL inside a domain method), and
misused inheritance is still "using classes" but violates the actual
principles OOP design is meant to achieve: protecting invariants,
keeping responsibilities focused, and modelling relationships honestly.
