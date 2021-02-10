from frame import render


def main_view(request):
    secret = request.get('secret_key', None)
    # используем шаблонизатор
    return '200 OK', render('index.html', secret=secret)


def about_view(request):
    secret = request.get('secret_key', None)
    # возвращаем шаблон about.html
    return '200 OK', render('about.html', secret=secret)
