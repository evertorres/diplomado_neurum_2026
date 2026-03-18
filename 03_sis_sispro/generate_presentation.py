import os
import shutil

base_dir = r"d:\EATS\repos\diplomado_neurum_2026\03_sis_sispro"
slides_dir = os.path.join(base_dir, "slides")

if not os.path.exists(slides_dir):
    os.makedirs(slides_dir)

# Data structure
parts = [
    {
        "title": "Ecosistema de los SIS",
        "slides": [
            "Entorno de la atención en salud",
            "De la salud 1.0",
            "Salud de la era de la información.",
            "Datos de la salud de las personas.",
            "Ecosistema de SIS en Salud",
            "RIS/PACS",
            "Sistema de información de anatomía patológica - SIAP",
            "Laboratory Information System - LIS",
            "Historia Clínica Electrónica - HCE",
            "Historia Clínica Personal - HCP",
            "Sistema de Información Hospitalario - HIS",
            "Adopción HCE - (EMRAM – Electronic Medical Record Adoption Model)",
            "Sistemas de Gestión de Mantenimiento",
            "Algunas ideas claves"
        ]
    },
    {
        "title": "Modelos de datos clínicos",
        "slides": [
            "Información Clínica en el hospital",
            "Bodegas de datos",
            "Almacenar datos diversos",
            "¿Qué es un modelo de datos?",
            "Objetos a ser almacenados: Pacientes – Profesionales - Visitas",
            "Modelos de datos clínicos.",
            "OpenMRS Data Model",
            "OpenEHR",
            "Modelo de referencia (2)",
            "OpenEHR Modelo de 2 capas",
            "OpenEHR Modelo de 2 capas (2)",
            "Ontología de información.",
            "Arquetipos",
            "Plantillas",
            "Modelos de datos en investigación en salud",
            "¿Por qué es necesario un modelo de datos?",
            "¿Por qué es necesario un modelo de datos? (2)",
            "¿Por qué es necesario un modelo de datos? (3)",
            "Modelo de datos común",
            "OMOP CDM",
            "Resumen modelos de datos."
        ]
    },
    {
        "title": "SISPRO",
        "slides": [
            "Qué es el SISPRO",
            "Actores del SGSSS",
            "Modelo conceptual de salud y protección social",
            "Marco normativo de la información en protección social",
            "Objetivos del SISPRO",
            "Sistema de Gestión de Datos",
            "Fuentes del SGD",
            "Aplicativos Misionales",
            "Análisis multidimensional (Tecnología OLAP)",
            "Conceptos para consulta en cubos",
            "Recomendaciones de desempeño y buenas prácticas"
        ]
    }
]

total_slides = 1 + sum(len(p["slides"]) for p in parts)

