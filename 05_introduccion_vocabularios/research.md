# **Análisis Exhaustivo de los Vocabularios y Terminologías en Salud: Arquitectura, Estándares e Interoperabilidad Semántica**

La digitalización de los ecosistemas sanitarios ha dejado de ser una transición técnica para convertirse en una transformación estructural de la práctica clínica y la gestión de la salud pública. En este escenario, la capacidad de los sistemas de información para intercambiar datos con un significado unívoco y procesable computacionalmente —fenómeno denominado interoperabilidad semántica— constituye el núcleo de la salud digital contemporánea.1 La ausencia de un lenguaje común estandarizado no solo perpetúa la fragmentación de la información en silos inconexos, sino que genera ineficiencias operativas masivas, incrementa el riesgo de errores médicos por falta de contexto y supone una pérdida significativa de recursos económicos en todos los niveles del sistema prestador.3 El presente informe técnico desglosa los fundamentos, la arquitectura de los principales estándares internacionales y los desafíos críticos para su implementación efectiva en el punto de atención.

## **El imperativo de la interoperabilidad semántica en la salud digital**

La interoperabilidad en salud se manifiesta en múltiples dimensiones, desde la conexión física de hardware (interoperabilidad técnica) hasta el acuerdo entre organizaciones para procesos de trabajo conjuntos (interoperabilidad organizacional).1 Sin embargo, la interoperabilidad semántica representa el desafío más sofisticado, ya que exige que el receptor de un dato clínico sea capaz de interpretar el significado de la información de la misma manera que el emisor original.1 Para lograr este objetivo, es indispensable el uso de vocabularios controlados, los cuales se definen como listas pre-aprobadas de términos que eliminan la ambigüedad inherente al lenguaje natural, aportando rigidez, precisión y estandarización a la documentación médica.1

La representación de la realidad clínica a través de códigos estandarizados permite que los sistemas de información no solo almacenen texto, sino que "entiendan" los conceptos. Esta capacidad es la que habilita funciones avanzadas como la generación de alertas por interacciones medicamentosas, el monitoreo epidemiológico en tiempo real y la agregación de datos para la investigación científica sin necesidad de limpieza manual exhaustiva.7 En países de América Latina, como Colombia y Uruguay, la adopción de estos estándares se ha vinculado estrechamente con políticas nacionales de Historia Clínica Electrónica (HCE) interoperable, buscando asegurar la continuidad del cuidado y la seguridad del paciente a través de un Resumen Digital de Atención en Salud (RDA) coherente.4

|Nivel de Interoperabilidad|Enfoque Principal|Mecanismo de Implementación|
|-|-|-|
|Técnica|Intercambio de bits y señales.|Protocolos de red, hardware, firewalls.1|
|Sintáctica|Estructura y formato del mensaje.|XML, JSON, estándares de mensajería como HL7 v2.x.8|
|Semántica|Significado compartido de los datos.|Vocabularios controlados, terminologías (SNOMED CT, LOINC).2|
|Organizacional|Procesos y políticas de negocio.|Acuerdos marcos, leyes de protección de datos, gobernanza.1|

## **Marcos teóricos y taxonómicos de la representación del conocimiento clínico**

Para profundizar en el estudio de los vocabularios de salud, es crucial distinguir entre los diversos tipos de recursos terminológicos según su formalismo y propósito. No todos los instrumentos de codificación tienen la misma estructura ni persiguen los mismos fines analíticos.

## **Vocabularios controlados y terminologías de interfaz**

Un vocabulario controlado es la unidad básica de estandarización, consistente en una lista cerrada de términos para un ámbito determinado.1 Dentro de esta categoría, las terminologías de interfaz juegan un rol vital en la usabilidad clínica. Estas herramientas proporcionan términos "amigables" o jergas médicas habituales que los profesionales de la salud utilizan en su práctica diaria, pero que están mapeados internamente a códigos de referencia.2 El uso de terminologías de interfaz evita la fricción que supondría obligar al médico a memorizar códigos técnicos, facilitando la captura de datos estructurados sin comprometer la agilidad de la consulta.2

## **Terminologías de referencia y clasificaciones**

La distinción técnica entre una terminología de referencia y una clasificación estadística es fundamental para el diseño de sistemas de información. Una terminología de referencia, como SNOMED CT, se caracteriza por una alta granularidad y una estructura de red donde un concepto puede tener múltiples relaciones y atributos.11 Su objetivo es representar la riqueza del acto médico con la mayor precisión posible. Por el contrario, una clasificación, como la CIE-10 o la CIE-11, organiza los conceptos en categorías jerárquicas mutuamente excluyentes.12 Esta estructura jerárquica es ideal para la agregación de datos, la facturación hospitalaria y el análisis de tendencias de mortalidad y morbilidad, pero a menudo carece del detalle necesario para el manejo clínico individual del paciente.2

## **Ontologías: El nivel superior de formalización**

