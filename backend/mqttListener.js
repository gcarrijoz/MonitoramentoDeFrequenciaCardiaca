const mqtt = require('mqtt');
const insertData = require('./inserirdados');  // Função para inserir dados no banco

// Conecta ao broker MQTT (ajuste o host se necessário)
const client = mqtt.connect('mqtt://localhost');

// Quando a conexão com o broker for estabelecida
client.on('connect', () => {
  console.log('Conectado ao broker MQTT');

  // Inscreve-se no tópico onde os dados do ESP32 estão sendo enviados
  client.subscribe('dados_bpm', (err) => {
    if (!err) {
      console.log('Inscrito no tópico "dados_bpm"');
    } else {
      console.error('Erro ao se inscrever no tópico:', err);
    }
  });
});

// Quando uma mensagem for recebida no tópico
client.on('message', (topic, message) => {
  try {
    const data = JSON.parse(message.toString());

    const { id_dispositivo, bpm, timestamp } = data;

    // Validação básica dos dados
    if (!id_dispositivo || typeof bpm !== 'number' || typeof timestamp !== 'number') {
      console.warn('⚠️ Mensagem MQTT inválida ou incompleta:', data);
      return;
    }

    // Insere os dados no banco de dados
    insertData(id_dispositivo, bpm, timestamp);

    console.log(`Dados recebidos - ID Dispositivo: ${id_dispositivo}, BPM: ${bpm}, Timestamp: ${timestamp}`);
  } catch (err) {
    console.error('Erro ao processar mensagem MQTT:', err.message);
  }
});
