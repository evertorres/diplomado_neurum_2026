# **Plan de Contenido: Inteligencia Artificial en Salud**

**De los Fundamentos Algorítmicos a la Confianza Médica**

## **🗂️ Estructura Diapositiva por Diapositiva (15 Diapositivas)**

### **Diapositiva 1: Portada (Title\_Slide)**

* **Título:** IA en la Medicina Moderna  
* **Subtítulo:** De la base matemática a la práctica clínica ética y segura.  
* **Diseño Visual:** Estructura limpia y minimalista.  
* **Soporte Gráfico (SVG Recomendado):** Un fondo interactivo o patrón geométrico dinámico que represente una red neuronal abstracta con nodos interconectados mediante líneas de pulso suaves.  
* **Notas del Orador:** Bienvenidos a esta presentación. Hoy realizaremos un viaje desde la física y matemática básica que hace posible la inteligencia artificial, pasando por los modelos generativos y LLMs, hasta llegar a la evaluación clínica estricta y los retos éticos y de equidad que enfrentamos en el sector salud hoy en día.

### **Diapositiva 2: Agenda / Índice (Tiled\_Text\_With\_Icons)**

* **Título:** Estructura de la Presentación  
* **Diseño Visual:** Tres contenedores (tiles) alineados horizontalmente que dividen la sesión.  
* **Soporte Gráfico (SVG Recomendado):** Tres iconos vectoriales limpios y personalizados para cada sección:  
  1. Sección 1: Un ábaco o calculadora digital estilizada (Fundamentos e Historia).  
  2. Sección 2: Un microchip con ondas neuronales (IA Generativa y LLMs).  
  3. Sección 3: Un escudo clínico con una cruz médica (Evaluación y Retos Clínicos).  
* **Contenido de los Contenedores:**  
  1. **Fundamentos e Historia:** La evolución de la IA, diferencias conceptuales (ML, DL) y el procesamiento del lenguaje.  
  2. **IA Generativa y LLMs:** Arquitectura Transformer, taxonomías de modelos y evolución técnica.  
  3. **Evaluación y Retos Clínicos:** Benchmarks de salud, vulnerabilidades de datos, sesgos y el estándar FUTURE-AI.  
* **Notas del Orador:** He organizado esta presentación en tres grandes bloques para facilitar la absorción del contenido. Primero comprenderemos de dónde viene la tecnología; luego profundizaremos en la revolución de los Transformers y los modelos de lenguaje; y finalmente nos enfocaremos en lo crucial para nosotros: cómo evaluar estos modelos y mitigar sus riesgos en la práctica médica real.

### **Diapositiva 3: Historia y Ciclo S de la IA (Timeline)**

* **Título:** Evolución de la IA y sus Inviernos  
* **Diseño Visual:** Timeline o línea de tiempo horizontal.  
* **Soporte Gráfico (SVG Recomendado):** Una curva en ![][image1] estilizada que muestre los picos de auge y los valles de los "inviernos de la IA", con nodos interactivos en los hitos históricos clave.  
* **Contenido de los Hitos:**  
  * 1950 \- Alan Turing: Propuesta del Turing Test (¿Pueden las máquinas pensar?).  
  * 1980 \- Sistemas Expertos: Primer auge comercial seguido del primer "invierno" por limitaciones técnicas.  
  * 1995/2006 \- ML & Deep Learning: Resurgimiento del aprendizaje automático y redes neuronales profundas adaptables.  
  * 2017+ \- Era Generativa: Publicación de "Attention is all you need" (Transformers) y la explosión de los LLMs.  
* **Notas del Orador:** La inteligencia artificial no es nueva. Ha vivido ciclos de enorme entusiasmo científico seguidos de "inviernos" donde las promesas superaban la capacidad computacional. Lo que vivimos hoy es la aceleración de la curva S gracias a la combinación de algoritmos revolucionarios y un poder computacional sin precedentes.

### **Diapositiva 4: Conceptos Clave (Two\_Column\_Tiled\_Text)**

* **Título:** IA, Machine Learning y Deep Learning  
* **Diseño Visual:** Dos columnas simétricas con cajas de contenido estructurado.  
* **Soporte Gráfico (SVG Recomendado):** Un diagrama de Euler concéntrico que muestre la jerarquía de inclusión: el círculo exterior es la Inteligencia Artificial, el intermedio es Machine Learning y el núcleo es Deep Learning.  
* **Contenido:**  
  * Columna 1 (La Jerarquía):  
    * **Inteligencia Artificial:** Sistemas computacionales diseñados para emular el razonamiento humano.  
    * **Machine Learning (ML):** Subcampo donde las máquinas aprenden patrones a partir de datos sin ser programadas explícitamente.  
  * Columna 2 (El Salto Adaptativo):  
    * **Deep Learning (DL):** Redes neuronales de múltiples capas capaces de adaptarse de manera autónoma a datos jerárquicos complejos.  
