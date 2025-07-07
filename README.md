# MiniservicewithAI
Construir um microserviço de mensagens onde um cliente envia uma mensagem e recebe uma resposta automática gerada por IA. A solução deve simular ou integrar um fluxo real de atendimento.


MiniservicewithAI/
│
├── app/
│   ├── api.py              # Endpoints Flask
│   ├── worker.py           # Worker que processa mensagens
│   ├── ai_service.py       # Integração com modelo de IA
│   ├── storage.py          # Armazenamento do histórico
│   └── config.py           # Configurações (chaves, Redis, etc.)
│
├── requirements.txt        # Dependências do projeto
└── run.py                  # Inicializador da API Flask


