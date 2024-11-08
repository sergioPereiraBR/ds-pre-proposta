# Contribuindo para a Pré-proposta

Queremos tornar a contribuição para este projeto o mais fácil e transparente
possível.

## Começando

Ao desenvolver a Pré-proposta, siga estas etapas para configurar seu ambiente,
formatar seu código e executar linters e testes de unidade:

1. Fork [Pré-proposta][] no Github.

1. Clone o repositório git:
```bash
$ git clone https://github.com/$USERNAME/ds-pre-proposta.git
$ cd ds-pre-proposta.git
```

1. Configure o ambiente virtual com dependências e ferramentas:
```bash
$ make dev
$ source .venv/bin/activate
```

1. Formate seu código usando [*Black*](https://github.com/ambv/black) e
[isort](https://pypi.org/project/isort/):
```bash
$ make format
```

1. Execute linter, verificações de tipo e testes de unidade:
```bash
$ make lint test
```

## Solicitações de pull

Aceitamos ativamente suas solicitações de pull.

1. Se você adicionou código que deve ser testado, adicione testes de unidade.
1. Se você alterou APIs, atualize a documentação.
1. Garanta que o conjunto de testes seja aprovado.
1. Garanta que seu código seja aprovado.
1. Se ainda não o fez, conclua o Contrato de Licença do Contribuidor ("CLA").

## Contrato de Licença do Contribuidor ("CLA")

Para aceitar sua solicitação de pull, precisamos que você envie um CLA. Você só precisa
fazer isso uma vez para trabalhar em qualquer um dos projetos de código aberto do Facebook.

Conclua seu CLA aqui: <https://code.facebook.com/cla>

## Problemas

Usamos problemas do GitHub para rastrear bugs públicos. Garanta que sua descrição seja
clara e tenha instruções suficientes para poder reproduzir o problema.

O Facebook tem um [programa de recompensas](https://www.facebook.com/whitehat/) para a divulgação segura
de bugs de segurança. Nesses casos, siga o processo
descrito naquela página e não registre um problema público.

## Licença

Ao contribuir para o Bowler, você concorda que suas contribuições serão licenciadas
sob o arquivo `LICENSE` no diretório raiz desta árvore de origem.

[Pré-proposta]: https://github.com/sergioPereiraBR/ds-pre-proposta.git

