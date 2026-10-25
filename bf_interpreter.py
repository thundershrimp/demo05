def run(code, inp="", size=30000, maxsteps=2_000_000):
    code = ''.join(c for c in code if c in '+-<>[].,')
    # bracket map
    m, st = {}, []
    for i, c in enumerate(code):
        if c == '[': st.append(i)
        elif c == ']':
            j = st.pop(); m[i], m[j] = j, i
    tape = [0]*size
    p = ip = 0; iq = 0; out = []
    steps = 0
    while ip < len(code) and steps < maxsteps:
        c = code[ip]; steps += 1
        if c == '+': tape[p] = (tape[p]+1) % 256
        elif c == '-': tape[p] = (tape[p]-1) % 256
        elif c == '>': p += 1
        elif c == '<': p -= 1
        elif c == '.': out.append(tape[p])
        elif c == ',':
            tape[p] = ord(inp[iq]) if iq < len(inp) else 0
            iq += 1
        elif c == '[':
            if tape[p] == 0: ip = m[ip]
        elif c == ']':
            if tape[p] != 0: ip = m[ip]
        ip += 1
    return out, tape[:6], steps

p1 = """,[
>+
<-
]
>-."""
p2 = """++++++++++
[
>++++++++
>++++++++
<<-
]
>-.
>."""
p3 = """,>,[<+>-]<."""

for name, code, inp in [("P1", p1, "A"), ("P1", p1, "Z"), ("P1", p1, "!"),
                        ("P2", p2, ""), ("P3", p3, "23"), ("P3", p3, "AA"), ("P3", p3, "0A")]:
    out, tape, steps = run(code, inp)
    print(f"{name} input={inp!r:6} -> values={out} chars={''.join(chr(v) for v in out)!r} tape={tape} steps={steps}")
