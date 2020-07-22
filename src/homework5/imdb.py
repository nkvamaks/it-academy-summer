#####################
# WORK IN PROGRESS! #
#####################

import re

pattern = r'^\s*\d*\s*\d*\s*\d\.\d\s*.*\(\d{4}\)\s*'

try:
    with open('ratings.list', encoding='utf8', errors='ignore') as fh:
        for line in fh:
            res = re.match(pattern, line)
            if res: print(res.group(0))
except FileNotFoundError:
    print('File not found.')