Las ontologías representan el grado más alto de sofisticación en la representación del conocimiento. Se definen como instrumentos que describen formalmente los conceptos de un dominio, sus propiedades (slots), las interacciones entre ellos (relaciones) y las reglas lógicas que los gobiernan (axiomas).15 Las ontologías "pesadas" utilizan lógica de descripción para permitir que las máquinas realicen inferencias automáticas, detectando inconsistencias o derivando nuevo conocimiento a partir de los datos existentes.15

|Recurso|Estructura|Uso Principal|Ejemplo|
|-|-|-|-|
|Clasificación|Jerárquica, excluyente (mono-parental).|Estadísticas, facturación, reporte epidemiológico.12|CIE-11|
|Terminología|Red conceptual, alta granularidad.|Registro clínico, soporte a la decisión.12|SNOMED CT|
|Ontología|Formalismo lógico, axiomas, relaciones complejas.|Razonamiento automático, integración de conocimiento.15|GALEN|

## **SNOMED CT: La ontología de referencia para el registro clínico detallado**

La Nomenclatura Sistematizada de Medicina – Términos Clínicos (SNOMED CT) es la terminología clínica multilingüe más extensa y completa disponible actualmente.9 Desarrollada y mantenida por SNOMED International, esta herramienta no es solo una lista de códigos, sino una estructura lógica basada en conceptos que permite una representación coherente y validada científicamente de la historia clínica electrónica.9

## **Arquitectura de componentes de SNOMED CT**

El modelo lógico de SNOMED CT se sustenta en tres pilares fundamentales que garantizan su robustez y flexibilidad 19:

1. **Conceptos**: Son las unidades básicas de significado. Cada concepto tiene un identificador numérico único (SCTID) de hasta 18 dígitos que no cambia con el tiempo. Los conceptos representan pensamientos clínicos específicos y están organizados en jerarquías que van de lo general a lo particular.9
2. **Descripciones**: Son los términos textuales asociados a los conceptos. Cada concepto tiene un Nombre Completamente Especificado (FSN), que incluye la etiqueta de jerarquía (por ejemplo, "neumonía (trastorno)"), y varios sinónimos que permiten que médicos de distintas regiones o especialidades encuentren el mismo concepto usando palabras diferentes.9
3. **Relaciones**: Vinculan los conceptos entre sí. La relación más importante es "es un" (is-a), que define la jerarquía (por ejemplo, "neumonía bacteriana es un tipo de infección pulmonar"). Además, existen relaciones de atributos que definen las propiedades del concepto, como el "sitio morfológico" o el "agente causal".19

## **Mecanismos de coordinación: Pre-coordinación y Pos-coordinación**

Una de las innovaciones más potentes de SNOMED CT es la capacidad de expresar detalles clínicos que no existen como conceptos individuales en la terminología base. Esto se logra mediante la pos-coordinación, un proceso donde el sistema combina dos o más identificadores de conceptos para crear una expresión nueva y específica.19 Por ejemplo, se puede combinar el concepto de "fractura de fémur" con el de "lado izquierdo" y "tercio distal" para registrar una información extremadamente detallada sin necesidad de que exista un único código para esa combinación exacta. Esta flexibilidad asegura que la terminología pueda cubrir requerimientos emergentes sin un crecimiento incontrolado del diccionario central.7

## **Jerarquías y riqueza semántica**

SNOMED CT se organiza en 19 jerarquías principales, que incluyen dominios tan diversos como hallazgos clínicos, procedimientos, estructuras corporales, sustancias, especímenes y contextos sociales.19 Esta cobertura integral permite que una misma terminología sea utilizada por enfermeras, médicos, farmacéuticos y administradores, facilitando la continuidad del flujo de información entre departamentos.20

|Jerarquía|Descripción de Contenido|Ejemplo de Concepto|
|-|-|-|
|Hallazgo Clínico|Resultados de exámenes, signos y síntomas.|Dolor abdominal.19|
|Procedimiento|Acciones realizadas en el cuidado de la salud.|Apendicectomía.19|
|Estructura Corporal|Anatomía normal y variante.|Lóbulo inferior del pulmón derecho.19|
|Sustancia|Químicos, alérgenos y materiales.|Penicilina G.19|
|Situación con contexto|Estado de un hallazgo (historia de, riesgo de).|Antecedente familiar de diabetes.21|

La adopción de SNOMED CT ha demostrado beneficios tangibles en la identificación temprana de problemas de salud poblacional y en la implementación de Sistemas de Soporte a la Decisión Clínica (CDSS).7 Organizaciones de prestigio como Kaiser Permanente y el Hospital Italiano de Buenos Aires han integrado SNOMED CT para lanzar alertas en tiempo real, como contraindicaciones de medicamentos basadas en diagnósticos previos registrados de forma estructurada.18

## **LOINC: Estandarización de observaciones y resultados de laboratorio**

Si SNOMED CT es el estándar para los diagnósticos y procedimientos, LOINC (Logical Observation Identifiers Names and Codes) es el estándar universal para la identificación de pruebas de laboratorio y mediciones clínicas.6 Mantenido por el Instituto Regenstrief, LOINC permite que los resultados de laboratorio fluyan entre sistemas heterogéneos sin perder su interpretación clínica original.23

