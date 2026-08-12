# Guía Detallada de Prompts & Transcripción Técnica: Google Flow Studio & Veo 3.1

**Video de Referencia:** [Google Flow AI Creative Studio Tutorial](https://www.youtube.com/watch?v=eZWN_8qW3VA)  
**Plataforma:** Google Labs / Google Flow Studio  
**Modelos Integrados:** Google Veo 3.1 (Video), Imagen 4 / Nano Banana (Imágenes), Gemini (Agente & Lenguaje).

---

## 📸 1. RECOMENDACIONES ESPECÍFICAS PARA PROMPTS DE IMÁGENES (Imagen 4 / Nano Banana)

En Google Flow Studio, la generación de imágenes estáticas sirve como la base (*grounding*) para crear los fotogramas clave y los personajes sintéticos.

### **Fórmula Tridimensional para Prompts de Imágenes**
$$\text{Prompt Imagen} = \text{[Sujeto Descriptivo]} + \text{[Entorno Detallado]} + \text{[Estilo Visual & Render]} + \text{[Iluminación & Color]}$$

### **Recomendaciones Clave del Tutorial para Imágenes:**
1. **Evitar la Vaguedad:** No escribir *"un médico"*. Escribir: *"Fotografía editorial de una médica pediatra hispana de 35 años, cabello recogido, bata médica limpia, sonriendo con calidez"*.
2. **Especificación del Entorno:** Detallar arquitectura y fondo para evitar elementos aleatorios: *"Fondo de consultorio pediátrico moderno, pared de color azul pastel suave, ventana amplia con luz natural entrando lateralmente, estantes con juguetes didácticos desenfocados en el fondo (shallow depth of field)"*.
3. **Control de Estilo Visual (Tokens Recomendados):**
   - **Fotografía Editorial:** `editorial healthcare photography, shot on 85mm lens, f/1.8, sharp focus on facial expression, natural skin texture`.
   - **3D Render Pixar/Blender:** `friendly 3D Pixar character render, soft ambient occlusion, bright vibrant pastel colors, clean studio lighting`.
   - **Ilustración Vectorial:** `clean flat vector illustration, minimal lines, isolated on white background, modern infographic style`.
4. **Fijación de Personajes (Character Locking):** Generar primero la imagen del personaje sobre fondo neutro o blanco y guardarla como **`Subject Ingredient 1`** en el panel de Google Flow.

---

## 🎥 2. RECOMENDACIONES ESPECÍFICAS PARA PROMPTS DE VIDEO (Veo 3.1 / Frame-to-Video)

Para generar video cinematográfico fluido con **Veo 3.1**, los prompts requieren una estructura en 3 capas cinemáticas y control temporal.

### **Fórmula Tridimensional para Prompts de Video**
$$\text{Prompt Video} = \text{[Trayectoria de Cámara]} + \text{[Acción del Sujeto]} + \text{[Dinámica Atmosférica]} + \text{[Timestamps \& Ingredients]}$$

### **Recomendaciones Clave del Tutorial para Videos:**

#### **A. Las 3 Capas Cinemáticas:**
- **Capa 1 (Trayectoria de Cámara):** Especificar exactamente cómo se mueve la cámara:
  - `slow camera panning left to right` (Panorámica lenta)
  - `gentle 360-degree camera orbit` (Órbita alrededor del sujeto)
  - `cinematic zoom in transition` (Acercamiento suave)
  - `crane shot tilting down` (Plano de grúa descendente)
- **Capa 2 (Acción del Sujeto):** Especificar el movimiento interno:
  - *"Pediatrician slowly raises her tablet and points to a glowing 3D heart diagram"*.
  - *"Blood cells flow smoothly through a clear transparent blood vessel"*.
- **Capa 3 (Físicas y Dinámica Atmosférica):**
  - `soft volumetric cyan light pulses, floating microscopic dust particles, gentle lens flare`.

#### **B. Sintaxis Temporal (Timestamp Prompting):**
Dividir la toma en bloques cronológicos para evitar que la IA mezcle acciones:
```text
[00:00-00:02] Slow camera zoom into pediatrician sitting at her desk.
[00:02-00:05] Pediatrician turns towards the camera with a warm empathetic smile and nods gently.
[Ingredients: Subject=Doctor_Hispanic_ID1, Scene=Pediatric_Office_02]
```

#### **C. Anclaje de Cuadro Inicial y Final (Start & End Frame Interpolation):**
- Cargar un **Start Frame (Cuadro 1)** y un **End Frame (Cuadro 2)** en Google Flow.
- Redactar el prompt indicando la transición: *"Smooth fluid video transition interpolating from Start Frame to End Frame, maintaining subject identity and soft lighting"*.

#### **D. Uso del Copiloto Agéntico (Agent Mode con Gemini):**
Instruir al agente conversacional de Google Flow para estructurar prompts complejos:
- *"Gemini, refina este prompt para Veo 3.1: quiero una escena de 4 segundos donde se muestre el pulso de un corazón 3D con movimiento de cámara orbital y luz azul médica, usando el personaje cargado en Ingredient 1"*.

---

## 🛠️ Banco Comparativo de Prompts Extraídos del Tutorial

| Tipo | Objetivo | Prompt Optimizado | Herramienta / Modelo |
|---|---|---|---|
| **Imagen** | Fotografía Pediátrica | `Editorial healthcare photography of a Hispanic female pediatrician warmly smiling at a child patient during routine checkup. Bright modern pediatric office, soft natural window daylight, 85mm lens, sharp focus, empathetic atmosphere.` | Imagen 4 / DaVinci AI |
| **Imagen** | Personaje 3D Diente | `Friendly 3D Pixar style animated character render of a healthy tooth wearing a red superhero cape and holding a giant toothbrush. Soft lighting, bright vibrant colors, clean white background, cute design.` | Imagen 4 / 3D Render |
| **Video** | Secuencia Cardiovascular | `[00:00-00:02] Slow 360-degree camera orbit around a 3D animated human heart. [00:02-00:04] Internal blood flow dynamics with glowing cyan pulses and smooth fluid motion. [Ingredients: Subject=Heart_3D_Ref]` | Google Flow (Veo 3.1) |
| **Video** | Atención Médica | `[00:00-00:03] Cinematic medium shot camera zoom onto doctor holding tablet. [00:03-00:05] Doctor smiles warmly and gestures explaining healthy habits. [Ingredients: Subject=Doctor_ID1, Scene=Clinic_Ref]` | Google Flow (Veo 3.1) |
