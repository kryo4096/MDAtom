import re, string

def extract_properties(regex_match):
    properties = {}
    properties["step"] = int(regex_match.group(1))
    properties["time"] = float(regex_match.group(2))
    properties["etot"] = float(regex_match.group(3))
    properties["ekin"] = float(regex_match.group(4))
    properties["epot"] = float(regex_match.group(5))
    properties["vir"] = float(regex_match.group(6))
    properties["pressure"] = float(regex_match.group(7))
    properties["scalet"] = float(regex_match.group(8))
    return properties

def find_properties(file, preceding_pattern):
    """
    This function first searches for preceding_pattern, and the next occurrence of
    a line containing properties is returned as a dictionary.
    """
    property_pattern = re.compile(r" +([0-9]+) +([0-9Ee\+-\.]+) +([0-9Ee\+-\.]+) +([0-9Ee\+-\.]+) +([0-9Ee\+-\.]+) +([0-9Ee\+-\.]+) +([0-9Ee\+-\.]+) +([0-9Ee\+-\.]+)")
    while True:
        line = file.readline()
        if preceding_pattern.search(line) != None:
            break
    while True:
        line = file.readline()
        m = property_pattern.search(line)
        if m != None:
            p = extract_properties(m)
            return p

def get_averages(filename):
    with open(filename, 'r') as f:
        pattern1 = re.compile("Averages:")
        return find_properties(f, pattern1)
    
def get_fluctuations(filename):
    with open(filename, 'r') as f:
        pattern1 = re.compile("Root mean square fluctuations:")
        return find_properties(f, pattern1)

def get_runtime(filename):
    with open(filename, 'r') as f:
        content = f.read()
        match = re.search("Time spent for MD iterations: ([0-9Ee\+-\.]+) sec", content, flags=re.MULTILINE)
        time = float(match.group(1))
        return time
