#!/usr/bin/env python3
from requests.exceptions import HTTPError
import requests
import json
import sys
import ast
from colorama import Fore
from colorama import init as colorama_init

colorama_init(autoreset=True)

def verify_error_connection(consulta):
    try:
        consulta.raise_for_status()

    except HTTPError:
        print('\nThere\'s a HTTP error\n')
        sys.exit(12)

    except Exception:
        print('\nOther error occurred\n')
        sys.exit(12)


def api(pergunta):
    UrlAPI = "https://api.openai.com/v1/completions"

    data_post = {'model': 'text-davinci-003', 'prompt': pergunta, 'temperature': 1, 'max_tokens': 2000}

    post_api = requests.post(UrlAPI, data=json.dumps(data_post), headers={'Content-Type':'application/json', 'Authorization': 'Bearer YOUR-TOKEN-HERE'})
    verify_error_connection(post_api)

    choices = ','.join(str(v) for v in post_api.json()['choices'])
    dici = ast.literal_eval(choices)
    print("Resposta:" + Fore.GREEN + dici['text'])

print("Don't type anything and press Enter to close the program!")
while True:
    pergunta = input("\n\n\nHuman question: ")

    if pergunta == '':
        break

    a = api(pergunta)
