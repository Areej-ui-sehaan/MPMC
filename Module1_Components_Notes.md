# ECE3004 – Microprocessors & Microcontrollers
## Module 1: List of Components (Exam Notes)

Source: *Module 1 mp.pdf* (Dr. Nella Anveshkumar)

---

## 1. Computer System Components (the 4 main blocks)

| # | Component | Function |
|---|-----------|----------|
| 1 | **Memory** | Stores instructions and data |
| 2 | **Input/Output (I/O)** | Used to input and output instructions and data; called *peripherals* |
| 3 | **Arithmetic and Logic Unit (ALU)** | Performs arithmetic and logical operations |
| 4 | **Control Unit (CU)** | Coordinates the operation of the computer |

- **ALU:** arithmetic (addition, subtraction); logical (AND, OR, XOR, SHIFT, ROTATE)
- **CU:** acts as the "brain" of the computer system

### System Interconnection – The Bus
- **Bus** = a group of lines used to transfer bits between the microprocessor and other components.
- Only **one transmitter at a time**; only the **addressed device** can respond.
- **Types of bus:**
  1. **Address bus** – carries memory/I/O addresses
  2. **Data bus** – carries data
  3. **Control bus** – carries control signals

---

## 2. CPU Components

### 2.1 Registers
- Hold data, instructions, or other items.
- Come in various sizes.
- **Program Counter (PC)** and **Memory Address Register (MAR)** must be the **same width as the address bus**.
- Registers that hold data must be the **same width as memory words**.

### 2.2 Control Unit (inside CPU)
- Generates the **control signals** needed to execute an instruction.
- Connects registers to the bus.
- Controls data flow between the CPU and peripherals (including memory).
- Provides **status, control and timing signals** required by memory and I/O devices.
- All its actions are tied to **decoding and executing instructions** (fetch–decode–execute cycle).

### 2.3 Arithmetic and Logic Unit (inside CPU)
- Executes arithmetic and logical operations.
- **Accumulator** = a special **8-bit register** associated with the ALU.
  - In the **8085**, register **A** is the accumulator.
- Accumulator is one source operand and one input to the ALU.
- The **final result** of an arithmetic/logic operation is placed in the accumulator.

**Operations performed by the ALU:**
- Addition
- Subtraction
- Logical AND
- Logical OR
- Logical EXCLUSIVE OR (XOR)
- Complement (logical NOT)
- Increment (add 1)
- Decrement (subtract 1)
- Left shift, Rotate Left, Rotate Right
- Clear, etc.

---

## 3. Microprocessor – Three Segments
A microprocessor is a semiconductor device made of electronic logic circuits, capable of computing and transporting data. It is divided into:
1. **Arithmetic and Logic Unit (ALU)**
2. **Register Unit**
3. **Control Unit**

## 4. Memory Concept (Von Neumann style)
- Data and instructions are stored in a **single set of read-write memory**.
- Memory is addressed by **memory address**, regardless of the type of data stored.
- Execution is **sequential** unless explicitly altered (e.g., by a jump).

## 5. CPU Performance Metrics
- Short response time for a given piece of work
- High throughput (rate of processing work)
- Low utilization of computing resource(s)
- High availability of the system/application
- Fast (or highly compact) data compression and decompression
- High bandwidth
- Short data transmission time

---

## 6. Development Tools (Software)

| Tool | Purpose |
|------|---------|
| **Assembler** | Translates assembly language into machine code (object code) |
| **Compiler** | Translates high-level language (e.g., C, Pascal, BASIC) into assembly/object code |
| **Linker** | Combines object files and libraries into one executable (.exe); performs symbol resolution and relocation |
| **Loader** | Loads object code into main memory, allocates memory, prepares program for execution |
| **Locator** | Assigns the specific addresses where code segments are loaded into memory |
| **Debugger** | Loads code into memory, runs it, sets breakpoints, views/changes registers and memory, single-steps |
| **Simulator** | Instruction-set simulator; runs the program in software instead of on the processor (slower) |
| **Libraries** | Pre-written code reused by programs |

## 7. Development Tools (Hardware)

| Tool | Purpose |
|------|---------|
| **In-Circuit Emulator (ICE)** | Hardware device that replaces/augments the processor to debug embedded software (single-step, breakpoints) |
| **Emulator** | Mix of hardware and software used to test/debug the hardware and software of an external system (e.g., prototype) |
| **Logic Analyzer** | Captures and displays multiple digital signals to analyse hardware behaviour |

---

## 8. Key Definitions (Quick Recall)
- **Linker:** combines object files and libraries into an executable; resolves symbols.
- **Relocation:** assigning load addresses to position-dependent code/data and adjusting it accordingly.
- **Loader:** reallocates code to physical RAM addresses and loads it for execution.
- **Locator:** fixes the specific addresses of object-code segments in memory.
- **Debugger:** a program to load, run and troubleshoot object code.
- **Emulator:** hardware + software used to test an external system.
- **ICE:** hardware device used to debug embedded system software.

## 9. Assembly vs High-Level Language (Comparison)

| Feature | Assembly Language | High-Level Language |
|---------|-------------------|---------------------|
| Portability | Program for one processor won't run on another | Runs independently of processor type |
| Performance / accuracy | Better | Lower |
| Ease of understanding/debugging | Harder | Easier |
| Code size | Smaller; faster execution | Larger; slower execution |
| Hardware access | Can directly access hardware actions and physical addresses | Needs no knowledge of processor registers |
| Bit manipulation | Easier | Harder |
| Translator | **Assembler** | **Compiler** |

