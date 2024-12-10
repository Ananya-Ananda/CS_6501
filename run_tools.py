import os
import subprocess
from pathlib import Path

# Define the tools and their configurations
TOOLS = {
    "FuzzySat": "./tools/fuzzy-sat/bin/tools/fuzzy-sat",
    "LibKluzzer": "./tools/libkluzzer",
    "AFL++_QSYM": "./tools/AFLplusplus",
}

# Define the benchmarks and their directories
BENCHMARKS = {
    "advmng": "./benchmarks/advmng.smt2",
    "bloaty": "./benchmarks/bloaty.smt2",
    "objdump": "./benchmarks/objdump.smt2",
    "optipng": "./benchmarks/optipng.smt2",
    "readelf": "./benchmarks/bloaty.smt2",
}

SEEDS_DIR = Path("./seeds/")
RESULTS_DIR = Path("./output/")

def run_tool(tool_name, tool_path, benchmark_name, benchmark_path, seeds_dir, output_dir):
    # Run each tool on benchmarks w/ corresponding seeds

    output_dir.mkdir(parents=True, exist_ok=True) 
    
    command = [
        tool_path,                 
        "-i", str(seeds_dir),      
        "-o", str(output_dir),    
        "--", str(benchmark_path) 
    ]
    
    print(f"Running {tool_name} on {benchmark_name}...")
    try:
        subprocess.run(command, check=True)
        print(f"{tool_name} completed for {benchmark_name}. Results saved in {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {tool_name} on {benchmark_name}: {e}")
        
def main():
    for tool_name, tool_path in TOOLS.items():
        for benchmark_name, benchmark_path in BENCHMARKS.items():
            output_dir = RESULTS_DIR / tool_name / benchmark_name
            run_tool(tool_name, tool_path, benchmark_name, benchmark_path, SEEDS_DIR / benchmark_name, output_dir)

if __name__ == "__main__":
    main()
