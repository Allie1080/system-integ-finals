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

    <city>
        <id>0</id>
        <name>string</name>
        <routes>
            <route>
                cities-routes-schema object
        </routes>
    </city>


## Responses:
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully created"
                "content": {
                    "id": 1,
                    "name": "Lucena",
                    "routes": []
                }
            }

    - *application/xml* sample:

            <response>
                <status-code>200</status-code>
                <details>Successfully created</details>
                <content> 
                    <city>
                        <id>1</id>
                        <name>Lucena</name>
                        <routes></routes>
                    </city>
                </content>
            </response>

- ### *400 - BAD REQUEST*
    - *application/json* sample:

            {
                "status-code": 400,
                "details": "Formatting Error"
                "content": {
                    "id": 1,
                    "name": "Lucena",
                    "routes": []
                }
            }

    - *application/xml* sample:

            <response>
                <status-code>400</status-code>
                <details>Formatting Error</details>
                <content> 
                    <city>
                        <id>1</id>
                        <name>Lucena</name>
                        <routes></routes>
                    </city>
                </content>
            </response>



> # POST - /api/cities/{city_name}/routes

## Request Body Schemas:
- *application/json*:

        {
            "id": 0,
            "name": "string",
            "city": "redirect link to /api/cities/{city_name}",
            "distance": 0,
            "fare": [
                {
                    "type": "Full",
                    "amount": 0.0
                },
                {
                    "type": "Discounted",
                    "amount": 0.0
                }
            ],
            "operating-hours": [
                0
            ],
            "time": 0,
            "terminals": [
                "string"
            ],
            "landmarks": [
                "string"
            ],
            "jeepneys": [
                "redirect link to /api/jeepneys/{jeepney_id}"
            ]
        }

- *application/xml*:



## Responses:
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample

            {   
                "status-code": 200,
                "details": "Successfully created"
                "content": {

                }
            }


    - *application/xml* sample



- ### *400 - BAD REQUEST*
    - *application/json* sample:

            {
                "status-code": 400,
                "details": "Formatting Error"
                "content": {

                }
            }

    - *application/xml* sample:



- ### *404 - NOT FOUND*
    - *if CITY NOT FOUND*
        - *application/json* sample:

                {
                    "status-code": 404,
                    "details": "City Not Found"
                    "content": {

                    }
                }

        - *application/xml* sample:


> # POST - /api/cities/{city_name}/routes/{route_id}/jeepneys

## Request Body Schemas:
- *text/plain*:
        
        /api/jeepneys/{jeepney_id}



## Responses:
- ### *200 - SUCCESSFUL RESPONSE*
    - *text/plain* sample:

            {
                "status-code": 200,
                "details": "Successfully created"
                "content": "/api/jeepneys/1"
            }



- ### *400 - BAD REQUEST*
    - *text/plain* sample:

            {
                "status-code": 200,
                "details": "Successfully created"
                "content": "/api/jeepneys/1"
            }

- ### *404 - NOT FOUND*
    - *if CITY NOT FOUND*
        - *text/plain* sample:

                {
                    "status-code": 404,
                    "details": "City Not Found"
                    "content": "/api/jeepneys/1"
                }


    - *if ROUTE NOT FOUND*
        - *text/plain* sample:

                {
                    "status-code": 404,
                    "details": "Route Not Found"
                    "content": "/api/jeepneys/1"
                }


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

            {
                "status-code": 200,
                "details": "Successfully created"
                "content": {

                }
            }

    - *application/xml* sample



- ### *400 - BAD REQUEST*
    - *application/json* sample:

            {
                "status-code": 400,
                "details": "Formatting Error"
                "content": {

                }
            }
    
    - *application/xml* sample:



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

        {
            "status-code": 200,
            "details": "Successfully created"
            "content": {

            }
        }

    - *application/xml* sample
            
          

- ### *400 - BAD REQUEST*

        {
            "status-code": 400,
            "details": "Formatting Error"
            "content": {

            }
        }



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
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully created"
                "content": {
                    
                }
            }

    - *application/xml* sample:



- ### *400 - BAD REQUEST*
    - *application/json* sample:

            {
                "status-code": 400,
                "details": "Formatting Error"
                "content": {

                }
            }

    - *application/xml* sample:








