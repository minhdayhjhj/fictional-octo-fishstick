import re
with open('1.py', 'r', encoding='utf-8') as f:
    text = f.read()

# find instances where mock process lists were used
print(re.findall(r'.*DEMO_PROCS.*', text))
print(re.findall(r'.*self._proc_sum.*', text))
print(re.findall(r'.*process.*', text))
