[**English**](README.md) | [Українська](README.uk.md)

# MongoDB CRUD + Quotes Scraper

Two-part homework:

- **`first/`** - basic CRUD over a MongoDB Atlas collection of cats (`name`, `age`, `features`).
- **`second/`** - a web scraper for [quotes.toscrape.com](https://quotes.toscrape.com) that walks every page, dumps `quotes.json` and `authors.json`, and seeds them into MongoDB.

## Stack

- Python 3.12
- `pymongo` for MongoDB
- `requests` + `beautifulsoup4` (with `lxml`) for scraping

## Configuration

Both parts read the MongoDB connection string from the `MONGODB_URI` environment variable. Copy `.env.example` to `.env` and fill it in:

```bash
cp .env.example .env
# edit .env, set MONGODB_URI=mongodb+srv://<user>:<pass>@<cluster>/<db>
```

## Run

```bash
# Part 1 - CRUD CLI
cd first
pip install -r requirements.txt
python main.py

# Part 2 - scrape + seed
cd ../second
pip install -r requirements.txt
python parsing.py        # writes quotes.json + authors.json
python creation_db.py    # loads them into MongoDB
```
