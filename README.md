# CS_6501
## FUZZY-SAT

## fuzzy-sat -> objdump.smt2
time ./fuzzy-solver --query ../../../../benchmarks/objdump.smt2 --seed ../../../../seeds/small_exec.elf --out ../../../../output/fuzzy-sat/objdump.smt2 --dsat --dproofs

## fuzzy-sat -> readelf.smt2
time ./fuzzy-solver --query ../../../../benchmarks/readelf.smt2 --seed ../../../../seeds/small_exec.elf --out ../../../../output/fuzzy-sat/readelf.smt2 --dsat --dproofs

## fuzzy sat ->

## AFL++ QSYM 
### install dependencies


### afl-fuzz
time ./afl-fuzz -Q -i ../../benchmarks/ -o ../../output/afl++/ -- ../../seeds/small_exec.elf -q ../../benchmarks/readelf.c

time ./qemuafl -Q -i ../../benchmarks/ -o ../../output/afl++/ -- ../../seeds/small_exec.elf -q ../../benchmarks/readelf.smt2

## LibKluzzer
## readelf.c

./bin/LibKluzzer ../../benchmarks/binutils-2.39/binutils/readelf.c

./binutils-2.39/binutils

../../benchmarks/test.c

### afl
afl-fuzz -i ../../benchmarks/in/ -o ../../output/afl++/testc -- ./testc

afl-clang-fast -o readelf readelf.c
