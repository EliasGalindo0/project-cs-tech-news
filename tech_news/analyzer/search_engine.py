from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    titles = search_news({"title": {"$regex": title, "$options": "i"}})

    result = [(news["title"], news["url"]) for news in titles]

    return result


# Requisito 7
def search_by_date(date):
    try:
        iso = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        dates = search_news({"timestamp": iso})
        result = [(news["title"], news["url"]) for news in dates]

        return result

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    tags = search_news({"tags": {"$regex": tag, "$options": "i"}})

    return [(news["title"], news["url"]) for news in tags]


# Requisito 9
def search_by_category(category):
    category = search_news({"category": {"$regex": category, "$options": "i"}})

    return [(news["title"], news["url"]) for news in category]
