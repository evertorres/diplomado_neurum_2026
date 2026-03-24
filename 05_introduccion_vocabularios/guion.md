# Guion de Presentación - Módulo 05: Vocabularios y Terminologías en Salud

Este documento detalla la estructura y el contenido de las 26 diapositivas, integrando la presentación base original con conceptos clave de investigación complementaria adaptadas para un formato web interactivo con Reveal.js.

---

## Diapositiva 01: Portada
- **Título**: Vocabularios y terminologías en salud
- **Contenido Visual**: Diseño limpio con el título central y el logo de la institución.
- **Narrativa Sugerida**: "Bienvenidos al módulo sobre vocabularios y terminologías en salud. En esta sesión abordaremos cómo el lenguaje clínico puede estructurarse para ser comprensible tanto para humanos como para computadoras."

## Diapositiva 02: Los Niveles de la Interoperabilidad (NUEVA)
- **Título**: Los cuatro niveles de la Interoperabilidad
- **Contenido Visual**: Gráfico de escalones con cuatro niveles: Técnica (redes), Sintáctica (estructura), Semántica (significado) y Organizacional (políticas).
- **Narrativa Sugerida**: "Antes de centrarnos en vocabularios, debemos entender que la interoperabilidad ocurre en 4 niveles. No basta con conectar cables (Técnica) o enviar formatos correctos (Sintáctica); si no compartimos el mismo significado (Semántica) o los mismos procesos institucionales (Organizacional), el intercambio falla. Nuestro foco de hoy será la interoperabilidad semántica."

## Diapositiva 03: Categoría de los estándares
- **Título**: Categoría de los estándares
- **Contenido Visual**: Dos bloques comparativos. 
  - Izquierda: *Interoperabilidad Sintáctica* (Estructura, gramática - ej. HL7 FHIR). 
  - Derecha: *Interoperabilidad Semántica* (Significado, diccionario - ej. CIE-10, SNOMED CT, LOINC).
  - Base: Propósitos (Gestión, Estadísticas, Soporte a decisiones).
- **Narrativa Sugerida**: "Los estándares se dividen en dos categorías principales. Los sintácticos nos dan el formato o la gramática, mientras que los semánticos nos dan el significado real, como un diccionario. Esto es fundamental para que los sistemas de información puedan brindar soporte avanzado."

## Diapositiva 04: La problemática del lenguaje natural
- **Título**: La problemática del lenguaje natural
- **Contenido Visual**: Texto interactivo o animación: "IMAGÍNESE UNA PANTALLA...".
- **Narrativa Sugerida**: "Para entender por qué necesitamos estándares semánticos, hagamos un ejercicio de imaginación sobre las pantallas clínicas que usamos a diario..."

## Diapositiva 05: Algunas definiciones
- **Título**: Algunas definiciones
- **Contenido Visual**: Lista de términos clave apareciendo en secuencia (fragments):
  - Palabra
  - Lexicón
  - Término
  - Concepto
  - Sinónimo
  - Homónimo
  - Código
- **Narrativa Sugerida**: "Antes de avanzar, repasemos conceptos clave de la lingüística en informática. Una 'palabra' es diferente a un 'concepto', y en informática médica, asociaremos conceptos únicos a 'códigos' específicos."

## Diapositiva 06: La problemática del lenguaje natural (Visual)
- **Título**: El reto de las interfaces libres
- **Contenido Visual**: Ejemplos visuales de diferentes "pantallas" o campos de texto libre donde los médicos escriben la misma idea de formas distintas.
- **Narrativa Sugerida**: "Si dejamos que cada profesional describa un evento en texto libre, la computadora no sabrá que están hablando de lo mismo. Esta es la principal falla de las historias clínicas no estructuradas."

