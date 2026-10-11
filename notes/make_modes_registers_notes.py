#!/usr/bin/env python3
"""Generate two compact, exam-ready PDFs from Module 5 (ARM):

  * ARM_Operating_Modes.pdf  - the seven processor modes (module p.13)
  * ARM_Register_Sets.pdf    - register organisation & banking (module pp.14-17)

Usage:  python3 make_modes_registers_notes.py
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
FULL_W = PAGE_W - 2 * MARGIN

NAVY = colors.HexColor("#0F2E4C")
BLUE = colors.HexColor("#1B5E8C")
GREY = colors.HexColor("#F2F4F7")
LINE = colors.HexColor("#C9D2DC")
AMBER_BG = colors.HexColor("#FFF6DC")
AMBER_TX = colors.HexColor("#6B5310")


def styles():
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
    return S


S = styles()


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


def deco(foot_title):
    def f(canv, doc):
        canv.saveState()
        canv.setStrokeColor(LINE)
        canv.setLineWidth(0.4)
        y = MARGIN - 4.5 * mm
        canv.line(MARGIN, y, PAGE_W - MARGIN, y)
        canv.setFont("Helvetica", 6.6)
        canv.setFillColor(colors.HexColor("#6C7A89"))
        canv.drawString(MARGIN, y - 7.5, foot_title + "  |  MPMC / ARM (Module 5)")
        canv.drawRightString(PAGE_W - MARGIN, y - 7.5, "Page %d" % doc.page)
        canv.restoreState()
    return f


def build(path, title, subtitle, story, frames, foot):
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=MARGIN, bottomMargin=MARGIN, title=title,
                          author="Arena agent")
    doc.addPageTemplates([PageTemplate(id="t", frames=frames, onPage=deco(foot))])
    head = [Paragraph(title, S["title"]),
            Paragraph(subtitle, S["sub"]), Spacer(1, 2.5)]
    doc.build(head + story)
    print("written:", path)


# ======================================================================
#  PDF 1 : ARM OPERATING MODES  (two columns, 1 page)
# ======================================================================
top = MARGIN + 6 * mm
hgt = PAGE_H - 2 * MARGIN - 8 * mm
modes_story = []
A = modes_story.append

A(h1("1. The seven processor modes (module verbatim)"))
wm = [COL_W * 0.155, COL_W * 0.475, COL_W * 0.37]
A(table(["Mode", "Entered when", "Class"],
        [["User", "Unprivileged mode under which <b>most tasks</b> run "
                 "(normal application code).", "Unprivileged; no SPSR"],
         ["FIQ", "A <b>high-priority (fast) interrupt</b> is raised.",
          "Privileged exception mode; own SPSR"],
         ["IRQ", "A <b>low-priority (normal) interrupt</b> is raised.",
          "Privileged exception mode; own SPSR"],
         ["SVC", "On <b>reset</b> and when a <b>Software Interrupt (SWI)</b> "
                 "instruction is executed.", "Privileged exception mode; own SPSR"],
         ["Abort", "A <b>memory access violation</b> occurs.",
          "Privileged exception mode; own SPSR"],
         ["Undef", "An <b>undefined instruction</b> is fetched.",
          "Privileged exception mode; own SPSR"],
         ["System", "Entered deliberately (OS tasks); <b>privileged mode using the "
                    "same registers as User mode</b>.", "Privileged; no SPSR"]],
        wm))
A(cm("Comment: remember the modes as <b>1 user + 5 exception + 1 system</b>. Only "
     "User is unprivileged; the five exception modes each get a private SPSR; System is "
     "&ldquo;User&rsquo;s registers with privilege&rdquo;."))

A(h1("2. Grouping the modes (classic exam view)"))
A(li("<b>Privileged vs unprivileged:</b> all modes except User are privileged &mdash; they "
     "may use the MSR instruction to change mode and can access all system resources and "
     "the banked registers."))
A(li("<b>Exception vs non-exception modes:</b> FIQ, IRQ, SVC, Abort and Undef are "
     "<b>exception modes</b> &mdash; hardware switches into them automatically and each "
     "has a <b>banked SPSR</b> to save the previous CPSR. User and System are "
     "non-exception modes (no SPSR)."))
A(li("<b>How the mode changes:</b> hardware on reset / interrupt / fault; or software via "
     "an <b>MSR</b> write to the mode bits of CPSR (privileged modes only)."))
A(cm("Comment: hardware mode switching + banked registers is why ARM exceptions are fast: "
     "the new mode gets its own sp/lr/spsr, so the old context is preserved <i>without "
     "saving anything first</i>."))

A(h1("3. CPSR mode bits (standard fact)"))
wb = [COL_W * 0.20] + [COL_W * 0.114] * 5 + [COL_W * 0.23]
A(table(["Mode", "M4", "M3", "M2", "M1", "M0", "Hex (M[4:0])"],
        [["User", "1", "0", "0", "0", "0", "0x10"],
         ["FIQ", "1", "0", "0", "0", "1", "0x11"],
         ["IRQ", "1", "0", "0", "1", "0", "0x12"],
         ["SVC", "1", "0", "0", "1", "1", "0x13"],
         ["Abort", "1", "0", "1", "1", "1", "0x17"],
         ["Undef", "1", "1", "0", "1", "1", "0x1B"],
         ["System", "1", "1", "1", "1", "1", "0x1F"]],
        wb, center=[1, 2, 3, 4, 5, 6]))
A(p("The CPSR also carries the condition flags <b>N, Z, C, V</b>, the interrupt disables "
    "<b>I</b> (IRQ) and <b>F</b> (FIQ) and the state bit <b>T</b> (ARM/Thumb)."))
A(cm("Comment: &ldquo;which bits of CPSR select the mode?&rdquo; is a 2-mark favourite "
     "&mdash; answer M[4:0], and quote two encodings (User 10000, SVC 10011) as proof."))

A(h1("4. Banked registers per mode (link to register sets)"))
A(li("FIQ banks <b>r8&ndash;r14</b> &rarr; its handler barely saves anything, which is why "
     "FIQ is the <b>fast</b> interrupt."))
A(li("IRQ, SVC, Abort and Undef each bank only <b>r13 (sp)</b> and <b>r14 (lr)</b>, plus a "
     "private <b>SPSR</b>."))
A(li("User and System share one register set; <b>r0&ndash;r12, r15 and CPSR</b> are common "
     "to every mode."))
A(cm("Comment: in an exam answer, pair the mode table with this banking table &mdash; they "
     "are two halves of the same question."))

A(h1("5. One-minute revision"))
A(p("<b>Numbers:</b> 7 modes &middot; 6 privileged &middot; 5 exception modes (5 SPSRs) "
    "&middot; 1 unprivileged (User) &middot; mode = CPSR M[4:0]."))
A(p("<b>Likely questions:</b> (1) List the ARM operating modes and when each is entered. "
    "(2) Distinguish privileged/unprivileged and exception/non-exception modes. (3) Explain "
    "how the processor changes mode. (4) Why are registers banked per mode?"))
A(cm("Comment: for full marks name the entry event of <i>every</i> mode &mdash; reset/SWI "
     "&rarr; SVC is the one most students forget."))

build("ARM_Operating_Modes.pdf",
      "ARM Operating Modes &mdash; Exam Ready Notes",
      "Source: Module 5 &ldquo;The ARM Instruction Set&rdquo; p.13 (plus standard CPSR "
      "facts). Highlighted italic lines are <b>comments</b>.",
      modes_story,
      [Frame(MARGIN, top, COL_W, hgt, leftPadding=0, rightPadding=0, topPadding=0,
             bottomPadding=0),
       Frame(MARGIN + COL_W + GUTTER, top, COL_W, hgt, leftPadding=0, rightPadding=0,
             topPadding=0, bottomPadding=0)],
      "ARM Operating Modes \u2014 Exam Ready Notes")

# ======================================================================
#  PDF 2 : ARM REGISTER SETS  (full width, 1 page)
# ======================================================================
reg_story = []
A = reg_story.append

A(h1("1. Headline facts (module pp.14&ndash;17)"))
A(li("ARM has <b>37 registers, all 32 bits long</b>: <b>1</b> dedicated program counter + "
     "<b>1</b> CPSR + <b>5</b> dedicated saved program status registers + <b>30</b> "
     "general-purpose registers."))
A(li("The <b>current processor mode governs which bank is visible</b>: each mode sees its "
     "own r13 (sp) and r14 (lr) &mdash; FIQ also its own r8&ndash;r12 &mdash; while "
     "r0&ndash;r12, r15 (pc) and CPSR are common to all modes. Privileged modes "
     "(except System) additionally see their private <b>SPSR</b>."))
A(li("<b>System mode uses the User-mode register set</b> (module note, p.17)."))
A(li("Visible at any moment: 16 data registers (r0&ndash;r15) + CPSR (+ SPSR in an "
     "exception mode). The register file has <b>3 read ports</b>, so most instructions "
     "fetch all operands in one cycle &mdash; the RISC &ldquo;register-rich&rdquo; idea."))

A(h1("2. The register banks (organisation summary)"))
w7 = [FULL_W * x for x in (0.145, 0.155, 0.13, 0.13, 0.13, 0.155, 0.155)]
A(table(["Register", "User / System", "FIQ", "IRQ", "SVC", "Abort", "Undef"],
        [["r0&ndash;r7", "shared", "shared", "shared", "shared", "shared", "shared"],
         ["r8&ndash;r12", "shared", "<b>FIQ_r8&ndash;FIQ_r12</b>", "shared", "shared",
          "shared", "shared"],
         ["r13 (sp)", "SP_usr", "<b>SP_fiq</b>", "<b>SP_irq</b>", "<b>SP_svc</b>",
          "<b>SP_abt</b>", "<b>SP_und</b>"],
         ["r14 (lr)", "LR_usr", "<b>LR_fiq</b>", "<b>LR_irq</b>", "<b>LR_svc</b>",
          "<b>LR_abt</b>", "<b>LR_und</b>"],
         ["r15 (pc)", "shared", "shared", "shared", "shared", "shared", "shared"],
         ["CPSR", "shared", "shared", "shared", "shared", "shared", "shared"],
         ["SPSR", "&mdash;", "<b>SPSR_fiq</b>", "<b>SPSR_irq</b>", "<b>SPSR_svc</b>",
          "<b>SPSR_abt</b>", "<b>SPSR_und</b>"]],
        w7, center=list(range(1, 7))))
A(p("Bold = private (banked) copy. Count check: 17 shared (r0&ndash;r15 + CPSR) + 5 "
    "(FIQ r8&ndash;r12) + 5&times;(sp+lr) + 5&times;spsr = 17+5+10+5 = 37 registers."))

A(h1("3. Special function registers"))
w5 = [FULL_W * 0.13, FULL_W * 0.87]
A(table(["Register", "Role (module p.16)"],
        [["PC &mdash; r15", "Program counter. Any instruction with <b>PC as its destination "
                           "register is a program branch</b>."],
         ["LR &mdash; r14", "Link register. Saves a copy of PC when executing <b>BL</b> "
                           "(subroutine call) or on jumping to an exception/interrupt "
                           "routine; copied back to PC on return."],
         ["SP &mdash; r13", "Stack pointer. There is <b>no stack in the ARM architecture</b> "
                           "&mdash; R13 is merely <i>reserved</i> as the pointer for a "
                           "program-managed stack."],
         ["CPSR", "Current Program Status Register &mdash; holds the visible status: "
                  "flags <b>N Z C V</b>, interrupt disables I/F, T bit and <b>mode bits "
                  "M[4:0]</b>."],
         ["SPSR", "Saved Program Status Register &mdash; holds a copy of the previous CPSR "
                  "while an exception/interrupt runs; copied back to CPSR on return. "
                  "<b>Not available in User or System mode.</b>"]],
        w5))

A(h1("4. Comments &mdash; the &ldquo;why&rdquo; that earns marks"))
A(cm("Comment 1: banking is a <b>performance</b> feature. On an exception the hardware "
     "hands the new mode its own sp/lr/spsr, so nothing must be pushed to memory first "
     "&rarr; minimal interrupt latency; the same trick makes mode switches cheap."))
A(cm("Comment 2: FIQ gets <b>seven</b> private registers (r8&ndash;r14) &mdash; the most of "
     "any mode &mdash; because the fast interrupt must spend (almost) zero time saving "
     "context. IRQ gets only two (sp, lr)."))
A(cm("Comment 3: &ldquo;no hardware stack&rdquo; is a classic trick line: the architecture "
     "defines no PUSH/POP hardware; SP is a convention, and even PUSH/POP are just LDM/STM "
     "using r13. The stack is entirely software-managed."))
A(cm("Comment 4: link to pipelining &mdash; while an instruction executes, r15 is already "
     "two fetches ahead, which is why <b>PC reads as PC+8</b> in ARM state (PC+4 in "
     "Thumb)."))

A(h1("5. One-minute revision"))
A(p("<b>Numbers:</b> 37 registers / 32-bit &middot; 30 GPRs &middot; 5 SPSRs &middot; FIQ "
    "banks r8&ndash;r14 &middot; others bank r13/r14(+SPSR) &middot; no SPSR in User or "
    "System &middot; System = User&rsquo;s register set."))
A(p("<b>Likely questions:</b> (1) Describe the ARM register organisation with the banking "
    "table. (2) Explain PC, LR, SP, CPSR and SPSR. (3) Why does ARM bank registers? "
    "(4) How many registers are visible in User mode and why?"))
A(cm("Comment: always draw the bank table (section 2) in the exam &mdash; it converts a "
     "prose answer into a diagram and scores full marks."))

build("ARM_Register_Sets.pdf",
      "ARM Register Sets &mdash; Exam Ready Notes",
      "Source: Module 5 &ldquo;The ARM Instruction Set&rdquo; pp.14&ndash;17. Highlighted "
      "italic lines are <b>comments</b>.",
      reg_story,
      [Frame(MARGIN, top, FULL_W, hgt, leftPadding=0, rightPadding=0, topPadding=0,
             bottomPadding=0)],
      "ARM Register Sets \u2014 Exam Ready Notes")
