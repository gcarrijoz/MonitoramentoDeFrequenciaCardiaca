import network
import time
import ujson
from umqtt.simple import MQTTClient
from machine import ADC, Pin
from config import WIFI_SSID, WIFI_PASSWORD, MQTT_BROKER, MQTT_PORT, MQTT_TOPIC

# Função para conectar ao Wi-Fi
def conecta_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando ao Wi-Fi...")
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        tentativas = 0
        while not wlan.isconnected() and tentativas < 10:
            time.sleep(1)
            tentativas += 1
    if wlan.isconnected():
        print("Conectado! IP:", wlan.ifconfig()[0])
    else:
        print("Falha ao conectar.")
    return wlan.isconnected()

# Função para pegar o MAC do ESP32
def get_mac():
    wlan = network.WLAN(network.STA_IF)
    mac = wlan.config('mac')
    return ':'.join('%02x' % b for b in mac)

# Função para ler e mapear o valor do potenciômetro para a faixa de BPM
def ler_potenciometro():
    pot = ADC(Pin(0))  # Usando GPIO 0 (ADC1_CH0 no ESP32-C3)
    pot.atten(ADC.ATTN_11DB)  # Faixa de 0-3.3V
    valor = pot.read()  # Lê valor de 0 a 4095 (12 bits)
    bpm = (valor / 4095) * 180  # Mapeia para 0-180 BPM
    return round(bpm)

# --- Programa principal ---
if conecta_wifi():
    client_id = get_mac().replace(":", "")  # remove os ":" para evitar problemas
    client = MQTTClient(client_id, MQTT_BROKER, port=MQTT_PORT)

    try:
        client.connect()
        print("Conectado ao broker MQTT.")
        while True:
            bpm = ler_potenciometro()
            payload = {
                "id_dispositivo": get_mac(),
                "bpm": bpm,
                "timestamp": time.time()
            }
            client.publish(MQTT_TOPIC, ujson.dumps(payload))
            print("Enviado:", payload)
            time.sleep(2)
    except Exception as e:
        print("Erro MQTT:", e)
    finally:
        client.disconnect()
else:
    print("Verifique sua conexão Wi-Fi.")