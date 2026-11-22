# P-12 Validation against the reference calculation

This is the success criterion (BRIEF). Built first, not last.

Steps
1. Encode the reference sample screen as a request fixture (input form values).
2. Encode the reference outputs as expected values, line by line, at whatever granularity the reference has (Q-G03).
3. Run the engine on the fixture; compare each expected value with the matching trace node.
4. Report: matched / delta / missing (O10).
5. For each delta, read the trace to find the first diverging node; fix the rule or the setting (MD-17), never by hard-coding the expected number.
6. Repeat until all lines match. Keep as an automated test so later changes cannot break it.

Demo value: show the comparison table live at the pitch, then change one parameter and show the whole plan recomputed in seconds.
