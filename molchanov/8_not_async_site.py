import requests
from time import time


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    t0 = time()
    url = 'https://loremflickr.com/320/240'

    for _ in range(20):
        write_file(get_file(url))

    print(f'Времени прошло {time() - t0}')


if __name__ == '__main__':
    main()
