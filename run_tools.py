import os
import subprocess
from pathlib import Path

# Define the tools and their configurations
TOOLS = {
    "HFL": "path_to_hfl_executable",
    "LeanSym": "path_to_leansym_executable",
    "FuzzySat": "path_to_fuzzysat_executable",
    "LibKluzzer": "path_to_libkluzzer_executable",
    "AFL++_QSYM": "path_to_afl_qsym_executable",
}

# Define the benchmarks and their directories
BENCHMARKS = {
    "advmng": "path_to_advmng_executable",
    "bloaty": "path_to_bloaty_executable",
    "objdump": "path_to_objdump_executable",
    "optipng": "path_to_optipng_executable",
    "readelf": "path_to_readelf_executable",
}

# Directory containing seeds
SEEDS_DIR = Path("seeds/")
RESULTS_DIR = Path("results/")

def run_tool(tool_name, tool_path, benchmark_name, benchmark_path, seeds_dir, output_dir):
    """
    Run a tool on a benchmark with the given seeds and output results.
    """
    output_dir.mkdir(parents=True, exist_ok=True)  # Create output directory if it doesn't exist
    
    command = [
        tool_path,                 # Path to the tool executable
        "-i", str(seeds_dir),      # Input seeds directory
        "-o", str(output_dir),     # Output directory for results
        "--", str(benchmark_path)  # Benchmark executable
    ]
    
    print(f"Running {tool_name} on {benchmark_name}...")
    try:
        # Execute the command
        subprocess.run(command, check=True)
        print(f"{tool_name} completed for {benchmark_name}. Results saved in {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {tool_name} on {benchmark_name}: {e}")
        
def main():
    for tool_name, tool_path in TOOLS.items():
        for benchmark_name, benchmark_path in BENCHMARKS.items():
            # Define the output directory for results
            output_dir = RESULTS_DIR / tool_name / benchmark_name
            run_tool(tool_name, tool_path, benchmark_name, benchmark_path, SEEDS_DIR / benchmark_name, output_dir)

if __name__ == "__main__":
    main()
