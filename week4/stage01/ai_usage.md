# AI Usage Log — Stage 1

## Tool used
Microsoft Copilot (UC-approved GenAI tool)

## Part C — AI as tutor

**Prompt used:** Act as a Python tutor. I am learning introductory
software technology. Here is a small appointment-booking function.
1. Explain what the code does. 2. Identify three limitations.
3. Suggest improvements. 4. Do not rewrite the whole application.
5. Ask me two questions to test my understanding.

**AI response:**

1. What the code does: Stores clinic appointments in a simple Python
list, with two operations — book_appointment() (adds an appointment,
minimal validation) and display_appointments() (prints all stored
appointments). The global appointments list acts as an in-memory
"database."

2. Three limitations:
   - No clash detection — allows two appointments for the same
     practitioner at the same time.
   - Weak validation — only patient name is checked; practitioner and
     time can be None, empty, or nonsense.
   - No persistence — all data disappears when the program stops.

3. Suggested improvements: add validation rules for practitioner/time,
implement clash checking before adding an appointment, introduce
persistence via a JSON or CSV file.

4. Two questions asked by the AI:
   1. Why does the current system allow two appointments for the same
      practitioner at the same time?
   2. What is one advantage of storing appointments in a file instead
      of a Python list?

**My answers:**
1. Because book_appointment() never checks the existing list before
appending — it only validates patient_name, so nothing stops a
duplicate practitioner/time combination from being added.
2. Data would survive after the program closes. Right now appointments
only exists in memory, so restarting the script wipes everything.

## Part D — AI-generated alternative

**Prompt used:** Write a simple beginner-friendly Python function that
stores patient name, practitioner name and appointment time. No
database, no GUI.

**AI response:**

```python
appointments = []

def add_appointment(patient, practitioner, time):
    """Store a single appointment in the appointments list."""
    appointment = {
        "patient": patient,
        "practitioner": practitioner,
        "time": time
    }
    appointments.append(appointment)

def show_appointments():
    """Display all saved appointments."""
    if not appointments:
        print("No appointments yet.")
        return

    for appt in appointments:
        print(f"Patient: {appt['patient']} | Practitioner: {appt['practitioner']} | Time: {appt['time']}")

# Example usage
add_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
add_appointment("Bob Johnson", "Dr. Jane Roe", "2024-07-20 11:30 AM")

show_appointments()
```

## Evaluate

| Suggestion | Useful | Unclear | Incorrect | Out of scope |
|---|---|---|---|---|
| Add validation for practitioner/time | ✓ | | | |
| Add clash detection | ✓ | | | |
| Persist data to file | | | | ✓ (out of scope for Stage 1) |

## Decide
- Add validation for practitioner/time: **Accept** (small, controlled change)
- Clash detection: **Reject for now** — bigger change than "improve one thing"
- File persistence: **Reject** — out of scope for this stage