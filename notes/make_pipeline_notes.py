#!/usr/bin/env python3
"""Generate a compact, exam-ready one-page PDF on ARM pipelining.

Source: Module 5 "The ARM Instruction Set" pp.22-35 (3/5-stage pipeline,
PC+8, throughput, ARM7 vs ARM9, hazards and fixes).

Usage:  python3 make_pipeline_notes.py  ->  ARM_Pipelining.pdf
"""
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle)

PAGE_W, PAGE_H = A4
MARGIN = 12 * mm
GUTTER = 5.5 * mm
COL_W = (PAGE_W - 2 * MARGIN - GUTTER) / 2.0

NAVY = colors.HexColor("#0F2E4C")
BLUE = colors.HexColor("#1B5E8C")
GREY = colors.HexColor("#F2F4F7")
LINE = colors.HexColor("#C9D2DC")
AMBER_BG = colors.HexColor("#FFF6DC")
AMBER_TX = colors.HexColor("#6B5310")

S = {}
S["h1"] = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=9.4, leading=11.2,
                         textColor=colors.white, backColor=NAVY,
                         borderPadding=(2.6, 3, 2.6, 3), spaceBefore=5.0, spaceAfter=3.2)
S["h2"] = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=8.1, leading=9.6,
                         textColor=BLUE, spaceBefore=3.4, spaceAfter=1.6)
S["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=7.5, leading=9.1,
                           alignment=TA_JUSTIFY, spaceAfter=1.8)
S["li"] = ParagraphStyle("li", parent=S["body"], leftIndent=7.2, bulletIndent=1.0,
                         spaceAfter=1.1)
S["cm"] = ParagraphStyle("cm", fontName="Helvetica-Oblique", fontSize=7.0, leading=8.5,
                         textColor=AMBER_TX, backColor=AMBER_BG,
                         borderPadding=(2.2, 3, 2.2, 3), spaceBefore=1.6, spaceAfter=3.0)
S["cell"] = ParagraphStyle("cell", fontName="Helvetica", fontSize=6.9, leading=8.1)
S["cellb"] = ParagraphStyle("cellb", parent=S["cell"], fontName="Helvetica-Bold")
S["cellc"] = ParagraphStyle("cellc", parent=S["cell"], alignment=1)
S["chd"] = ParagraphStyle("chd", parent=S["cell"], fontName="Helvetica-Bold",
                          textColor=colors.white)
S["title"] = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=14.5,
                            leading=16.5, textColor=NAVY)
S["sub"] = ParagraphStyle("sub", fontName="Helvetica", fontSize=7.6, leading=9.4,
                          textColor=colors.HexColor("#3B4A5A"))


def h1(t):
    return Paragraph(t, S["h1"])


def h2(t):
    return Paragraph(t, S["h2"])


def p(t):
    return Paragraph(t, S["body"])


def li(t):
    return Paragraph(t, S["li"], bulletText="\u25aa")


def cm(t):
    return Paragraph(t, S["cm"])


def table(header, rows, widths, first_bold=True, center=None):
    c = center or []
    data = [[Paragraph(x, S["chd"]) for x in header]]
    for r in rows:
        row = []
        for i, x in enumerate(r):
            if i == 0 and first_bold:
                st = S["cellb"]
            elif i in c:
                st = S["cellc"]
            else:
                st = S["cell"]
            row.append(Paragraph(str(x), st))
        data.append(row)
    t = Table(data, colWidths=widths, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.3, LINE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, GREY]),
        ("LEFTPADDING", (0, 0), (-1, -1), 2.4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2.4),
        ("TOPPADDING", (0, 0), (-1, -1), 1.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
    ]))
    return t


def deco(canv, doc):
    canv.saveState()
    canv.setStrokeColor(LINE)
    canv.setLineWidth(0.4)
    y = MARGIN - 4.5 * mm
    canv.line(MARGIN, y, PAGE_W - MARGIN, y)
    canv.setFont("Helvetica", 6.6)
    canv.setFillColor(colors.HexColor("#6C7A89"))
    canv.drawString(MARGIN, y - 7.5,
                    "ARM Pipelining \u2014 Exam Ready Notes  |  MPMC / ARM (Module 5)")
    canv.drawRightString(PAGE_W - MARGIN, y - 7.5, "Page %d" % doc.page)
    canv.restoreState()