* **Notas del Orador:** Es común confundir estos términos. Piensen en la IA como el concepto macro. El Machine Learning es el método por el cual entrenamos a las computadoras para reconocer patrones en los datos. Y el Deep Learning es la especialización que utiliza redes neuronales profundas para modelar relaciones extremadamente complejas, imitando el procesamiento biológico.

### **Diapositiva 5: Pilares del Sistema (Tiled\_Text\_With\_Icons)**

* **Título:** Componentes de un Sistema de IA  
* **Diseño Visual:** Matriz de 4 cuadrantes (2x2) de alto contraste visual.  
* **Soporte Gráfico (SVG Recomendado):** Cuatro mini-esquemas técnicos vectoriales para cada cuadrante:  
  1. *Datos:* Un cilindro de base de datos interconectado.  
  2. *Algoritmos:* Una serie de engranajes lógicos matemáticos.  
  3. *Modelos IA:* Un grafo de red neuronal simple y compacto.  
  4. *Poder Computacional:* Un rack de servidores o clúster de GPUs.  
* **Contenido de los Contenedores:**  
  1. **Datos:** El combustible. Definen el alcance y rendimiento del modelo. En medicina, abarcan desde notas clínicas hasta genómica.  
  2. **Algoritmos:** Las instrucciones matemáticas sistemáticas para procesar los datos.  
  3. **Modelos IA:** Las representaciones matemáticas entrenadas que toman decisiones finales.  
  4. **Poder Computacional:** La infraestructura física indispensable (GPUs/TPUs) para el entrenamiento de trillones de parámetros.  
* **Notas del Orador:** Para que un sistema de IA funcione, necesitamos cuatro pilares simbióticos. Sin datos representativos, el modelo está sesgado; sin algoritmos refinados, no hay aprendizaje; sin poder de cómputo, es imposible procesar la escala actual de la medicina; y el modelo final es la síntesis de todo este ecosistema.

### **Diapositiva 6: Datos Biomédicos y su Complejidad (Image\_Right\_Text\_Left)**

* **Título:** El Reto del Big Data en Salud  
* **Diseño Visual:** Texto estructurado a la izquierda, diagrama comparativo a la derecha.  
* **Soporte Gráfico (SVG Recomendado):** Un diagrama de división clara (bipartito) que ilustre el contraste entre:  
  * *Lado Izquierdo (Estructurado):* Una tabla médica limpia con datos demográficos, códigos CIE-10 y dosis exactas.  
  * *Lado Derecho (No Estructurado):* Una silueta de un historial clínico en texto libre, una señal de electrocardiograma (ECG) analógica y una radiografía simplificada.  
* **Contenido:**  
  * **Datos Estructurados:** Demografía del paciente, códigos CIE-10, dosis de medicamentos y laboratorios numéricos (fáciles de almacenar y procesar).  
  * **Datos No Estructurados:** Notas médicas de texto libre, audios de consultas, imágenes diagnósticas (radiografías) y publicaciones científicas (complejos, representan el 80% del valor clínico y requieren procesamiento de lenguaje natural avanzado).  
* **Notas del Orador:** Los datos médicos son únicos en su complejidad. El 80% de la información valiosa de un paciente reside en datos no estructurados, como la narrativa de la evolución clínica escrita por el médico. De ahí surge la necesidad crítica del NLP para estructurar y extraer sentido de estas notas.

### **Diapositiva 7: La Neurona Matemática (Two\_Column\_Tiled\_Text)**

* **Título:** De la Biología a la Matemática  
* **Diseño Visual:** Comparativa de dos columnas con alineación simétrica.  
* **Soporte Gráfico (SVG Recomendado):** Diagrama esquemático de una neurona computacional donde se aprecie el flujo desde las entradas ![][image2], pasando por los pesos ![][image3], un nodo sumatorio ![][image4], la función de activación ![][image5] y el resultado ![][image6].  
* **Contenido:**  
  * Columna 1 (Inspiración Biológica): La neurona biológica recibe señales eléctricas a través de las dendritas, las procesa en el cuerpo celular (soma) y transmite la respuesta a través del axón hacia las sinapsis de otras neuronas.  
  * Columna 2 (La Abstracción Matemática): Se modela mediante la ecuación fundamental de activación que rige las redes neuronales:  
    ![][image7]  
    Donde ![][image8] representa los datos de entrada, ![][image9] los pesos de aprendizaje, ![][image10] el sesgo y ![][image5] la función de activación.  
* **Notas del Orador:** La genialidad del Deep Learning es que toma prestada la arquitectura de procesamiento de nuestro propio cerebro. Cada neurona matemática calcula la suma ponderada de sus entradas, le añade un sesgo y aplica una función para decidir si pasa o no la información a la siguiente capa del modelo.

### **Diapositiva 8: Procesamiento de Lenguaje Natural (Image\_Right\_Text\_Left)**

