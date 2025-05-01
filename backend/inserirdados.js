const client = require('./db');  // Agora você importa diretamente a instância do cliente

// Função para inserir dados de BPM no banco
const insertData = (macAddress, bpm) => {
  const query = 'INSERT INTO measurements(mac_address, bpm) VALUES($1, $2)';
  const values = [macAddress, bpm];

  // Inserção no banco de dados
  client.query(query, values)
    .then(res => console.log('Dados inseridos:', res))
    .catch(err => console.error('Erro ao inserir dados no banco', err));
};

module.exports = insertData;
