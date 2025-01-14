# conda install -c conda-forge openjdk

import os
import yt_dlp
import whisper
import warnings
import re
import language_tool_python  # <-- Importamos la librería de LanguageTool

# Ignorar advertencias de tipo FutureWarning (opcional)
warnings.filterwarnings("ignore", category=FutureWarning)

def limpiar_nombre_archivo(nombre):
    """Limpia caracteres no válidos para nombres de archivos."""
    return re.sub(r'[\\/*?:"<>|]', "", nombre)

def descargar_audio(url, contador):
    """
    Descargar el audio de un video dado su URL.
    Soporta YouTube (y también TikTok).
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'audio_{contador}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        titulo = info_dict.get('title', f"video_{contador}")

    audio_path = f'audio_{contador}.mp3'
    return audio_path, limpiar_nombre_archivo(titulo)

def transcribir_audio(archivo_audio):
    """Transcribe el audio usando el modelo Whisper."""
    modelo = whisper.load_model("large-v2")
    resultado = modelo.transcribe(archivo_audio, language="es")
    return resultado['text']

def corregir_texto(texto):
    """
    Corrige la ortografía y gramática usando LanguageTool.
    Devuelve el texto corregido.
    """
    # Cargamos la herramienta en español
    tool = language_tool_python.LanguageTool('es')
    # Buscamos coincidencias (errores) en el texto
    matches = tool.check(texto)
    # Retornamos el texto corregido
    texto_corregido = language_tool_python.utils.correct(texto, matches)
    return texto_corregido

def guardar_transcripcion(texto, nombre_archivo):
    """Guarda la transcripción en un archivo de texto."""
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(texto)

def main():
    # Lista de URLs a procesar
    urls = [
        # Pega aquí tus URLs de YouTube
        # "https://www.youtube.com/watch?v=TU_VIDEO"
    ]

    for idx, url in enumerate(urls, start=1):
        try:
            print(f"\nProcesando URL {idx}: {url}")
            
            # 1. Descargar el audio
            archivo_audio, titulo = descargar_audio(url, idx)
            print("Audio descargado correctamente.")

            # 2. Transcribir el audio
            print("\nTranscribiendo audio, este proceso puede llevar tiempo...")
            transcripcion = transcribir_audio(archivo_audio)
            print("Transcripción completa.")

            # 3. Corregir el texto usando LanguageTool
            print("Corrigiendo ortografía y gramática...")
            transcripcion_corregida = corregir_texto(transcripcion)
            print("Corrección completa.")

            # 4. Guardar la transcripción corregida
            nombre_archivo = f"{titulo}.txt"
            guardar_transcripcion(transcripcion_corregida, nombre_archivo)
            print(f"Transcripción guardada en el archivo {nombre_archivo}.")
        
        except yt_dlp.utils.DownloadError:
            print(f"Error al descargar el video {idx}. Verifica la URL: {url}")
        except RuntimeError as e:
            print(f"Error durante la transcripción del video {idx}: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado con el video {idx}: {e}")
        finally:
            # Eliminar el archivo de audio para ahorrar espacio
            audio_file = f'audio_{idx}.mp3'
            if os.path.exists(audio_file):
                os.remove(audio_file)
                print(f"Archivo temporal {audio_file} eliminado.")

if __name__ == "__main__":
    main()
