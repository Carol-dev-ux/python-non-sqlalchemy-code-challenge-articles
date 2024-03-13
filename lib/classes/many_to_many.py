class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        assert isinstance(title, str) and 5 <= len(title) <= 50
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all_articles.append(self)
        author.articles_written.append(self)
        magazine.articles_published.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title is immutable")


class Author:
    def __init__(self, name):
        assert isinstance(name, str) and len(name) > 0
        self.name = name
        self.articles_written = []

    def articles(self):
        return self.articles_written

    def magazines(self):
        return list(set(article.magazine for article in self.articles_written))

    def add_article(self, magazine, title):
        assert isinstance(magazine, Magazine)
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        if not self.articles_written:
            return None
        return list(set(article.magazine.category for article in self.articles_written))


class Magazine:
    def __init__(self, name, category):
        assert isinstance(name, str) and 2 <= len(name) <= 16
        assert isinstance(category, str) and len(category) > 0
        self.name = name
        self.category = category
        self.articles_published = []

    def articles(self):
        return self.articles_published

    def contributors(self):
        authors = [article.author for article in self.articles_published]
        return list(set(authors))

    def article_titles(self):
        return [article.title for article in self.articles_published]

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles_published:
            author_name = article.author.name
            author_counts[author_name] = author_counts.get(author_name, 0) + 1
        return [author for author, count in author_counts.items() if count > 2]

