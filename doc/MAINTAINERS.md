# Manutenção da Pré-proposta

Isso documenta os processos para manter a Pré-proposta.

## Revisão de solicitações de pull

Quando os desenvolvedores enviam solicitações de pull, os seguintes pontos devem ser considerados
ao decidir aceitar, solicitar alterações ou rejeitá-las:

Para novos recursos:

* O recurso é apropriado para a Pré-proposta?
* Queremos assumir a responsabilidade por manter e corrigir esse recurso?
* Isso foi implementado de uma forma que corresponda aos padrões e casos de uso existentes a Pré-proposta?
* Esta é uma implementação completa ou há um caminho claro para a conclusão?
* O recurso está documentado adequadamente?

Para todas as alterações de código:

* O CI (teste, lint, formatação) passa em todas as plataformas suportadas?
* Isso inclui cobertura de caso de teste apropriada?
* A documentação é atualizada conforme necessário?

Quando um PR é aceito:

* Atualize o título do PR, se necessário, para esclarecer o propósito.
* Prefira usar commits de mesclagem do Github para registrar o nome e o número do PR.
* Para PRs automatizados (como pyup.io), prefira usar o rebase da IU do Github.

## Lançando novas versões

1. Decida o próximo número de versão, com base no que foi adicionado a `main`
desde o lançamento anterior:

* As principais mudanças de quebra devem incrementar o primeiro número e redefinir os outros
dois, por exemplo, `0.10.0 -> 1.0.0`
* Os novos recursos devem incrementar o segundo número e redefinir o terceiro,
por exemplo, `0.10.0 -> 0.11.0`
* As correções de bugs devem incrementar apenas o terceiro número, por exemplo, `0.10.0 -> 0.10.1`.

2. Atualize `pre-proposta/__init__.py` com o novo número de versão.

3. Atualize `CHANGELOG.md` com a nova versão, seguindo o mesmo padrão das
versões anteriores. As entradas devem fazer referência ao número PR e a quaisquer
números de problemas associados relacionados ao recurso ou alteração descrita.

Os contribuidores desta versão devem ser reconhecidos incluindo a saída
de `git shortlog -sn <tag anterior>...`.

4. Confirme o número da versão atualizada e o changelog com uma mensagem seguindo
o padrão "(Feature | bugfix) release v<version>".

5. Envie este commit para o branch master upstream e aguarde a execução/aprovação do CI.

6. Marque este commit com o número da versão (incluindo o "v" precedente)
usando `git tag -s v<version>` e cole o conteúdo do changelog
para esta versão como a mensagem da tag. Certifique-se de criar uma tag assinada (`-s`)
usando uma chave GPG anexada ao seu perfil do Github.

7. Envie esta tag para o upstream usando `git push --tags` e aguarde a aprovação do CI.

8. Publique esta versão no PyPI usando `make release` para construir e fazer o upload da distribuição de código-fonte e dos pacotes.