## Diapositiva 07: Modelo de comunicación exitoso
- **Título**: Modelo de comunicación exitoso
- **Contenido Visual**: Diagrama Emisor -> Mensaje -> Receptor.
- **Narrativa Sugerida**: "En una comunicación humana exitosa, el contexto y la experiencia ayudan a decodificar el mensaje. Sin embargo, las computadoras carecen de este sentido común biológico para inferir la intención."

## Diapositiva 08: Modelo de comunicación exitoso (Contexto)
- **Título**: La importancia del contexto en datos
- **Contenido Visual**: Comparación: "120/80" vs datos estructurados detallados (Sistólica: 120, Diastólica: 80, Unidad: mmHg, Paciente, Fecha, Posición).
- **Narrativa Sugerida**: "Para un médico, '120/80' claramente es presión arterial. Para una computadora, son solo números. Necesitamos especificar unidad, técnica, y variables asociadas para hacer la información útil computacionalmente."

## Diapositiva 09: Ambigüedad
- **Título**: Retos semánticos: Ambigüedad
- **Contenido Visual**: Tres columnas explicando:
  1. Sinonimia (Fiebre / Pirexia)
  2. Polisemia (ej. Enfermedad de Paget - ósea vs mama)
  3. Homonimia (Banco de sangre / Banco financiero, Cara facil / Cara costosa)
- **Narrativa Sugerida**: "El lenguaje humano está lleno de ambigüedades. Tenemos sinónimos donde distintas palabras significan lo mismo, y polisemia u homonimia donde una palabra idéntica significa varias cosas según el caso."

## Diapositiva 10: Ambigüedad - Ejemplo Clínico
- **Título**: Ejemplo: Fiebre en el ámbito clínico
- **Contenido Visual**: Múltiples variaciones en texto de cómo un médico puede registrar fiebre ("paciente febril", "T 39C", "calentura").
- **Narrativa Sugerida**: "Veamos el ejemplo de la fiebre. Todas estas frases describen el mismo evento clínico, pero textualmente son cadenas de caracteres totalmente diferentes para una base de datos de un hospital."

## Diapositiva 11: Ambigüedad - Ejemplo (HL7)
- **Título**: Ejemplo en mensajería: Grupo sanguíneo
- **Contenido Visual**: Representaciones transaccionales del "Grupo sanguíneo O" en diversos sistemas enviando mensajes. La palabra clave **CODIFICACIÓN** aparece destacada como solución definitiva.
- **Narrativa Sugerida**: "Aún en mensajes estructurados sintácticamente por estándares como HL7, si el contenido del mensaje (el valor) varía libremente, la interoperabilidad fracasa. La única solución escalable es la codificación unificada del vocabulario."

## Diapositiva 12: Representación del conocimiento
- **Título**: Representación del conocimiento
- **Contenido Visual**: El Triángulo Semántico interactivo. Relaciones animadas de designación, descripción y denotación de forma secuencial.
- **Narrativa Sugerida**: "El triángulo de Ogden-Richards o triángulo semántico nos muestra cómo los símbolos lingüísticos se relacionan con los conceptos mentales y los objetos finitos del mundo real."

## Diapositiva 13: Representación del conocimiento (Definiciones)
- **Título**: Objetos, Conceptos y Símbolos
- **Contenido Visual**: Definiciones claras. Ejemplo ilustrativo, como el uso de la imagen de una persona contrastado con sus respectivos símbolos o emojis.
- **Narrativa Sugerida**: "El objeto es la entidad real independiente. El concepto es nuestro modelo mental que lo representa, y el símbolo es la palabra en cualquier idioma o código alfanumérico que usamos para invocar y comunicar el concepto."

## Diapositiva 14: Sistemas de soporte a la toma de decisiones
- **Título**: Sistemas de soporte a la toma de decisiones (CDSS)
- **Contenido Visual**: Flujo de proceso visual que va desde "Datos del paciente", interactuando con un motor clínico para derivar en "Alertas y recordatorios".
- **Narrativa Sugerida**: "Toda esta semántica estructurada permite implementar verdaderos Sistemas de Soporte de Decisiones. Si nuestro vocabulario de entrada no está estandarizado o validado, un motor de reglas generará falsos positivos perjudiciales."

