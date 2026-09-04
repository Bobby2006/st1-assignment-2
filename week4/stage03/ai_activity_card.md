# AI Activity Card — Ask, Check, Explain

## Before AI
I think the code stores appointments in memory and prints them back out.
Problems I can already see: no validation beyond patient name, and
nothing stops the same practitioner being booked twice at the same time.

## AI request
**Prompt used:** Act as a tutor. Explain this code and identify
potential problems. Do not provide a complete replacement. Ask me
questions that help me reason about the solution.

**AI response:**

What this code does: You start with an empty list called appointments
(temporary storage). book_appointment() creates a dictionary with
patient name, practitioner name, and appointment time, checks only that
patient_name isn't empty, and appends it to the list. display_appointments()
prints each stored appointment.

Potential problems:
1. Only patient name is validated — practitioner name and appointment
   time could be empty or nonsense.
2. No clash detection — two appointments for the same practitioner at
   the same time are allowed.
3. No data persistence — all appointments disappear when the program ends.
4. No feedback when adding an appointment — it's added silently with no
   confirmation.
5. No type checking — a number, list, or None could be passed as the
   patient name and Python won't stop it.

Tutor-style reasoning questions asked by the AI:
1. If you wanted to prevent double-booking a practitioner, what
   information would you need to compare before adding a new appointment?
2. What kinds of mistakes might happen if you don't validate the
   appointment time — and how could you detect them?

**My answers:**
1. I'd need to compare the practitioner name and appointment time of the
new booking against every existing appointment already in the list —
if both match an existing entry, reject or flag it before adding.
2. Without validating time, someone could enter nonsense text, an
impossible date, a past date, or None. This could be detected by
checking the value isn't empty/None and matches an expected date/time
format before accepting it.

## Evaluate

| Suggestion | Useful | Unclear | Incorrect | Out of scope |
|---|---|---|---|---|
| Add validation for practitioner/time | ✓ | | | |
| Add clash detection | ✓ | | | |
| Add confirmation feedback on booking | ✓ | | | |
| Add type checking | | ✓ | | |
| Add file persistence | | | | ✓ |

## Decide
- Add validation for practitioner/time: **Accept**
- Clash detection: **Reject for now** — bigger than a single controlled improvement
- Confirmation feedback: **Accept** — small, easy addition
- Type checking: **Reject for now** — unclear how strict this needs to be at this stage
- File persistence: **Reject** — out of scope for this stage

## Verify
- Ran the code myself
- Tested normal input
- Tested unusual input (blank name, None values)
- Compared against the case study's stated requirements

## Explain
Yes — I can explain the final code without re-reading the AI's response.
What I'd still want to firm up: exactly how a clash check would compare
existing entries once it's actually implemented, rather than just
identifying it as a gap.