* **Título:** Cómo la IA Comprende el Lenguaje  
* **Diseño Visual:** Texto explicativo a la izquierda, gráfico de coordenadas a la derecha.  
* **Soporte Gráfico (SVG Recomendado):** Un plano bidimensional (![][image11]) interactivo que represente un espacio vectorial de palabras (*Word Embeddings*). Debe ilustrar la cercanía semántica agrupando palabras relacionadas en burbujas de colores (ej. un grupo con "médico", "estetoscopio", "tratamiento" y otro grupo lejano con "rey", "reina", "corona").  
* **Contenido:**  
  * **Preprocesamiento y Tokenización:** Desglose del texto clínico en fragmentos mínimos (*tokens*) para analizar frecuencias, n-gramas y dependencias sintácticas.  
  * **Word Embeddings:** Conversión de términos en vectores numéricos de alta dimensión. El modelo agrupa conceptos que comparten contextos clínicos similares en regiones geográficas cercanas del espacio matemático.  
* **Notas del Orador:** ¿Cómo lee una computadora? No comprende letras; comprende números. Primero tokenizamos el texto, y luego utilizamos Word Embeddings, que posicionan cada palabra en un espacio multidimensional según su significado. Así, la máquina entiende que "remedio" y "tratamiento" tienen un contexto e intención clínica similar.

### **Diapositiva 9: Transición a la Era Generativa (Section\_Title)**

* **Título:** La Revolución Generativa  
* **Subtítulo:** De entender y clasificar el lenguaje a razonar sobre casos clínicos complejos y generar respuestas.  
* **Diseño Visual:** Diapositiva de transición limpia, tipografía destacada y foco de atención absoluto en el cambio de bloque.  
* **Soporte Gráfico (SVG Recomendado):** Un diseño minimalista que represente un haz de luz o vector de energía dividiendo la IA analítica tradicional de la IA generativa moderna.  
* **Notas del Orador:** Hasta aquí, la IA se limitaba mayormente a clasificar y predecir. Ahora entraremos al segundo bloque: la IA Generativa. Veremos cómo la introducción de los "Transformers" cambió para siempre el paradigma, permitiendo a los modelos no solo leer, sino redactar, razonar y proponer soluciones.

### **Diapositiva 10: La Arquitectura Transformer (Tiled\_Text\_With\_Icons)**

* **Título:** El Poder de los Transformers  
* **Diseño Visual:** Tres contenedores con iconos geométricos y descripciones.  
* **Soporte Gráfico (SVG Recomendado):** Un esquema dinámico en tres bloques paralelos que muestre los núcleos de la arquitectura Transformer:  
  1. *Paralelización:* Líneas horizontales paralelas que avanzan al mismo tiempo.  
  2. *Codificación Posicional:* Un vector de entrada con índices numerados.  
  3. *Auto-Atención:* Líneas interconectadas que unen dinámicamente diferentes palabras dentro de una misma frase, simulando la "atención ponderada".  
* **Contenido de los Contenedores:**  
  1. **Procesamiento en Paralelo:** Supera las limitaciones de las redes secuenciales antiguas al procesar oraciones completas a la vez, acelerando radicalmente el entrenamiento con grandes volúmenes de datos.  
  2. **Codificación Posicional:** Sello de tiempo matemático que preserva el orden de cada palabra dentro del texto, garantizando la coherencia semántica.  
  3. **Mecanismo de Auto-Atención:** Capacidad de la red para evaluar la relación e importancia relativa de cada palabra con respecto a las demás dentro de una misma oración clínica.  
* **Notas del Orador:** En 2017 se publicó el histórico artículo "Attention is all you need". Introdujo la arquitectura Transformer. Sus tres innovaciones principales permiten que los modelos actuales lean expedientes médicos completos en segundos y comprendan que un síntoma mencionado al inicio está conectado directamente con un diagnóstico al final del texto.

### **Diapositiva 11: Taxonomía de los LLMs (Table)**

* **Título:** Clasificación de Grandes Modelos (LLMs)  
* **Diseño Visual:** Tabla comparativa estructurada y altamente legible.  
* **Soporte Gráfico (SVG Recomendado):** Filas con sutil sombreado interactivo para facilitar la lectura del usuario.  
* **Contenido de la Tabla:**  
  * **Tipo de Arquitectura** | **Función Principal** | **Modelos de Referencia**  
  * *Codificadores (Encoder-only)* | Clasificación de textos, extracción de entidades (NER), preguntas y respuestas extractivas. | RoBERTa, DeBERTa, ALBERT.  
  * *Decodificadores (Decoder-only)* | Generación de texto creativo, predicción de la siguiente palabra. | GPT-3, GPT-4, LLaMA, Mistral.  
  * *Híbridos (Encoder-Decoder)* | Traducción automática, resúmenes médicos abstractivos, generación interactiva de texto. | BART, T5, FLAN-T5.  
