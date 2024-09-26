import subprocess

def count_lines_in_gzfile(path):
    
    command = f"zcat {path} | wc -l"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        return int(result.stdout.strip())
    else:
        return f"Error: {result.stderr.strip()}"
    
def count_matching_files(protein, round_id, directory):
    """
        Count matching files in given directory which matches protein_**_round_id
    """
    
    command = f"find . -name '{protein}_*_{round_id}.txt.gz' | wc -l"
    result = subprocess.run(command, cwd=directory, shell=True, capture_output=True, text=True)
    return int(result.stdout.strip())