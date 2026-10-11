#!/usr/bin/env python3
"""Generate compact, exam-ready PDF notes on RISC for MPMC (Module 5 - ARM).

Content is grounded in "Module 5.pdf" (The ARM Instruction Set, ARM University
Program V1.0) plus the standard university RISC/CISC syllabus.

Usage:  python3 make_risc_notes.py  ->  writes RISC_Exam_Notes.pdf
"""
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                               Spacer, Table, TableStyle, KeepTogether)

PAGE_W, PAGE_H = A4
MARGIN = 13 * mm
GUTTER = 5.5 * mm
COL_W = (PAGE_W - 2 * MARGIN - GUTTER) / 2.0

NAVY = colors.HexColor("#0F2E4C")
BLUE = colors.HexColor("#1B5E8C")
GREY = colors.HexColor("#F2F4F7")
LINE = colors.HexColor("#C9D2DC")
AMBER_BG = colors.HexColor("#FFF6DC")
AMBER_TX = colors.HexColor("#6B5310")
GREEN = colors.HexColor("#0B5D3B")

S = {}
S["h1"] = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=9.6, leading=11.4,
                         textColor=colors.white, backColor=NAVY, borderPadding=(2.6, 3, 2.6, 3),
                         spaceBefore=5.5, spaceAfter=3.4)
S["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=7.5, leading=9.15,
                           alignment=TA_JUSTIFY, spaceAfter=1.8)
S["li"] = ParagraphStyle("li", parent=S["body"], leftIndent=7.2, bulletIndent=1.0,
                         spaceAfter=1.1)
S["li2"] = ParagraphStyle("li2", parent=S["body"], leftIndent=14.5, bulletIndent=8.5,
                          fontSize=7.3, leading=8.8, spaceAfter=0.9)
S["cm"] = ParagraphStyle("cm", fontName="Helvetica-Oblique", fontSize=7.0, leading=8.5,
                         textColor=AMBER_TX, backColor=AMBER_BG, borderPadding=(2.2, 3, 2.2, 3),
                         leftIndent=0, spaceBefore=1.6, spaceAfter=3.0)
S["cell"] = ParagraphStyle("cell", fontName="Helvetica", fontSize=6.9, leading=8.2)
S["cellb"] = ParagraphStyle("cellb", parent=S["cell"], fontName="Helvetica-Bold")
S["chd"] = ParagraphStyle("chd", parent=S["cell"], fontName="Helvetica-Bold",
                          textColor=colors.white)
S["title"] = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=15, leading=17,
                            textColor=NAVY)
S["sub"] = ParagraphStyle("sub", fontName="Helvetica", fontSize=7.6, leading=9.4,
                          textColor=colors.HexColor("#3B4A5A"))


def h1(t):
    return Paragraph(t, S["h1"])


def h2(t):
    return Paragraph(t, ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=8.1,
                                       leading=9.6, textColor=BLUE, spaceBefore=3.6,
                                       spaceAfter=1.6))


def p(t):
    return Paragraph(t, S["body"])


def li(t):
    return Paragraph(t, S["li"], bulletText="\u25aa")


def li2(t):
    return Paragraph(t, S["li2"], bulletText="\u2013")


def cm(t):
    return Paragraph(t, S["cm"])


def table(header, rows, widths, first_bold=True):
    data = [[Paragraph(x, S["chd"]) for x in header]]
    for r in rows:
        data.append([Paragraph(str(r[0]), S["cellb"] if first_bold else S["cell"])
                     if first_bold else Paragraph(str(r[0]), S["cell"])]
                    + [Paragraph(str(c), S["cell"]) for c in r[1:]])
    t = Table(data, colWidths=widths, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.3, LINE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, GREY]),
        ("LEFTPADDING", (0, 0), (-1, -1), 2.6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2.6),
        ("TOPPADDING", (0, 0), (-1, -1), 1.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.6),
    ]))
    return t


