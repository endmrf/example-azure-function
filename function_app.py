import azure.functions as func
import logging
from json import dumps
import uuid

app = func.FunctionApp()

@app.function_name(name="CreateMovie")
@app.route(route="movies", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_output(arg_name="outputDocument", database_name="my-database", container_name="my-container", connection="CosmosDbConnectionSetting")
def create_movie(req: func.HttpRequest, outputDocument: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP function processed a request.')
    logging.info('Python Cosmos DB function processed a request.')
     
    req_body = req.get_json()

    title = req_body.get('title')
    gender = req_body.get('gender')
    year = req_body.get('year')

    if title and gender and year:
        outputDocument.set(
            func.Document.from_dict(
                {
                    "id": str(uuid.uuid4()), 
                    "title": title,
                    "gender": gender,
                    "year": year
                }
            )
        )
        
        return func.HttpResponse(f"Movie {title} created successfully", status_code=201)
    else:
        return func.HttpResponse(
            "Please pass a valid request body",
            status_code=400
        )
    
@app.function_name(name="ListMovies")
@app.route(route="movies", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_input(arg_name="documents", database_name="my-database", container_name="my-container", connection="CosmosDbConnectionSetting")
def list_movies(req: func.HttpRequest, documents: func.DocumentList) -> func.HttpResponse:
    logging.info("Listing all documents from Cosmos DB")

    results = [doc.to_dict() for doc in documents]

    return func.HttpResponse(
        body=dumps(results),
        mimetype="application/json"
    )