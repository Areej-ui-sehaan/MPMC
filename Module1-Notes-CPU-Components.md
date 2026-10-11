# ECE3004 · MPMC — Module 1: Computer System & CPU Components
*Last-minute revision sheet · Source: "Module 1 mp.pdf" (Dr. Nella Anveshkumar) · ⭐ = expected in exam*

## 1. QUICK-REFERENCE TABLE

| Component | Location | Main Function | Key Detail |
|---|---|---|---|
| **Memory** | System (outside µP) | Stores instructions and data | Read-write; single set (Von Neumann) |
| **I/O (Peripherals)** | System (external) | Input/output instructions and data | ⭐ "Peripherals" is the other name for I/O |
| **ALU** | CPU | Arithmetic + logical operations | Add, SUB, AND, OR, XOR, SHIFT, ROTATE |
| **Control Unit** | CPU (also system-level) | Coordinates operation of the computer | ⭐ "Brain"; issues status/control/timing signals |
| **Bus** | Interconnection | Group of lines transferring bits | ⭐ One transmitter at a time; only addressed device responds |
| **Registers** | CPU | Hold data, instructions, or other items | PC/MAR width = address bus; data reg width = memory word |
| **Accumulator** | CPU, tied to ALU | Operand source + result destination | ⭐ Special **8-bit**; is Register **A** in 8085 |

---

## 2. TOPIC 1 — COMPUTER SYSTEM COMPONENTS

- **Memory** — stores instructions and data. ⭐
- **Input/Output** — also called **peripherals**; input *and* output of instructions/data.
- **ALU** — arithmetic: **addition**, **subtraction**.
- **ALU** — logical: **AND**, **OR**, **XOR**, **SHIFT**, **ROTATE**. ⭐
- **Control Unit** — **coordinates** the operation of the computer.
- **Bus** — a **group of lines** transferring bits between µP and other components.
- Bus is the communication path between parts of the computer.
- ⭐ **Only one transmitter at a time**; **only the addressed device responds**.
- ⭐ Bus types (3): **Address Bus**, **Data Bus**, **Control Signals Bus**.

---

## 3. TOPIC 2 — CPU COMPONENTS

### 3.1 Registers
- Hold **data**, **instructions**, or other items; come in **various sizes**.
- ⭐ **Program Counter** and **Memory Address Register** → same width as **address bus**.
- ⭐ Registers holding **data** → same width as **memory words**.

### 3.2 Control Unit (CPU level)
- Generates **control signals** needed to **execute an instruction**.
- **Connects registers to the bus**.
- Controls **data flow between CPU and peripherals** (memory included).
- Provides **status, control and timing signals** for memory and I/O devices. ⭐
- ⭐ Acts as the **brain** of the computer system.
- All actions tied to **decoding and execution** — **fetch** and **execute** cycles.

### 3.3 ALU (CPU level)
- **Executes arithmetic and logical operations**.
- **Accumulator** = special **8-bit** register associated with the ALU. ⭐
- ⭐ In **8085**, register **'A'** is the accumulator.
- ⭐ **Source of one operand** of an arithmetic/logical operation.
- **Serves as one input to the ALU**.
- ⭐ **Final result** of any op is **placed in the accumulator**.

---

## 4. TOPIC 3 — ALU OPERATIONS (complete list)

| Arithmetic Operations | Logical Operations |
|---|---|
| **Addition** | **Logical AND** |
| **Subtraction** | **Logical OR** |
| **Increment** (add 1) | **Logical EXCLUSIVE OR** (XOR) |
| **Decrement** (subtract 1) | **Complement** (logical NOT) |
| **Left Shift** | **Rotate Left** |
| — | **Rotate Right** |
| — | **Clear** |

- ⭐ ALU slide lists **12 operations** — write all 12 when asked "ALU operations".
- ⭐ Slide 2 (ALU summary) groups **SHIFT** and **ROTATE** under *logical* operations.
- ⭐ Table above = **ALU slide (p.7)** split: shift→arithmetic, rotate/clear→logical.

