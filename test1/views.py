import time

from django.views import View
from django.http import StreamingHttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

class IndexView(View):
    initial = {}
    template_name = 'test1.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'data':  "abc"})


def event_stream():
    i = 1
    while i <= 3:
        yield "\ndata: {} {}\n\n".format(i, "data")
        i += 1
        time.sleep(1)

class PostStreamView(View):

    def get(self, request):
        response = StreamingHttpResponse(event_stream())
        response['Content-Type'] = 'text/event-stream'
        return response