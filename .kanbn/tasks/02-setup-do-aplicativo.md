---
created: 2024-11-07T19:47:53.957Z
updated: 2024-11-08T01:43:21.288Z
assigned: 'Sérgio Pereira'
progress: 1
tags:
  - ref00002
due: 2024-11-04T00:00:00.000Z
started: 2024-11-04T00:00:00.000Z
completed: 2024-11-04T00:00:00.000Z
---

# 02 - Setup do Aplicativo

Configurar os recursos iniciais necessários ao desenvolvimento.

## Sub-tasks

- [x] Versiona o aplicativo vazio - v0.0.0
- [x] Provisiona o repositório remoto e adiciona conexão ao repo. local
- [x] Sincriniza os repositórios na branch main (upload)
- [x] Torna a tag v0.0.0 num marco no repositório remoto
- [x] Cria branch dev (longa duração), na main
- [x] Cria branch feat/setup-dev (temporária), na branch dev
- [x] Atualiza repositório pip e instala libs básicas. na branch dev/feat/setup-dev
- [x] Ativa extensão kanban, no VS Code
- [x] Cria projeto 'pre-proposta' no kanban
- [x] Add alterações e faz commit
- [ ] preparar ambiente para o desenvolvimento
- [ ] cria pasta e sava recursos nas pastas
- [ ] Prepara arquivos para que a documentação seja criada durante o desenvoilvimento
- [ ] Prepara arquivos de utilitários e configurações para serem atualizados durante o desenvoilvimento
- [ ] cria e executa o makefile
- [ ] instala e configura mkdocs
- [ ] instala e configura pytest
- [ ] merge da feat na dev e cria pasta ./src/infra/log
- [ ] cria os protótipos dos logs na pasta src/infra/log
- [ ] registra falha dos testes com relatório
- [ ] regista sucesso dos testas sos logs
- [ ] cria arquivo main com argumentos e decorator do log

## Relations

- [](.md)

## Comments

- author: Sérgio Pereira
  date: 2024-11-07T19:50:17.497Z
  chore: preparar ambiente para o desenvolvimento
  
  O setup inicial prepara as configurações iniciais para o desenvolvimento do projeto pre-proposta, onde:
  - cria tag v0.0.0 para marcar o projeto vazio;
  - prepara branch dev/feat/setup-dev para setup do projeto
  - atualiza repositório e instala lib rich
  - preparar kanbn para gerenciamento das tarefas do projeto
  - cria o arquivo .kanbn/index.md
  
  ref00002
- author: Sérgio Pereira
  date: 2024-11-08T00:51:12.747Z
  chore: cria pasta e sava recursos nas pastas
  
  Prepara o ambiente para desenvolvimento:
  - Cria as pastas principais da estrutura do projeto;
  - Copia os recursos de mídias, imagens, doc, e etc. para as pasta correspondentes.
  
  ref00002
- author: Sérgio Pereira
  date: 2024-11-08T00:52:22.206Z
  chore: cria docs
  
  Prepara arquivos para que a documentação seja criada durante o desenvoilvimento
  - Cria 'LICENSE'
  - Cria 'README.md'
  - Cria 'CODE_OF_CONDUCT.md'
  - Cria 'CONTRIBUTING.md'
  - Cria 'MAINTAINERS.md'
  
  ref00002
- author: Sérgio Pereira
  date: 2024-11-08T00:54:10.775Z
  chore: cria docs
  
  Prepara arquivos de utilitários e configurações para serem atualizados durante o desenvoilvimento
  - Cria 'requirements.txt'
  - Cria 'requirements-dev.txt'
  - Cria 'MANIFEST.in'
  - Cria 'setup.py'
  - Cria 'setup.cfg'
  - Cria helpers.py
  
  ref00002
- author: Sérgio Pereira
  date: 2024-11-08T00:54:23.945Z
  chore: cria e executa o makefile
  
  ref00002
  
  
  chore: instala e configura mkdocs
  
  ref00002
  
  
  chore: instala e configura pytest
  
  ref00002
- author: Sérgio Pereira
  date: 2024-11-08T00:54:34.575Z
  chore: merge da feat na dev
  cria pasta ./src/infra/log
  
  ref00002
  
  
  chore: cria testes para o log na pasta ./tests/log 
  
  ref00002
- author: Sérgio Pereira
  date: 2024-11-08T00:54:46.560Z
  chore: cria os protótipos dos logs na pasta src/infra/log 
  
  ref00002
- author: Sérgio Pereira
  date: 2024-11-08T00:54:57.642Z
  chore:  registra falha dos testes com relatório
  
  ref00002
- author: Sérgio Pereira
  date: 2024-11-08T00:55:08.074Z
  chore:  regista sucesso dos testas sos logs
  
  ref00002
- author: Sérgio Pereira
  date: 2024-11-08T00:55:19.639Z
  chore: cria arquivo main com argumentos e decorator do log
  
  ref00002
