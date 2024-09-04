import re
import os

def get_regex_matches(string, verbose = False):
    """
        Given a file name of an Illumina HiSeq 2000 experiment file, extract out the relevant information
    """
    pattern = r'([A-Za-z0-9-]+)_([A-Za-z]+)_([A-Za-z]+)(\d+N)([A-Z]+)?_(\d+)\.txt\.gz'
    matches = re.findall(pattern, string)
    
    if matches and verbose:
        code1, code2, code3, code4, code5, code6 = matches[0]
        print(code1)  # Output: Alx1
        print(code2)  # Output: ESZ
        print(code3)  # Output: TAAAGC
        print(code4)  # Output: 20N
        print(code5)  # Output: CG
        print(code6)  # Output: 1

    if not(matches):
        print(f"Regex failed at {string}")
        
    return matches[0]
    
def additional_check(file_name, regex_out):
    """
        Use regular string splitting and check if Regex has worked (helps to identify misnamed files if any)
    """
    codes = file_name.split("_")

    assert regex_out[0]  == codes[0], f"{file_name} --> {regex_out[0]}<>{codes[0]}"
    assert regex_out[1]  == codes[1]
    assert regex_out[-1] == codes[-1][:-len('.txt.gz')]

    return