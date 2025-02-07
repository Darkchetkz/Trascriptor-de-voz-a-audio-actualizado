Descripción General
El programa utiliza el modelo de reconocimiento de voz vosk para capturar audio desde un micrófono y transcribirlo en tiempo real. El audio se procesa en fragmentos pequeños, y los resultados se muestran en la consola. Además, incluye funcionalidades como pausar y reanudar la transcripción, manejar errores y reiniciar el flujo de audio si es necesario.

Componentes Principales
1. Importaciones
vosk : Biblioteca de reconocimiento de voz que permite convertir audio en texto.
pyaudio : Biblioteca para capturar audio desde el micrófono.
threading : Permite ejecutar la escucha y transcripción en un hilo separado, evitando bloquear la interfaz principal.
json : Se utiliza para procesar los resultados JSON devueltos por vosk.
2. Clase Transcriptor
La clase Transcriptor encapsula toda la lógica del sistema de transcripción.

Método __init__
Inicializa el modelo de reconocimiento de voz (vosk.Model) con un modelo específico para el idioma español (vosk-model-es-0.42).
Configura el reconocedor de voz (vosk.KaldiRecognizer) con una tasa de muestreo de 16 kHz.
Abre un flujo de audio (pyaudio.PyAudio) para capturar datos del micrófono seleccionado (índice 5 en este caso).
Define variables para almacenar el texto transcrita (texto_completo), el estado de pausa (pausado) y el estado del flujo de audio (stream_abierto).
Método escuchar_y_convertir
Escucha continuamente el audio del micrófono en un bucle.
Lee fragmentos de audio (read) y los pasa al reconocedor de voz.
Si el reconocedor detecta texto válido, llama al método procesar_resultado.
Maneja errores como la interrupción del flujo de audio (OSError) o excepciones inesperadas.
Permite reiniciar el flujo de audio si se cierra inesperadamente.
Método procesar_resultado
Procesa el resultado JSON devuelto por vosk.KaldiRecognizer.
Extrae el texto transcrita y lo agrega al atributo texto_completo.
Implementa comandos de voz para pausar ("pausar") y reanudar ("reanudar") la transcripción.
Métodos pausar y reanudar
Cambian el estado de la transcripción entre pausado y activo.
Método reiniciar_stream
Cierra y vuelve a abrir el flujo de audio en caso de que se cierre inesperadamente.
Método run
Inicia la escucha y transcripción en un hilo separado utilizando threading.Thread.
3. Función main
Crea una instancia de la clase Transcriptor.
Llama al método run para iniciar el proceso de transcripción.
Flujo de Ejecución
Al ejecutar el script, se crea una instancia de la clase Transcriptor.
El método run inicia un hilo que ejecuta el método escuchar_y_convertir.
El programa comienza a escuchar el audio del micrófono y transcribe el texto en tiempo real.
Si el usuario dice "pausar", la transcripción se detiene temporalmente.
Si el usuario dice "reanudar", la transcripción continúa.
En caso de errores o interrupciones, el programa maneja las excepciones y ofrece opciones para reiniciar o salir.
Características Notables
Multithreading : La transcripción se ejecuta en un hilo separado, lo que permite mantener la interfaz principal receptiva.
Manejo de Errores : El programa maneja errores como la interrupción del flujo de audio y ofrece opciones para recuperarse.
Comandos de Voz : Implementa comandos simples ("pausar" y "reanudar") para controlar la transcripción.
Reinicio Automático : Si el flujo de audio se cierra inesperadamente, el programa puede reiniciarlo.

Para que el código funcione correctamente, necesitas descargar e instalar un modelo de Vosk compatible con el idioma y la configuración que estás utilizando. En este caso, el código está configurado para usar un modelo en español (vosk-model-es-0.42). A continuación, te explico cómo obtener y configurar el modelo.

Modelo Vosk Necesario
El modelo utilizado en el código es:

Nombre del Modelo : vosk-model-es-0.42
Idioma : Español
Tamaño : Aproximadamente 50 MB (modelo pequeño y ligero).
Este modelo está diseñado para reconocimiento de voz en tiempo real y es adecuado para aplicaciones como la transcripción de voz a texto.

Pasos para Descargar e Instalar el Modelo
Descargar el Modelo
Ve al repositorio oficial de modelos de Vosk: https://alphacephei.com/vosk/models .
Busca el modelo vosk-model-es-0.42 (español).
Haz clic en el enlace para descargarlo. El archivo descargado será un archivo .zip.
Descomprimir el Modelo
Una vez descargado, descomprime el archivo .zip en una carpeta de tu elección.
Por ejemplo, puedes crear una carpeta llamada modelos_vosk en tu directorio de trabajo y colocar el modelo allí:
Copy
1
/ruta/a/tu/proyecto/modelos_vosk/vosk-model-es-0.42
Configurar la Ruta en el Código
En el código, asegúrate de que la ruta al modelo coincida con la ubicación donde lo descomprimiste. En el constructor de la clase Transcriptor, la línea relevante es:
python
Copy
1
self.modelo = vosk.Model("vosk-model-es-0.42")
Si el modelo está en una carpeta diferente, actualiza la ruta. Por ejemplo:
python
Copy
1
self.modelo = vosk.Model("/ruta/a/tu/proyecto/modelos_vosk/vosk-model-es-0.42")
Verificación del Modelo
Antes de ejecutar el programa, asegúrate de que:

El modelo esté correctamente descomprimido y accesible.
La ruta especificada en el código sea correcta.
Tengas instaladas las dependencias necesarias (vosk, pyaudio, etc.).
Instalación de Dependencias
Si aún no has instalado las bibliotecas necesarias, puedes hacerlo con los siguientes comandos:

bash
Copy
1
2
pip install vosk
pip install pyaudio
Nota : Si tienes problemas para instalar pyaudio, puedes intentar instalarlo desde un binario precompilado o usar un administrador de paquetes como conda:

bash
Copy
1
conda install pyaudio
Ejemplo de Estructura de Directorios
Aquí tienes un ejemplo de cómo podría verse la estructura de tu proyecto:

Copy
1
2
3
4
/proyecto_transcripcion/
    ├── main.py                # Archivo principal con el código
    ├── modelos_vosk/          # Carpeta para los modelos de Vosk
    │   └── vosk-model-es-0.42 # Modelo en español descomprimido
En este caso, la ruta en el código sería:

python
Copy
1
self.modelo = vosk.Model("modelos_vosk/vosk-model-es-0.42")
Prueba del Código
Una vez que hayas descargado y configurado el modelo, ejecuta el programa:

bash
Copy
1
python main.py
Si todo está configurado correctamente, el programa comenzará a escuchar el audio del micrófono y transcribirlo en tiempo real.

Otros Modelos Disponibles
Si deseas experimentar con otros modelos, aquí tienes algunas opciones adicionales del repositorio de Vosk:

Modelos en Español :
vosk-model-small-es-0.42: Modelo más pequeño y rápido, pero con menor precisión.
vosk-model-es-0.42: Modelo estándar (el que estás usando).
Modelos en Otros Idiomas :
vosk-model-small-en-us-0.15: Modelo pequeño para inglés (EE.UU.).
vosk-model-en-us-0.22: Modelo estándar para inglés (EE.UU.).
Puedes cambiar el modelo en el código simplemente actualizando la ruta y el nombre del modelo.

Conclusión
El modelo vosk-model-es-0.42 es el adecuado para que el código funcione con el idioma español. Asegúrate de descargarlo, descomprimirlo y configurar la ruta correctamente en el código. Con esto, estarás listo para realizar transcripciones de voz a texto en tiempo real.


