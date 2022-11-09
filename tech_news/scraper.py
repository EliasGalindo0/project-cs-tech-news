import pip._vendor.requests
import time
import parsel


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
    selector = parsel.Selector(html_content)
    url = selector.css("h2.entry-title a::attr(href)").getall()

    return url


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    next_page_link = selector.css("a.next::attr(href)").get()

    if next_page_link:
        return next_page_link
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".entry-header-inner h1.entry-title::text").getall()
    title = "".join(title).strip()
    timestamp = selector.css("ul.post-meta li.meta-date::text").get()
    writer = selector.css(
      "ul.post-meta li.meta-author span.author a::text").get()
    comments_count = selector.css(
      "div.post-comments h5.title-block::text").re_first(r"\d")
    summary = selector.css(
      "div.entry-content > p:first-of-type *::text").getall()
    summary = "".join(summary).strip()
    tags = selector.css("section.post-tags li a[rel=tag]::text").getall()
    category = selector.css("div.meta-category a span.label::text").get()

    result = {
      "url": url,
      "title": title,
      "timestamp": timestamp,
      "writer": writer,
      "comments_count": comments_count or 0,
      "summary": summary,
      "tags": tags,
      "category": category
    }

    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
