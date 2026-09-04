# Human vs AI Version Comparison

| Question | Human version | AI version |
|---|---|---|
| Easy to understand? | Yes, clear naming | Yes, equally simple |
| Runs successfully? | Yes | Yes |
| Uses only required features? | Yes | Yes |
| Adds assumptions? | Assumes patient_name is the only field worth checking | Assumes all input is always valid — no checks at all |
| Handles errors? | Partially — raises ValueError on empty patient name only | No — accepts blank names, None values, and duplicate bookings with no error |
| Could I explain it? | Yes | Yes |

## Notes
Both versions are structurally similar — a list of dictionaries with an
add function and a display function. The difference is validation: my
version rejects an empty patient name but still allows None values for
practitioner/time and duplicate bookings. The AI version validates
nothing at all, so it's slightly cleaner code but functionally weaker —
it would let genuinely broken data into the system silently. Running
both with the same edge cases (blank name, None fields, duplicate
practitioner/time) confirmed this: my version caught the blank name,
the AI version caught nothing.