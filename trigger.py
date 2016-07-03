#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
from pprint import PrettyPrinter

secret_token = "" # Fill in the secret token

def trigger(request):
    os.system('git pull')
    os.system('./manage.py collectstatic --noinput')
    os.system('skill -HUP gunicorn')

def application(environ, start_response):
    ok_status = '200 OK'
    unauth_status = "401 Unauthorized"


    def reply(status, msg):
        headers = [('Content-type', 'text/plain; charset=utf-8')]
        start_response(status, headers)

        return [bytes(msg, "UTF-8")]

    if secret_token and secret_token != environ.get('HTTP_X_GITLAB_TOKEN'):
        return reply(unauth_status, "Wrong secret token!")

    request_body = None
    response_body = "OK"
    if environ.get('CONTENT_LENGTH'):
        try:
            request_body_size = int(environ['CONTENT_LENGTH'])
            print(request_body_size)
            request_body = environ['wsgi.input'].read(request_body_size)
        except (TypeError, ValueError):
            request_body = ""
        if request_body:
            try:
                trigger(str(request_body))
                return reply(ok_status, "OK")
            except:
                response_body = "error"

    return reply(ok_status, response_body)
