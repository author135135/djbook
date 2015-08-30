def context_data(request):
    return {
        'counter': request.COOKIES['counter'] if 'counter' in request.COOKIES else 1
    }


class ContextData(object):
    def __new__(cls, request, *args, **kwargs):
            return {
                'counter': request.COOKIES['counter'] if 'counter' in request.COOKIES else 1
            }
