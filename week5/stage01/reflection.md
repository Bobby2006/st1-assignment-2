# Stage 2 Reflection

Running the requirements document through Copilot surfaced gaps I hadn't
noticed while writing it. I hadn't considered that "double-booking"
could mean more than an exact time match — a 10:00–10:30 appointment
and a 10:15–10:45 one for the same practitioner would currently slip
through unflagged, since my acceptance criteria only tested identical
timestamps. I also hadn't spotted the inconsistency between listing
"practitioner schedule viewing" as in scope while separately assuming
practitioners only view schedules indirectly through reception — those
two statements don't actually agree with each other.

What stood out was that the AI didn't invent anything: every point it
raised cited an exact phrase from my own document, and where it wasn't
sure, it labelled the point as a question requiring validation rather
than asserting a new requirement. The one place I pushed back was its
suggestion to broaden patient search beyond ID — FR-02 was a deliberate
scoping decision, not an oversight, so I rejected that one rather than
expanding scope on the AI's say-so.

Requirements need evidence because a system built on invented or
assumed needs risks solving the wrong problem entirely. Evidence keeps
every requirement traceable back to something the client (or their
brief) actually said, rather than to what a system "usually" has.
