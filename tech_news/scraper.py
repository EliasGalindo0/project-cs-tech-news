import pip._vendor.requests
import time


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = pip._vendor.requests.get(
          url, timeout=3, headers={"user-agent": "Fake user-agent"})
        if response.status_code == 200:
            return response.text

    except pip._vendor.requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
