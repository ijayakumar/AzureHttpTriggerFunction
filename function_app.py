import azure.functions as func
import logging
import requests
import os

app = func.FunctionApp()

@app.function_name(name="AscendHttpTrigger")
@app.route(route="title", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    API_URL = os.environ['API_URL']
    API_Attribute = os.environ['API_Attribute']
    try:
        refCounter = req.params.get('refCounter')
        response = requests.get(API_URL + refCounter)

        title = response.json().get(API_Attribute)

        if response.status_code == 200:
            return func.HttpResponse(title)
        else:
            return func.HttpResponse("Title not found",status_code=404)
    except:
        return func.HttpResponse("Error in fetching title", status_code=400)