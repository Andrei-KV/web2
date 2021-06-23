import re


def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/plain')])
    string = env['QUERY_STRING']
    result = [i + '\n' for i in result.split('&')]

    return result


