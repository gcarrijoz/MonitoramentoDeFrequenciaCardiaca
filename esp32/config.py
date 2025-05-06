# esp32/config.py

# Configurações de rede
WIFI_SSID = "S23 de Gabriel"
WIFI_PASSWORD = "12345678"

# Configurações do MQTT
MQTT_BROKER = '192.168.184.35'  # IP do seu computador (ou o IP do dispositivo que está executando o Mosquitto)
MQTT_PORT = 1883           # Porta padrão do Mosquitto
MQTT_TOPIC = 'dados_bpm'   # O tópico onde o ESP32 publicará os dados