## Diapositiva 15: Control del vocabulario en medicina
- **Título**: Jerarquía del control de vocabulario
- **Contenido Visual**: Gráfico ascendente desde el Lenguaje Natural, ascendiendo a Vocabularios Controlados, y culminando en Clasificaciones y Agrupamientos clínicos limitados.
- **Narrativa Sugerida**: "En medicina no todo requiere el mismo abordaje tecnológico. Dependiendo del caso de uso transicionamos desde el texto literario necesario para entender la evolución de un paciente, hasta jerarquías rígidas apropiadas para la facturación a los seguros."

## Diapositiva 16: Vocabularios en salud
- **Título**: Tipos de Vocabularios
- **Contenido Visual**: Tres conceptos principales desplegables:
  - Vocabulario Controlado.
  - Terminología / Tesauro (Conecta semánticamente).
  - Taxonomía (Establece mapas jerárquicos).
- **Narrativa Sugerida**: "Un vocabulario riguroso simplemente restringe los términos válidos mediante listas consensuadas. Un tesauro da un paso más al enlazar sinónimos permitidos, mientras que una taxonomía construye un árbol estricto organizando elementos mayores a menores."

## Diapositiva 17: Vocabularios en salud (Nomenclaturas y Clasificaciones)
- **Título**: Diferencia: Nomenclaturas y Clasificaciones
- **Contenido Visual**: Componentes listados por separado.
  - Nomenclaturas: Subset oficial, granularidad expansiva (ej. la riqueza de SNOMED).
  - Clasificaciones: Sistemas cerrados y reduccionistas (ej. epígrafes del CIE-10).
- **Narrativa Sugerida**: "Las nomenclaturas persiguen designar exhaustivamente cada hallazgo clínico con alta micro-resolución para el experto, pero las clasificaciones engloban dichos hallazgos en grandes 'cajones' genéricos diseñados primordialmente para estudios epidemiológicos."

## Diapositiva 18: Ontologías y Mayor Formalización (NUEVA)
- **Título**: Ontologías: El nivel superior de formalización
- **Contenido Visual**: Tres componentes comparativos: Clasificación (Jerárquica), Terminología (Red de conceptos), Ontología (Reglas lógicas y axiomas).
- **Narrativa Sugerida**: "Como complemento, existe un peldaño superior: las Ontologías. Estas no solo catalogan, sino que le enseñan a la computadora las 'leyes lógicas' de los conceptos, permitiendo realizar inferencias automáticas complejas que los otros modelos no logran."

## Diapositiva 19: Vocabularios según su aplicación
- **Título**: Vocabularios según su aplicación
- **Contenido Visual**: Tableros visuales sobre las tres capas de aplicación:
  - Vocabulario de Interfaz.
  - Vocabulario de Referencia.
  - Vocabulario de Salida o Agrupación.
- **Narrativa Sugerida**: "Un aspecto clave del UX médico es reconocer que los doctores no quieren teclear complejos códigos CIE o SNOMED; ellos quieren herramientas que presenten Vocabularios de Interfaz familiares y amigables atados a terminologías canónicas."

## Diapositiva 20: Modelos de vocabularios en capas
- **Título**: Arquitectura de Vocabularios en capas
- **Contenido Visual**: Diagrama piramidal que consolida las capas: Lenguaje Natural (base inmensa) -> Interfaz (traductor) -> Referencia (nodo central unificado) -> Salida (cúspide especializada).
- **Narrativa Sugerida**: "Este modelo piramidal ejemplifica una arquitectura informática saludable: la expresión fluye con flexibilidad mientras las reglas sistémicas traducen todo hacia nomenclaturas normalizadas globalmente y reportes administrativos."

