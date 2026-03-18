import os
import re

d = r'd:\EATS\repos\diplomado_neurum_2026\03_sis_sispro\slides'

# Print out what files exist
print("Current files:")
files = sorted([f for f in os.listdir(d) if f.startswith('slide') and f.endswith('.html')])
for f in files:
    with open(os.path.join(d, f), 'r', encoding='utf-8') as file:
        content = file.read()
        match = re.search(r'id="([^"]+)"', content)
        print(f"{f} -> {match.group(1) if match else 'NO ID'}")

