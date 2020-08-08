"""IMDB TOP250.

В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле
./data5/ ratings.list.
    a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
    b. Найдите ТОП250 фильмов и извлеките заголовки.
    c. Программа создает 3 файла  top250_movies.txt – названия файлов,
    ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""


def imdb():
    """Return 3 files with names of movies, hystograms of years and ratings."""
    import re

    TOP250 = 250
    top250_count = 0

    pattern = r'(\d\.\d)\s+(.+)\s+\((\d{4})'
    RATING = 1
    TITLE = 2
    YEAR = 3

    names, ratings, years = [], {}, {}

    f_imdb = './data5/ratings.list'
    f_names = 'top250_movies.txt'
    f_ratings = 'ratings.txt'
    f_years = 'years.txt'

    try:
        with open(f_imdb, encoding='cp1252') as fh:
            for line in fh:
                res = re.search(pattern, line)
                if res:
                    names.append(res.group(TITLE))
                    ratings[res.group(RATING)] = ratings.get(res.group(RATING),
                                                             0) + 1
                    years[int(res.group(YEAR))] = years.get(int(res.group(YEAR)), 0) + 1
                    top250_count += 1
                    if top250_count >= TOP250:
                        break
    except FileNotFoundError:
        print('File not found.')

    with open(f_names, 'wt', encoding='cp1252') as fh:
        fh.write('\n'.join(names))

    with open(f_ratings, 'wt', encoding='cp1252') as fh:
        fh.write('\n'.join(
                 ['{} {}'.format(k, '*' * v) for k, v in ratings.items()]
                 ))

    with open(f_years, 'wt', encoding='cp1252') as fh:
        fh.write('\n'.join(
                 ['{} {}'.format(k, '*' * v) for k, v in sorted(years.items())]
                 ))


if __name__ == '__main__':
    imdb()
