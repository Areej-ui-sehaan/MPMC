# ECE3004 – Microprocessor vs Microcontroller: Metrics & Comparison

Source: *Module 1 mp.pdf* (Dr. Nella Anveshkumar), slides on performance metrics, differentiating features, and microprocessor vs microcontroller comparison.

---

## 1. Performance Metrics of a CPU (from PDF)

| Metric | Meaning |
|--------|---------|
| Short response time | Time taken to complete a given piece of work is small |
| High throughput | Rate at which work is processed is high |
| Low utilization of resources | Computing resources are not overloaded |
| High availability | System/application is available for use most of the time |
| Fast (or compact) data compression & decompression | Efficient handling of data encoding/decoding |
| High bandwidth | Large amount of data can be transferred per unit time |
| Short data transmission time | Data moves quickly between components |

---

## 2. Key Hardware Metrics (Intel family data from the PDF)

| Metric | What it measures | Example from PDF |
|--------|------------------|------------------|
| Bit width (word size) | Size of data processed at once | 4004 = 4-bit, 8085 = 8-bit, 8086 = 16-bit, 80386 = 32-bit, Core 2 = 64-bit |
| Data bus width | Bits transferred per cycle | 8085 = 8-bit, 8086 = 16-bit, 80386 = 32-bit |
| Address bus width | Determines addressable memory | 8085 = 16-bit (64 KB), 8086 = 20-bit (1 MB), 80286 = 24-bit (16 MB), 80386 = 32-bit (4 GB) |
| Clock speed | Operations (clock cycles) per second | 4004 = 740 kHz, 8085 = 3 MHz, 8086 = 4.77–10 MHz, Core i9 = 3.33–5.2 GHz |
| Instructions per second | Execution rate | 8085 ≈ 7,69,230; 8086 = 2.5 million; Pentium = 110 million; Pentium II = 333 million |
| Transistor count | Circuit complexity | 4004 = 2,300; 8085 = 6,500; 8086 = 29,000; Pentium IV = 42 million |
| Cache memory | Fast memory close to CPU | Pentium = 8 KB I + 8 KB D; Core 2 = 64 KB L1/core + 4 MB L2 |
| Number of cores | Parallel processing units | Dual core = 2; Core i3 = 2; Core i5/i7 = 4; Core i9 = 10 |
| Technology | Fabrication process | 4004 = PMOS; 8080 = NMOS; 8086 = HMOS |
| Number of instructions | Instruction set size | 8008 = 48; 8085 = 246; 8086 = 22,000 (as stated in PDF) |

> Note: the PDF gives 22,000 instructions for the 8086, which is the value stated in the slides. Standard textbooks usually quote far fewer; use the figure your lecturer uses.

---

## 3. Differentiating Features – Microprocessor vs Microcontroller (from PDF)

| Feature | Microprocessor (µP) | Microcontroller (µC) |
|---------|---------------------|----------------------|
| Function | Processes the **general** task only | Both **processes and controls** the **specific** task |
| Memory | **No** in-built memory | **In-built** ROM and RAM |
| Application | General purpose (PC, modems, calculators, LED display boards) | Specific purpose (A/C, washing machine, home automation) |
| Complexity | More complex; large number of instructions | Less complex; fewer instructions |
| Cost | High (design time is more) | Low (design time is less) |
| Architecture | **Von Neumann** (program and data in the same memory) | **Harvard** (program and data in different memories) |
| Example | 8085, 8086 | 8051 |

---

## 4. Detailed Comparison (from PDF)

| Aspect | Microprocessor | Microcontroller |
|--------|----------------|-----------------|
| Memory | Needs external memory & storage; flexible | On-chip memory (RAM, ROM, EEPROM) |
| Peripherals | Needs additional parts via external bus; ideal for complex, powerful applications | Integrated peripherals: SPI, UART, RTI, ADC for direct hardware control |
| Clock speed | Fast (GHz) for heavy-duty tasks | kHz – MHz; efficient for specific tasks |
| Power consumption | High; no low-power option | Low; power-saving options available |
| Connectivity | Handles high-speed data transfer | Supports low-to-moderate speed communication (I2C, SPI, UART) |
| Operating system | Needs a full-fledged OS (Linux, Windows) | OS optional (no-OS or light-weight RTOS) |
| Use case | Generic computing; highly complex, capacity-heavy systems | Compact systems; battery-powered; logic-processing devices |
| Cost | Higher – suited to performance-driven applications | Lower – economical for mass production |

---

## 5. Summary: Which Metric Favours Which Device?

| Metric | Microprocessor | Microcontroller |
|--------|----------------|-----------------|
| Speed / throughput | Higher | Lower |
| Power consumption | Higher | Lower |
| Cost | Higher | Lower |
| Integrated memory & I/O | No (external) | Yes (on-chip) |
| Flexibility / expandability | High | Limited |
| Real-time control of hardware | Needs extra chips | Built in |

---

## 6. Quick Exam Points
- **µP** = CPU only; **µC** = CPU + memory + I/O on one chip.
- **µP** uses **Von Neumann**; **µC** uses **Harvard** architecture.
- **µP** examples: 8085, 8086. **µC** example: 8051.
- Performance metrics: response time, throughput, utilization, availability, bandwidth, transmission time.
- Hardware metrics: bit width, bus widths, clock speed, instructions per second, transistor count, cache.
- Higher clock and more transistors → more performance, but also more power and cost.
