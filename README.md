# Symbolic Fuzzing Tools and Benchmark Usage Guide

This README provides a comprehensive guide for setting up and running benchmarks using **Fuzzy-SAT**, **AFL++**, **QSYM**, and **LibKluzzer**. The benchmarks include `objdump`, `readelf`, `advmng`, and `optipng`. Each tool's setup and benchmark-specific commands are detailed below.

---

## Directory Structure

Ensure the following directory structure is in place:

benchmarks/ # Contains benchmark files (e.g., objdump.smt2, readelf.smt2, etc.) seeds/ # Contains seed files (e.g., small_exec.elf). output/ # Directory to store outputs for each tool.


---

## 1. Fuzzy-SAT

### Setup

1. Clone the repository and build the solver:
   ```bash
   git clone https://github.com/path/to/fuzzy-sat.git
   cd fuzzy-sat
   make
Commands for Benchmarks
objdump

time ./fuzzy-solver \
  --query ../../../../benchmarks/objdump.smt2 \
  --seed ../../../../seeds/small_exec.elf \
  --out ../../../../output/fuzzy-sat/objdump.smt2 \
  --dsat --dproofs
readelf

time ./fuzzy-solver \
  --query ../../../../benchmarks/readelf.smt2 \
  --seed ../../../../seeds/small_exec.elf \
  --out ../../../../output/fuzzy-sat/readelf.smt2 \
  --dsat --dproofs
advmng

time ./fuzzy-solver \
  --query ../../../../benchmarks/advmng.smt2 \
  --seed ../../../../seeds/small_exec.elf \
  --out ../../../../output/fuzzy-sat/advmng.smt2 \
  --dsat --dproofs
optipng

time ./fuzzy-solver \
  --query ../../../../benchmarks/optipng.smt2 \
  --seed ../../../../seeds/small_exec.elf \
  --out ../../../../output/fuzzy-sat/optipng.smt2 \
  --dsat --dproofs
2. AFL++

Setup
Install AFL++ dependencies:
sudo apt-get update
sudo apt-get install build-essential clang llvm
Clone and build AFL++:
git clone https://github.com/AFLplusplus/AFLplusplus.git
cd AFLplusplus
make
sudo make install
Commands for Benchmarks
objdump

time afl-fuzz \
  -Q \
  -i ../../benchmarks/objdump/ \
  -o ../../output/afl++/objdump/ \
  -- ../../seeds/small_exec.elf
readelf

time afl-fuzz \
  -Q \
  -i ../../benchmarks/readelf/ \
  -o ../../output/afl++/readelf/ \
  -- ../../seeds/small_exec.elf
advmng

time afl-fuzz \
  -Q \
  -i ../../benchmarks/advmng/ \
  -o ../../output/afl++/advmng/ \
  -- ../../seeds/small_exec.elf
optipng

time afl-fuzz \
  -Q \
  -i ../../benchmarks/optipng/ \
  -o ../../output/afl++/optipng/ \
  -- ../../seeds/small_exec.elf
3. QSYM

Setup
Install QSYM dependencies:
sudo apt-get install python3-pip
pip3 install -r requirements.txt
Clone the QSYM repository:
git clone https://github.com/sslab-gatech/qsym.git
cd qsym
make
Commands for Benchmarks
objdump

time ./qsym-afl \
  -Q \
  -i ../../benchmarks/objdump/ \
  -o ../../output/qsym/objdump/ \
  -- ../../seeds/small_exec.elf
readelf

time ./qsym-afl \
  -Q \
  -i ../../benchmarks/readelf/ \
  -o ../../output/qsym/readelf/ \
  -- ../../seeds/small_exec.elf
advmng

time ./qsym-afl \
  -Q \
  -i ../../benchmarks/advmng/ \
  -o ../../output/qsym/advmng/ \
  -- ../../seeds/small_exec.elf
optipng

time ./qsym-afl \
  -Q \
  -i ../../benchmarks/optipng/ \
  -o ../../output/qsym/optipng/ \
  -- ../../seeds/small_exec.elf
4. LibKluzzer

Setup
Clone the LibKluzzer repository:
git clone https://github.com/path/to/LibKluzzer.git
cd LibKluzzer
make
Commands for Benchmarks
objdump

./bin/LibKluzzer ../../benchmarks/objdump.c
readelf

./bin/LibKluzzer ../../benchmarks/readelf.c
advmng

./bin/LibKluzzer ../../benchmarks/advmng.c
optipng

./bin/LibKluzzer ../../benchmarks/optipng.c
Output Directory Structure

Outputs will be organized as follows:

output/
├── afl++/
│   ├── objdump/
│   ├── readelf/
│   ├── advmng/
│   └── optipng/
├── fuzzy-sat/
│   ├── objdump.smt2
│   ├── readelf.smt2
│   ├── advmng.smt2
│   └── optipng.smt2
├── qsym/
│   ├── objdump/
│   ├── readelf/
│   ├── advmng/
│   └── optipng/
└── LibKluzzer/
    ├── objdump_output/
    ├── readelf_output/
    ├── advmng_output/
    └── optipng_output/
