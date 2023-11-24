import json
import sys
from json import JSONDecodeError
from time import sleep

import openai

from common.env_vars import OPENAI_KEY

openai.api_key = OPENAI_KEY


def call_openai(messages: list, function_call: dict, temperature=0.8, model='gpt-3.5-turbo', timeout=60) -> dict:

    max_retries = 3
    errors = []
    for retry in range(max_retries):
        try:
            response = openai.chat.completions.create(
                model=model,
                messages=messages,
                tools=[function_call],
                tool_choice={'type': 'function', 'function': {'name': function_call['function']['name']}},
                temperature=temperature,
                timeout=timeout
            )
        except (openai.APIError,
                openai.APITimeoutError,
                openai.APIConnectionError,
                openai.InternalServerError) as openai_error:
            errors.append(openai_error)
            print(f"Falha ao obter resposta da OpenAI, tentando novamente... ({retry+1}/{max_retries}): {openai_error}")
            sleep(5)
            continue

        try:
            args = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
        except JSONDecodeError as json_error:
            print(f"Falha ao obter resposta da OpenAI, tentando novamente... ({retry + 1}/{max_retries}): {json_error}")
            sleep(5)
            continue

        missing_key = False
        missing_val = False
        for key in function_call['function']['parameters']['properties']:
            if key not in args.keys():
                print(f"Resposta incompleta da OpenAI, tentando novamente... ({retry + 1}/{max_retries}): KeyError \"{key}\"")
                sleep(5)
                missing_key = True
                break
            if not args.get(key):
                print(f"Resposta vazia da OpenAI, tentando novamente... ({retry + 1}/{max_retries}): EmptyVal \"{key}\"")
                sleep(5)
                missing_val = True
        if missing_key or missing_val:
            continue

        return args

    print(f"Falha ao obter resposta da OpenAI: {errors}")
    raise Exception(f"{errors}")
