from gpiozero import Button
from signal import pause
import subprocess
import sys

# Debounce 0.05 segundos para evitar múltiplos cliques
button = Button(23, bounce_time=0.05)

processo = None
video = 0

# Inserir nome dos arquivos aqui
arquivos = {
    1: "video1",
    2: "video2"
}

def trocar_video():
    global processo, video # pra não criar novas variaveis

    # Corta o vídeo em execução
    if processo:
        processo.kill()

    # próximo vídeo
    video += 1
    if video > 5:
        video = 1

    # trocar "seuusuario"
    processo = subprocess.Popen(
        [sys.executable, "/home/seuusuario/play-video-st7735.py", arquivos[video]],
        cwd="/home/seuusuario"
    )

button.when_pressed = trocar_video

pause()
