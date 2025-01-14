# pip install openai-whisper yt_dlp

import os
import yt_dlp
import whisper
import warnings
import re

# Ignorar advertencias de tipo FutureWarning
warnings.filterwarnings("ignore", category=FutureWarning)

def limpiar_nombre_archivo(nombre):
    """Limpia caracteres no válidos para nombres de archivos."""
    return re.sub(r'[\\/*?:"<>|]', "", nombre)

def descargar_audio(url):
    """
    Descargar el audio de un video dado su URL.
    Soporta YouTube y TikTok.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        titulo = info_dict.get('title', "sin_titulo")

    audio_path = 'audio.mp3'
    return audio_path, limpiar_nombre_archivo(titulo)

def transcribir_audio(archivo_audio):
    """Transcribe el audio usando el modelo Whisper."""
    modelo = whisper.load_model("large-v2")
    resultado = modelo.transcribe(archivo_audio)
    return resultado['text']

def guardar_transcripcion(texto, nombre_archivo):
    """Guarda la transcripción en un archivo de texto."""
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(texto)

def main():
    url = input("Introduce la URL del video: ")

    try:
        archivo_audio, titulo = descargar_audio(url)
        print("Audio descargado correctamente.")

        # Transcribir el audio
        print("Transcribiendo audio...")
        transcripcion = transcribir_audio(archivo_audio)
        print("Transcripción completa.")

        # Guardar la transcripción
        nombre_archivo = f"{titulo}.txt"
        guardar_transcripcion(transcripcion, nombre_archivo)
        print(f"Transcripción guardada en el archivo {nombre_archivo}.")
    
    except yt_dlp.utils.DownloadError:
        print("Error al descargar el video. Verifica la URL.")
    except RuntimeError as e:
        print(f"Error durante la transcripción: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        # Eliminar el archivo de audio para ahorrar espacio
        if os.path.exists('audio.mp3'):
            os.remove('audio.mp3')

if __name__ == "__main__":
    main()