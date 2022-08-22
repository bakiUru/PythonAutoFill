@echo Reconectando WIFI
ipconfig /flushdns
ipconfig /renew
echo "Desconectando..."
netsh wlan disconnect
timeout /T 3
netsh wlan connect antel
echo "Conectando...."
timeout /T 2
echo "Conectado.. " | ipconfig

