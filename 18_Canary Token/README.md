# 18 — Canary Token

## Описание

Веб-сервис для обнаружения несанкционированного доступа (ловушка / canary token), фиксирующий IP-адрес, время и User-Agent при обращении.

## Концепции

* Flask, request.remote_addr, User-Agent
* Логирование инцидентов и обработка временных меток (`datetime`)
* Веб-ловушки (Canary Tokens / Honeypot)

## Как запустить

python Canary_token.py