* **Notas del Orador:** No todos los LLM son iguales. Dependiendo de si usan solo el codificador, el decodificador o ambos, su utilidad clínica varía. Para buscar un dato específico en una historia clínica usamos codificadores. Para generar un reporte médico de alta o redactar un resumen, preferimos decodificadores o arquitecturas híbridas.

### **Diapositiva 12: Evaluación General e HLE (Area\_Chart\_For\_Trends)**

* **Título:** HLE: El Examen Final de la Humanidad  
* **Diseño Visual:** Distribución porcentual limpia del nuevo estándar de evaluación.  
* **Soporte Gráfico (SVG Recomendado):** Un gráfico circular interactivo o un diagrama de piezas de rompecabezas interconectadas que representen las disciplinas del benchmark de nivel doctorado *Humanity's Last Exam (HLE)*:  
  * Matemáticas: 41%  
  * Biología y Medicina: 11%  
  * Ciencias de la Computación: 10%  
  * Física: 9%  
  * Humanidades/Ciencias Sociales: 9%  
  * Química: 7%  
  * Otros: 9%  
* **Contenido:**  
  * **Saturación de Benchmarks:** Los modelos de IA modernos obtienen casi el 100% en exámenes tradicionales como MMLU o GSM8K.  
  * **Humanity's Last Exam (HLE):** Un examen interdisciplinario de nivel de doctorado diseñado para medir la frontera real del razonamiento científico.  
  * **Relevancia Médica:** La Biología y Medicina componen el segundo bloque temático más grande de esta evaluación global de frontera.  
* **Notas del Orador:** Evaluar estas inteligencias es sumamente complejo. Los benchmarks tradicionales están saturados; los modelos obtienen casi el 100%. Por ello se creó "Humanity's Last Exam" (HLE), que recopila preguntas tan difíciles que requieren nivel de doctorado para ser resueltas. Es fascinante que el 11% de este examen experto esté compuesto exclusivamente por Biología y Medicina.

### **Diapositiva 13: Evaluación en el Área de la Salud (Table)**

* **Título:** Estándares Clínicos de Evaluación  
* **Diseño Visual:** Tabla ejecutiva de alta legibilidad basada en la revisión sistemática de *JAMA 2025*.  
* **Contenido de la Tabla (Recomendaciones JAMA 2025):**  
  * **Recomendación Clave** | **Estado Actual** | **Justificación Clínica**  
  * *Usar Datos Reales* | Solo 5% de estudios los usan | La práctica clínica real es mucho más compleja que los datos de laboratorio.  
  * *Priorizar Tareas Administrativas* | Evaluación muy limitada | El ROI administrativo en hospitales es inmenso y seguro de implementar.  
  * *Definir y Cuantificar Sesgo* | Solo 15.8% lo evalúa | Mandatorio para garantizar la equidad de acceso al diagnóstico clínico.  
  * *Reportar Modos de Falla* | No existe plataforma global | Permite el análisis de causa raíz para evitar desenlaces clínicos graves.  
* **Notas del Orador:** La revista *JAMA* publicó en 2025 una revisión sistemática contundente. Nos advierte que la mayoría de las evaluaciones de LLMs en salud se hacen en entornos artificiales. Para implementar IA de forma segura en nuestros hospitales, debemos evaluar con datos de pacientes reales, cuantificar activamente los sesgos y reportar de manera transparente los errores del sistema.

### **Diapositiva 14: Retos Críticos en Medicina (Two\_Column\_Tiled\_Text)**

* **Título:** Seguridad, Privacidad y Sesgos  
* **Diseño Visual:** Dos columnas simétricas con cajas de datos de alto impacto analítico.  
* **Soporte Gráfico (SVG Recomendado):** Un diagrama que compare esquemáticamente:  
  * *Columna 1 (Inyección de datos):* Una jeringa o vector inyectando un fragmento de código rojo (0.1% de envenenamiento) en un flujo de datos limpio, alterando por completo las salidas lógicas del modelo.  
  * *Columna 2 (Sesgo Demográfico):* Gráficos de barras simplificados que ilustren la disparidad de estimaciones de GPT-4 (basados en el estudio de *The Lancet 2024*) frente a la prevalencia real en diferentes etnias y géneros.  
* **Contenido:**  
  * Columna 1 (Envenenamiento y Privacidad):  
    * **Ataques de Envenenamiento de Datos (Nature Medicine 2025):** Inyectar solo el 0.1% de datos alterados sobre vacunas en el conjunto de entrenamiento desestabiliza las recomendaciones médicas del modelo.  
    * **Soluciones de Privacidad:** Adopción de Aprendizaje Federado y Datos Sintéticos controlados (como *Synthea*) para cumplir con leyes como HIPAA y GDPR.  
  * Columna 2 (Sesgos Algorítmicos):  
    * **La Evidencia de The Lancet (2024):** GPT-4 tiende a perpetuar sesgos históricos de raza y género, sobreestimando o subestimando prevalencias clínicas reales en patologías como preeclampsia, diabetes tipo 2 y lupus.  
