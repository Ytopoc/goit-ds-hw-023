[English](README.md) | [**Українська**](README.uk.md)

# MongoDB CRUD + скрейпер цитат

Двочастинне домашнє завдання:

- **`first/`** - базовий CRUD над MongoDB Atlas-колекцією котів (`name`, `age`, `features`).
- **`second/`** - веб-скрейпер для [quotes.toscrape.com](https://quotes.toscrape.com), який обходить усі сторінки, скидає у файли `quotes.json` та `authors.json`, і завантажує їх до MongoDB.

## Стек

- Python 3.12
- `pymongo` для MongoDB
- `requests` + `beautifulsoup4` (з `lxml`) для скрейпінгу

## Конфігурація

Обидві частини читають connection-рядок MongoDB зі змінної середовища `MONGODB_URI`. Скопіюйте `.env.example` у `.env` і заповніть:

```bash
cp .env.example .env
# відредагуйте .env, встановіть MONGODB_URI=mongodb+srv://<user>:<pass>@<cluster>/<db>
```

## Запуск

```bash
# Частина 1 - CRUD CLI
cd first
pip install -r requirements.txt
python main.py

# Частина 2 - скрейп + наповнення БД
cd ../second
pip install -r requirements.txt
python parsing.py        # створює quotes.json + authors.json
python creation_db.py    # завантажує їх у MongoDB
```
