const { Client } = require('pg');

// Criação do cliente de conexão
const client = new Client({
  user: 'postgres',
  host: 'localhost',
  database: 'dbMonitoramentoCardiaco',
  password: '102030',
  port: 5432,
});

// Conexão ao banco de dados
client.connect()
  .then(() => console.log('Conectado ao banco de dados PostgreSQL'))
  .catch((err) => console.error('Erro ao conectar ao banco de dados', err));

// Exportando o client para ser usado em outros módulos
module.exports = client;