story = []
A = story.append

# --------------------------------------------------------------- 1
A(h1("1. What pipelining is + the ARM7 3-stage pipeline"))
A(p("The ARM uses a pipeline to <b>increase the speed of the flow of instructions</b> to "
    "the processor: several operations are undertaken <b>simultaneously</b> rather than "
    "serially, so throughput rises without a faster clock."))
A(li("<b>Fetch</b> &mdash; read the opcode from memory into the internal instruction "
     "register."))
A(li("<b>Decode</b> &mdash; activate the appropriate control lines depending on the "
     "opcode; decode the registers used and prepare the data-path control signals for "
     "the <b>next</b> cycle."))
A(li("<b>Execute</b> &mdash; read register(s) from the register bank; shift + ALU "
     "operation; write register(s) back to the register bank (for LDR/STR the ALU "
     "computes the memory address)."))
ws = [COL_W * 0.30] + [COL_W * 0.14] * 5
A(table(["", "c1", "c2", "c3", "c4", "c5"],
        [["Instr 1 (at PC)", "F", "D", "E", "", ""],
         ["Instr 2 (at PC+4)", "", "F", "D", "E", ""],
         ["Instr 3 (at PC+8)", "", "", "F", "D", "E"]],
        ws, first_bold=False))
A(p("<b>Key fact (module p.23):</b> the PC points to the instruction being "
    "<b>fetched</b>, not the one being executed. At any cycle: executing = PC&minus;8, "
    "decoding = PC&minus;4, fetching = PC &rArr; the stored PC reads "
    "<font face='Courier'><b>PC = current instruction + 8</b></font> in ARM state "
    "(<b>PC+4</b> in Thumb)."))
A(cm("Comment: &ldquo;Why PC+8?&rdquo; is the favourite question here. Answer in one line: "
     "3-stage pipeline &rArr; fetch is two stages ahead of execute, and ARM instructions "
     "are 4 bytes, so 2 &times; 4 = 8."))

# --------------------------------------------------------------- 2
A(h1("2. Throughput &amp; the pipeline cost formula"))
A(li("<b>Simple instructions</b> (e.g. <b>ADD</b>) complete at a rate of <b>one per "
     "cycle</b> on ARM7TDMI."))
A(li("<b>More complex:</b> <b>STR needs 2 effective clock cycles (+1 cycle)</b> for the "
     "memory access; every cycle still does a memory access, datapath use and a decode "
     "for the next cycle."))
A(p("<b>Cost formula:</b> CPU time = instruction count &times; <b>CPI</b> &times; clock "
    "period. Ideal pipelined CPI = 1; every stall raises CPI."))
A(cm("Comment: pipelining improves <i>throughput</i>, not the time of one instruction "
     "(latency stays 3 or 5 cycles). Examiners love this distinction."))

# --------------------------------------------------------------- 3
A(h1("3. The ARM9 5-stage pipeline"))
A(li("<b>Fetch</b> &mdash; instruction fetched and placed in the pipeline."))
A(li("<b>Decode</b> &mdash; register operands read; the file has <b>3 operand read "
     "ports</b>, so most instructions source all operands in one cycle."))
A(li("<b>Execute</b> &mdash; operand shifted and ALU result generated; load/store "
     "addresses computed in the ALU."))
A(li("<b>Buffer/Data</b> &mdash; data memory accessed if required, else the ALU result is "
     "simply buffered one cycle."))
A(li("<b>Write back</b> &mdash; results, including data loaded from memory, written to "
     "the register file."))
wa = [COL_W * 0.30, COL_W * 0.35, COL_W * 0.35]
A(table(["Item", "ARM7", "ARM9"],
        [["Architecture", "Von Neumann (one shared bus)",
          "Harvard (separate I &amp; D memory)"],
         ["Pipelining", "3-stage (F&ndash;D&ndash;E)",
          "5-stage (F&ndash;D&ndash;E&ndash;Buf&ndash;WB)"],
         ["ISA", "v4T", "v4T"]],
        wa))
