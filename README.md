# video-lcd-st7735
Colocando um vídeo para rodar por SPI no LCD TFT 128*160 1.8 com Raspberry Pi

Este projeto demonstra como reproduzir um vídeo em um display TFT SPI 1.8" (128x160) utilizando um Raspberry Pi. O vídeo é convertido previamente para um formato bruto (.raw) e enviado diretamente ao display via SPI para obter melhor desempenho.

# Funcionamento

- O vídeo é convertido em uma sequência de frames brutos (.raw)
- O Raspberry Pi lê esses frames continuamente
- Cada frame é enviado ao display como um bloco de pixels

# Configurando o Raspberry

## Habilitando SPI

- sudo raspi-config -> Interface Options -> Enable SPI

## Instalar em venv

- pip install adafruit-circuitpython-rgb-display pillow
- sudo apt install python3-pip python3-spidev

# Conversão de vídeo

A conversão é feita utilizando o ffmpeg, no site:
- https://onlineffmpegrunner.pages.dev/

## Comando utilizado

ffmpeg -i video.mp4 -vf transpose=1,scale=128:160,fps=8 -f rawvideo -pix_fmt bgr565le video.raw

# Parâmetros

- -i video.mp4: vídeo de entrada
- transpose=1: rotaciona o vídeo (corrige orientação)
- scale=128:160: ajusta para resolução do display
- fps=8: define taxa de frames (equilíbrio entre fluidez e desempenho)
-f rawvideo: saída sem compressão
- -pix_fmt bgr565le: formato compatível com o display

# Diagrama

Rasp -> ST7735
(1) 3.3V  : VCC
(6) GND   : GND
(24) GPIO8  : CS
(18) GPIO24 : RESET
(22) GPIO25 : A0
(19) GPIO10 : SDA
(23) GPIO11 : SCL
(12) GPIO18 : LED (opcional PWM)

# Obs

- O nome do vídeo deve ser igual, tanto para a conversão quanto no código
- O Raspberry Pi deve estar com a conexão SPI ligada, em rasp-confi 
- A resolução deve ser exatamente 128x160
- O formato RGB565/BGR565 é obrigatório
- Qualquer diferença resulta em imagem corrompida

## Limitações

- Comunicação SPI limita o desempenho
- FPS típico: 8 a 20 FPS
- Python + processamento de bytes impacta fluidez

## Poss melhorias

- Remover byte swap (corrigindo direto no ffmpeg)
- Reduzir FPS para maior estabilidade
- Usar resolução menor (com ajustes)
- Implementar buffer duplo

# Conclusão

Este projeto demonstra um método eficiente para reproduzir vídeo em um display SPI limitado, utilizando:

- Pré-processamento do vídeo
- Envio direto de frames
- Controle manual de FPS

Apesar das limitações de hardware, é possível obter um resultado visual estável e funcional com baixo custo computacional.
