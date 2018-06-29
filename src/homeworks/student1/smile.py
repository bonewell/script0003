import re

def count_smiles(lines):
    pattern = re.compile('([:;B]{1}[-~]{0,1}[)D]{1})')
    return sum((len(pattern.findall(line)) for line in lines))
