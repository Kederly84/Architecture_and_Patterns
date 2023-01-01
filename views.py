from framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html')


class Page:
    def __call__(self, request):
        return '200 OK', render('page.html')
