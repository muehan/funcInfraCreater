import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    location = req.params.get('location')

    return func.HttpResponse(
f'''{{
    "azurerm_resource_group": [
        {{
        "example": [
            {{
            "location": {location},
            "name": {name}
            }}
        ]
        }}
    ]
}}''',
mimetype="application/json"
            )

