# Stage 1 Tutorial Activities

## Activity 1 — Think-Pair-Share

If ChatGPT or Copilot can produce a 100-line Python application very
quickly, what knowledge does a software engineer still need?

1. Understanding *why* the software needs to do what it does — talking
   to stakeholders, working out what's actually required versus assumed.
2. Judging whether the generated code is correct, secure, and handles
   edge cases — AI doesn't know your specific business rules.
3. Making design decisions that trade off cost, maintainability, and
   scale — AI optimizes for "working code," not the decisions around it.

## Activity 2 — Is This Software Engineering?

| Scenario | Programming? | Software engineering? | Why? |
|---|---|---|---|
| A (50-line calculator) | Yes | No | Small, self-contained, no stakeholders, no requirements process, no long-term maintenance concerns |
| B (payroll system, 5,000 employees) | Yes | Yes | Requires requirements gathering, stakeholder management, testing, compliance, maintainability at scale |
| C (AI-generated appointment app from one prompt) | Yes | No — not by itself | Producing code isn't engineering; no requirements analysis, validation, or stakeholder input happened |

## Activity 3 — SmartCare Problem Analysis

### Task 1 — Identify stakeholders

| Stakeholder | What do they need? |
|---|---|
| Receptionist | Fast, error-free way to book/cancel appointments without duplicate entries |
| Patients | Confidence their appointment is correctly recorded and not double-booked |
| Practitioners (GPs) | Accurate visibility of their own schedule/availability |
| Clinic management | Reliable reporting on appointment volume, cancellations, no-shows |

### Task 2 — Identify current problems

1. Duplicate appointment bookings caused by manual, spreadsheet-based entry
2. Difficulty locating patient records quickly across paper and spreadsheets
3. No reliable, centralised view of practitioner availability
4. No consistent appointment history for reporting or auditing

### Task 3 — Ask client questions

1. Should the system prevent double-booking automatically, or just flag it?
2. Do practitioners need to see their own schedule, or only the receptionist?
3. Is patient history (past visits) required at this stage, or just current bookings?
4. How should cancellations be recorded — deleted, or kept with a "cancelled" status?
5. Will this run on one computer, or does it need multiple staff accessing it at once?

## Activity 4 — Critique an AI Response

| Suggestion | Client evidence? | In scope? | Decision |
|---|---|---|---|
| Appointment management | Yes — directly stated | Yes | Keep |
| Facial recognition login | No | No | Reject |
| AI diagnosis recommendations | No | No | Reject — clinical risk, not requested |
| Patient search | Implied (difficulty locating records) | Yes | Keep |
| Online payment | No | No | Reject — not mentioned as a problem |
| Practitioner schedule view | Yes — "limited visibility of practitioner availability" | Yes | Keep |
| Insurance processing | No | No | Reject |
| Treatment-plan generation | No | No | Reject — out of scope, clinical decision-making |

## Exit question

Deciding what *not* to build — scoping out features an AI suggests that
aren't backed by an actual client need — is something that can't safely
be delegated to AI, because it requires judgement about the client's
real problem, not pattern-matching to "what appointment apps usually have."