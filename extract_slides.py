import os
import re

html_file = r"01_datos_vida_real/index.html"
slides_dir = r"01_datos_vida_real/slides"

os.makedirs(slides_dir, exist_ok=True)

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract slides
# We look for <section class="slide" id="slideX"> ... </section>
slides = re.findall(r'(<section class="slide" id="[a-zA-Z0-9_]+">.*?</section>)', content, re.DOTALL)

for i, slide_content in enumerate(slides, start=1):
    slide_filename = f"slide{i:02d}.html"
    with open(os.path.join(slides_dir, slide_filename), 'w', encoding='utf-8') as f:
        f.write(slide_content)

# Extract modals
modals_match = re.search(r'<!-- Modals -->(.*?)<!-- Global Image Modal -->', content, re.DOTALL)
if modals_match:
    modals = modals_match.group(1).strip()
    with open(os.path.join(slides_dir, 'modals.html'), 'w', encoding='utf-8') as f:
        f.write(modals)

print(f"Extracted {len(slides)} slides and modals.")