def page_deco(canv, doc):
    canv.saveState()
    canv.setStrokeColor(LINE)
    canv.setLineWidth(0.4)
    y = MARGIN - 4.5 * mm
    canv.line(MARGIN, y, PAGE_W - MARGIN, y)
    canv.setFont("Helvetica", 6.6)
    canv.setFillColor(colors.HexColor("#6C7A89"))
    canv.drawString(MARGIN, y - 7.5, "RISC \u2014 Exam Ready Notes  |  MPMC / ARM (Module 5)")
    canv.drawRightString(PAGE_W - MARGIN, y - 7.5, "Page %d" % doc.page)
    canv.restoreState()


story = []
A = story.append

# ---------------------------------------------------------------- title
A(Paragraph("RISC &mdash; Exam Ready Notes", S["title"]))
A(Paragraph("Microprocessor &amp; Microcontrollers (MPMC) &middot; ARM = <b>Acorn RISC "
            "Machine</b> &middot; Source: Module 5 &ldquo;The ARM Instruction Set&rdquo; "
            "(ARM University Program V1.0). Highlighted italic lines are <b>comments</b> "
            "(why it is asked / how to remember it).", S["sub"]))
A(Spacer(1, 3))

# ---------------------------------------------------------------- 1
A(h1("1. What RISC is (definition + origin)"))
A(p("<b>RISC</b> = <b>Reduced Instruction Set Computer / Computing</b>. A design "
    "philosophy that keeps only a <b>small set of simple, uniform-length "
    "instructions</b>, each executing in (almost) <b>one clock cycle</b>, operating "
    "<b>only on registers</b>; memory is touched exclusively by explicit "
    "<b>LOAD</b> and <b>STORE</b> instructions."))
A(li("<b>Origin:</b> early-1980s university research &mdash; <b>Berkeley RISC</b> (David "
     "Patterson) and <b>Stanford MIPS</b> (John Hennessy)."))
A(li("<b>Idea behind it:</b> real programs spend most of their time in a small subset of "
     "instructions (locality). Make that subset extremely fast; push everything rare into "
     "software / the compiler."))
A(li("<b>ARM = Acorn RISC Machine</b> &mdash; developed by <b>Acorn Computers (UK)</b>; the "
     "official project started <b>October 1983</b>, silicon partner <b>VLSI Technology</b>, "
     "design led by <b>Wilson and Furber</b>."))
A(li("ARM is a <b>32-bit RISC load/store architecture</b>. Memory <b>cannot</b> be "
     "manipulated directly &mdash; data must first be brought into registers."))
A(cm("Comment: RISC &ldquo;reduces&rdquo; the <i>hardware</i>, not the work. Complexity does "
     "not disappear &mdash; it moves from the chip into the <b>compiler</b> and the "
     "<b>programmer</b>. This one line earns marks in almost every RISC question."))

# ---------------------------------------------------------------- 2
A(h1("2. The RISC design rules (feature list)"))
A(li("<b>Large, uniform register file</b> &mdash; operands live in registers, not memory."))
A(li("<b>Load/store architecture</b> &mdash; only LDR/STR access memory; ALU instructions "
     "never do."))
A(li("<b>Few, simple addressing modes</b> (immediate, register, register-offset, "
     "pre/post-indexed, PC-relative)."))
A(li("<b>Fixed-length instructions</b> &rarr; simple, fast, hard-wired decoding."))
A(li("<b>Single-cycle execution</b> for most instructions &rarr; high clock rate."))
A(li("<b>Pipelining</b> is the main throughput mechanism."))
A(li("<b>Hard-wired control unit</b> (no micro-code / control store)."))
A(li("<b>3-operand register format</b>: <font face='Courier'>Rd = Rn op Rm</font>."))
A(li("<b>Simple data types</b> &mdash; 8 / 16 / 32-bit integers, few formats."))
A(li("<b>Compiler does the heavy lifting</b> &mdash; register allocation, scheduling, "
     "expansion of complex operations."))
A(cm("Comment: every one of these exists for the same reason &mdash; to shorten the "
     "<i>critical path</i> so the clock can run faster. Learn the list as "
     "&ldquo;<b>few, fixed, fast, register-only, pipelined, compiler-driven</b>&rdquo;."))