- **Machine language** example: `7E` (`0111 1110`) = **MOV A, M** in assembly.
- Assembly and machine language are both **low-level languages**.
- One high-level statement expands into many assembly instructions.

**Program levels:** Machine language (binary / hex / machine or object code) → Assembly language (mnemonics + assembler) → High-level language (Pascal, BASIC, C + compiler).

---

## 10. Intel Microprocessor Family – Component/Spec Summary

| Processor | Year | Bits | Key Points |
|-----------|------|------|------------|
| 4004 | 1971 | 4-bit | 1st Intel µP, 1st generation, 2,300 transistors, 740 KHz, 4 KB memory, PMOS |
| 4040 | 1974 | 4-bit | 4-bit µP |
| 8008 | 1972 | 8-bit | 1st 8-bit µP, 500 KHz, 16 KB memory, PMOS, slow |
| 8080 | 1974 | 8-bit | 6,000 transistors, 2 MHz, 64 KB, NMOS, needed 3 power supplies |
| 8085 | 1976 | 8-bit | Data bus 8-bit, address bus 16-bit, 3 MHz, 6,500 transistors, 246 instructions, 64 KB, single +5 V supply |
| 8086 | 1978 | 16-bit | 1st 16-bit µP; data bus 16-bit, address bus 20-bit; 1 MB memory; 29,000 transistors; HMOS; 4.77/8/10 MHz |
| 8088 | 1979 | 16-bit | Cheaper 8086 with 8-bit external bus; used in IBM's first PC |
| 80186 / 80188 | 1982 | 16-bit | Added interrupt controller, clock generator, local bus controller, counters (80188: 8-bit external bus) |
| 80286 | 1982 | 16-bit | Data bus 16-bit, address bus 24-bit; 16 MB memory; 134,000 transistors |
| 80386 | 1986 | 32-bit | 1st 32-bit µP; 32-bit data and address bus; 4 GB memory; 275,000 transistors; DX, SX, SL versions |
| 80486 | 1989 | 32-bit | 1.2 million transistors; 8 KB cache introduced; DX, SX, DX2, SL, DX4 |
| Pentium | 1993 | 32-bit | Originally named 80586; 66 MHz; 110 MIPS; 8 KB instruction + 8 KB data cache |
| Pentium Pro | 1995 | 32-bit | 21 million transistors; 256 KB L2 cache; mainly for servers |
| Pentium II | 1997 | 32-bit | 233–500 MHz; 333 MIPS; MMX support; L2 cache and processor on one circuit |
| Pentium II Xeon | 1998 | 32-bit | For servers; 400–450 MHz; L1 32 KB, L2 512 KB/1 MB/2 MB |
| Pentium III | 1999 | 32-bit | 500 MHz–1.4 GHz; 9.5 million transistors |
| Pentium IV | 2000 | 32-bit | 1.3–3.8 GHz; L1 32 KB, L2 256 KB; 42 million transistors; aluminium → copper interconnects |
| Dual Core | 2006 | 32/64-bit | Two cores; each has own internal bus and L1 cache; share external bus and L2 cache; SMT support |
| Core 2 | 2006 | 64-bit | 1.2–3 GHz; 291 million transistors; 64 KB L1 per core, 4 MB L2; versions: Duo, Quad, Extreme |
| Core i3 | 2010 | 64-bit | 2 physical cores; 2.93–3.33 GHz; 781 million transistors; 64 KB L1/core, 512 KB L2, 4 MB L3 |
| Core i5 | 2009 | 64-bit | 4 physical cores; 2.40–3.60 GHz; 781 million transistors; 64 KB L1/core, 256 KB L2, 8 MB L3 |
| Core i7 | 2008 | 64-bit | 4 physical cores; 2.66–3.33 GHz; 230 billion transistors (as stated in PDF); 64 KB L1/core, 256 KB L2, 8 MB L3 |
| Core i9 | 2017 | 64-bit | 10 physical cores; 3.33–5.2 GHz; 430 billion transistors (as stated in PDF); 64 KB L1/core, 1 MB L2/core, 13.75 MB L3 |

**Generations:** 4-bit → 8-bit → 16-bit → 32-bit → 64-bit.

---

## 11. Important Terms
- **Accumulator:** 8-bit special register tied to the ALU; holds results.
- **Bus:** shared set of lines (address, data, control).
- **Cache:** fast memory between CPU and main memory (L1, L2, L3).
- **SMT (Simultaneous Multi-Threading):** runs multiple threads on one core at the same time (e.g., Adobe Photoshop).
- **MMX:** multimedia instruction extension (Pentium II).
- **ICE:** In-Circuit Emulator.
- **Peripherals:** external I/O devices connected to the system.

---

## 12. Quick Revision Checklist
- [ ] 4 computer components: Memory, I/O, ALU, Control Unit
- [ ] 3 bus types: Address, Data, Control
- [ ] 3 microprocessor segments: ALU, Register Unit, Control Unit
- [ ] Accumulator = 8-bit register, result stored here
- [ ] 8085: 8-bit data bus, 16-bit address bus, 246 instructions, 64 KB
- [ ] 8086: 16-bit data, 20-bit address, 1 MB
- [ ] 80386: first 32-bit µP, 4 GB
- [ ] Software tools: Assembler, Compiler, Linker, Loader, Locator, Debugger, Simulator
- [ ] Hardware tools: ICE, Emulator, Logic Analyzer
- [ ] Assembler → assembly; Compiler → high-level language
