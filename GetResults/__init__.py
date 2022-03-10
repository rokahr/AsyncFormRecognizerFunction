import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
             "Could not read body",
             status_code=500
        )

    lookUpUrl = req_body.get('lookupurl')

    url = lookUpUrl

    payload={}
    headers = {
    'Ocp-Apim-Subscription-Key': 'your_key'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text
