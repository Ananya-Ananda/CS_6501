# Symbolic Fuzzing Tools and Benchmark Usage Guide

A guide for setting up and running benchmarks using **Fuzzy-SAT**, **AFL++ w/QSYM**, and **LibKluzzer**. The benchmarks include `objdump`, `readelf`, `advmng`, and `optipng`. Each tool's setup and benchmark-specific commands are detailed below.

---

## Directory Structure

Ensure the following directory structure is in place:

benchmarks/ # Contains benchmark files (e.g., objdump.smt2, readelf.smt2, etc.) 
seeds/ # Contains seed files (e.g., small_exec.elf)
output/ # Directory to store outputs for each tool
tools/ 


---

## 1. Fuzzy-SAT

### Setup

1. Clone the repository and build the solver:
   ```bash
   git clone https://github.com/path/to/fuzzy-sat.git
   cd fuzzy-sat
   make
   
### Commands for Benchmarks
**objdump**
   ```bash
   time ./fuzzy-solver \
     --query ../../../../benchmarks/objdump.smt2 \
     --seed ../../../../seeds/small_exec.elf \
     --out ../../../../output/fuzzy-sat/objdump.smt2 \
     --dsat --dproofs
   ```

**readelf**
   ```bash
   time ./fuzzy-solver \
     --query ../../../../benchmarks/readelf.smt2 \
     --seed ../../../../seeds/small_exec.elf \
     --out ../../../../output/fuzzy-sat/readelf.smt2 \
     --dsat --dproofs
   ```

**advmng**
   ```bash
   time ./fuzzy-solver \
     --query ../../../../benchmarks/advmng.smt2 \
     --seed ../../../../seeds/small_exec.elf \
     --out ../../../../output/fuzzy-sat/advmng.smt2 \
     --dsat --dproofs
   ```

**optipng**
   ```bash
   time ./fuzzy-solver \
     --query ../../../../benchmarks/optipng.smt2 \
     --seed ../../../../seeds/small_exec.elf \
     --out ../../../../output/fuzzy-sat/optipng.smt2 \
     --dsat --dproofs
   ```

## 2. AFL++ w/ QSYM

### Setup
Install AFL++ dependencies:
   ```bash
   sudo apt-get update
   sudo apt-get install build-essential clang llvm
   ```
Clone and build AFL++:
   ```bash
   git clone https://github.com/AFLplusplus/AFLplusplus.git
   cd AFLplusplus
   make distrib
   sudo make install
   ```
Install QSYM dependencies:
   ```bash
   sudo apt-get install python3-pip
   pip3 install -r requirements.txt
   ```
Clone the QSYM repository:
   ```bash
   git clone https://github.com/sslab-gatech/qsym.git
   cd qsym
   make
   ```
### Commands for Benchmarks
**objdump**
   ```bash
   time ./qsym-afl \
     -Q \
     -i ../../benchmarks/objdump/ \
     -o ../../output/qsym/objdump/ \
     -- ../../seeds/small_exec.elf

   ```

**readelf**
   ```bash
   time ./qsym-afl \
     -Q \
     -i ../../benchmarks/readelf/ \
     -o ../../output/qsym/readelf/ \
     -- ../../seeds/small_exec.elf

   ```

**advmng**
   ```bash
   time afl-fuzz \
     -Q \
     -i ../../benchmarks/advmng/ \
     -o ../../output/afl++/advmng/ \
     -- ../../seeds/small_exec.elf

   ```

**optipng**
   ```bash
   time ./qsym-afl \
     -Q \
     -i ../../benchmarks/optipng/ \
     -o ../../output/qsym/optipng/ \
     -- ../../seeds/small_exec.elf

   ```
## 3. LibKluzzer

### Setup
Clone the LibKluzzer repository:
```bash
git clone https://github.com/path/to/LibKluzzer.git
cd LibKluzzer
make
```
### Commands for Benchmarks
**objdump**
```bash
./bin/LibKluzzer ../../benchmarks/objdump.c
```
**readelf**
```bash
./bin/LibKluzzer ../../benchmarks/readelf.c
```
**advmng**
```bash
./bin/LibKluzzer ../../benchmarks/advmng.c
```
**optipng**
```bash
./bin/LibKluzzer ../../benchmarks/optipng.c
```