# 1. Generate index.html
index_html = f"""<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>03. Sistemas de información en Salud</title>
    <!-- Relative path to global styles -->
    <link rel="stylesheet" href="../shared/styles.css">
    <style>
        .slide-image {{
            max-width: 100%;
            max-height: 55vh;
            border-radius: 12px;
            box-shadow: var(--shadow-lg);
            margin: var(--space-md) auto;
            border: 1px solid #E2E8F0;
            display: block;
        }}

        /* Loading indicator */
        .loader {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: white;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            font-size: 1.5rem;
            color: var(--color-primary);
            transition: opacity 0.5s;
        }}

        .loader.hidden {{
            opacity: 0;
            pointer-events: none;
        }}
    </style>
</head>

<body>

    <div class="loader" id="loader">Cargando presentación...</div>

    <!-- Main Container -->
    <div class="presentation-container">

        <div id="slide-container" style="width: 100%; height: 100%; display: flex; flex-direction: column;">
            <!-- Slides will be injected here -->
        </div>

        <!-- Navigation UI -->
        <div class="slide-controls">
            <button class="control-btn" id="prevSlide" disabled title="Anterior">
                <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
                </svg>
            </button>
            <span class="slide-counter" id="slideCounter">1 / {total_slides}</span>
            <button class="control-btn" id="nextSlide" title="Siguiente">
                <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                </svg>
            </button>
        </div>

    <div id="modals-container">
        <!-- Modals will be injected here -->
    </div>

    <!-- Global Image Modal -->
    <div class="modal-overlay" id="global-image-modal">
        <div class="modal modal-image-wrapper">
            <button class="modal-close modal-image-close" title="Cerrar Imagen">&times;</button>
            <img src="" id="global-image-content" class="modal-image-content">
        </div>
    </div>

    <!-- Global App Logic -->
    <script src="../shared/app.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', async () => {{
            const container = document.getElementById('slide-container');
            const modalsContainer = document.getElementById('modals-container');
            const loader = document.getElementById('loader');

            try {{
                const totalSlides = {total_slides};
                let slidesHtml = '';

                const slidePromises = [];
                for (let i = 1; i <= totalSlides; i++) {{
                    const slideNum = i.toString().padStart(2, '0');
                    slidePromises.push(fetch(`slides/slide${{slideNum}}.html`).then(res => res.text()));
                }}

                const slideTexts = await Promise.all(slidePromises);
                slidesHtml = slideTexts.join('\\n');
                container.innerHTML = slidesHtml;

                const modalResponse = await fetch('slides/modals.html');
                if (modalResponse.ok) {{
                    const modalText = await modalResponse.text();
                    modalsContainer.innerHTML = modalText;
                }}

                loader.classList.add('hidden');

                if (window.initApp) {{
                    window.initApp();
                }}
            }} catch (error) {{
                console.error("Error loading presentation content:", error);
                loader.textContent = "Error al cargar la presentación. Verifica la consola.";
            }}
        }});
    </script>
</body>

</html>
"""

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

# 2. Generate title slide (Slide 1)
title_slide = """<section class="slide" id="slide1">
    <div class="slide-content">
        <p class="text-muted" style="margin-bottom: var(--space-md);">P R E S E N T A C I Ó N 0 3</p>
        <h1>Sistemas de información en Salud</h1>
        <p style="font-size: 1.2rem; color: var(--color-secondary); margin-bottom: var(--space-xl);">
            Ecosistema de los SIS, Modelos de datos clínicos, y SISPRO.
        </p>
        <div class="grid-2" style="max-width: 600px; margin-top: var(--space-xl);">
            <button class="btn-primary"
                onclick="document.dispatchEvent(new KeyboardEvent('keydown', {key: 'ArrowRight'}))">
                Comenzar
                <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7">
                    </path>
                </svg>
            </button>
            <a href="../index.html" class="btn-secondary">Volver al Directorio</a>
        </div>
    </div>
</section>
"""

with open(os.path.join(slides_dir, "slide01.html"), "w", encoding="utf-8") as f:
    f.write(title_slide)

# 3. Generate all other slides
slide_number = 2
for part in parts:
    section_title = part["title"]
    for slide_title in part["slides"]:
        slide_num_str = str(slide_number).zfill(2)
        slide_html = f"""<section class="slide" id="slide{slide_number}">
    <div class="slide-content left" style="max-width: 1000px; width: 100%;">
        <div style="font-size: 0.9rem; color: var(--color-primary); margin-bottom: var(--space-sm); font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">
            {section_title}
        </div>
        <h2 style="text-align: center; margin-bottom: var(--space-xl);">{slide_title}</h2>
        <div style="display: flex; flex-direction: column; gap: var(--space-md); width: 100%;">
            <!-- Content for this slide goes here -->
            <div class="card fragment">
                <p>Contenido para: {slide_title}</p>
            </div>
        </div>
    </div>
</section>
"""
        with open(os.path.join(slides_dir, f"slide{slide_num_str}.html"), "w", encoding="utf-8") as f:
            f.write(slide_html)
        slide_number += 1

# 4. Copy modals.html if it doesn't exist
source_modals = r"d:\EATS\repos\diplomado_neurum_2026\02_datos_tipos\slides\modals.html"
target_modals = os.path.join(slides_dir, "modals.html")

if os.path.exists(source_modals) and not os.path.exists(target_modals):
    shutil.copy2(source_modals, target_modals)
elif not os.path.exists(target_modals):
    # create empty modals if source not found
    with open(target_modals, "w", encoding="utf-8") as f:
        f.write("<!-- Modals -->\n")
