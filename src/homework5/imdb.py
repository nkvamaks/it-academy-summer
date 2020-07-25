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
    pattern = r'(\d\.\d)\s+(.+)\s+\((\d{4})'
    top250_count = 0
    names, ratings, years = [], {}, {}

    f_imdb = './data5/ratings.list'
    f_names = 'top250_movies.txt'
    f_ratings = 'ratings.txt'
    f_years = 'years.txt'

    # Open source file, find top250 movies and save their data in vars
    try:
        with open(f_imdb, encoding='cp1252') as fh:
            for line in fh:
                res = re.search(pattern, line)
                if res:
                    names.append(res.group(2))
                    ratings[res.group(1)] = ratings.get(res.group(1), 0) + 1
                    years[int(res.group(3))] = (
                          years.get(int(res.group(3)), 0) + 1)
                    top250_count += 1
                    if top250_count >= TOP250:
                        break
    except FileNotFoundError:
        print('File not found.')

    # Save data from vars into three different files
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
