import time
import digitalio
import board
import busio
import adafruit_rgb_display.st7735 as st7735

#SPI
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI)

#Pinos
cs = digitalio.DigitalInOut(board.CE0)
dc = digitalio.DigitalInOut(board.D25)
bl.switch_to_output(value=True)

#Display
display = st7735.ST7735R(
    spi,
    cs=cs,
    dc=dc,
    rst=rst,
    width=128,
    height=160,
    rotation=0
)

#Config vídeo
FRAME_WIDTH = 128
FRAME_HEIGHT = 160
FRAME_SIZE = FRAME_WIDTH * FRAME_HEIGHT * 2  # RGB565
FPS = 8
DELAY = 1 / FPS

# Reproduzir vídeo
with open("video.raw", "rb") as f:
    while True:
        start = time.time()

        frame = f.read(FRAME_SIZE)

        if len(frame) < FRAME_SIZE:
            f.seek(0)
            continue

        #correção de cores (byte swap)
        frame = bytearray(frame)
        for i in range(0, len(frame), 2):
            frame[i], frame[i+1] = frame[i+1], frame[i]

        #envia direto pro display
        display._block(0, 0, FRAME_WIDTH - 1, FRAME_HEIGHT - 1, frame)

        # controle de FPS
        elapsed = time.time() - start
        if elapsed < DELAY:
            time.sleep(DELAY - elapsed)