* **Notas del Orador:** Aquí entramos en el terreno de las realidades complejas. *Nature Medicine* nos alertó que los modelos de salud son altamente vulnerables a ataques de envenenamiento de datos, donde la inyección maliciosa de información distorsiona los diagnósticos. Por otro lado, *The Lancet* evidenció que modelos líderes como GPT-4 aún arrastran sesgos históricos, estimando de manera errónea riesgos de enfermedades críticas según la raza o género del paciente.

### **Diapositiva 15: Confianza y Cierre (Q\&A)**

* **Título:** El Estándar FUTURE-AI y Cierre  
* **Diseño Visual:** Cierre formal con cita destacada y llamada de atención sobre principios de confianza.  
* **Soporte Gráfico (SVG Recomendado):** Una representación limpia de los seis pilares del consenso internacional **FUTURE-AI** distribuidos de manera circular u horizontal con sutiles iconos vectoriales:  
  * **F** (Fair \- Equitativo)  
  * **U** (Universal)  
  * **T** (Traceable \- Trazable)  
  * **U** (Usable)  
  * **R** (Robust \- Robusto)  
  * **E** (Explainable \- Explicable)  
* **Contenido:**  
  * **Consenso FUTURE-AI (BMJ 2025):** Marco ético regulatorio internacional indispensable para desplegar algoritmos de IA en sistemas de salud reales de manera segura.  
  * **Cita:** *"Cualquier tecnología suficientemente avanzada es indistinguible de la magia."* — Arthur C. Clarke.  
