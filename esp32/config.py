# esp32/config.py

# Configurações de rede
WIFI_SSID = "victor"
WIFI_PASSWORD = "victor1109"

# Configurações do MQTT
MQTT_BROKER = '192.168.100.122'  # IP do seu computador (ou o IP do dispositivo que está executando o Mosquitto)
MQTT_PORT = 1883           # Porta padrão do Mosquitto
MQTT_TOPIC = 'dados_bpm'   # O tópico onde o ESP32 publicará os dados