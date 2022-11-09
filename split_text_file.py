import os
from tqdm import tqdm
import re

# File/Folder Path
fp_in = input('File: ').replace('"', '')
dir_out = input('Out Folder: ').replace('"', '')

# Encoding
# Type in 'ascii' for ascii encoding.
encoding = input('Encoding: ').replace('"', '')

# Splitter
# Type in "0A" for single new line '\n' <CR><LF>
# Type in "0A0A" for double new lines '\n\n' like <CR><LF><CR><LF>
splitter = bytes.fromhex(input('splitter: ')).decode(encoding=encoding)

# Regular Expression Match
# Type in regular expression to match the text block.
pattern = re.compile(input('Regular Expression: '), re.DOTALL)
msg_count = 0

# Read File
with open(fp_in, 'r', encoding=encoding) as f:
    txt_all = f.read()

# Split
for msg in tqdm(txt_all.split(splitter)):
    # Match Pattern
    if pattern.match(msg):
        msg_count += 1
        fn_out = f'{msg_count: 08d}' + '.txt'
        fp_out = os.path.join(dir_out, fn_out)
        with open(fp_out, 'w', encoding=encoding) as f:
            f.write(msg)

print(f'msg_count={msg_count}')
