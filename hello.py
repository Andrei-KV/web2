
import re


def app(env, start_response):
    string = env['QUERY_STRING']
    result = [bytes(i + '\n', 'utf-8') for i in string.split('&')]
    start_response('200 OK', [('Content-Type','text/plain')])
  
    return result