---

## 5. TOPIC 4 — MICROPROCESSOR (µP)

- ⭐ **µP** = a **semiconductor device** consisting of **electronic logic circuits**.
- Manufactured using various **fabrication schemes**.
- Capable of **performing computing functions**.
- Capable of **transporting data/information**.
- ⭐ Divided into **3 segments**: **ALU**, **Register Unit**, **Control Unit**.

> System view = 5 components (Memory, I/O, ALU, Control Unit, Bus) · µP view = 3 segments (ALU, Register Unit, Control Unit).

---

## 6. TOPIC 5 — PERFORMANCE METRICS OF CPU

- **Short response time** for a given piece of work.
- ⭐ **High throughput** — the **rate of processing work**.
- ⭐ **Low utilization** of computing resource(s).
- **High availability** of the computing system or application.
- **Fast / highly compact** data **compression and decompression**.
- **High bandwidth**.
- **Short data transmission time**.

---

## 7. TOPIC 6 — MEMORY MODEL (Von Neumann principle)

- ⭐ **Data and instructions** stored in a **single set of read-write memory**.
- Memory contents addressed by **memory address**, **without regard to type of data**.
- ⭐ **Execution is sequential** — one instruction to the next — **unless explicitly altered**.

---

## 8. TOP 10 EXAM QUESTIONS

**Q1. List the components of a computer system with one line each.**
**Memory** stores instructions and data; **I/O (peripherals)** input and output them. **ALU** does arithmetic/logic, **Control Unit** coordinates everything, and the **Bus** carries bits between all parts.

**Q2. What is an accumulator? Why is it called special?**
It is a special **8-bit** register bound to the **ALU** (register **A** in the **8085**). It supplies one **operand**, acts as **one ALU input**, and holds the **final result** of every arithmetic/logical operation.

**Q3. State the Von Neumann principle.**
Data and instructions live in **one read-write memory**, addressed purely by **memory address** with no regard to data type. **Execution is sequential** unless explicitly altered by a jump/branch.

**Q4. Why must PC and MAR match the address bus width?**
The **Program Counter** and **Memory Address Register** must hold a **complete memory address**, so their width equals the **address bus**. Data-holding registers instead match the **memory word** size.

**Q5. Define a bus and give its types plus the bus-sharing rule.**
A **bus** is a group of lines transferring bits between the µP and other components. Types: **Address**, **Data**, **Control Signals**. Only **one transmitter at a time**, and only the **addressed device** responds.

**Q6. Classify: ADD, SUB, AND, OR, XOR, complement, increment, decrement, shift, rotate, clear.**
**Arithmetic:** addition, subtraction, increment, decrement, **left shift** (per the ALU list). **Logical:** AND, OR, XOR, complement (NOT), **rotate left**, **rotate right**, **clear**.

**Q7. What is the role of the Control Unit during instruction execution?**
It generates the **control signals** needed to execute an instruction and **connects the registers to the bus**. It also supplies **status, control and timing** signals to memory and I/O — hence "brain" of the system.

**Q8. Enlist the performance metrics of a CPU.**
Short **response time**, high **throughput**, low **resource utilization**, high **availability**. Add fast **compression/decompression**, high **bandwidth**, and short **data transmission time**.

**Q9. Define microprocessor and name its three segments.**
A **µP** is a semiconductor device of electronic logic circuits, built by various fabrication schemes, that **computes** and **transports data**. Segments: **ALU**, **Register Unit**, **Control Unit**.

**Q10. Differentiate CPU components from computer system components.**
CPU holds **registers**, **control unit** and **ALU** (3 segments of a µP). The **computer system** adds **memory**, **I/O/peripherals** and the **bus** that interconnects them all.

---

### One-line recall card
5 system components · 3 buses · 3 µP segments · 12 ALU ops · 7 CPU metrics · 3 Von Neumann rules · **8085 Reg A = 8-bit accumulator**.
