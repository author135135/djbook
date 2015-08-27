from django.http import HttpResponse


class LearnMiddleware(object):
    """
    Use this if middleware must be disabled
    def __init__(self):
        from django.core.exceptions import MiddlewareNotUsed

        raise MiddlewareNotUsed
    """

    def process_request(self, request):
        print request.COOKIES

        # return HttpResponse("Middleware `process_request` method replace page content!!!")
        return None

    def process_view(self, request, view_func, view_args, view_kwargs):
        print view_func.func_name
        print view_args
        print view_kwargs

        # return HttpResponse("Middleware `process_view` method replace page content!!!")
        return None

    def process_template_response(self, request, response):
        # Add variable to response context
        response.context_data['middleware_var'] = 'some value'

        return response

    def process_response(self, request, response):
        # Request / response counter
        response.set_cookie('counter', int(request.COOKIES.get('counter', 0)) + 1)

        return response

    def process_exception(self, request, exception):
        return HttpResponse(u"Exception: {0}".format(exception))
