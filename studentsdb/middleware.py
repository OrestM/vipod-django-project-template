from HTMLParser import HTMLParser
from datetime import datetime

from django.http import HttpResponse

class RequestTimeMiddleware(object):
	""" Display request time on a page """
	
	def process_request(self, request):
		request.start_time = datetime.now()
		return None
		
	def process_response(self, request, response):
		# if our process_request was canceled somewhere within
		# middleware stack, we can not calculate request time
		if not hasattr(request, 'start_time'):
			return response
		
		# calculate request execution time
		request.end_time = datetime.now()
		if 'text/html' in response.get('Content-Type', ''):
			response.write('<br />Request took: %s' % str(request.end_time - request.start_time))
		return response
		
	def process_view(self, request, view, args, kwargs):
		return None
		
	def process_template_response(self, request, response):
		return response
		
	def process_exception(self, request, exception):
		return HttpResponse('Exception found: %s' % exception)

"""
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    def handle_data(self, data):
        print "Encountered some data  :", data

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed()
"""