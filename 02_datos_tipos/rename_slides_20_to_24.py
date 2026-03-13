import os
import re

slides_dir = r"d:\EATS\repos\diplomado_neurum_2026\02_datos_tipos\slides"
guion_file = os.path.join(slides_dir, "guion.md")

# 1. Rename HTML files and update their internal IDs
# Original 20 -> temp
# Original 21 -> 20
# Original 22 -> 21
# Original 23 -> 22
# Original 24 -> 23
# temp -> 24

def update_html_id(filepath, new_id):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace id="slideX" with id="slide{new_id}"
    content = re.sub(r'id="slide\d+"', f'id="slide{new_id}"', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Rename to temp
os.rename(os.path.join(slides_dir, "slide20.html"), os.path.join(slides_dir, "slide_temp.html"))

# Shift 21-24 down
for i in range(21, 25):
    old_file = os.path.join(slides_dir, f"slide{i}.html")
    new_file = os.path.join(slides_dir, f"slide{i-1}.html")
    os.rename(old_file, new_file)
    update_html_id(new_file, i-1)

# Move temp to 24
new_file_24 = os.path.join(slides_dir, "slide24.html")
os.rename(os.path.join(slides_dir, "slide_temp.html"), new_file_24)
update_html_id(new_file_24, 24)

print("HTML files renamed and IDs updated.")

# 2. Update guion.md
with open(guion_file, 'r', encoding='utf-8') as f:
    guion_content = f.read()

# Split guion by "## Slide "
sections = re.split(r'(?<=^)\#\# Slide (\d{2}):', guion_content, flags=re.MULTILINE)

# sections[0] is preamble
# sections[1] is '01', sections[2] is text for 01
# etc.

# Build a dictionary of slide text
script_dict = {}
for i in range(1, len(sections), 2):
    slide_num = int(sections[i])
    script_dict[slide_num] = sections[i+1]

# Now we need to shift the contents in the dictionary
# Original 20 -> new 24
# Original 21 -> new 20
# Original 22 -> new 21
# Original 23 -> new 22
# Original 24 -> new 23

temp_text = script_dict[20]
script_dict[20] = script_dict[21]
script_dict[21] = script_dict[22]
script_dict[22] = script_dict[23]
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