# ---------------------------------------------------------------- 3
A(h1("3. RISC vs CISC (classic 10-mark table)"))
w3 = [COL_W * 0.235, COL_W * 0.385, COL_W * 0.38]
A(table(["Parameter", "RISC", "CISC"],
        [["Instructions", "Small set (~30&ndash;100), simple &amp; uniform",
          "Large set (~100&ndash;300+), complex, varied"],
         ["Length", "Fixed (ARM: 32 bit)", "Variable (1&ndash;15 bytes in x86)"],
         ["Execution", "~1 cycle / instruction", "Several cycles, varies per instruction"],
         ["Addressing modes", "Few and simple", "Many and complex"],
         ["Memory operand", "Only via LOAD / STORE", "ALU can operate directly on memory"],
         ["Registers", "Many (large file, banked)", "Few"],
         ["Control unit", "Hard-wired", "Micro-programmed (control store)"],
         ["Decoding", "Simple, fast", "Complex, slow"],
         ["Code density", "Poor (more instructions, larger code)",
          "Good (dense code, less memory)"],
         ["Compiler role", "Heavy dependence", "Light dependence"],
         ["Pipelining", "Easy and efficient", "Difficult"],
         ["Chip cost / power", "Smaller, cheaper, low power",
          "Larger, costlier, more power"],
         ["Examples", "ARM, RISC-V, MIPS, AVR, PowerPC, SPARC",
          "Intel x86, 8051, Motorola 68k, VAX"],
         ["Typical use", "Mobile, embedded, low-power, SoC",
          "Desktop / server, legacy compatibility"]],
        w3))
A(cm("Comment: bonus line &mdash; modern x86 is <b>CISC outside, RISC inside</b>: it "
     "translates CISC instructions into simple RISC-like <i>micro-ops</i> that are then "
     "pipelined."))

# ---------------------------------------------------------------- 4
A(h1("4. ARM as a RISC processor &mdash; main features of the ARM ISA"))
A(li("<b>All instructions are 32 bits long</b> &rarr; uniform fetch and decode."))
A(li("<b>Most instructions execute in a single cycle.</b>"))
A(li("<b>Every instruction can be conditionally executed</b> (4-bit condition field: "
     "EQ, NE, GT, LT, AL&hellip;)."))
A(li("<b>Load/store architecture</b> &mdash; data-processing instructions act "
     "<b>only on registers</b>."))
A(li("<b>Three-operand format</b> (Rd, Rn, Rm)."))
A(li("<b>Combined ALU and barrel shifter</b> &rarr; high-speed bit manipulation at no "
     "extra cycle cost."))
A(li("<b>Specific memory-access instructions</b> with powerful <b>auto-indexing</b> "
     "addressing modes (address updates as you load/store)."))
A(li("<b>32-bit and 8-bit data types</b>, plus <b>16-bit</b> from ARM Architecture v4."))
A(li("<b>Flexible multiple-register load/store</b> &mdash; LDM / STM (and PUSH/POP)."))
A(li("<b>Instruction-set extension via coprocessors</b> (CP0&ndash;CP15)."))
A(cm("Comment: &ldquo;conditional execution&rdquo; is ARM&rsquo;s trick to avoid branches "
     "&mdash; fewer branches means fewer pipeline stalls, which is exactly what a RISC "
     "pipeline needs."))
A(h2("Why ARM (RISC) is chosen &mdash; advantages"))
A(li("Cheap compared with other processors; simple design &rarr; minimum energy waste."))
A(li("Low power consumption &rarr; much better battery life (mobiles, tablets, MP3 "
     "players, PDAs, hand-held gaming, hard drives)."))
A(li("Performs <b>one operation at a time</b>, hence works faster per operation."))
A(li("Wide availability and application support."))
A(h2("ARM vs Intel (RISC vs CISC in the market)"))
A(li("ARM: very simple structure, minimum energy wastage, low chip price, long history in "
     "portable devices."))
A(li("Intel: complicated design kept for compatibility with its desktop / laptop CPUs; "
     "entered the mobile space later; ARM&rsquo;s growth forced Intel to raise its "
     "efficiency."))
