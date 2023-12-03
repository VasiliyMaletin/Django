from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def log(view_func):
    def wrapper(request):
        logger.info(f'The view function was called {view_func.__name__}')
        return view_func(request)
    return wrapper


@log
def index(request):
    return HttpResponse("Hello, world!")


@log
def main(request):
    html = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' \
           'Mauris ultricies scelerisque ipsum nec aliquam. Lorem ipsum dolor sit amet,' \
           'consectetur adipiscing elit. Cras blandit non lacus eu faucibus. In velit magna,' \
           'ultricies a lorem non, laoreet auctor risus. Nullam consectetur turpis quis iaculis aliquam.' \
           'Vestibulum gravida aliquet ex, sed varius.'
    return HttpResponse(html)


@log
def about(request):
    html = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' \
           'Fusce eu dignissim mauris, fermentum pharetra urna.'
    return HttpResponse(html)
