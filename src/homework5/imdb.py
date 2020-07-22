"""IMDB TOP250."""


def imdb():
    """
    Обработка информации из файла с сайта IMDB.

    Скопированные данные с сайта IMDB хранятся в файле './data5/ratings.list'
    - Функция открывает и читает файл (если его нет, выводится ошибка).
    - Находит ТОП250 фильмов.
    - Создает 3 файла: top250_movies.txt – названия файлов,
                       ratings.txt – гистограмма рейтингов,
                       years.txt – гистограмма годов.
    """
    import re

    TOP250 = 250
    pattern = r'(\d\.\d)\s+(.+)\s+\((\d{4})'
    top250_count = 0
    names, ratings, years = [], {}, {}

    fimdb = './data5/ratings.list'
    fnames = 'top250_movies.txt'
    fratings = 'ratings.txt'
    fyears = 'years.txt'

    # Open source file, find top250 movies and save their data in vars
    try:
        with open(fimdb, encoding='cp1252') as fh:
            for line in fh:
                res = re.search(pattern, line)
                if res:
                    names.append(res.group(2))
                    ratings[res.group(1)] = ratings.get(res.group(1), 0) + 1
                    years[int(res.group(3))] = years.get(
                                                   int(res.group(3)), 0) + 1
                    top250_count += 1
                    if top250_count >= TOP250:
                        break
    except FileNotFoundError:
        print('File not found.')

    # Save data from vars into three different files
    with open(fnames, 'wt', encoding='cp1252') as fh:
        fh.write('\n'.join(names))

    with open(fratings, 'wt', encoding='cp1252') as fh:
        fh.write('\n'.join(
                 ['{} {}'.format(k, '*'*v) for k, v in ratings.items()]
                 ))

    with open(fyears, 'wt', encoding='cp1252') as fh:
        fh.write('\n'.join(
                 ['{} {}'.format(k, '*'*v) for k, v in sorted(years.items())]
                 ))


if __name__ == '__main__':
    imdb()