A(cm("Comment: link the three facts &mdash; Harvard &rarr; fetch and data access in the "
     "same cycle &rarr; a deeper 5-stage pipeline is possible. Always quote them "
     "together."))

# --------------------------------------------------------------- 4
A(h1("4. Pipeline hazards and their fixes (module pp.28&ndash;35)"))
wh = [COL_W * 0.24, COL_W * 0.42, COL_W * 0.34]
A(table(["Hazard", "Cause", "Fix"],
        [["Structural", "Two instructions want the <b>same resource</b> in the same "
                        "cycle (one memory for instr + data).",
          "Separate instruction &amp; data memories/caches (<b>I$ and D$</b>); register "
          "file: <b>read in 2nd half</b> of cycle, <b>write in 1st half</b>."],
         ["Data", "An instruction needs a <b>result not yet ready</b> (classic "
                 "<font face='Courier'>lw</font> then "
                 "<font face='Courier'>add</font> using it).",
          "Stall (bubbles), or <b>forwarding/bypassing</b> the result."],
         ["Control", "A <b>branch</b> must decide the next PC before the condition is "
                    "evaluated and the target computed.",
          "Stall (this <b>hurts CPI</b>), branch prediction, or ARM&rsquo;s "
          "<b>conditional execution</b>."]],
        wh))
A(p("<b>General rule (module):</b> a hazard can always be resolved by <b>waiting</b> "
    "(stalling) &mdash; but pipeline control must first <b>detect</b> the hazard and "
    "<b>take action</b> to resolve it; stalling costs CPI."))
A(cm("Comment: memorise one example per hazard &mdash; single memory (structural), "
     "lw&rarr;add (data), beq (control). &ldquo;Fix by waiting but it affects CPI&rdquo; "
     "is the module&rsquo;s own sentence for the control hazard."))

# --------------------------------------------------------------- 5
A(h1("5. One-minute revision"))
A(p("<b>Numbers:</b> ARM7 = 3 stages &middot; ARM9 = 5 stages &middot; both ISA v4T "
    "&middot; PC+8 (ARM) / PC+4 (Thumb) &middot; ADD = 1/cycle &middot; STR = 2 cycles "
    "&middot; 3 read ports &middot; ideal CPI = 1."))
A(p("<b>Likely questions:</b> (1) Explain the ARM instruction pipeline with a diagram. "
    "(2) Why does PC read as PC+8? (3) Compare ARM7 and ARM9 pipelining. (4) Define the "
    "three hazard types and give a fix for each. (5) How does pipelining increase "
    "throughput?"))
A(cm("Comment: always draw the F&ndash;D&ndash;E staircase with PC, PC&minus;4, PC&minus;8 "
     "labels (section 1) &mdash; it is the diagram that scores full marks."))

doc = BaseDocTemplate("ARM_Pipelining.pdf", pagesize=A4, leftMargin=MARGIN,
                      rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN,
                      title="ARM Pipelining - Exam Ready Notes", author="Arena agent")
top = MARGIN + 6 * mm
hgt = PAGE_H - 2 * MARGIN - 8 * mm
doc.addPageTemplates([PageTemplate(id="t", onPage=deco, frames=[
    Frame(MARGIN, top, COL_W, hgt, leftPadding=0, rightPadding=0, topPadding=0,
          bottomPadding=0),
    Frame(MARGIN + COL_W + GUTTER, top, COL_W, hgt, leftPadding=0, rightPadding=0,
          topPadding=0, bottomPadding=0),
])])
doc.build([Paragraph("ARM Pipelining &mdash; Exam Ready Notes", S["title"]),
           Paragraph("Source: Module 5 &ldquo;The ARM Instruction Set&rdquo; pp.22&ndash;35. "
                     "Highlighted italic lines are <b>comments</b>.", S["sub"]),
           Spacer(1, 2.5)] + story)
print("written: ARM_Pipelining.pdf")
