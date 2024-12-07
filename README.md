# CS_6501
path from tools that has fuzzy-solver to benchmarks:
../../../../benchmarks

time ./fuzzy-solver --query ../../../../benchmarks/objdump.smt2 --seed ../../../../seeds/small_exec.elf --out ../../../../output/fuzzy-sat/objdump.smt2 --dsat --dproofs

time ./fuzzy-solver --query ../../../../benchmarks/objdump.smt2 --seed ../../../../seeds/small_exec.elf --out ../../../../output/fuzzy-sat/objdump.smt2 --dsat --dproofs > ../../../../output/fuzzy-sat/objdump_output.txt 2>&1
