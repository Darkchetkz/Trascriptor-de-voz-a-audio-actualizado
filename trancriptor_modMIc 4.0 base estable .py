import vosk
import pyaudio
import threading
import json

class Transcriptor:
    def __init__(self):
        self.modelo = vosk.Model("vosk-model-es-0.42")
        self.reconocedor = vosk.KaldiRecognizer(self.modelo, 16000)
        self.microfono = pyaudio.PyAudio()
        self.microfono_index = 5
        self.microfono_stream = self.microfono.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=1024,
            input_device_index=self.microfono_index
        )
        self.texto_completo = ""
        self.pausado = False
        self.stream_abierto = True

    def escuchar_y_convertir(self):
        print("Escuchando... Habla ahora.")
        while self.stream_abierto:
            try:
                data = self.microfono_stream.read(10240, exception_on_overflow=False)
                if len(data) == 0:
                    break

                if self.reconocedor.AcceptWaveform(data):
                    resultado = self.reconocedor.Result()
                    self.procesar_resultado(resultado)

            except OSError as e:
                if e.errno == -9988:
                    self.stream_abierto = False
                    print("Stream de audio cerrado. ¿Desea reiniciar? (s/n)")
                    respuesta = input().lower()
                    if respuesta == "s":
                        self.reiniciar_stream()
                    else:
                        print("Saliendo del programa.")
                        break
                else:
                    print(f"Error de entrada/salida: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")
            except KeyboardInterrupt:
                print("Has cancelado la grabación.")
                break

    def procesar_resultado(self, resultado):
        if resultado:
            resultado_dict = json.loads(resultado)
            texto_nuevo = resultado_dict.get("text", "")

            if texto_nuevo:
                if texto_nuevo.lower() == "pausar" and not self.pausado:
                    self.pausar()
                elif texto_nuevo.lower() == "reanudar" and self.pausado:
                    self.reanudar()
                elif not self.pausado:
                    self.texto_completo += texto_nuevo + " "
                    print(texto_nuevo)

    def pausar(self):
        self.pausado = True
        print("Transcripción pausada.")

    def reanudar(self):
        self.pausado = False
        print("Transcripción reanudada.")

    def reiniciar_stream(self):
        self.microfono_stream.close()
        self.microfono_stream = self.microfono.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=1024,
            input_device_index=self.microfono_index
        )
        self.stream_abierto = True
        print("Stream de audio reiniciado.")

    def run(self):
        thread = threading.Thread(target=self.escuchar_y_convertir)
        thread.start()

def main():
    transcriptor = Transcriptor()
    transcriptor.run()

if __name__ == "__main__":
    main()