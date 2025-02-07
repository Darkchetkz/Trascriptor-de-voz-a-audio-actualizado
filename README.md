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