A(h2("AVR &mdash; another RISC family (module fact)"))
A(p("AVR = <b>Alf-Egil Bogen &amp; Vegard Wollan RISC</b> (also called Advanced Virtual "
    "RISC), by <b>Atmel, 1996</b>. First device <b>AT90S8515</b>; first commercial part "
    "<b>AT90S1200 (1997)</b>. Categories: <b>TinyAVR</b> (small, simple apps), "
    "<b>MegaAVR</b> (up to 256&nbsp;KB, most popular), <b>XmegaAVR</b> (large memory, high "
    "speed, complex apps)."))
A(p("<b>PIC</b> (Microchip) also uses <b>RISC</b> &mdash; <b>PIC = Harvard / RISC</b>, "
    "<b>AVR = Harvard / RISC</b>, whereas <b>8051</b> is an 8-bit <b>CISC-style</b> family "
    "(128&nbsp;B RAM, 4&nbsp;KB ROM, 2 timers, 1 serial port, 4 ports on one chip)."))

# ---------------------------------------------------------------- 5
A(h1("5. Register file &mdash; RISC means register-rich"))
A(li("ARM has <b>37 registers, all 32-bit</b>: 1 PC + 1 CPSR + <b>5 SPSRs</b> + "
     "<b>30 general-purpose</b> registers."))
A(li("<b>7 processor modes</b>: <b>User</b> (unprivileged, normal tasks), <b>FIQ</b> "
     "(fast/high-priority interrupt), <b>IRQ</b> (normal interrupt), <b>SVC</b> "
     "(supervisor &mdash; reset &amp; SWI), <b>Abort</b> (memory access violation), "
     "<b>Undef</b> (undefined instruction), <b>System</b> (privileged, uses User "
     "registers)."))
A(li("<b>Banking:</b> the current mode decides which bank is visible. FIQ banks "
     "<b>r8&ndash;r14</b>; IRQ/SVC/Abort/Undef bank only <b>r13(sp), r14(lr)</b> (+ SPSR)."))
A(li("Visible in <i>every</i> mode: <b>r0&ndash;r12</b>, <b>r13 = sp</b>, "
     "<b>r14 = lr</b>, <b>r15 = pc</b>, <b>CPSR</b>."))
w5 = [COL_W * 0.20, COL_W * 0.80]
A(table(["Register", "Role (must-know)"],
        [["PC (r15)", "Program counter. Any instruction with PC as destination = a "
                      "<b>branch</b>."],
         ["LR (r14)", "Link register. Holds a copy of PC on <b>BL</b> (subroutine call) or "
                      "on an exception; copied back to PC on return."],
         ["SP (r13)", "Stack pointer. There is <b>no stack in the architecture</b> &mdash; "
                      "the stack is program-managed."],
         ["CPSR", "Current Program Status Register: flags <b>N Z C V</b> + mode bits."],
         ["SPSR", "Saved CPSR while an exception/interrupt runs; restored on return. "
                  "<b>None in User or System mode.</b>"]],
        w5))
A(cm("Comment: banked registers are a pure RISC performance choice &mdash; on a mode switch "
     "the hardware gives the interrupt its own sp/lr, so nothing has to be saved first "
     "&rarr; very fast interrupts. FIQ gets the most private registers (r8&ndash;r14) "
     "because it must be the <i>fastest</i>."))

# ---------------------------------------------------------------- 6
A(h1("6. Data-flow model &mdash; how load/store actually happens"))
A(li("Sources <b>Rn</b> and <b>Rm</b> are read from the register file on internal buses "
     "<b>A</b> and <b>B</b>; the result is written back to <b>Rd</b>."))
A(li("The <b>ALU</b> or <b>MAC</b> (multiply-accumulate) unit computes the result."))
A(li("<b>Rm may first pass through the barrel shifter</b> (LSL, LSR, ASR, ROR). Barrel "
     "shifter and ALU work together <b>in the same cycle</b>, so a shifted operand and an "
     "address calculation cost nothing extra."))
A(li("<b>Load/store:</b> the ALU is used to <b>compute the address</b>, which is held in "
     "the address register and broadcast on the address bus."))
A(li("<b>Sign-extend hardware</b> widens signed 8/16-bit values to 32 bits as they are "
     "loaded; unsigned values are zero-filled."))