* **Notas del Orador:** Para navegar este futuro con seguridad, la comunidad científica ha diseñado el consenso FUTURE-AI publicado en el *BMJ*. Esta guía nos da la hoja de ruta para exigir que cada herramienta de IA que entre a un hospital sea robusta, explicable y, sobre todo, equitativa. Con esto cierro la presentación de hoy y abro el espacio para sus preguntas. Muchas gracias.

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAaCAYAAACHD21cAAAB/klEQVR4Xo1SzSsFURSf6XlFXpRnqDf3a56xUFZGyc5KVjYUxe4tlIUViWwlZSEW1nY2VvaSJSsLG6Uo/4CFJc/vfszcOx/KqTNz7u+c8zsf93pepfhFQEF+GZboX5j+593ylGoBzyC3jAUtlrEbCYaDhhBijlI6P9ZuD0pf2Aqb43Ec5BJT4iRJ6oyzA874K2dsi3O2yTl/xPlEROIe9oTNAoPu2O9hjF1Ar0ZGR/tTXxiGTSGiB8b4XRAEjRTPBOyz0He0N6mZrBOV9qFnGs7m0gFwHKLND1QgxZnh26GULGbRTkEvisQlZuliKXs41hRoIgkhMaFkSB3cJCmREKuM8y5Xyr5Bcgu7E8fxQCE0L0kyVcdijhD8jb8hUCRPqn3PKWbnzEkNwRNo+RiJnzIZW90otKmsmpzB17eiUWMheQGJP+hgV+W5EbifNpznOPXoZZh7xQdbTuD7wrxraYop5nuU0EU4bsDem9U01CBdR7WXVqtFSwvFPIfQLxGJGadZDw8hlovBppcMZN1BMNxAtWu0sw19hkq7gyqn+L+hixWdktIZIYT2ycVIWz5wVJlG0nIUiTnV+n9Es+WmyJ2sXW6gQiydvS132BRwTBVotlumLiOeBXUdZVV1p9zmnOPJBVdWsOK8uso2/06vrGxBXdsYGWphB3MkDcHnFxdmTftg9WD0AAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAaCAYAAABCfffNAAAC8klEQVR4XoVWPYgTQRTehQgnsVGSrCa7M7uJv5wo3NZXnSm1EAQhFlbaWNgdHqJwKoqVFmojgo2Knf1xCIIKV9gLFlZWlhY2F783v28mu+e7m52Z9/N935vZhCQJWaofqZqdg83NFqbTw+c3rVoc0T7Ypuqv0Ri7F84s6GEhgetjwXSB/3+mM/bK47FmMdqcezgc9qSUXzDmNISefwkh6tFolGP9jfnn8H8fj8fHqRbrK7bOxD5kg0G3gUabkGLdAN1wTpMD34YBuhjHqqo6A/92VVZljEkWuJA4M2rWeZieUgpNIuTMV+gwYrdRM6VMe08NXNqEkOeN2g3aUyKNEgrh+6FJrABbI5bhf1zX9T7rs3VqHbBhA4BzKNgty/K1cyql8j7AnoRdKutg/xB1yyzfdeOMs6KTGkB/PIm6pxpAj+guiITHiiJfRZO3nF4OFiy1WLUkQCLB2MqyQXcFR1CV5dM8z49CrRZQaZJ+v38A5C/wZhYex1oa7ZkB5AjGT4yPBmSK+7hJBapLYQQMsi7mGQRc9+L9CmLXULvW+ElXJEKR7Cj1Ur6aTCYDRSLlKex/k4CiKCaYn5EQW2spcB8dYDwA0dQjG0tBC7UH8TruUDdQchfjko2zLj8B4E4ziJniDnyTSdKjI4JSAO2C8B262W/jjGSO8Za/stZwtIcRe46xaeMcX1mWZV2QbKHdv0VerCqnyaCjoaOie0GHdVipLC2r8io+9WeR9xmEMgr7Bb2iOLKX2HQ4UL8HEqG6vKcrIpY06eR5cQz3dQEY7xOqD+O+hF5V+sL0MQ8G8hUc4aHFQ08sQAci3oDksvfHufHeWOhu2BmVUr+BX9HRadzpNeVtwXTm4w3AC9UpfRufAMk27nWzrMqTNoXhxEWRGbU0Fiidg+60WsJxLfGM0DjRnpzNp2B9THm0t2YV25BdBwg8RrPdR/Bpy48IMlcTulusBSgQteANBDUYBVmCW7IjdACtalup7b83tdGeNmHW/Q8Op40or5ABhQAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAaCAYAAACzdqxAAAACeUlEQVR4Xp1VvYoUQRCe5jxQUA6VFY6d7Z9ZYVGjc+GeQFMDFc7ETPAJTjA0NBMUg1MfwAMDA5PjnsBIwUgMxMxALhe89avunu7qmh4Vv6W2un67qnp6pmk8FH4ZfM0xpq8iOIuQv2UQVagkMwPpp9PpeWPMpiTtud40OqyD3JNO3Fp3MmeMmEwmp621B3Baaa2/gb8A7WXSaa0DvQJ9gPzTxxi9An9GNRbdE4NhS2tzBH7knNtOu3r76FzWEHMd3XxB3NdZ206DmiWmf7SzA4dj0KduPr8Qg4Vj3oY4Udu25xBziK7vBENviVgul+vYnVpeESc5W5ucqQKM4wpinmN5wiv47vQ3R6VUMZyOUcFONOeiUU16AtImvguF8zkLYa3XiuxN4zBjmnWkrbLIIIVUWc6IbUl1gKLdH5hw2ofdvNtIFu5WA3dgHSW+XF5dxyj2MZIV+EPullAprB9ToQ9CVjnnDCr/jKp/zWazG4WfyFjTBc1Q6VVIeosSm3AB2MEwsE7/jP7+KKrabltn9/mc/w9UvG9ANc5iFEa/JT4sJmpYs8SF3zCs67oNOjxH13toFmCXnu+SeBToxiHpYxzctWguUd9IGbogauQc6DFD+09wWDelLSP0n4pR/n1xETF7/vVZ2VjBuItX4i6tR0sTJiQ9hbiX6PJ+aYqr8Gjpp/Llw9PLDxjGddk6+x6n/APxl5gxwFlL74ePoHtwvt2T8dwkmQiVPULLr+H7XdObMFz9d9D7r0jaerFYnIHhjf96gIgnMpybvDYm8uR7txxcfYzs4yiFMfyLTzOcZR9YCy90NYcSOdkwqYiuilFZ2mSirJU6CW7/DcKUfx6E2in/AAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAaCAYAAAC+aNwHAAAB0ElEQVR4XoVUrU4DQRDuBlAggNA0NNeZO1lFQoNDYngAVD14DI+AqceQEHwtCYI34BmwSAShGAR8s7uzN7t3odPOdX6+b352cx0Morj0WCfOf9TOf1WsL7ZrKWqUlExcASqn65Dzhi5UCN8OoCfWWsx0zsy/QSmq+pmuiGiWV/MajLquHwH6IeLTYr4NYrpE7h067e4CQeU9JF+hb03TjCSm9UXG4/EBJntC/rB3jaZujpD8JOYlBtqMGTcajbbFkAKY7G44HO4kkrkknAPPmfgXo16b2BSxhUCx3i4TXWQkET0CAO8xIvan05jYQMfbpq6vFNcvTvbnPVR/hcpJv2ONr3jq35NJdWLB/qbLMwBxhu4rTOH3l7gfn+lFdm+RuRUdAdNcumP8G81IAUyykIaJZLn+1QgBB+IDCD+s+yM3mx1v+RtIpAj2HyPoHu6f+K2O95+kIKsVSviYC/sTr1BoicBmQirEOOr7X9z3GYhy4nLaqh/wn6uq2jdUpRQVbcBM1Eqb7PByCely3CyWLj5L2MpFlwLfE7CST+Cyv6VY2BmUGKotzpLyPhaXcZJkpLUHVr4HBl4wk/tfRe2qzwzrnT52B9lK29UWjU87Er5/m6VNq+sV2OUAAAAASUVORK5CYII=>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAZCAYAAADXPsWXAAABzElEQVR4XoVTPUsEMRC9hbvKQhTxwLtNslvYaOWCP0CutrERrrC0sdXSP2FjIViJIP4JrQRtbaxFQbDTUtY3+diZZIM+vGTmzcybSbIOBn+iiMxC+oFM4SifGhb3xwneicoF3xEZfYvQRG6MoBS6RwFaexXM0VZOy12t9Rd+rdaq1Uq3SumXuq7XbU5BOdNlxB9cjo3/GGMOWNELovjIJ93CHUbHIqGy3ETsCXk7jkkBSilVI+ldaf2KvfK0BaZaNJW5qSqzzUUBIYv2YjBE8bWfZh5SVsfjBfgXEN/LtO+PVJlq398LjlQMm6YZaaXOMeWJy++VCMZbdAyI0HE+UbwB+xgCp02zNXJpqYjwpYmiS2VfQN1B5Iym4bBNSVzruwsJQbzCLj2zMdU9XWgocXt/lhh8pDldLr6DQ0ELcEOmumnsMy9B4BHHeZ6sTVY4Kdpy4BAus4HIN+7iygbEWdJjScsCxTMUvvlvpLXPrNUHJpvJ7p2dHyllqTV367jgp3RKWjP42WRvyx7pDB3SIlrCfyuTeVBelBshHfkfxJPKVfIRZIdMmBDRfdHOYzL+vItUOBW0fiLS9ZEDciCymbArs8GLPtlENLj0+wX7f0OPyJv2UgAAAABJRU5ErkJggg==>

