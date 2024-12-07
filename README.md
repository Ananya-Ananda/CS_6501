# CS_6501
## path from tools that has fuzzy-solver to benchmarks:
../../../../benchmarks

## fuzzy-sat -> objdump.smt2
time ./fuzzy-solver --query ../../../../benchmarks/objdump.smt2 --seed ../../../../seeds/small_exec.elf --out ../../../../output/fuzzy-sat/objdump.smt2 --dsat --dproofs

time ./fuzzy-solver --query ../../../../benchmarks/objdump.smt2 --seed ../../../../seeds/small_exec.elf --out ../../../../output/fuzzy-sat/objdump.smt2 --dsat --dproofs > ../../../../output/fuzzy-sat/objdump_output.txt 2>&1

## fuzzy-sat -> readelf.smt2
time ./fuzzy-solver --query ../../../../benchmarks/readelf.smt2 --seed ../../../../seeds/small_exec.elf --out ../../../../output/fuzzy-sat/readelf.smt2 --dsat --dproofs
