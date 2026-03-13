import os
import re

slides_dir = r"d:\EATS\repos\diplomado_neurum_2026\02_datos_tipos\slides"
guion_file = os.path.join(slides_dir, "guion.md")

# 1. Swap HTML files and update their internal IDs
def update_html_id(filepath, new_id):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace id="slideX" with id="slide{new_id}"
    content = re.sub(r'id="slide\d+"', f'id="slide{new_id}"', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

file23 = os.path.join(slides_dir, "slide23.html")
file24 = os.path.join(slides_dir, "slide24.html")
file_temp = os.path.join(slides_dir, "slide_temp.html")

os.rename(file23, file_temp)
os.rename(file24, file23)
os.rename(file_temp, file24)

update_html_id(file23, 23)
update_html_id(file24, 24)

print("HTML files swapped and IDs updated.")

# 2. Update guion.md
with open(guion_file, 'r', encoding='utf-8') as f:
    guion_content = f.read()

# Split guion by "## Slide "
sections = re.split(r'(?<=^)\#\# Slide (\d{2}):', guion_content, flags=re.MULTILINE)

# Build a dictionary of slide text
script_dict = {}
for i in range(1, len(sections), 2):
    slide_num = int(sections[i])
    script_dict[slide_num] = sections[i+1]

# Swap contents in the dictionary
temp_text = script_dict[23]
script_dict[23] = script_dict[24]
script_dict[24] = temp_text

# Reconstruct guion.md
new_guion = sections[0]
for i in range(1, 32):
    # Format number to two digits
    num_str = f"{i:02d}"
    if i in script_dict:
        new_guion += f"## Slide {num_str}:{script_dict[i]}"

with open(guion_file, 'w', encoding='utf-8') as f:
    f.write(new_guion)

print("guion.md updated.")