[image7]: <data:image/png;base64,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>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAaCAYAAABVX2cEAAACKElEQVR4XoVUvWobQRC+gwQTUgiS4gi62x9JGBzSCQyBpDdJ4daNX8BdCtURhFQp8xACFzbukiZFKuMXMCSBPEI6gx2k+Jvbnd3Z3RMZsXcz38x8Mzu7uqqqavxIxDM+nNRRJ42tFGUleJmQMUEY3d4QOosMyFITK0dKbyZDwfTmQSSO0hACXCn1XGv9C+sfL6X1Tde2rykE9melFeP0/j2ZTHZTFq5Qu20j6CXWLdZPrfQzrj+bzXZgn4PwfdM0j5lBbIOJYstt2z7SSn1B4sYYc8ABWqsFiBZU00EhRYjviI0aBkiO/HZW8/n8IYgXsD+RLlNZSt5wNarKWtsg+RrrD9YHmpcjkmnb9AEBwUfqzlrzHYMe/S++GmZ0GIjeYG2w1cspkQVPFLIHBkiDixgI9jDwbziIH0RIB8HhIixS9COSHg9aa8GhLnCqs/4gVH+nVvA+SEKF4nWn0RUh8ulkOjLWnIJwn3BrTTiIruteRDJJO2DTkJF0hk7eBjd1asxSoTt0uSx20reRCeZjQXSBxHfR6zKx5VeY4V9j7NV4PH4q0rx4QgQeI/COroD/v61BeMghwE4II7+PWaPzr23bPUkJgxSNetmOJ80nW81mINWUzluDNYrgTLyfY2L9ktQ1KAgdEPypUFz4GuQsCSQZnJ4SD0RyE9s6IVVQZVJiMd/74ncsSkIqPkt5YSl+nmkvRTXSuGKAqIh8C1y8Ml2cX1Kt1Em9B+BZVqlhoafvAAAAAElFTkSuQmCC>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAaCAYAAACzdqxAAAACeUlEQVR4XpVSPWgUQRTegaSQ2Bjubrm93ZnbOxFEsMjWdqa0CaQyvY2FXTCIFgqKlRZiI0Iqbe2PELCwsLAXLFJZWaawyfm9mTdzb2bHQz9u9ma+9973fmaKwkOF3Xr8qx+h5xuIxKIkI21uL7/xoQfilfj+F3xAJjBDOeTrjjCpqoEx+osxZqmx6B/rp9a6m0yqGvtvzGHpJfjvs9nsGsXC/8DoEEO2T6Oy3IoSgDxkh/uhcS4H3JG1ab3Hc2Goom3bm0hwMgWYioHAu1QRgg8jqxLC8GHKfxW4RyhqdxWQQGtzx7VjjgKJWKoE/A9qmboSIdTlDdhedl23GQL88rVB8DZauoDOMVN2Igh8Bv4VzT8SVsUGzs9JnM950GVB5FwKE6eNfoFq96iblU0VTdPcwvkhJQ+ivmAP2nthrEWJm6X2EPi6ruurq6StFR4Oh5fBva2qqolEvKoS6qhqjHUGgVMO3IXwA7ZZYYxjQc+JLhG2e0IqPwki8RrGCCThr7ZKY97P57MRWSF8HS/mFyWt62YO25sBkrtg7l9WaXnOhQqvkCgSnGH/BGvf+4AfQ5iSfgb/mLpJB+pOkbg7UPtUEaq7wIV9RNWXvIcTtt0ssT503c5mrnnHJHxZjrbw5BYI/E03Lm125pSU5oyLJC6udR1gn7bTYwi8w3ZDmlw3+hS2p2m/DoJKZ002un08oQEfIwXYdjCebUHFSAMiIk3WQ1yuPblfgiAYu4f/QCeZ+0qMjE7qq3KzSo+pC0PQOY+kSgnbjOMz1gQ9Dx/IpWXscuLr01D7f7UlVXK+IBmF9kSY8Hxq7/FBPYakZMb03+6jQ3zOSBd/AAD0eZvmtJc7AAAAAElFTkSuQmCC>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAaCAYAAABl03YlAAABWElEQVR4XpVSPUvEQBBNUOEKC0XCcSQ7sxtBsN5WO2sR70+IWHuVlYi9vYWVja29vfYngqA2VpYWCqe+ySabjRsLH+zXmzdvZjdJ0gSopi5a6lcwDMR5IVNb/1khz/MVrfVSy9STrMx8xEyfWL+Z+MTHOwBDRFsQzZRS2yHvnQREPCHmV2IqvSgE+hjA5RrjJsuyReGixgtV5BA8oeRpuVquaW12cB55gYhRAv3QF8o9I3gM5z0kPGC/63uCaALRDOS4STZaX4Tl53Htq5CQ1EpE4kyjpChcPxhnwU2XUfoWokdj9FDex0LwLvWbGyF7Hec3iC6lUsIQoacXZNvaSL7AAZw+VKE26yw2GPdw3BAnY+RIUyQfOl83p7DdR+AO0XPsp+IEfq5xdkjl1c1AGzO01i74p26aDJXtsRPoIk4MiZ5opO1hHGKT7n/dY97P9FEO/3aqkCY/5oE+iP1kEHMAAAAASUVORK5CYII=>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAaCAYAAADMp76xAAADgElEQVR4Xp1WMWgUQRS9hYiKgqKG0+zdzu55KIpWAUHQziIqaiFIGsFGEDuRINgoiIVoF3vLgIWSIqCNipXaWaiggk1AtLETNCTx/dmZnfmzf/bWe/Dvbv9//82f+TOz1+n4SNhTFFGaCSQCo+4pYf1SXPIxxAgxvw/OSUJHY2EcNaVYTsRtoKPuYySaWSaaNLMIjYzG4Bhoq1erO1hWFvYfsiw7qJT6Clv37He/3z9OcfyeD2LfBoPBPk/CA68C3OuZUn+Vyqr8oshfp1PpTsvp9XtDlallT78aWyOcmAWIR2F/YF9ge6x/OBxuxPNTTOxWt9vd4uc4JKKw3QTIf2iKucsZJfI8n8HE3tLihTEZUO71epuR8AyzXSMB46bB5iA2Zx6DRI5YFLrHoLMCe4PubKsCSCiKQiG+SN8thuDxvMhnTfsWpqenN1CxsPv0u6YjbkIZe1EkFQvtFSqefMTGwuym7qHYIxXZl2FjmN++C4ldCHyC/YLdgc3bYjXP5sRriwLF3fa3Ba00OreESZyPz5UF6izykCAJ5zgcrH0xCBN3cF7lzsgHHLQUW28ek7ikSZYmizQDgqdga9RCV3BMqbFa1pbJXZNbofnKaL9U9lx4nApJzRPA9BgiB2AvcAo+k7A9fBzNUlEkdPjUDazsOvbxI9pqIaXC6CESc1rVIm6LIQqdzfR+yxYQmqjyR86c4DM4W5XbbQ0Fn2ABEWVufe075QFAkY8Lc1oL7/DhEj/EUjpVQ0KxADwK/U3QW8JCLKdp2gvjBH9hhHAJKhZCT2CnfZI91QW+nZfgkRLN207mnDKwqgNsh+9UNBUfxhthh0RyQZc2BK6FDdCXfaZWEHs3lbpXaUkpeejEfmj8gNGrtag4GnyJ0KmztH/Bu+nHbLcagWIuKv2OxwEo78bVPC/O2Tier5KP4toytYqc59jfO3wdai3y36tyX55xEVcFJnwF8Z/eWLDsI7QOOz4HnwPvaAR020hRyacX4DIKORn6I/QWiCaGG6E9vJwJFPsAXQi2RHu0rEIgaJfg15D9aPkM7F4SjivTmxHmhM8lPG81ahMYYwLb4QL9ufGdLUQ8SGR/7kFcotfA51SD5GsFc0XQZwuNOqXucfBjTTyGxHDDhFYVWsJIYh1jpATgCpKetCAST3b+N9yfrnH04i8P+XIdgREpYXjMoisIyf8AyS2p+49ACPkAAAAASUVORK5CYII=>