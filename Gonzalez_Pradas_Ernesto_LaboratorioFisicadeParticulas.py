# %% [markdown]
# 
#  # Objetivo del laboratorio
#  Se pide un informe técnico personal, elegante y bien presentado de todas las tareas necesarias para la ejecución de la actividad. Es decir, reproducid en vuestro escenario todos los pasos realizados y que más o menos imiten a los que ya vienen descritos en este documento (instalación de software, configuración, accesos remotos, etc.).
#
#  Contestad a todas las preguntas intermedias que se proponen.
#  **Pregunta:** ¿cuál es la diferencia entre una imagen y un contenedor? Un poco de ayuda.
#   > La diferencia entre una **<u>imagen y un contenedor</u>** es que la imagen contiene lo necesario para ejecutar una aplicación como contendor, y un contenedor es una instancia en tiempo de ejecución de una imagen.
#
#  **Preguntas:** ¿Qué otros formatos estándar de representación 3D conoces (Collada, Stanford, Wavefront, X3D Extensible, Standard Tessellation Language, x3dom, etc.)? ¿Quién desarrolla Instant Player qué contribuciones ha hecho al mundo de la tecnología?
#   > Collada que está desarrollado por Sony Computer Entertainment y grupo Khronos, en Octubre de 2004 y fue pensado como un un formato para transportar datos desde una herramieta de creación de contenido digital a otra aplicación. Además extiende de XML.
#     Wavefront Technologies que desarrolló el formato OBJ de datos simples que representa geometría 3D. Existe una biblioteca de plantillas de material que describe lads propiedades de superficie de los objetos dentro de un OBJ.
#     Instant Player ha sido desarrollado por Fraunhofer IGD y ZGDV. El diseño incluye varios estándares para facilitar el proceso de desarrollo como por ejemplo OpenGL2.0 y GLSL (del grupo Khronos) o CG (Nvidia corporation)  
# 
#  **Pregunta:** ¿en qué proyectos está involucrada la empresa Kitware y cómo han cambiado el mundo de la informática, la tecnología, la ciencia y la medicina? Pista: CMake, VTK, ITK, etc.
#  > Kitware, Inc es una empresa de tecnología ubicada en Nueva York y está especializada en el desarrollo y la investigación de programas y herramientas de código abierto. Estas herramientas se enfocan sobre todo en áreas como visión por computador, imágens médicas y análisis de información multidimensional.
#    Algunas como CMake, VTK o ITK son herrramientas de desarrollo de código libre.
# 
# **Pregunta:** ¿qué es Docker? ¿Qué son los contenedores virtuales? ¿Qué alternativas a Docker existen (OpenVZ, LXC, Vagrant, rkt, etc.)?
#   > Docker es como una caja o contenedor donde tendremos todo lo necesario para poder ejecutar nuestra aplicación. Tendremos nuestro servidor por ejemplo tomcat, framworks, maven etc y nos lo podemos llevar a cualquier lado y a cualquier máquina, ya que quien ejecuta mi aplicación no es el ordenador en el que esté si no el propio contenedor o docker.
#     Los contenedores virtuales son máquinas virtuales que permiten aislarse de la máquina real o sistema operativo subyacente y ejecutra nuestra aplicación.
#     El mayor competidor de docker es rkt. rkt nace como resultado de la insatisfacción con el propio docker ya que se había desviado de su objetico, que hacer tecnología estandar de virtualización pero finalmente ha quedado más como una plataforma de desarrollo de aplicaciones.
#
#  # Ejecución del Laboratorio
#   Para llevar a cabo este laboratorio empezaremos creando una instancia en Play with Docker haciendo ADD NEW INSTANCE:
#
#   ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/Captura1AddNewInstance.PNG "ADD NEW INSTANCE")
#      
#
#   A continuación creamos un workspace donde guardaremos los archivos .key y .ppk y también desde dondeiremos editando el archivo simulacion.py:
#   
#   ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/Captura2workspace.PNG "workspace")  
#
#   **Preguntas:** ¿Qué es un fichero ppk? ¿Qué es una clave RSA público/privada (fichero key)?
#
#   > Un fichero **<u>ppk</u>** es un archivo creado por por PuTTYgen que no es más que una utilidad para generar claves de tipo RSA y DSA. Las claves RSA son un sistema criptográfico de clave pública
#     o también llamados criptografía asimétrica o de dos claves desarrollado por los criptógrafos Ronald Rivest, Adi Shamir y el biólogo molecular Leonard Adleman y que es válido tanto para
#     cifrar como para firmar digitalmente.
#
#   # Descargamos la imagen Docker del laboratorio
#   Una vez realizado el workspace y preparado todas las herramientas comenzamos con la descarga de la imagen de la pila de contenedores que conforman una imagen con todo lo necesario para ejecutar Geant4.
#   **Preguntas:** ¿qué es el Hub de Docker? ¿Cuál es la diferencia entre una imagen y un contenedor?
#
#   > El **<u>Hub de docker</u>** es un repositorio donde se encuentran las imágenes Docker, dicho de otra forma, es como una especie de biblioteca donde se almacenan las imágenes Docker.
#      La diferencia entre una **<u>imagen y un contenedor</u>** es que la imagen contiene lo necesario para ejecutar una aplicación como contendor, y un contenedor es una instancia en tiempo de ejecución de una imagen.
#
#   Para esto enviamos una orden ejecutando un comando remoto desde SSH sin salir de VS Code. Como usamos una consola PowerShell guardamos previamente la cadena que identifica la conexión en una variable de entorno $usuariopwd.
#   
#   ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/Captura3usuariopwd.PNG "usuariopwd")
#
#   Nos aseguramos previamente de tener bien configurado el settings.json de nuestro VS Code para poder lanzar conexiones ssh:
#
#   ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/Captura4settings.PNG "settings.json")
#
#   Y lanzamos, como hemos dicho, una conexión a la consola remota de Play with Docker con SSH:
#
#   ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/Captura5plink.PNG "plink")
#
#   Como vemos ya estamos conectados, y podemos lanzar la descargar de la imagen Docker con el siguiente comando:
#   
#   ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/Captura6DescargaImagen.PNG "Descargar Imagen Docker")
#
#   Este comando, docker pull, nos eprmite descargarnos la imagen de geant4lab alojada en el hub de Docker.
#
#   A continuación tenemos guardado en nuestro workspace el archivo simulacion.py que describe un experimento de física de partículas, en un universo cuboide donde las particulas son acelaradas y proyectadas contra un objeto (fantoma) de un material y tamaño concreto a nuestra elección.
#
#   ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/Captura7imagenparticulas.PNG "imagen partículas")
#
#   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**Pregunta:** ¿Cómo se llama a este tipo de haz de partículas?!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#   > 
#
#   Editamos este .py con lo comentado en clase y lo copiamos de forma remota cada vez que hagamos un cambio:
#   
#   ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/Captura8copiaarchivo.PNG "copiar archivo")
#
#   **Preguntas:** comenta las líneas más importantes del código Python anterior (el de la simulación). Intenta extraer su significado por sus palabras. Si tienes dudas, pregunta en el foro. ¿En qué unidades viene descrita la energía de las partículas? Verifica que verdaderamente se corresponden con unidades de energía y expresa un par de ejemplos en Julios (unidad de energía en el S.I.).
#
#   > Las **<u>unidades</u>** de las partículas son el Megaelectronvoltio.
#
#   # Ejecución de la simulación
#   
#   Ahora lanzamos el comando de ejecución de la simulación:
#   
#   ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/Captura9ejecucionprograma.PNG "ejecucion programa") 
#
#   Al lanzar este comando nos aparece un fichero nuevo en la instancia remota, simulacion.wrl. Este fichero es una simulación 3D que podemos ver simplemente pasándolo a html y visualizándolo en nuestro navegador (por ejemplo google Chrome)
#   **Pregunta:** ¿Qué son los archivos wrl? ¿De qué estándar internacional se trata?
# 
#   > Los **<u>archivos wrl</u>** son archivos creados en Lenguaje Modelado de Realidad Virtual es decir en VRML, que representa un entorno 3D y se guarda en texto ASCII pudiendo ser editado en cualquier editor de textos.
#       El **<u>estándar internacionl</u>** del que se trata es ISO/IEC 14772-1:1997
#
#   # Visualización de la simulación
# 
#   Como hemos comentado anteriormente para visualizar nuestra simulación, tenemos que realizar los siguientes pasos:
#       
#   1. Descargamos nuestro archivo de la simulación con el siguiente comando:
#
#      ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/Captura10descargarsimulacion.PNG "descargar simulación")
#
#   2. Para poder ver visualizarlo en html, tenemos que convertir nuestra simulación recién descargada a formato html. Para ello primero descargamos wrl2html.py en nuestro workdpace:
#
#       ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/Captura11descargaromsconversorhtml.PNG "descargarmos conversor html")
#
#   3. Con el siguiente comando convertimos el archivo de nuestra simulación en formato html:
#
#       ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/Captura12convertirahtml.PNG "convertir a html")
#
#   4. Copiamos el html generado a nuestro disco duro mediante el siguiente comando:
#
#       ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/Captura13copiahtmlanuestrodiscoduro.PNG "copiar html a nuestro dicos duro")
#
#   5. Abrimos nuestra simulacion.html en nuestro navegador favorito:
#
#   https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/simulacion.html
#
#   **Pregunta:** ¿Cómo es posible que veamos figuras 3D en una página web? ¿Qué estándares, alternativas, consorcios e instituciones están implicados? ¿Qué alternativa estamos usando en este ejercicio (pista) y qué gran centro de investigación en matemáticas estuvo implicado (pista)?
#   > El consorcio Web3D es una organización sin fines de lucro que desarrolla y mantiene estándares internacionales X3D, VRML y H-Anim. Usamos un modelo que integra directamente X3D en el DOM de HTML5. Con este modelo podemos observar imágenes 3D en nuestro navegador.
# 
#   # Identificación de los tipos de interacciones de partículas con la materia
#
#   **Ionización**
#   ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/ionizaci%C3%B3n.PNG "Ionización")
#  
#   **Producción de Pares**
#   ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/produccionpares.PNG "Producción de Pares")
#   
#   **Efecto fotoeléctrico**
#   ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/Captura15particula1.PNG "Efecto fotoeléctrico")
#
#   **Efecto Compton**
#   ![Error, captura no encontrada](https://nbviewer.jupyter.org/github/ErnestoGPradas/LaboratorioFisicaDeParticulas/blob/master/Captura16particula2.PNG "Efecto Compton")
#   
#   **Pregunta:** ¿cuánto tiempo puede estar serpenteando un fotón que nace en el centro del Sol hasta llegar a la retina de cualquiera de tus ojos?
#       > Un fotón para llegar a la Tierra desde el Sol, primero tiene que atravesar diferentes capas de dicho astro. El tiempo que tarda en cruzar todas estas capas va desde los 10000 hasta los 170000 años ya que debido a la gran densidad del interior del Sol el fotón va colisionando con otras
#           partículas como los átomos de hidrógeno ionizado. Después una vez que esta ya en la superficie del Sol, tarda unos 8 minutos en cruzar los 150 millones de Km que separan al astro rey con respecto a la Tierra.
#
#   **Pregunta:** ¿qué es un positrón? ¿Quién postuló su existencia teórica y cuándo y cómo se descubrió experimentalmente?
#       > El positrón es una antipartícula, más concretamente del electrón, que tiene la misma masa y la misma carga pero de signo contrario. Su existencia teórica fue de la mano de Paul Dirac en el año 1928 y su descubrimiento experimental fue llevado a cabo por
#           el científico Carl Anderson el 2 de agosto de 1932. Esto ocurrió mientras Carl Anderson estaba examinando fotografías de rayos cósmicos en una cámara de niebla.
#
#   **Pregunta:** ¿qué relación tiene la modalidad radiológica PET con la aniquilación de pares electrón-positrón? ¿Cómo se trasladan positrones hasta el interior de las células cancerígenas?
#       > Los PET se realizan suminstrándole al paciente un radiofármaco y los tomógrafos son capaces de detectar los fotones gamma emitidos por el paciente. Estos fotones gamma son el producto de una aniquilación entre un positrón, que es emitido por el radiofármaco suministrado previamente, y in electrón cortical del cuerpo del paciente.

# %%