A(li("<b>Incrementer:</b> PC goes into the address register, is incremented, and the new "
     "value is copied back into r15 and used for the next fetch."))
A(li("<b>Von Neumann</b> core (ARM7): one shared bus carries <i>either</i> instruction "
     "<i>or</i> data; the instruction decoder translates the instruction before execution."))
A(cm("Comment: the sentence to quote in an exam &mdash; &ldquo;there are <b>no data-"
     "processing instructions that directly manipulate data in memory</b>; data items are "
     "placed in the register file.&rdquo; That is the definition of a load/store (RISC) "
     "architecture."))

# ---------------------------------------------------------------- 7
A(h1("7. Pipelining &mdash; the RISC throughput trick"))
A(p("The pipeline lets several operations overlap instead of running serially, raising "
    "throughput without a faster clock."))
A(h2("ARM7: 3-stage pipeline"))
A(li("<b>Fetch</b> &mdash; read the opcode from memory into the internal instruction "
     "register."))
A(li("<b>Decode</b> &mdash; activate the control lines for that opcode; read register "
     "operands (the file has <b>3 read ports</b>, so most instructions get all operands in "
     "one cycle)."))
A(li("<b>Execute</b> &mdash; shift + ALU operation; for a load/store the ALU computes the "
     "memory address."))
A(p("<b>Throughput:</b> simple instructions such as <b>ADD</b> complete at a rate of "
    "<b>one per cycle</b>. More complex ones cost extra &mdash; <b>STR needs 2 effective "
    "clock cycles (+1 cycle)</b> for the memory access."))
wp = [COL_W * 0.30] + [COL_W * 0.14] * 5
A(table(["", "c1", "c2", "c3", "c4", "c5"],
        [["Instr 1 (at PC)", "F", "D", "E", "", ""],
         ["Instr 2 (at PC+4)", "", "F", "D", "E", ""],
         ["Instr 3 (at PC+8)", "", "", "F", "D", "E"]],
        wp, first_bold=False))
A(p("<i>At cycle c3:</i> executing = instruction at PC, decoding = PC+4, fetching = PC+8 "
    "&rArr; the stored PC value reads <b>8 bytes ahead</b> of the executing instruction."))
A(p("<b>Key fact:</b> the PC points to the instruction being <b>fetched</b>, not the one "
    "being executed. In ARM state, therefore, "
    "<font face='Courier'><b>PC = address of current instruction + 8</b></font> "
    "(two words ahead): executing = PC&minus;8, decode = PC&minus;4, fetch = PC."))
A(cm("Comment: &ldquo;Why is PC = PC+8 in ARM?&rdquo; is a favourite 2/5-mark question. "
     "Answer: 3-stage pipeline &rarr; fetch is 2 stages ahead of execute, and ARM "
     "instructions are 4 bytes, so 2 &times; 4 = 8. (In Thumb state, instructions are 2 "
     "bytes &rarr; PC+4.)"))
A(h2("ARM9: 5-stage pipeline"))
A(p("<b>Fetch</b> &rarr; <b>Decode</b> &rarr; <b>Execute</b> &rarr; <b>Buffer/Data</b> "
    "(access data memory, or simply buffer the ALU result for one cycle) &rarr; "
    "<b>Write back</b> (result, including loaded data, returned to the register file)."))
w7 = [COL_W * 0.30, COL_W * 0.35, COL_W * 0.35]
A(table(["Item", "ARM7", "ARM9"],
        [["Architecture", "Von Neumann (shared bus)", "Harvard (separate I &amp; D memory)"],
         ["Pipelining", "3-stage", "5-stage"],
         ["ISA", "v4T", "v4T"]],
        w7))
A(cm("Comment: the 5-stage pipeline is only possible because Harvard architecture has "
     "separate instruction and data memories &mdash; an instruction fetch and a data access "
     "can then happen in the same cycle. Link ARM7/ARM9 &rarr; Von Neumann/Harvard &rarr; "
     "3/5-stage; they are always asked together."))