## Diapositiva 21: Vocabularios controlados
- **Título**: Atributos de un Vocabulario Controlado
- **Contenido Visual**: Destacados visuales de las propiedades más importantes:
  - Consistencia Rígida.
  - No ambiguos.
  - Altamente precisos.
  - Robustez estandarizada.
- **Narrativa Sugerida**: "Podemos resumirlo así: sin importar su origen, un excelente vocabulario controlado clínico nunca deja de caracterizarse por neutralizar la subjetividad idiomática y proveer identidades únicas (códigos puros) por entidad."

## Diapositiva 22: ¿Para qué sirve un vocabulario controlado?
- **Título**: Casos de uso general
- **Contenido Visual**: Casuística desplegable:
  1. Codificación semántica universal.
  2. Integración de resultados de laboratorio (ej. LOINC).
  3. Formulación e interoperabilidad farmacéutica.
  4. Agilización del Machine Learning y Soporte Analítico Avanzado.
- **Narrativa Sugerida**: "Poder enlazar estos términos globalizados es lo que habilita la Historia Clínica Única, portales del paciente avanzados, y la actual revolución de analítica de datos a nivel poblacional sin fronteras sistémicas."

## Diapositiva 23: Gobernanza y Retos de Adopción (NUEVA)
- **Título**: Desafíos en Implementación y Gobernanza 
- **Contenido Visual**: Puntos destacando la dificultad del Mapeo de términos locales, la importancia de una Gobernanza Nacional o de centros de referencia, y la usabilidad para evitar resistencia médica.
- **Narrativa Sugerida**: "Implementar esto es un enorme reto organizacional. Implica mapeos minuciosos de catálogos locales, requiere gobernanza activa para mantenerse actualizados, y un diseño de interfaz centrado en el usuario para evitar que la carga administrativa abrume a los médicos."

## Diapositiva 24: Sistemas de codificación más comunes
- **Título**: Panorama de Sistemas de Codificación
- **Contenido Visual**: Matriz mostrando logotipos (si disponibles) y ejemplos:
  - **SNOMED CT**: Representación analítica completa.
  - **LOINC**: Especialidad en variables numéricas y reactivos.
  - **CIE-10/CIE-11**: Líder en estadística poblacional y diagnóstico.
  - Códigos regionales locales, como **CUPS** (análisis para Colombia).
- **Narrativa Sugerida**: "Para cerrar a modo de mención introductoria, hoy disponemos de estándares para dominios específicos: SNOMED CT como diccionario maestro y de referencia clínica, LOINC liderando en pruebas de laboratorio, y clasificaciones como la CIE acompañadas de códigos locales de procedimientos como CUPS."

## Diapositiva 25: El Futuro con Inteligencia Artificial y PLN (NUEVA)
- **Título**: Sinergia con Procesamiento de Lenguaje Natural (PLN)
- **Contenido Visual**: Ilustración de cómo un algoritmo lee texto natural y sugiere códigos (Human in the loop).
- **Narrativa Sugerida**: "La tendencia que resolverá grandes desafíos es converger estas terminologías con Procesamiento de Lenguaje Natural e Inteligencia Artificial. Esto permitirá a los médicos expresarse en texto libre de forma natural, mientras sistemas automatizados sugieren o asisten la tarea transaccional pesada de mapear códigos internamente."

## Diapositiva 26: Limitaciones
- **Título**: Limitaciones de la codificación estandarizada
- **Contenido Visual**: Resumen crítico del 'lado oscuro': Desconexiones expresivas con pacientes y médicos, desafíos de granularidad (gravedad, lateralidad natural), y distorsiones (Sesgos y overcoding pro-facturaciones).
- **Narrativa Sugerida**: "Por muy avanzados que sean nuestros ecosistemas estandarizados, no hay soluciones perfectas, a menudo obligando a clasificar pacientes en términos 'inadecuados'. La codificación es una abstracción útil, mas no la realidad íntegra y completa del fenómeno de la vida. Con esto finalizamos la introducción."
