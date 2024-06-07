[![Test Unit Tests](https://github.com/ArduPilot/ardupilot/workflows/test%20unit%20tests%20and%20sitl%20building/badge.svg?branch=master)](https://github.com/ArduPilot/ardupilot/actions/workflows/test_unit_tests.yml)[![test size](https://github.com/ArduPilot/ardupilot/actions/workflows/test_size.yml/badge.svg)](https://github.com/ArduPilot/ardupilot/actions/workflows/test_size.yml)

# qds-fapa-qui-noite
Repositório de exemplo para a turma de qualidade de software 

## Comandos do Git (Básico)
- `git clone <url do repositório>` Clone um repositório remoto para sua máquina
- `git status` Mostra informações do projeto
- `git add <nome do arquivo>` Adiciona arquivo para ser incluído no próximo commit
- `git commit -m "<mensagem>"` Cria um commit com uma mensagem de descrição
- `git push` Envia os commits que ainda não foram enviados para o servidor remoto
- `git pull` Baixa os commit que existem no servidor remoto e ainda não estão no seu computador


## Mais Comandos do Git (Médio)
- `git add -A` Adiciona TODOS os arquivos que foram alterados ou criados para serem incluídos no próximo commit

## Comandos de Branch
- `git checkout -b <nome nova branch>` Cria uma nova branch local
- `git checkout <nome da branch>` Troca a branch ativa (somente uma branch pode estar ativa por vez!)
- `git push --set-upstream origin <nome branch>` Envia a nova branch para o github (ou gitlab, ou bitbucket, ... origin)

## Comandos de Merge
- `git merge <nome da branch a ser juntada>` Combina os commits da branch a ser junto na branch atual (normalmente, se junta na main)