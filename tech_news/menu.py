import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
from tech_news.analyzer.ratings import (
    top_5_news,
    top_5_categories
)


def option_0():
    news = input("Quantas notícias serão buscadas?")
    return get_tech_news(news)


def option_1():
    title = input("Digite um título:")
    return search_by_title(title)


def option_2():
    date = input("Digite uma data no formato aaaa-mm-dd:")
    return search_by_date(date)


def option_3():
    tag = input("Digite uma tag:")
    return search_by_tag(tag)


def option_4():
    category = input("Digite uma categoria:")
    return search_by_category(category)


# Requisito 12
def analyzer_menu():
    menu_op = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
 """
    )

    if menu_op in ["0", "1", "2", "3", "4"]:
        eval(f"option_{menu_op}")()
    elif menu_op == "5":
        return top_5_news()
    elif menu_op == "6":
        return top_5_categories()
    elif menu_op == "7":
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)
