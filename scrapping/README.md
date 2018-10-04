# Scrapping

## get_feed_url.py - получение фидов (RSS, Atom) ссылки на которые есть на главной странице
## Html parser

# Получение фидов

Уточнения:

- пути к файлам, названия файлов, папок зашиты в параметры: 
    SOURCE_FILE_NAME = 'sourses.csv'
    FEED_FILE_NAME = 'feeds.csv'
    CONF_FOLDER = 'data\parser\conf'
- источник данных - файл sources.csv (data/parser/conf); столбцы: "Название ресурса", "URL" (главной страницы)
- тип фидов "зашит" внутри - параметр FEED_LINKS_ATTRIBUTES:
    'application/rss+xml'
    'application/atom+xml'
    'application/rss'
    'application/atom'
    'application/rdf+xml'
    'application/rdf'
    'text/rss+xml'
    'text/atom+xml'
    'text/rss'
    'text/atom'
    'text/rdf+xml'
    'text/rdf'
    'text/xml'
    'application/xml'
- полученные фиды сохраняются в файл feed.csv; столбцы "name", "URL", "feed_url"

## Запуск
скрипт надо запускать из корневой директории
```python
python get_feed_url.py
```