A(h2("Pipeline hazards and their fixes"))
A(li("<b>Structural hazard</b> &mdash; two instructions need the same resource in the same "
     "cycle. <i>Fix:</i> separate instruction and data memories / caches (I$ and D$); for "
     "register-file ports, <b>read in the second half</b> of the cycle and <b>write in the "
     "first half</b>."))
A(li("<b>Data hazard</b> &mdash; an instruction needs a result still inside the pipeline "
     "(classic <font face='Courier'>lw</font> followed by "
     "<font face='Courier'>add</font>). <i>Fix:</i> stall the pipeline, or forward/bypass "
     "the result."))
A(li("<b>Control hazard</b> &mdash; a branch must decide the next PC before the condition "
     "is evaluated and the target computed. <i>Fix:</i> stall (this hurts CPI), branch "
     "prediction, or ARM&rsquo;s conditional execution."))
A(p("<b>Cost formula:</b> CPU time = instruction count &times; CPI &times; clock period. "
    "Every stall raises CPI."))

# ---------------------------------------------------------------- 8
A(h1("8. Advantages and limitations of RISC"))
w8 = [COL_W * 0.50, COL_W * 0.50]
A(table(["Advantages", "Limitations"],
        [["Simple hardware &rarr; smaller, cheaper, lower-power chip",
          "Lower code density &rarr; more instructions, more program memory"],
         ["Fixed-length, single-cycle instructions &rarr; high clock, easy pipelining",
          "Heavy dependence on a good compiler"],
         ["Regularity &rarr; excellent compiler optimisation",
          "Simple loops need extra load/store instructions"],
         ["Many registers &rarr; less memory traffic",
          "Pipeline hazards / stalls reduce the theoretical 1 CPI"],
         ["Predictable timing &rarr; ideal for embedded &amp; real-time",
          "Poor fit for complex legacy (CISC) software"]],
        w8))

# ---------------------------------------------------------------- 9
A(h1("9. One-minute revision block"))
A(p("<b>Mnemonic &mdash; R.I.S.C.:</b> <b>R</b>egisters many &middot; "
    "<b>I</b>nstructions few and fixed-length &middot; <b>S</b>ingle-cycle and "
    "load/Store only &middot; <b>C</b>ompiler does the rest."))
A(p("<b>Numbers to memorise:</b> 32-bit instructions &middot; 37 registers / 30 GPRs "
    "&middot; 7 modes &middot; 5 SPSRs &middot; 3 read ports &middot; ARM7 = 3-stage, "
    "ARM9 = 5-stage &middot; PC+8 &middot; STR = 2 cycles &middot; ARM project Oct 1983 "
    "&middot; AVR 1996."))
A(p("<b>Likely questions:</b> (1) Define RISC and explain its features. (2) Compare RISC "
    "with CISC. (3) Explain why ARM is a RISC processor / list the main features of the ARM "
    "instruction set. (4) Describe ARM register organisation and banking. (5) Explain the "
    "ARM pipeline and why PC = PC+8. (6) Explain pipeline hazards with remedies. "
    "(7) Distinguish ARM7 and ARM9."))
A(cm("Comment: for 10-mark answers always draw the 3-stage pipeline diagram (F &ndash; D "
     "&ndash; E with PC, PC&minus;4, PC&minus;8) or the RISC-vs-CISC table &mdash; a diagram "
     "or table is what separates a 6 from a 9."))

doc = BaseDocTemplate("RISC_Exam_Notes.pdf", pagesize=A4,
                      leftMargin=MARGIN, rightMargin=MARGIN,
                      topMargin=MARGIN, bottomMargin=MARGIN,
                      title="RISC - Exam Ready Notes (MPMC / ARM)",
                      author="Arena agent")
tpl = PageTemplate(id="two", frames=[
    Frame(MARGIN, MARGIN + 7 * mm, COL_W, PAGE_H - 2 * MARGIN - 9 * mm,
          leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0),
    Frame(MARGIN + COL_W + GUTTER, MARGIN + 7 * mm, COL_W,
          PAGE_H - 2 * MARGIN - 9 * mm,
          leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0),
])
doc.addPageTemplates([tpl])
doc.build(story)
print("written: RISC_Exam_Notes.pdf")