## **La estructura de seis ejes de LOINC**

A diferencia de otros sistemas de codificación, cada término de LOINC se construye sobre una definición formal que consta de seis ejes o dimensiones. Esta estructura garantiza que cada prueba sea identificada de forma única según su contexto biológico y analítico.25

|Eje|Nombre|Función|Ejemplo|
|-|-|-|-|
|1|Componente|El analito o entidad medida.|Glucosa, Sodio, Hemoglobina.27|
|2|Propiedad|La característica medida del componente.|Concentración de masa (MCnc), Presencia (Prid).27|
|3|Tiempo|El intervalo o momento de la observación.|Punto en el tiempo (Pt), 24 horas.23|
|4|Sistema|El espécimen o sistema sobre el que se mide.|Suero (Ser), Orina (Ur), Sangre total (Bld).23|
|5|Escala|El tipo de valor del resultado.|Cuantitativo (Qn), Ordinal (Ord), Nominal (Nom).23|
|6|Método|La técnica utilizada (opcional).|PCR, Aglutinación, Espectrometría.23|

Esta precisión dimensional es lo que permite que un sistema informático distinga, por ejemplo, entre una glucosa medida en ayunas en suero y una glucosa medida tras una carga de 100g de azúcar.28 Además de las pruebas de laboratorio clásicas, LOINC ha extendido su cobertura a documentos clínicos (como el alta hospitalaria), signos vitales (presión arterial, frecuencia cardíaca) y cuestionarios de salud evaluados por el paciente.23

## **Integración y interoperabilidad de LOINC**

LOINC es una pieza central en los mensajes HL7 y los recursos FHIR, actuando como el identificador de la "pregunta" en una observación clínica.23 Durante la respuesta global a la pandemia de COVID-19, LOINC fue instrumental para estandarizar el reporte de resultados de pruebas de detección viral, permitiendo la agregación de datos epidemiológicos a nivel mundial de forma coherente.23 Sin embargo, el mapeo de códigos locales a LOINC presenta desafíos técnicos considerables, como la variabilidad en la nomenclatura de los especímenes y la falta de información detallada en los catálogos de laboratorio preexistentes.26

## **Clasificaciones internacionales y la transición hacia la CIE-11**

La Clasificación Internacional de Enfermedades (CIE), publicada por la Organización Mundial de la Salud (OMS), es el estándar mundial para la documentación clínica, las estadísticas de salud y la gestión sanitaria.2 Con la llegada de la undécima revisión (CIE-11), el estándar ha evolucionado desde una estructura de libro impreso hacia un recurso nativo digital, diseñado para una integración fluida en los sistemas de información modernos.2

## **Innovaciones estructurales de la CIE-11**

La CIE-11 introduce cambios paradigmáticos en la forma en que se organiza el conocimiento médico 13:

* **Componente de Fundación**: Es una base de datos masiva que contiene todas las entidades médicas (enfermedades, síntomas, lesiones), organizadas de forma que permiten que un concepto tenga múltiples padres (multi-parenting).13
* **Linealizaciones**: Son subconjuntos de la Fundación creados para propósitos específicos. La más común es la MMS (Estadísticas de Mortalidad y Morbilidad), que mantiene una estructura jerárquica estricta de un solo padre por categoría para evitar errores de conteo estadístico.13
* **Codificación en Clúster**: Similar a la pos-coordinación de SNOMED CT, la CIE-11 permite combinar códigos de "tallo" (stem codes) con códigos de "extensión" para añadir detalles de severidad, lateralidad o agentes causales.13 Por ejemplo, se puede codificar una "infección urinaria" y enlazarla mediante un símbolo "/" con el código del agente específico "Escherichia coli".13

## **Sinergia entre SNOMED CT y CIE-11**

Históricamente, se ha visto a SNOMED CT y a la CIE como competidores, pero la tendencia actual es hacia la complementariedad. SNOMED CT se utiliza para el registro clínico detallado en el punto de atención, mientras que la CIE-11 se utiliza para el reporte estadístico y la facturación.6 Existen proyectos de mapeo masivo entre ambos estándares para que, cuando un médico registre un diagnóstico detallado en SNOMED CT, el sistema sea capaz de derivar automáticamente el código CIE-11 correspondiente, reduciendo la carga administrativa y mejorando la calidad de las estadísticas nacionales.19

|Característica|CIE-10|CIE-11|
|-|-|-|
|Formato|Impreso / PDF.|Nativo digital (API/Navegador).2|
|Estructura|Jerárquica simple.|Red conceptual (Fundación).13|
|Combinación|Códigos de "Daga y Asterisco".|Codificación en clúster (Post-coordinación).13|
|Mapeo|Complejo y manual.|Alineado con SNOMED CT y digitalmente asistido.31|

## **Implementación técnica y orquestación mediante HL7 FHIR**

