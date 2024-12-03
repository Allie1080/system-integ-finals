> # POST - /api/cities

## Request Body Schemas:
- *application/json*:

        {
            "id": 0,
            "name": "string",
            "routes": [
                "cities-routes-schema object"
            ]
        }



- *application/xml*:



## Responses:
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "id": 1,
                "name": "Lucena",
                "routes": []
            }


    - *application/xml* sample:




- ### *400 - BAD REQUEST*
    - *application/json* sample



    - *application/xml* sample



> # POST - /api/cities/{city_name}/routes

## Request Body Schemas:
- *application/json*:



- *application/xml*:




## Responses:
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample


    - *application/xml* sample



- ### *400 - BAD REQUEST*
    - *application/json* sample


    - *application/xml* sample



- ### *404 - NOT FOUND*
    - *if CITY NOT FOUND*



> # POST - /api/cities/{city_name}/routes/{route_id}/jeepneys

## Request Body Schemas:
- *text/plain*:
        
        /api/jeepneys/{jeepney_id}



## Responses:
- ### *200 - SUCCESSFUL RESPONSE*
    - *text/plain* sample:



- ### *400 - BAD REQUEST*




- ### *404 - NOT FOUND*
    - *if CITY NOT FOUND*




    - *if ROUTE NOT FOUND*




> # POST - /api/jeepneys

## Request Body Schemas:
- *application/json*:

        {
            "id": 0,
            "driver": "redirect link to api/users/drivers/{driver_id}",
            "route": "redirect link to /api/cities/{city_name}/routes/{route_id}",
            "plate-number": "string",
            "date-registered": "string",
            "type": "string",
            "status": "string",
            "reviews": {
                "word-cloud": {
                    "string": 0
                },
                "sentences": [
                    "users-passengers-comments-sentences-schema object"
                ]
            }
        }

- *application/xml*:




## Responses:
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample




    - *application/xml* sample



- ### *400 - BAD REQUEST*
    



> # POST - /api/users/drivers

## Request Body Schemas:
- *application/json*:

        {
            "id": 0,
            "name": "string",
            "jeepney": "redirect link to /api/jeepneys/{jeepney_id}"
        }   

- *application/xml*:




## Responses:
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample




    - *application/xml* sample



- ### *400 - BAD REQUEST*



> # POST - /api/users/passengers

## Request Body Schemas:
- *application/json*:

        {
            "id": 0,
            "name": "string",
            "username": "string",
            "comments": [
                "string"
            ]
        }

- *application/xml*:



## Responses:
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample




    - *application/xml* sample



- ### *400 - BAD REQUEST*









