from gpiozero import Button
from signal import pause
import subprocess
import sys

# Debounce 0.05 segundos para evitar múltiplos cliques
button = Button(23, bounce_time=0.05)

processo = None
video = 0

arquivos = {
    1: "badapple",
    2: "fnaf2",
    3: "ncs",
    4: "silksong",
    5: "undertale"
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

    # iniciar novo
    processo = subprocess.Popen(
        [sys.executable, "/home/maximus/playlcd.py", arquivos[video]],
        cwd="/home/maximus"
    )

button.when_pressed = trocar_video

pause()