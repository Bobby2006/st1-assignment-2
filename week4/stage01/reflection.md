# Stage 1 Reflection

Before using AI, I built a simple appointment-booking prototype using a
list of dictionaries and two functions: one to add appointments (with a
check that the patient name isn't empty) and one to display them.
Running it showed a real limitation quickly — my own code let me
double-book Dr. John Doe at the exact same time slot for two different
patients, with no error at all.

Using AI as a tutor helped confirm and name the gaps precisely: no clash
detection, weak validation beyond the patient name, and no persistence
once the program ends. It also asked me two questions rather than just
handing me answers, which pushed me to explain, in my own words, why the
validation only lives in one place in my code.

The AI's own generated version made a different trade-off than mine. It
assumed all input would always be valid and skipped validation entirely.
I didn't just take that on faith — I ran it myself with the same edge
cases I'd tested on my own code: a blank patient name, None values for
practitioner and time, and a duplicate booking. All three went through
completely silently. My version at least caught the blank name with a
ValueError; the AI version caught nothing. That difference only showed
up because I actually executed both versions rather than reading the
code and assuming it worked.

What remained my job as the engineer: deciding which of the AI's
suggestions were actually worth adopting at this stage, rejecting the
bigger ones (clash detection, file persistence) as out of scope for a
"improve one thing" exercise, and understanding both versions well
enough to explain exactly where and why they diverge.