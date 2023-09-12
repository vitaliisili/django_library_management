class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        # Do something before the view or next middleware is calling
        if 'checked' not in request.session:
            self.stats(request.user_agent.os.family)
            request.session['checked'] = True

        response = self.get_response(request)

        # Do something after the view or next middleware is calling

        return response

    def stats(self, os_info):
        print(os_info)



