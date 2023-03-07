import os

# Verifique se a ferramenta adb está instalada em seu computador
# Se não estiver instalado, instale-o em seu sistema operacional
# Adicione o caminho do adb à variável de ambiente PATH

# Conecte o smartphone ao computador usando um cabo USB
# Certifique-se de que a depuração USB esteja ativada no dispositivo

# Verifique se o dispositivo está conectado corretamente
os.system("adb devices")

# Capture a tela do dispositivo e salve-a em um arquivo
os.system("adb shell screencap -p /sdcard/screenshot.png")
os.system("adb pull /sdcard/screenshot.png \\lixo\screenshot.png")