El intercambio efectivo de términos y códigos requiere de un marco técnico que gestione los recursos terminológicos de manera eficiente. HL7 FHIR (Fast Healthcare Interoperability Resources) se ha consolidado como el estándar de facto para esta tarea, gracias a su enfoque basado en recursos modulares y APIs web modernas.10

## **El módulo de terminología en FHIR**

FHIR proporciona un conjunto específico de recursos diseñados para abstraer la complejidad de los sistemas de códigos, permitiendo que las aplicaciones utilicen terminologías sin necesidad de ser expertas en sus detalles internos.33 Los recursos fundamentales incluyen:

1. **CodeSystem**: Declara la existencia de un sistema de códigos (como SNOMED CT o un catálogo local), definiendo sus conceptos y propiedades.34
2. **ValueSet**: Representa una selección de códigos de uno o más sistemas, diseñados para un uso específico. Por ejemplo, un ValueSet de "procedimientos quirúrgicos cardiacos" filtrado desde la jerarquía de SNOMED CT.34
3. **ConceptMap**: Define las relaciones de equivalencia o mapeo entre códigos de diferentes sistemas. Es la herramienta principal para la migración de datos de sistemas antiguos a estándares nuevos.34

## **Operaciones del servidor de terminología**

Un servidor de terminología compatible con FHIR no solo almacena códigos, sino que ofrece servicios lógicos mediante operaciones específicas que pueden ser invocadas vía HTTP 35:

* **$lookup**: Recupera todos los detalles de un código dado su sistema e identificador. Es esencial para mostrar la descripción correcta de un código en la interfaz de usuario.34
* **$expand**: Genera la lista completa de conceptos incluidos en un ValueSet. Se utiliza para llenar listas desplegables o componentes de autocompletado en el registro clínico.34
* **$validate-code**: Verifica si un código específico es válido dentro de un sistema o un ValueSet determinado, garantizando la integridad de los datos antes de su almacenamiento.35
* **$translate**: Utiliza un ConceptMap para convertir un código de un sistema de origen a uno de destino, facilitando la interoperabilidad entre diferentes instituciones que usan estándares distintos.35
* **$closure**: Permite navegar la jerarquía de una terminología para determinar relaciones de herencia (por ejemplo, saber si una "Fractura de fémur distal" es una instancia de "Fractura de fémur").35

## **Retos de implementación, gobernanza y calidad del dato**

La implementación de terminologías en salud no es solo un reto de ingeniería de software; es un desafío de gestión del cambio y gobernanza organizacional. La experiencia acumulada en diversos países ha permitido identificar lecciones críticas para el éxito de estos proyectos.

## **El desafío del mapeo y la granularidad**

Uno de los obstáculos más comunes es el mapeo de los códigos locales preexistentes a estándares internacionales. Este proceso es propenso a errores debido a la falta de coincidencia exacta en la granularidad: a menudo, un código local es demasiado general para un código SNOMED CT específico, o viceversa.26 El mapeo incompleto o incorrecto puede llevar a una pérdida de información crítica, especialmente en áreas como los resultados de laboratorio donde el método analítico puede ser determinante para la interpretación del resultado.26

## **Gobernanza y mantenimiento de versiones**

Las terminologías de salud son entes vivos que se actualizan periódicamente (por ejemplo, SNOMED CT tiene actualizaciones internacionales mensuales y extensiones nacionales semestrales).9 Mantener la coherencia de los datos históricos mientras se adoptan nuevas versiones requiere una gobernanza robusta que defina políticas claras de actualización y versionado de los componentes de terminología en el servidor central.19 En países como Uruguay, se han creado Centros de Referencia Nacional (NRC) para gestionar la extensión nacional de SNOMED CT, asegurando que los términos locales se integren correctamente en el estándar global.9

## **Capacitación y aceptación del usuario**

La adopción de vocabularios controlados a menudo enfrenta resistencia por parte del personal clínico debido a la percepción de una mayor carga administrativa.37 La solución a este reto no es técnica, sino de diseño de interfaces: el uso de terminologías de interfaz que permitan la búsqueda en lenguaje natural y el autocompletado inteligente es esencial para que el médico perciba el valor de la codificación sin que esta interfiera en su flujo de trabajo.2

|Factor de Riesgo|Impacto|Estrategia de Mitigación|
|-|-|-|
|Mapeo Incorrecto|Diagnósticos erróneos, pérdida de datos.|Validación por expertos clínicos, uso de herramientas de IA para mapeo.38|
|Falta de Gobernanza|Inconsistencia entre sistemas, fallos de IO.|Creación de una autoridad nacional de terminología (NRC).4|
|Baja Usabilidad|Resistencia médica, datos incompletos.|Implementación de terminologías de interfaz y buscadores potentes.7|
|Desactualización|Falta de soporte para nuevas patologías.|Procesos automáticos de sincronización con servidores internacionales.19|

## **Convergencia con la inteligencia artificial y tendencias futuras**

