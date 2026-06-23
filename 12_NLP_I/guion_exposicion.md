# Guion de Exposición: Procesamiento de Lenguaje Natural (NLP I)

Este documento contiene el guion detallado para la presentación del módulo **12. Procesamiento de Lenguaje Natural: Introducción y Conceptos Básicos** para el Diplomado Neurum. 

* **Estructura del tiempo:** 2 minutos por diapositiva (Total: 40 minutos para 20 diapositivas).
* **Ritmo sugerido:** ~120-130 palabras por minuto. Esto permite hablar con claridad, hacer pausas reflexivas y coordinar con los efectos de animación (fragments).
* **Enfoque:** Clínico y educativo, alineado con los ejemplos médicos presentes en las diapositivas.

---

## Índice de Diapositivas
1. [Diapositiva 1: Portada e Introducción](#diapositiva-1-portada-e-introducción) - [[slide01.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide01.html)]
2. [Diapositiva 2: Objetivos y Temario](#diapositiva-2-objetivos-y-temario) - [[slide02.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide02.html)]
3. [Diapositiva 3: Inteligencia Artificial (IA)](#diapositiva-3-inteligencia-artificial-ia) - [[slide03.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide03.html)]
4. [Diapositiva 4: IA, Machine Learning y Prueba de Turing](#diapositiva-4-ia-machine-learning-y-prueba-de-turing) - [[slide04.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide04.html)]
5. [Diapositiva 5: ¿Qué es NLP?](#diapositiva-5-qué-es-nlp) - [[slide05.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide05.html)]
6. [Diapositiva 6: Evolución Histórica del NLP](#diapositiva-6-evolución-histórica-del-nlp) - [[slide06.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide06.html)]
7. [Diapositiva 7: El Ecosistema de Tareas en NLP](#diapositiva-7-el-ecosistema-de-tareas-en-nlp) - [[slide07.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide07.html)]
8. [Diapositiva 8: Tareas Comunes en NLP](#diapositiva-8-tareas-comunes-en-nlp) - [[slide08.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide08.html)]
9. [Diapositiva 9: Niveles de Comprensión del Lenguaje](#diapositiva-9-niveles-de-comprensión-del-lenguaje) - [[slide09.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide09.html)]
10. [Diapositiva 10: Morfología, Sintaxis y POS Tagging](#diapositiva-10-morfología-sintaxis-y-pos-tagging) - [[slide10.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide10.html)]
11. [Diapositiva 11: Tokenización (Segmentación)](#diapositiva-11-tokenización-segmentación) - [[slide11.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide11.html)]
12. [Diapositiva 12: Estadísticas del Lenguaje: Riqueza y Zipf](#diapositiva-12-estadísticas-del-lenguaje-riqueza-y-zipf) - [[slide12.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide12.html)]
13. [Diapositiva 13: Estadísticas del Lenguaje: Legibilidad y Comprensibilidad](#diapositiva-13-estadísticas-del-lenguaje-legibilidad-y-comprensibilidad) - [[slide13.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide13.html)]
14. [Diapositiva 14: Stopwords (Palabras Vacías)](#diapositiva-14-stopwords-palabras-vacías) - [[slide14.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide14.html)]
15. [Diapositiva 15: N-gramas](#diapositiva-15-n-gramas) - [[slide15.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide15.html)]
16. [Diapositiva 16: Representación de Textos: One-Hot Encoding](#diapositiva-16-representación-de-textos-one-hot-encoding) - [[slide16.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide16.html)]
17. [Diapositiva 17: Bolsa de Palabras (Bag of Words)](#diapositiva-17-bolsa-de-palabras-bag-of-words) - [[slide17.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide17.html)]
18. [Diapositiva 18: Word Embeddings y Word2Vec](#diapositiva-18-word-embeddings-y-word2vec) - [[slide18.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide18.html)]
19. [Diapositiva 19: Pipeline de Preprocesamiento Clásico](#diapositiva-19-pipeline-de-preprocesamiento-clásico) - [[slide19.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide19.html)]
20. [Diapositiva 20: Cierre y Preguntas](#diapositiva-20-cierre-y-preguntas) - [[slide20.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide20.html)]

---

### Diapositiva 1: Portada e Introducción
* **Archivo:** [slide01.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide01.html)
* **Elementos en pantalla:** Ícono de robot, Título principal, Subtítulo y Nombre del Docente (Ever Augusto Torres Silva).
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~240 palabras.

#### Guion Hablado:
"Muy buenos días a todos. Les doy una cordial bienvenida a esta sesión del módulo doce de nuestro diplomado Neurum. Hoy comenzaremos un viaje fascinante a una de las áreas más dinámicas, complejas y de mayor impacto en la Inteligencia Artificial moderna: el Procesamiento de Lenguaje Natural, comúnmente conocido como PLN o por sus siglas en inglés, NLP.

`[Clic para revelar Título y Subtítulo]`

A lo largo de este encuentro, nos centraremos en realizar una introducción sólida a sus conceptos básicos y fundamentos teóricos. Mi nombre es Ever Augusto Torres Silva, y los estaré acompañando como docente en esta materia. 

Cuando pensamos en Inteligencia Artificial, solemos imaginar algoritmos matemáticos y análisis numéricos complejos. Sin embargo, una de las mayores expresiones de la inteligencia humana no son los números, sino el lenguaje: nuestra capacidad de transmitir ideas, emociones, diagnósticos e historias a través del habla o la escritura. Durante años, lograr que una máquina interactúe de forma natural con este tipo de datos ha sido el 'santo grial' de la computación. 

`[Clic para revelar datos del Docente y botón Comenzar]`

En este módulo sentaremos las bases conceptuales para entender cómo pasamos de un texto clínico desestructurado, lleno de abreviaturas e imperfecciones, a una representación matemática compacta que una computadora puede analizar para predecir patologías, clasificar pacientes o asistir en la toma de decisiones médicas. Prepárense para cuestionar qué significa realmente 'comprender' el lenguaje y cómo la tecnología ha evolucionado para aproximarse a esta capacidad humana. Comencemos."

---

### Diapositiva 2: Objetivos y Temario
* **Archivo:** [slide02.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide02.html)
* **Elementos en pantalla:** Dos columnas principales: "Objetivos de Aprendizaje" y "Temario General".
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~250 palabras.

#### Guion Hablado:
"Antes de sumergirnos en el contenido, es fundamental trazar la hoja de ruta que seguiremos en esta sesión. ¿Qué buscamos lograr hoy y cuáles son los hitos de aprendizaje que abordaremos?

`[Clic para revelar Objetivos de Aprendizaje]`

En primer lugar, queremos que comprendan con total claridad el rol que juega el NLP dentro del ecosistema general de la Inteligencia Artificial. No es una herramienta aislada, sino un puente crítico entre la percepción computacional y la cognición. En segundo lugar, y con un enfoque muy especial en nuestro diplomado, estudiaremos las complejidades del lenguaje clínico y sus diferentes niveles de análisis, un dominio donde la precisión puede salvar vidas. Posteriormente, aprenderemos las técnicas fundamentales de preprocesamiento y limpieza de texto libre, el paso esencial para transformar datos brutos y 'ruidosos' en información estructurada. Finalmente, analizaremos los métodos clásicos y modernos de representación vectorial, es decir, cómo convertimos palabras en vectores numéricos usando técnicas como Bolsa de Palabras, TF-IDF o Embeddings.

`[Clic para revelar Temario General]`

Para alcanzar estos objetivos, dividiremos nuestra sesión en cuatro grandes ejes temáticos que ven en pantalla: 
Primero, exploraremos los Fundamentos de la IA y la famosa Prueba de Turing. Segundo, debatiremos qué es realmente el NLP y qué significa que una máquina 'entienda'. Tercero, estudiaremos las Estadísticas del Lenguaje y las tareas de Preprocesamiento fundamentales. Y cuarto, analizaremos las Representaciones Vectoriales clásicas y modernas como Bag of Words y Word2Vec. Como ven, es un temario completo que nos llevará desde la teoría filosófica hasta la ingeniería de datos."

---

### Diapositiva 3: Inteligencia Artificial (IA)
* **Archivo:** [slide03.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide03.html)
* **Elementos en pantalla:** Definición de IA, cuadrícula con facetas de la inteligencia y un diagrama ilustrativo de IA.
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~260 palabras.

#### Guion Hablado:
"Para entender el Procesamiento del Lenguaje Natural, primero debemos ubicarlo dentro de su marco contenedor: la Inteligencia Artificial. Definimos formalmente a la IA como la rama de la informática dedicada al desarrollo de sistemas y procesos que intentan imitar o emular los comportamientos y la inteligencia de los seres vivos.

`[Clic para revelar las facetas de la inteligencia]`

Pero, ¿qué compone realmente la inteligencia? No es un bloque monolítico, sino una red de capacidades interconectadas que se muestran en el panel izquierdo de nuestra diapositiva. Empezamos por el **Aprendizaje**, la habilidad de mejorar con la experiencia; la **Percepción**, para interpretar estímulos; y la adquisición de **Conocimiento** y su posterior **Descubrimiento**. 

Sin embargo, presten especial atención a la **Comunicación** y la **Inferencia**. El lenguaje es, ante todo, el vehículo de la comunicación y el razonamiento. Para que una máquina demuestre verdadera inteligencia general, debe ser capaz de planificar, razonar a partir de premisas complejas y, crucialmente, comunicarse de forma efectiva con nosotros.

`[Clic para revelar la Imagen de la derecha]`

Como muestra el diagrama de la derecha, la IA engloba capacidades sensomotoras y cognitivas. Tradicionalmente, la robótica se encargaba de la percepción física y la acción, pero el verdadero desafío cognitivo reside en cómo representamos el conocimiento del mundo en una computadora. El NLP no es solo procesar texto; es decodificar la estructura del pensamiento humano plasmado en palabras. A continuación, veremos cómo el campo de la computación ha intentado trazar la línea divisoria entre la computación mecánica y la verdadera inteligencia."

---

### Diapositiva 4: IA, Machine Learning y Prueba de Turing
* **Archivo:** [slide04.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide04.html)
* **Elementos en pantalla:** Explicaciones de Machine Learning y Deep Learning, la cita de Alan Turing sobre la Prueba de Turing, y diagramas ilustrativos de cada concepto.
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~250 palabras.

#### Guion Hablado:
"Para entender cómo la tecnología procesa el lenguaje, debemos distinguir los niveles de especialización tecnológica que usamos hoy en día. 

`[Clic para revelar Machine Learning]`

El primer nivel clave es el **Machine Learning** o Aprendizaje Automático. A diferencia de la programación tradicional, donde un humano escribe reglas explícitas del tipo 'si ocurre A, entonces haz B', en Machine Learning alimentamos a la máquina con datos para que sea ella quien reconozca los patrones subyacentes de forma autónoma.

`[Clic para revelar Deep Learning]`

Un paso más allá está el **Deep Learning** o Aprendizaje Profundo. Aquí utilizamos redes neuronales artificiales de múltiples capas que extraen y aprenden representaciones sumamente complejas y abstractas directamente desde los datos crudos, sin necesidad de que un ingeniero diseñe manualmente las características del texto. Este enfoque ha sido el motor de la revolución actual en el procesamiento de texto.

`[Clic para revelar la Prueba de Turing e imágenes]`

Ahora bien, ¿cómo evaluamos si una máquina es realmente inteligente? En 1950, el matemático Alan Turing propuso un criterio elegante y profundamente ligado al lenguaje: la **Prueba de Turing**. Él postuló que 'existirá Inteligencia Artificial cuando no seamos capaces de distinguir entre un ser humano y un programa de computadora en una conversación a ciegas'. 

Observen la importancia histórica de este concepto: Turing no propuso medir la inteligencia con cálculos matemáticos rápidos ni con juegos de ajedrez, sino a través de una conversación interactiva en lenguaje natural. Esto demuestra que, desde el nacimiento de la informática, el dominio del lenguaje ha sido considerado el indicador definitivo de la inteligencia artificial."

---

### Diapositiva 5: ¿Qué es NLP?
* **Archivo:** [slide05.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide05.html)
* **Elementos en pantalla:** Definición formal y detallada de Procesamiento de Lenguaje Natural (NLP) en una tarjeta central.
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~240 palabras.

#### Guion Hablado:
"Con este contexto claro, llegamos al núcleo de nuestro módulo. Definamos formalmente qué es el Procesamiento del Lenguaje Natural. 

`[Clic para revelar la definición de NLP]`

El NLP es un campo de estudio interdisciplinario que se sitúa en la intersección de tres grandes áreas: la lingüística teórica y computacional, las ciencias de la computación y la inteligencia artificial. Su propósito fundamental es modelar y analizar las complejas interacciones entre las computadoras y el lenguaje humano, tanto en su forma escrita como oral.

Pero, ¿cuál es el verdadero objetivo de esta disciplina? No se trata simplemente de que la máquina almacene texto o realice búsquedas de palabras clave como un procesador de textos básico. El fin último es permitir que las máquinas procesen, analicen, interpreten y, sobre todo, comprendan grandes volúmenes de datos lingüísticos no estructurados. 

En la práctica clínica, este punto es crucial. Cerca del ochenta por ciento de la información médica relevante (síntomas, antecedentes familiares, evoluciones del paciente, notas de enfermería) está atrapada en formato de texto libre en la historia clínica electrónica. Sin el NLP, esta riqueza de datos es invisible para los modelos predictivos tradicionales basados en tablas. El NLP actúa como el traductor que transforma este conocimiento narrativo y desestructurado en variables estructuradas y accionables que pueden alimentar algoritmos de soporte a la decisión clínica. Es el puente entre la narrativa humana y la computación analítica."

---

### Diapositiva 6: Evolución Histórica del NLP
* **Archivo:** [slide06.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide06.html)
* **Elementos en pantalla:** Línea de tiempo interactiva dividida en "Era Clásica" y "Era Moderna", con hitos desde 1950 hasta 2020.
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~270 palabras.

#### Guion Hablado:
"El NLP no surgió de la noche a la mañana; es el resultado de décadas de evolución teórica y técnica que podemos dividir en dos grandes etapas: la Era Clásica y la Era Moderna.

`[Clic para mostrar 1954: Georgetown]`
En la Era Clásica, tras la propuesta de Turing en 1950, el primer gran hito práctico fue el **Experimento de Georgetown en 1954**, donde se demostró la traducción automática básica del ruso al inglés. Esto generó un optimismo desmedido y gran financiamiento, aunque las limitaciones de la época pronto se hicieron evidentes.

`[Clic para mostrar 1956: Dartmouth]`
Poco después, en **1956**, se acuñó formalmente el término Inteligencia Artificial en la Conferencia de Dartmouth, consolidando la disciplina. Durante los años 80 y 90, el enfoque cambió drásticamente: pasamos de sistemas rígidos basados en reglas gramaticales hechas a mano, a los primeros algoritmos de Machine Learning estadístico y minería de texto.

`[Clic para cambiar a Era Moderna (2000s - 2020)]`
`[Clic para mostrar 2003: LDA y 2006: Deep Learning]`
La Era Moderna se inicia en los 2000 con corpus masivos y modelos de N-gramas. En **2003**, Blei, Ng y Jordan revolucionan la clasificación temática con el modelo LDA. Y en **2006**, Geoffrey Hinton introduce el entrenamiento práctico de redes neuronales profundas (Deep Learning), sentando las bases del procesamiento actual.

`[Clic para mostrar 2015: LSTM, 2017: Transformers y 2020: LLMs]`
En **2015**, la traducción automática supera la estadística gracias a las redes recurrentes LSTM. Pero el verdadero punto de inflexión ocurre en **2017** con la arquitectura *Transformer* ('Attention Is All You Need'), que elimina las limitaciones de secuencia y permite entrenar modelos gigantescos. Esto nos lleva al **2020** con la explosión de los Grandes Modelos de Lenguaje, como GPT-3, capaces de realizar múltiples tareas lingüísticas con mínima supervisión."

---

### Diapositiva 7: El Ecosistema de Tareas en NLP
* **Archivo:** [slide07.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide07.html)
* **Elementos en pantalla:** Tres tarjetas temáticas (Preprocesamiento, Generación y Comprensión) y un mapa mental detallado de tareas.
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~250 palabras.

#### Guion Hablado:
"Para abordar el Procesamiento de Lenguaje Natural de manera estructurada, es útil organizar sus múltiples aplicaciones y subdisciplinas en tres grandes familias o categorías de tareas, las cuales representamos en el ecosistema en pantalla.

`[Clic para revelar Preprocesamiento y Estructura]`

La primera categoría es el **Preprocesamiento y la Estructura**. Aquí agrupamos las tareas fundamentales de bajo nivel que preparan el texto para análisis posteriores. Incluye el análisis sintáctico, la identificación de partes de la oración (POS Tagging), la desambiguación y la extracción de características básicas. Sin esta fase, las etapas más complejas no tendrían bases sólidas.

`[Clic para revelar Generación y Traducción]`

La segunda categoría es la **Generación y Traducción** (conocida también como NLG o Generación de Lenguaje Natural). Esta área abarca la traducción automática de un idioma a otro, la simplificación de textos complejos (por ejemplo, traducir un informe médico especializado a un lenguaje comprensible para el paciente), la creación de resúmenes automáticos y los sistemas multimedia de conversión de voz a texto y viceversa.

`[Clic para revelar Comprensión y Razonamiento]`

La tercera y más avanzada categoría es la **Comprensión y el Razonamiento** (NLU). Aquí es donde evaluamos la semántica profunda del texto. Incluye la clasificación semántica, el análisis de sentimientos o emociones, el modelado del diálogo (necesario para agentes conversacionales o chatbots en salud) y el razonamiento basado en sentido común. 

`[Clic para revelar Mapa Mental]`

En el mapa mental de la derecha, pueden ver cómo estas tareas se ramifican. En la práctica clínica, combinamos componentes de las tres áreas para construir soluciones completas, como asistentes virtuales que comprenden al paciente y generan una respuesta clínicamente válida."

---

### Diapositiva 8: Tareas Comunes en NLP
* **Archivo:** [slide08.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide08.html)
* **Elementos en pantalla:** Descripciones y diagramas de tres tareas específicas: Clasificación de texto, QA (Pregunta-Respuesta) y Speech to Text (ASR).
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~250 palabras.

#### Guion Hablado:
"Profundicemos ahora en tres de las tareas más comunes e importantes en el ámbito práctico del NLP, aplicándolas directamente al contexto de la salud.

`[Clic para revelar Clasificación de Texto y su diagrama]`

La primera es la **Clasificación de Texto**. Su objetivo es asignar categorías automáticas a documentos o fragmentos de texto basándose en su contenido. En medicina, un ejemplo crítico es el *triaje clínico automatizado*, donde un algoritmo analiza el motivo de consulta escrito por admisión y prioriza la atención del paciente. También abarca el análisis de sentimiento para evaluar la satisfacción de los usuarios.

`[Clic para revelar Pregunta-Respuesta (QA) y su diagrama]`

La segunda tarea es **Pregunta - Respuesta (QA)**. A diferencia de un buscador tradicional que solo devuelve enlaces, un sistema de QA analiza un contexto o base documental dada y extrae la respuesta precisa a una pregunta formulada en lenguaje natural. Imaginemos a un médico consultando una guía de práctica clínica extensa: el sistema localiza instantáneamente la dosis exacta para un grupo etario específico.

`[Clic para revelar Speech to Text (ASR) y su diagrama]`

La tercera es **Speech to Text** o Reconocimiento Automático del Habla. Esta tecnología permite la transcripción en tiempo real de audios médicos. Es vital para el dictado automático de notas clínicas durante la consulta, reduciendo la carga administrativa de los profesionales de la salud y permitiéndoles centrar su atención en el paciente en lugar del teclado.

Estas tres tareas ilustran cómo el NLP transforma la interacción diaria en el entorno clínico, haciendo los procesos más eficientes y precisos."

---

### Diapositiva 9: Niveles de Comprensión del Lenguaje
* **Archivo:** [slide09.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide09.html)
* **Elementos en pantalla:** Tres tarjetas detalladas para Sintaxis, Semántica y Pragmática con ejemplos prácticos, y una lista de niveles adicionales.
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~250 palabras.

#### Guion Hablado:
"Cuando decimos que una computadora debe 'entender' el lenguaje, nos enfrentamos a un problema filosófico y técnico enorme. El lenguaje humano no es plano; se compone de múltiples niveles de abstracción estructurados que van desde los sonidos físicos hasta el contexto social del mensaje.

`[Clic para revelar Sintaxis]`

El primer nivel esencial es la **Sintaxis**. Hace referencia al orden correcto y a la estructura de las palabras dentro de una oración para que sea gramaticalmente válida. Como vemos en el ejemplo, la oración 'El médico atiende al paciente' sigue la estructura sintáctica del español, mientras que 'Paciente el atiende médico al' es incomprensible, aunque contenga exactamente las mismas palabras.

`[Clic para revelar Semántica]`

El segundo nivel es la **Semántica**, que estudia el significado literal e inequívoco de las palabras y frases de forma aislada. Aquí nos topamos con la ambigüedad. La palabra 'Operación' tiene un significado completamente diferente si estamos en un quirófano o en una clase de matemáticas. El NLP debe usar el contexto para desambiguar.

`[Clic para revelar Pragmática]`

El tercer nivel, y quizás el más complejo para la IA, es la **Pragmática**. Analiza cómo influye el contexto social, situacional y comunicativo en la interpretación del mensaje. Por ejemplo, si un paciente escribe 'Tiene fiebre' en una consulta clínica, es un dato fisiológico objetivo. Pero si lo dice en una conversación informal, podría significar que alguien está sumamente ansioso o emocionado. 

`[Clic para revelar Niveles Adicionales]`

Debajo de estos, existen otros niveles indispensables como la **Fonología** (sonidos), la **Morfología** (estructura de palabras) y el análisis del **Discurso**. Comprender el lenguaje requiere que la IA sea capaz de operar en todos estos niveles en paralelo."

---

### Diapositiva 10: Morfología, Sintaxis y POS Tagging
* **Archivo:** [slide10.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide10.html)
* **Elementos en pantalla:** Definiciones de Análisis Morfológico, Análisis Sintáctico y Etiquetado POS, acompañadas de gráficos de un árbol de dependencias y un ejemplo de etiquetado gramatical.
* **Duración estimada:** 2 minutes.
* **Palabras estimadas:** ~250 palabras.

#### Guion Hablado:
"Aterricemos ahora estos conceptos abstractos en técnicas computacionales concretas que implementamos en nuestras canalizaciones de procesamiento de datos.

`[Clic para revelar Análisis Morfológico]`

El **Análisis Morfológico** se encarga de estudiar la estructura interna de las palabras. Su objetivo es descomponerlas en sus unidades básicas de significado: los morfemas y lexemas. Esto permite comprender cómo se forman palabras complejas o derivadas a partir de una raíz común, lo cual es muy útil para identificar términos médicos relacionados (por ejemplo: cardio, cardiología, cardiovascular).

`[Clic para revelar Análisis Sintáctico y Árbol de Dependencias]`

El **Análisis Sintáctico** genera una representación jerárquica de la oración. Muestra cómo se agrupan las palabras y cuáles dependen de cuáles. En la imagen de la derecha, vemos un *Árbol de Dependencias Sintácticas*. Este árbol nos permite mapear que el sujeto realiza la acción del verbo sobre un objeto directo, ayudando a la máquina a entender 'quién le hizo qué a quién', independientemente de la voz activa o pasiva.

`[Clic para revelar Etiquetado POS y Ejemplo]`

Finalmente, el **Etiquetado Gramatical** o **POS Tagging** consiste en clasificar cada palabra de un texto en su categoría correspondiente: sustantivo, verbo, adjetivo, pronombre o determinante. Observen el ejemplo gráfico: cada palabra recibe una etiqueta (como 'NOUN' para sustantivos o 'VERB' para verbos). En el procesamiento de textos clínicos, esto es vital: nos permite extraer rápidamente todos los sustantivos (que suelen ser síntomas o diagnósticos) e ignorar palabras de conexión."

---

### Diapositiva 11: Tokenización (Segmentación)
* **Archivo:** [slide11.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide11.html)
* **Elementos en pantalla:** Concepto de Tokenización y los desafíos asociados en el procesamiento de texto.
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~240 palabras.

#### Guion Hablado:
"Toda gran tarea comienza con un primer paso. En el procesamiento de lenguaje natural, ese primer paso crítico e indispensable es la segmentación de palabras, técnicamente conocida como **Tokenización**.

`[Clic para revelar ¿Qué es Tokenizar?]`

Tokenizar es el proceso de dividir una cadena continua de texto en unidades individuales más pequeñas y manejables denominadas **tokens**. En la mayoría de los casos, estos tokens corresponden a palabras individuales, pero también pueden ser subpalabras o incluso caracteres individuales. Es la base sobre la que se construye cualquier modelo o análisis de texto posterior. Si la tokenización falla o es imprecisa, todo el pipeline de IA que viene después heredará esos errores.

`[Clic para revelar Desafíos en la Segmentación]`

A primera vista, tokenizar parece una tarea trivial que podría resolverse dividiendo el texto cada vez que encontremos un espacio en blanco. Sin embargo, esto presenta grandes desafíos. En idiomas como el chino, el japonés o el tailandés, no existen espacios físicos de separación entre palabras; la máquina debe deducir dónde termina una palabra y empieza otra.

E incluso en español o inglés, la división simple por espacios es insuficiente. Los signos de puntuación pegados a las palabras, las abreviaturas (como 'Dr.' o 'ej.'), las contracciones y los caracteres especiales requieren de reglas complejas. Por ejemplo, en medicina, no queremos que la abreviatura de una dosis o una temperatura se divida incorrectamente y pierda su significado. Por ello, dependemos de tokenizadores especializados basados en expresiones regulares o en modelos estadísticos avanzados."

---

### Diapositiva 12: Estadísticas del Lenguaje: Riqueza y Zipf
* **Archivo:** [slide12.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide12.html)
* **Elementos en pantalla:** Explicación de Riqueza Léxica y Ley de Zipf, junto con dos gráficos representativos (gráfica de riqueza y distribución de Zipf).
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~260 palabras.

#### Guion Hablado:
"Antes de aplicar algoritmos complejos, es sumamente útil analizar las propiedades matemáticas de nuestro corpus de texto. Dos de las métricas estadísticas más reveladoras son la riqueza léxica y la distribución de frecuencias.

`[Clic para revelar Riqueza Léxica y su gráfica]`

La **Riqueza Léxica** evalúa la diversidad del vocabulario empleado en un texto. Se calcula matemáticamente mediante la relación entre el número de palabras únicas (llamadas 'types') y el número total de palabras en el texto (llamadas 'tokens'). Un texto con un alto ratio de riqueza léxica indica un vocabulario variado y complejo, mientras que un ratio bajo sugiere repetición de palabras. En el ámbito clínico, esto ayuda a comparar la complejidad de las notas redactadas por diferentes especialistas o departamentos.

`[Clic para revelar Ley de Zipf y su gráfica]`

Por otro lado, nos encontramos con una de las leyes más curiosas y consistentes de la lingüística: la **Ley de Zipf**. Esta ley empírica establece que, en cualquier idioma humano, la frecuencia de aparición de una palabra es inversamente proporcional a su rango en la clasificación de frecuencias. 

¿Qué significa esto en términos prácticos? Que unas pocas palabras sumamente comunes (como determinantes y preposiciones) aparecen la inmensa mayoría de las veces, mientras que la inmensa mayoría de las palabras de nuestro vocabulario ocurren muy raramente. 

Observen la gráfica de la esquina inferior derecha: muestra una caída abrupta. Esto nos da una justificación matemática de por qué es tan importante realizar una fase de limpieza de texto, ya que la gran cantidad de palabras muy frecuentes y poco informativas pueden sesgar nuestros modelos."

---

### Diapositiva 13: Estadísticas del Lenguaje: Legibilidad y Comprensibilidad
* **Archivo:** [slide13.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide13.html)
* **Elementos en pantalla:** Fórmulas y escalas de Legibilidad (Flesch-Szigriszt), Comprensibilidad (Crawford) y Legibilidad Mu (μ).
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~280 palabras.

#### Guion Hablado:
"En el procesamiento de textos en español, y muy especialmente en el sector salud, evaluar la complejidad y legibilidad de los textos es fundamental. Si un consentimiento informado o unas instrucciones de alta médica son demasiado complejos, el paciente no los comprenderá, lo que representa un riesgo clínico directo. Para medir esto de forma objetiva, disponemos de tres métricas matemáticas clave.

`[Clic para revelar Legibilidad Flesch-Szigriszt]`

La primera es el índice de **Legibilidad de Flesch-Szigriszt**. Adaptado al español, utiliza la fórmula basada en el promedio de sílabas por palabra y palabras por frase. Nos devuelve una puntuación de cero a cien. Como ven en la tabla, una puntuación entre 60 y 70 se considera un nivel normal (para educación básica), mientras que valores inferiores a 50 indican textos difíciles o universitarios.

`[Clic para revelar Comprensibilidad de Crawford]`

La segunda métrica es la **Comprensibilidad de Crawford**. A diferencia de la anterior, esta fórmula estima directamente el nivel escolar o los años de escolarización requeridos para que una persona comprenda el texto. Analiza la densidad de oraciones y sílabas por cada 100 palabras. El resultado numérico equivale directamente al grado académico necesario.

`[Clic para revelar Legibilidad Mu (μ)]`

La tercera es la **Legibilidad Mu (μ)**. Esta es una alternativa ideal para nuestro idioma porque evita por completo la complejidad de contar sílabas algorítmicamente. En su lugar, calcula el cociente entre el promedio de letras por palabra y su varianza. Un valor alto de Mu indica un texto fácil de leer con palabras cortas y uniformes. Estas métricas nos permiten auditar automáticamente la calidad y accesibilidad de la documentación médica."

---

### Diapositiva 14: Stopwords (Palabras Vacías)
* **Archivo:** [slide14.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide14.html)
* **Elementos en pantalla:** Qué son las Stopwords, por qué es necesario eliminarlas y un diagrama de flujo del filtrado.
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~240 palabras.

#### Guion Hablado:
"Como vimos al estudiar la Ley de Zipf, los textos están plagados de palabras que se repiten constantemente pero que no aportan información sobre el tema del documento. A estas palabras las llamamos **Stopwords** o palabras vacías.

`[Clic para revelar ¿Qué son las Stopwords?]`

Las stopwords son términos extremadamente frecuentes en un idioma que carecen de significado semántico informativo por sí solas. Hablamos de artículos, preposiciones, conjunciones y algunos verbos auxiliares muy comunes. En español, ejemplos típicos son 'un', 'una', 'de', 'con', 'el', 'la', o 'es'. 

`[Clic para revelar ¿Por qué eliminarlas?]`

¿Por qué invertimos tiempo en eliminarlas de nuestro texto durante la fase de preparación de datos? Principalmente por dos razones. Primero, para reducir drásticamente el tamaño del vocabulario que el modelo debe procesar, lo que mejora la eficiencia computacional y ahorra memoria. Segundo, para evitar que nuestros algoritmos estadísticos se confundan al enfocarse en palabras irrelevantes en lugar de los términos verdaderamente informativos.

Observen el diagrama de la derecha: al procesar la frase, el filtro detiene palabras como 'de' o 'la', dejando pasar únicamente las palabras clave con carga semántica. Sin embargo, una advertencia importante en el campo clínico: a veces, palabras que parecen stopwords pueden alterar por completo el sentido de una frase, como el adverbio de negación 'no'. Por lo tanto, la lista de stopwords debe diseñarse con mucho cuidado según la aplicación."

---

### Diapositiva 15: N-gramas
* **Archivo:** [slide15.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide15.html)
* **Elementos en pantalla:** Definición de N-gramas, ejemplos prácticos de bigramas y trigramas, y representación visual en un diagrama.
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~240 palabras.

#### Guion Hablado:
"Una limitación importante de analizar palabras sueltas es que perdemos por completo el orden y la relación de cercanía entre ellas. Para mitigar esto sin recurrir a modelos de aprendizaje profundo extremadamente complejos, utilizamos el concepto de **N-gramas**.

`[Clic para revelar ¿Qué son los N-gramas?]`

Un N-grama es, por definición, una secuencia contigua de 'n' elementos extraída de una muestra de texto. En la gran mayoría de los casos de NLP, estos elementos son palabras, aunque también pueden ser caracteres. Cuando 'n' es igual a uno, hablamos de un unigrama; cuando es dos, de un bigrama; y cuando es tres, de un trigrama.

`[Clic para revelar el Ejemplo Práctico]`

Veamos el ejemplo práctico de la diapositiva con la oración: 'Estoy aprendiendo procesamiento de lenguaje natural'. 

Si extraemos los bigramas (secuencias de longitud dos), obtenemos parejas consecutivas como: ('Estoy', 'aprendiendo'), ('aprendiendo', 'procesamiento'), ('procesamiento', 'de'), y así sucesivamente. Si pasamos a trigramas (longitud tres), la ventana se amplía a ternas como: ('Estoy', 'aprendiendo', 'procesamiento').

Como muestra el diagrama gráfico de la derecha, esta técnica nos permite capturar el contexto local y la estructura de las frases. En medicina, esto es fundamental: la palabra 'infarto' por sí sola es ambigua, pero los bigramas 'infarto agudo' o 'infarto cerebral' definen entidades clínicas precisas y totalmente distintas. Los N-gramas son nuestra primera herramienta para rescatar el contexto perdido."

---

### Diapositiva 16: Representación de Textos: One-Hot Encoding
* **Archivo:** [slide16.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide16.html)
* **Elementos en pantalla:** Concepto de One-Hot Encoding, limitaciones críticas y diagrama vectorial.
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~250 palabras.

#### Guion Hablado:
"Hasta ahora hemos hablado de procesar palabras y textos, pero las computadoras no entienden de letras; solo entienden de números, matrices y vectores. ¿Cómo representamos entonces una palabra en un formato matemático? La aproximación clásica más sencilla es el **One-Hot Encoding** o codificación uno-caliente.

`[Clic para revelar ¿Qué es One-Hot Encoding?]`

Este método consiste en representar cada palabra del vocabulario como un vector binario de gran tamaño. El tamaño del vector es exactamente igual al tamaño total de nuestro vocabulario, al que llamamos V. Este vector tendrá un valor de uno en la posición que corresponde al índice de la palabra y un valor de cero en todas las demás posiciones. Si nuestro vocabulario tiene diez mil palabras, cada palabra se representará con un vector de tamaño diez mil lleno de ceros y un único uno.

`[Clic para revelar las Limitaciones Críticas]`

Aunque es muy fácil de implementar, este enfoque tiene dos limitaciones críticas que ven en pantalla. 

La primera es la **dispersión o *sparseness***: al ser vectores gigantescos donde casi todos los elementos son cero, desperdiciamos una cantidad enorme de memoria y capacidad de cómputo. 

La segunda, y más grave, es que **carece de semántica**. Geométricamente, todos los vectores resultantes son ortogonales entre sí. Esto significa que la distancia matemática entre la palabra 'médico' y 'paciente' es exactamente la misma que entre 'médico' y 'plátano'. El modelo no tiene forma de saber que las dos primeras palabras guardan una estrecha relación conceptual. Para solucionar esto, necesitaremos representaciones más avanzadas."

---

### Diapositiva 17: Bolsa de Palabras (Bag of Words)
* **Archivo:** [slide17.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide17.html)
* **Elementos en pantalla:** Definición de Bag of Words (BoW), extensión a Bolsa de N-gramas y una tabla de frecuencias representativa.
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~250 palabras.

#### Guion Hablado:
"Si One-Hot Encoding nos sirve para representar palabras individuales, ¿cómo representamos un documento completo, como un informe médico o un correo electrónico? Aquí es donde entra el modelo clásico de **Bolsa de Palabras**, o *Bag of Words* (BoW).

`[Clic para revelar ¿Qué es Bag of Words?]`

Este modelo consiste en representar un documento completo como el conjunto o 'saco' de las palabras que contiene. Bajo esta premisa, ignoramos por completo el orden original en el que aparecen las palabras y la estructura gramatical del texto. Sin embargo, conservamos un dato muy valioso: la frecuencia de ocurrencia de cada palabra. 

Como ven en la tabla de frecuencias de la derecha, cada fila representa un documento y cada columna una palabra del vocabulario general. Los valores indican cuántas veces aparece cada término en dicho documento.

`[Clic para revelar Bolsa de N-gramas]`

A pesar de su utilidad para tareas de clasificación básicas, ignorar el orden puede generar problemas semánticos graves. Para paliar esto, extendemos el modelo a la **Bolsa de N-gramas**. Al contar la frecuencia de secuencias de palabras en lugar de términos individuales, el modelo logra conservar contexto local clave. 

Por ejemplo, un modelo de Bolsa de Palabras unigramas trataría igual las frases 'es bueno, no malo' y 'es malo, no bueno' porque contienen las mismas palabras. En cambio, una bolsa de bigramas detectará la diferencia fundamental entre 'no bueno' y 'no malo'. Es un avance simple pero sumamente efectivo."

---

### Diapositiva 18: Word Embeddings y Word2Vec
* **Archivo:** [slide18.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide18.html)
* **Elementos en pantalla:** Concepto de Word Embeddings, el modelo Word2Vec de Mikolov, y las dos arquitecturas CBOW y Skip-gram con su esquema gráfico.
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~260 palabras.

#### Guion Hablado:
"Para superar definitivamente la falta de semántica del One-Hot Encoding y la rigidez de la Bolsa de Palabras, la Inteligencia Artificial dio un salto cuantitativo con la invención de los **Word Embeddings** o incrustaciones de palabras.

`[Clic para revelar ¿Qué son los Word Embeddings?]`

A diferencia de los vectores dispersos y gigantescos del One-Hot, los embeddings son representaciones vectoriales densas y de baja dimensión, típicamente de 100 a 300 dimensiones. La magia de este enfoque es que los vectores se aprenden de forma que capturen la semántica y relaciones de las palabras. Palabras con significados o usos similares se proyectan en puntos geométricamente cercanos en este espacio multidimensional.

`[Clic para revelar Word2Vec y sus arquitecturas]`

El modelo pionero que popularizó esto fue **Word2Vec**, propuesto por Tomas Mikolov y su equipo en Google en 2013. Utiliza una red neuronal simple entrenada con corpus masivos para aprender estos vectores basándose en la premisa lingüística de que 'conocerás a una palabra por las compañeras que tiene'.

Word2Vec implementa dos arquitecturas de entrenamiento que vemos en el gráfico:
La primera es **CBOW** (Bolsa de Palabras Continua), la cual intenta predecir una palabra central a partir de las palabras de su contexto vecino.
La segunda es **Skip-gram**, que hace lo contrario: toma una sola palabra e intenta predecir cuáles son las palabras de su contexto circundante. Este avance permitió a las máquinas realizar analogías vectoriales famosas como 'Rey menos Hombre más Mujer es igual a Reina', revolucionando el NLP."

---

### Diapositiva 19: Pipeline de Preprocesamiento Clásico
* **Archivo:** [slide19.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide19.html)
* **Elementos en pantalla:** Dos bloques de pasos de procesamiento (Limpieza inicial y Segmentación/Reducción) y un diagrama que ilustra Stemming y Lematización.
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~250 palabras.

#### Guion Hablado:
"Ahora que hemos revisado todas las piezas del rompecabezas, consolidemos este conocimiento observando cómo se estructuran de forma secuencial en una canalización o **pipeline** de procesamiento y limpieza clásica de texto.

`[Clic para revelar 1. Limpieza Inicial]`

El proceso se divide en dos grandes fases. La primera es la **Limpieza Inicial**, cuyo objetivo es eliminar el ruido. Comenzamos convirtiendo todo el texto a minúsculas, lo que evita que el sistema trate 'Médico' con mayúscula y 'médico' con minúscula como palabras distintas. Luego, removemos números e hipervínculos si no aportan valor clínico relevante, y eliminamos caracteres especiales y signos de puntuación innecesarios que puedan entorpecer el análisis.

`[Clic para revelar 2. Segmentación y Reducción con su diagrama]`

La segunda fase es la **Segmentación y Reducción**. Aquí es donde el texto ya limpio se tokeniza en palabras individuales. Posteriormente, aplicamos el filtro de stopwords para descartar conectores irrelevantes. 

Finalmente, realizamos la reducción léxica. Como muestra el diagrama de la derecha, tenemos dos opciones:
El **Stemming**, que corta las palabras de forma heurística para quedarse con una raíz básica o 'stem' (que a veces no es una palabra real, como 'gat' para 'gatos' y 'gatitos').
Y la **Lematización**, un proceso más avanzado que utiliza diccionarios y análisis gramatical para reducir la palabra a su lema base o forma de diccionario (como llevar 'pacientes' a 'paciente' o 'atendió' a 'atender'). Este pipeline es el estándar para preparar datos antes de entrenar cualquier modelo."

---

### Diapositiva 20: Cierre y Preguntas
* **Archivo:** [slide20.html](file:///d:/EATS/repos/diplomado_neurum_2026/12_NLP_I/slides/slide20.html)
* **Elementos en pantalla:** Diapositiva de cierre, llamado a preguntas y botón para volver al directorio.
* **Duración estimada:** 2 minutos.
* **Palabras estimadas:** ~230 palabras.

#### Guion Hablado:
"Con esto cerramos los conceptos fundamentales de nuestra primera sesión introductoria al Procesamiento de Lenguaje Natural en este módulo doce de Neurum. Hemos recorrido un camino que va desde los fundamentos filosóficos de la inteligencia artificial con Alan Turing, pasando por las complejidades inherentes al lenguaje clínico, hasta llegar a las técnicas de ingeniería de datos que nos permiten tokenizar, limpiar, filtrar y transformar palabras en vectores semánticos densos.

`[Clic para revelar Preguntas y Comentarios]`

Espero que esta sesión les haya brindado una perspectiva clara de cómo la tecnología puede comenzar a decodificar la narrativa médica, abriendo un abanico enorme de posibilidades para la analítica clínica y la mejora en la atención de la salud.

Quiero abrir el espacio para escuchar sus dudas, comentarios o reflexiones sobre lo que hemos discutido hoy. ¿Cómo visualizan la aplicación de estas técnicas en sus respectivos entornos profesionales? ¿Qué desafíos específicos de legibilidad o tokenización anticipan en sus propios proyectos con historias clínicas? 

`[Clic para revelar enlace de retorno]`

Los invito a participar activamente en nuestro foro de discusión y a revisar los materiales complementarios en el directorio de la plataforma. Agradezco enormemente su atención e interés en esta sesión. Quedo atento a sus preguntas. ¡Muchas gracias a todos!"