El futuro de las terminologías en salud está intrínsecamente ligado al avance de la Inteligencia Artificial (IA) y el Procesamiento de Lenguaje Natural (PLN). Estas tecnologías están transformando la forma en que capturamos y estructuramos la información clínica, cerrando la brecha entre el texto libre de los médicos y los códigos estandarizados.

## **PLN y codificación automática**

El PLN permite analizar automáticamente las notas clínicas no estructuradas para extraer conceptos de SNOMED CT o códigos CIE-11.40 Estudios recientes han demostrado que las herramientas de codificación asistida por PLN pueden identificar diagnósticos en registros históricos con una precisión comparable a los codificadores humanos, reduciendo el tiempo de procesamiento en un 75%.39 Esto es especialmente valioso para la gestión de listas de espera y la auditoría de calidad asistencial a gran escala.42

## **Grandes Modelos de Lenguaje (LLM) y Ontologías**

La integración de modelos como GPT-4o o Gemini en los flujos de trabajo de terminología está abriendo nuevas posibilidades para el mapeo entre instituciones.39 Los LLMs pueden ser utilizados para traducir términos locales a inglés, expandir abreviaturas ambiguas (como distinguir si "MS" significa esclerosis múltiple o estenosis mitral según el contexto) y sugerir los códigos más probables en terminologías complejas como SNOMED CT.21 Investigaciones de 2024 indican que el uso de LLMs para asistir en la creación de nuevos conceptos puede reducir la tasa de duplicados en un 83% y las violaciones de reglas de modelado en un 72%.39

## **Desafíos Éticos de la IA en Terminología**

A pesar de su potencial, la aplicación de la IA en salud introduce riesgos significativos. Las alucinaciones de los modelos de lenguaje pueden generar códigos inexistentes o incorrectos, y los sesgos en los datos de entrenamiento pueden llevar a diagnósticos erróneos en grupos minoritarios.5 Por ello, la tendencia actual es hacia un enfoque de "humano en el bucle" (human-in-the-loop), donde la IA propone y el codificador experto valida, asegurando que la tecnología potencie la eficiencia sin comprometer la seguridad clínica.5

## **Propuesta de esquema para una presentación profesional**

Para facilitar la difusión de este conocimiento, se propone el siguiente esquema estructurado para una presentación de nivel experto dirigida a profesionales de la salud, gestores hospitalarios y especialistas en TI.

## **Módulo 1: El Lenguaje de la Salud Digital**

* **Introducción**: La crisis de la información fragmentada y el costo de la "no interoperabilidad".
* **Conceptos Clave**: ¿Por qué un código vale más que mil palabras? Definición de interoperabilidad semántica.1
* **Taxonomía de Recursos**: Clasificaciones, terminologías y ontologías. Diferencias estructurales y propósitos de uso.12

## **Módulo 2: Estándares de Referencia Mundial**

* **SNOMED CT**: El "ADN" del registro clínico. Conceptos, jerarquías y el poder de la pos-coordinación.9
* **LOINC**: Estandarizando la observación. El modelo de 6 ejes y su aplicación en laboratorio y clínica.23
* **CIE-11**: La evolución hacia la salud digital. Fundación, linealizaciones y codificación en clúster.13

## **Módulo 3: La Tecnología Detrás del Estándar**

* **HL7 FHIR**: El lenguaje de intercambio. Recursos de terminología y servicios web.33
* **Servidores de Terminología**: Cómo operan $lookup, $expand y $translate para dar vida a los códigos.34
* **Ecosistema Interconectado**: Integración de RxNorm para fármacos y DICOM para imágenes.6

## **Módulo 4: Estrategia de Implementación y Gobernanza**

* **Mapeo de Datos**: Del caos local al orden internacional. Herramientas y metodologías.26
* **Gobernanza Nacional**: El rol de los NRC y las políticas de interoperabilidad en la región (Ejemplo: Uruguay y Colombia).4
* **Usabilidad Clínica**: Terminologías de interfaz y diseño centrado en el usuario para reducir la carga cognitiva.2

## **Módulo 5: Innovación y Futuro**

* **IA y PLN**: Extrayendo valor del texto libre. Codificación automática y soporte a la decisión.39
* **El Rol de los LLM**: Cómo la IA generativa está acelerando la normalización semántica.21
* **Conclusiones y Desafíos Éticos**: Transparencia, sesgos y el futuro de la seguridad del paciente en un mundo codificado.5

Este análisis demuestra que la implementación de vocabularios y terminologías en salud no es un fin en sí mismo, sino el medio indispensable para lograr una atención sanitaria más segura, eficiente y basada en la evidencia. La convergencia de estándares robustos, arquitecturas técnicas modernas como FHIR y el potencial de la IA ofrece una oportunidad histórica para transformar los datos de salud en conocimiento accionable para el beneficio del paciente.

#### **Works cited**

1. Interoperabilidad para principiantes - IADB Publications, accessed March 24, 2026, [https://publications.iadb.org/publications/spanish/document/Interoperabilidad\_para\_principiantes\_La\_base\_de\_la\_salud\_digital.pdf](https://publications.iadb.org/publications/spanish/document/Interoperabilidad_para_principiantes_La_base_de_la_salud_digital.pdf)
2. Introducción a la interoperabilidad semántica - PAHO IRIS, accessed March 24, 2026, [https://iris.paho.org/bitstreams/fc1f6590-2487-41ed-8c75-e09e18b337ac/download](https://iris.paho.org/bitstreams/fc1f6590-2487-41ed-8c75-e09e18b337ac/download)
3. Arquetipos, terminologías e interoperabilidad semántica en salud - SciELO Cuba - Infomed, accessed March 24, 2026, [http://scielo.sld.cu/scielo.php?script=sci\_arttext\&pid=S0864-03002015000400007](http://scielo.sld.cu/scielo.php?script=sci_arttext&pid=S0864-03002015000400007)
4. Resolucion No 1888 de 2025.pdf - Ministerio de Salud y Protección Social, accessed March 24, 2026, [https://www.minsalud.gov.co/Normatividad\_Nuevo/Resolucion%20No%201888%20de%202025.pdf](https://www.minsalud.gov.co/Normatividad_Nuevo/Resolucion%2520No%25201888%2520de%25202025.pdf)
5. Aplicaciones, oportunidades y desafíos de implementar la inteligencia artificial en medicina, accessed March 24, 2026, [http://www.scielo.org.co/scielo.php?script=sci\_arttext\&pid=S0122-06672024000200089](http://www.scielo.org.co/scielo.php?script=sci_arttext&pid=S0122-06672024000200089)
6. Interoperabilidad semántica: ¿El reto más grande en el sector salud? - Siftia, accessed March 24, 2026, [https://siftia.tech/es/recursos/interoperabilidad-semantica-el-reto-mas-grande-en-el-sector-salud/](https://siftia.tech/es/recursos/interoperabilidad-semantica-el-reto-mas-grande-en-el-sector-salud/)
7. 2\. Vocabularios Controlados Snomed-CT-UML-XML-JSON, accessed March 24, 2026, [https://www.alephn.com/doc/Clase\_2.pdf](https://www.alephn.com/doc/Clase_2.pdf)
8. fundamentos sobre terminología clínica SNOMED CT - GUB.UY, accessed March 24, 2026, [https://www.gub.uy/agencia-gobierno-electronico-sociedad-informacion-conocimiento/sites/agencia-gobierno-electronico-sociedad-informacion-conocimiento/files/documentos/publicaciones/Fundamentos%20sobre%20terminolog%C3%ADa%20cl%C3%ADnica%20SNOMED%20CT.pdf](https://www.gub.uy/agencia-gobierno-electronico-sociedad-informacion-conocimiento/sites/agencia-gobierno-electronico-sociedad-informacion-conocimiento/files/documentos/publicaciones/Fundamentos%2520sobre%2520terminolog%25C3%25ADa%2520cl%25C3%25ADnica%2520SNOMED%2520CT.pdf)
9. SNOMED CT | Agencia de Gobierno Electrónico y Sociedad de la Información y del Conocimiento, accessed March 24, 2026, [https://www.gub.uy/agencia-gobierno-electronico-sociedad-informacion-conocimiento/node/346](https://www.gub.uy/agencia-gobierno-electronico-sociedad-informacion-conocimiento/node/346)
10. impacto del estándar health level seven (hl7) -fhir en el desarrollo de software para la - Repositorio UTN, accessed March 24, 2026, [https://repositorio.utn.edu.ec/bitstream/123456789/9124/1/ART%C3%8DCULO.pdf](https://repositorio.utn.edu.ec/bitstream/123456789/9124/1/ART%25C3%258DCULO.pdf)
11. SNOMED CT como terminología - Sociedad Española de Informática de la Salud, accessed March 24, 2026, [https://seis.es/wp-content/uploads/2018/02/Revista-80.pdf](https://seis.es/wp-content/uploads/2018/02/Revista-80.pdf)
12. Estándares de codificación e interoperabilidad en Salud: evaluación del proyecto AmIHEALTH - SciELO Cuba, accessed March 24, 2026, [http://scielo.sld.cu/scielo.php?script=sci\_arttext\&pid=S2307-21132019000300007](http://scielo.sld.cu/scielo.php?script=sci_arttext&pid=S2307-21132019000300007)
13. The new International Classification of Diseases 11th edition: a comparative analysis with ICD-10 and ICD-10-CM - PMC, accessed March 24, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7309235/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7309235/)
14. \[ICD-11, ICHI and SNOMED CT-What do the standards mean for eHealth applications?], accessed March 24, 2026, [https://pubmed.ncbi.nlm.nih.gov/29846742/](https://pubmed.ncbi.nlm.nih.gov/29846742/)
15. Análisis de terminologías de salud para su utilización como ontologías computacionales en los sistemas de información clínicos | Gaceta Sanitaria, accessed March 24, 2026, [https://www.gacetasanitaria.org/es-content-articulo-S0213911108724178](https://www.gacetasanitaria.org/es-content-articulo-S0213911108724178)
16. La ontología como herramienta de representación terminológica: consideraciones para su construcción - SciELO México, accessed March 24, 2026, [https://www.scielo.org.mx/scielo.php?script=sci\_arttext\&pid=S2007-50572023000100082](https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S2007-50572023000100082)
17. Clasificaciones y terminologias, accessed March 24, 2026, [https://www.who.int/es/standards/classifications](https://www.who.int/es/standards/classifications)
18. Implementación de SNOMED CT | Practical Guides Guía de ..., accessed March 24, 2026, [https://docs.snomed.org/snomed-ct-practical-guides/guia-de-introduccion-a-snomed-ct/8-implementacin-de-snomed-ct](https://docs.snomed.org/snomed-ct-practical-guides/guia-de-introduccion-a-snomed-ct/8-implementacin-de-snomed-ct)
19. Introducción a SNOMED CT | Practical Guides Intro a SCT para proveedores, accessed March 24, 2026, [https://docs.snomed.org/snomed-ct-practical-guides/intro-a-sct-para-proveedores/introduccin-a-snomed-ct](https://docs.snomed.org/snomed-ct-practical-guides/intro-a-sct-para-proveedores/introduccin-a-snomed-ct)
20. La creciente adopción de SNOMED CT en América Latina, respalda las estrategias de salud digital, para la interoperabilidad y una mejor atención médica | Innova - Hospital Italiano, accessed March 24, 2026, [https://www1.hospitalitaliano.org.ar/landing/innova-salud-digital/articulos/la-creciente-adopcion-de-snomed-ct-en-america-latina-respalda-las-estrategias-de-salud](https://www1.hospitalitaliano.org.ar/landing/innova-salud-digital/articulos/la-creciente-adopcion-de-snomed-ct-en-america-latina-respalda-las-estrategias-de-salud)
21. Use of SNOMED CT in Large Language Models: A Scoping Review (Preprint), accessed March 24, 2026, [https://www.researchgate.net/publication/384059962\_Use\_of\_SNOMED\_CT\_in\_Large\_Language\_Models\_A\_Scoping\_Review\_Preprint](https://www.researchgate.net/publication/384059962_Use_of_SNOMED_CT_in_Large_Language_Models_A_Scoping_Review_Preprint)
22. Uso de SNOMED CT en informática médica, accessed March 24, 2026, [https://docs.snomed.org/snomed-ct-practical-guides/guia-de-introduccion-a-snomed-ct/3-uso-de-snomed-ct-en-informtica-mdica](https://docs.snomed.org/snomed-ct-practical-guides/guia-de-introduccion-a-snomed-ct/3-uso-de-snomed-ct-en-informtica-mdica)
23. What is LOINC (Logical Observation Identifiers Names and Codes)? - Clinii, accessed March 24, 2026, [https://www.clinii.com/healthcare-abbreviation-list/what-is-loinc/](https://www.clinii.com/healthcare-abbreviation-list/what-is-loinc/)
24. Recent Developments in Clinical Terminologies — SNOMED CT, LOINC, and RxNorm, accessed March 24, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6115234/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6115234/)
25. LOINC Features | Implementation Guides LOINC Implementation Guide, accessed March 24, 2026, [https://docs.snomed.org/implementation-guides/loinc-implementation-guide/about-loinc/2.1-loinc-features](https://docs.snomed.org/implementation-guides/loinc-implementation-guide/about-loinc/2.1-loinc-features)
26. Logical Observation Identifiers Names and Codes (LOINC®) Applied to Microbiology: A National Laboratory Mapping Experience in Taiwan - PMC, accessed March 24, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8464801/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8464801/)
27. loinc - Health Data Standards and Terminologies: A Tutorial - NIH, accessed March 24, 2026, [https://www.nlm.nih.gov/oet/ed/healthdatastandards/02-530.html](https://www.nlm.nih.gov/oet/ed/healthdatastandards/02-530.html)
28. An introduction to LOINC Daniel J. Vreeman, PT, DPT, MSc - eHealth, accessed March 24, 2026, [https://www.ehealth.gov.hk/filemanager/content/pdf/en/loinc/3\_Introduction\_to\_LOINC.pdf](https://www.ehealth.gov.hk/filemanager/content/pdf/en/loinc/3_Introduction_to_LOINC.pdf)
29. The ICD-11 Foundation and classifications based on it, including ICD-11... - ResearchGate, accessed March 24, 2026, [https://www.researchgate.net/figure/The-ICD-11-Foundation-and-classifications-based-on-it-including-ICD-11-for-mortality-and\_fig1\_356076595](https://www.researchgate.net/figure/The-ICD-11-Foundation-and-classifications-based-on-it-including-ICD-11-for-mortality-and_fig1_356076595)
30. Development and Current Status of ICD-11 Mental, Behavioral, or Neurodevelopmental Disorders (Chapter 17) - Cambridge University Press \& Assessment, accessed March 24, 2026, [https://www.cambridge.org/core/books/mental-health-research-and-practice/development-and-current-status-of-icd11-mental-behavioral-or-neurodevelopmental-disorders/ED0C2B3659D634700AFA09E4C268F3C5](https://www.cambridge.org/core/books/mental-health-research-and-practice/development-and-current-status-of-icd11-mental-behavioral-or-neurodevelopmental-disorders/ED0C2B3659D634700AFA09E4C268F3C5)
31. Promoting interoperability between SNOMED CT and ICD-11: lessons learned from the pilot project mapping between SNOMED CT and the ICD-11 Foundation - PMC, accessed March 24, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11258399/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11258399/)
32. Guías de implementación de la #Interroperabilidad en salud en Colombia - YouTube, accessed March 24, 2026, [https://www.youtube.com/watch?v=f0IyM0G7mlg](https://www.youtube.com/watch?v=f0IyM0G7mlg)
33. Introduction to FHIR Terminology Module - Kodjin, accessed March 24, 2026, [https://kodjin.com/blog/introduction-to-fhir-terminology-module/](https://kodjin.com/blog/introduction-to-fhir-terminology-module/)
34. What is a FHIR Terminology Service? - Medblocks Blog, accessed March 24, 2026, [https://medblocks.com/blog/terminologies-in-fhir](https://medblocks.com/blog/terminologies-in-fhir)
35. FHIR terminology - TermX tutorial, accessed March 24, 2026, [https://tutorial.termx.org/en/fhir-terminology](https://tutorial.termx.org/en/fhir-terminology)
36. LinuxForHealth FHIR Server – FHIR Terminology Guide - GitHub Pages, accessed March 24, 2026, [https://linuxforhealth.github.io/FHIR/guides/FHIRTerminologyGuide/](https://linuxforhealth.github.io/FHIR/guides/FHIRTerminologyGuide/)
37. Hacer que los sistemas EHR funcionen para las AP - AAPA, accessed March 24, 2026, [https://www.aapa.org/es/news-central/2017/12/making-ehr-systems-work-pas/](https://www.aapa.org/es/news-central/2017/12/making-ehr-systems-work-pas/)
38. ¿Cuáles Son Los Retos De Implementar Inteligencia Artificial En Los Sistemas De Salud Y Cómo Manejarlos Eficientemente? - Atlantis University, accessed March 24, 2026, [https://atlantisuniversity.edu/es/au\_blog/retos-inteligencia-artificial-en-salud/](https://atlantisuniversity.edu/es/au_blog/retos-inteligencia-artificial-en-salud/)
39. Development and Evaluation of SNOMED CT Automated Mapping Tool: Advancing Terminology Standardization and Semantic Interoperability - JMIR Medical Informatics, accessed March 24, 2026, [https://medinform.jmir.org/2026/1/e82670](https://medinform.jmir.org/2026/1/e82670)
40. Retos de la inteligencia artificial y sus posibles soluciones desde la perspectiva de un editorialista humano - PMC, accessed March 24, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10620000/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620000/)
41. Procesamiento de lenguaje natural (PLN) supervisado con codificación automática para una mejor atención clínica - Plantl, accessed March 24, 2026, [https://plantl.digital.gob.es/content/dam/plantl/tecnologias-lenguaje/comunicacion-formacion/bsc-2019/sesi%C3%B3n-4/pln-codificaci%C3%B3n-automatica.pdf](https://plantl.digital.gob.es/content/dam/plantl/tecnologias-lenguaje/comunicacion-formacion/bsc-2019/sesi%25C3%25B3n-4/pln-codificaci%25C3%25B3n-automatica.pdf)
42. Implementación y aplicaciones de un sistema de codificación automática de la lista de espera chilena, accessed March 24, 2026, [https://repositorio.uchile.cl/bitstream/handle/2250/196194/Implementacion-y-aplicaciones-de-un-sistema-de-codificacion-automatica-de-la-lista-de-espera-chilena.pdf?sequence=1\&isAllowed=y](https://repositorio.uchile.cl/bitstream/handle/2250/196194/Implementacion-y-aplicaciones-de-un-sistema-de-codificacion-automatica-de-la-lista-de-espera-chilena.pdf?sequence=1&isAllowed=y)
43. Avances de la IA en la Salud Pública: Tendencias y Desafíos, accessed March 24, 2026, [https://saludbydiaz.com/2024/08/24/avances-de-la-ia-en-la-salud-publica-tendencias-y-desafios/](https://saludbydiaz.com/2024/08/24/avances-de-la-ia-en-la-salud-publica-tendencias-y-desafios/)
44. RxNorm - National Library of Medicine - NIH, accessed March 24, 2026, [https://www.nlm.nih.gov/research/umls/rxnorm/index.html](https://www.nlm.nih.gov/research/umls/rxnorm/index.html)
45. About DICOM: Overview, accessed March 24, 2026, [https://www.dicomstandard.org/about-home/](https://www.dicomstandard.org/about-home/)

