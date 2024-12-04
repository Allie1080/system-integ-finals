> # DELETE - /api/cities/{city_name}

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully deleted",
                "content": {
                    "id": 1,
                    "name": "Lucena",
                    "routes": [
                        {
                            "id": 1,
                            "name": "Lucena City Proper - Site",
                            "city": "/api/cities/1",
                            "distance": 4,
                            "fare": [
                                {
                                    "type": "Full",
                                    "amount": 13
                                },
                                {
                                    "type": "Discounted",
                                    "amount": 11
                                }
                            ],
                            "operating-hours": [
                                530,
                                2100
                            ],
                            "time": 30,
                            "terminals": [
                                "Enverga University, Gate 3",
                                "C.M Recto St."
                            ],
                            "landmarks": [
                                "Moscow St",
                                "Enverga University",
                                "Enverga Gymnasium",
                                "Alfamart Ibabang Dupay",
                                "SM City Lucena",
                                "Saint Anne General Hospital",
                                "STI College",
                                "New Lucena City Public Market"
                            ],
                            "jeepneys": [
                                "/api/jeepneys/1",
                                "/api/jeepneys/2",
                                "/api/jeepneys/3",
                                "/api/jeepneys/4",
                                "MORE"
                            ]
                        },
                        "MORE"
                    ]
                }
            }



    - *application/xml* sample:

            <response>
                <status-code>200</status-code>
                <details>Successfully deleted</details>
                <content>
                    <city>
                        <id>1</id>
                        <name>Lucena</name>
                        <routes>
                            <route>
                                <id>1</id>
                                <name>Lucena City Proper - Site</name>
                                <city>/api/cities/1</city>
                                <fare>
                                    <fare>
                                        <type>Full</type>
                                        <amount>13</amount>
                                    </fare>
                                    <fare>
                                        <type>Discounted</type>
                                        <amount>11</amount>
                                    </fare>
                                </fare>
                    
                                <operating-hours>
                                    <operating-hour>530</operating-hour>
                                    </operating-hours>2100</operating-hour>
                                </operating-hours>
                                <landmarks>
                                    <landmark>Moscow St</landmark>
                                    <landmark>Enverga University</landmark>
                                    <landmark>Enverga Gymnasium</landmark>
                                    <landmark>Alfamart Ibabang Dupay</landmark>
                                    <landmark>SM City Lucena</landmark>
                                    <landmark>Saint Anne General Hospital</landmark>
                                    <landmark>"STI College</landmark>
                                    <landmark>New Lucena City Public Market</landmark>
                                </landmarks>
                                <jeepneys>
                                    <jeepney>/api/jeepneys/1</jeepney>
                                    <jeepney>/api/jeepneys/2</jeepney>
                                    <jeepney>/api/jeepneys/3</jeepney>
                                    <jeepney>/api/jeepneys/4</jeepney>
                                    <more></more>
                                </jeepneys>
                            </route>
                            <more></more>
                        </routes>
                        <more></more>
                    </city>
                </content>
            </response>

- ### *403 - FORBIDDEN*
    - *application/json* sample:

            {
                "status-code": 403,
                "details": "Deletion Forbidden",
                "content": "None"
            }

    - *application/xml* sample:

            <response>
                <status-code>403</status-code>
                <details>Deletion Forbidden</details>
                <content>None</content>
            </response>

- ### *404 - NOT FOUND ERROR*
    - *if CITY NOT FOUND*
        - *application/json* sample:

                {
                    "status-code": 404,
                    "details": "City Not Found",
                    "content": "None"
                }

        - *application/xml* sample:

                <response>
                    <status-code>404</status-code>
                    <details>City Not Found</details>
                    <content>None</content>
                </response>

> # DELETE - /api/cities/{city_name}/routes/{route_id}

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully deleted",
                "content": {
                    "id": 1,
                    "name": "Lucena City Proper - Site",
                    "city": "/api/cities/1",
                    "distance": 4,
                    "fare": [
                        {
                            "type": "Full",
                            "amount": 13
                        },
                        {
                            "type": "Discounted",
                            "amount": 11
                        }
                    ],
                    "operating-hours": [
                        530,
                        2100
                    ],
                    "time": 30,
                    "terminals": [
                        "Enverga University, Gate 3",
                        "C.M Recto St."
                    ],
                    "landmarks": [
                        "Moscow St",
                        "Enverga University",
                        "Enverga Gymnasium",
                        "Alfamart Ibabang Dupay",
                        "SM City Lucena",
                        "Saint Anne General Hospital",
                        "STI College",
                        "New Lucena City Public Market"
                    ],
                    "jeepneys": [
                        "/api/jeepneys/1",
                        "/api/jeepneys/2",
                        "/api/jeepneys/3",
                        "/api/jeepneys/4",
                        "MORE"
                    ]
                }                
            }

    - *application/xml* sample:
  
            <response>
                <status-code>200</status-code>
                <details>Successfully deleted</details>
                <content>
                    <route>
                        <id>1</id>
                        <name>Lucena City Proper - Site</name>
                        <city>/api/cities/1</city>
                        <fare>
                            <fare>
                                <type>Full</type>
                                <amount>13</amount>
                            </fare>
                            <fare>
                                <type>Discounted</type>
                                <amount>11</amount>
                            </fare>
                        </fare>
            
                        <operating-hours>
                            <operating-hour>530</operating-hour>
                            </operating-hours>2100</operating-hour>
                        </operating-hours>
                        <landmarks>
                            <landmark>Moscow St</landmark>
                            <landmark>Enverga University</landmark>
                            <landmark>Enverga Gymnasium</landmark>
                            <landmark>Alfamart Ibabang Dupay</landmark>
                            <landmark>SM City Lucena</landmark>
                            <landmark>Saint Anne General Hospital</landmark>
                            <landmark>"STI College</landmark>
                            <landmark>New Lucena City Public Market</landmark>
                        </landmarks>
                        <jeepneys>
                            <jeepney>/api/jeepneys/1</jeepney>
                            <jeepney>/api/jeepneys/2</jeepney>
                            <jeepney>/api/jeepneys/3</jeepney>
                            <jeepney>/api/jeepneys/4</jeepney>
                            <more></more>
                        </jeepneys>
                    </route>
                </content>
            </response>

- ### *403 - FORBIDDEN*
    - *application/json* sample:

            {
                "status-code": 403,
                "details": "Deletion Forbidden",
                "content": "None"
            }

    - *application/xml* sample:

            <response>
                <status-code>403</status-code>
                <details>Deletion Forbidden</details>
                <content>None</content>
            </response>

- ### *404 - NOT FOUND*
    - *if CITY NOT FOUND*
        - *application/json* sample:

                {
                    "status-code": 404,
                    "details": "City Not Found",
                    "content": "None"
                }

        - *application/xml* sample:

                <response>
                    <status-code>404</status-code>
                    <details>City Not Found</details>
                    <content>None</content>
                </response>

    - *if ROUTE NOT FOUND*
        - *application/json* sample:

                {
                    "status-code": 404,
                    "details": "Route Not Found",
                    "content": "None"
                }

        - *application/xml* sample:

                <response>
                    <status-code>404</status-code>
                    <details>Route Not Found</details>
                    <content>None</content>
                </response>

> # DELETE - /api/cities/{city_name}/routes/{route_id}/jeepneys/{jeepney_index}

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully deleted",
                "content": "/api/jeepneys/1"
            }

    - *application/xml* sample:

            <response>
                <status-code>200</status-code>
                <details>Successfully deleted</details>
                <content>/api/jeepneys/1</content>
            </response>

- ### *403 - FORBIDDEN*
    - *application/json* sample:

            {
                "status-code": 403,
                "details": "Deletion Forbidden",
                "content": "None"
            }

    - *application/xml* sample:

            <response>
                <status-code>403</status-code>
                <details>Deletion Forbidden</details>
                <content>None</content>
            </response>

- ### *404 - NOT FOUND*
    - *if CITY NOT FOUND*
        - *application/json* sample:

                {
                    "status-code": 404,
                    "details": "City Not Found",
                    "content": "None"
                }

        - *application/xml* sample:

                <response>
                    <status-code>404</status-code>
                    <details>City Not Found</details>
                    <content>None</content>
                </response>

    - *if ROUTE NOT FOUND*
        - *application/json* sample:

                {
                    "status-code": 404,
                    "details": "Route Not Found",
                    "content": "None"
                }

        - *application/xml* sample:

                <response>
                    <status-code>404</status-code>
                    <details>Route Not Found</details>
                    <content>None</content>
                </response>

    - *if JEEPNEY NOT FOUND*
        - *application/json* sample:

                {
                    "status-code": 404,
                    "details": "Jeepney Out of Index",
                    "content": "None"
                }

        - *application/xml* sample:

                <response>
                    <status-code>404</status-code>
                    <details>Jeepney Out of Index</details>
                    <content>None</content>
                </response>

> # DELETE - /api/jeepneys/{jeepney_id}

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully deleted",
                "content": {
                    "id": 1,
                    "driver": "api/users/drivers/1",
                    "route": "/api/cities/1/routes/1",
                    "plate-number": "OWO-UWU",
                    "date-registered": "",
                    "type": "traditional",
                    "status": "unavailable",
                    "reviews": {
                        "word-cloud": {
                            "not good": 34,
                            "very cramped": 12,
                            "MORE": -1
                        },
                        "sentences": [
                            {
                                "user": "/api/user/passengers/1",
                                "comment": "api/user/passengers/1/comments/1"
                            },
                            {
                                "user": "/api/user/2",
                                "comment": "api/user/passengers/2/comments/1"
                            },
                            "MORE"
                        ]
                    }
                }
            }

    - *application/xml* sample:

            <response>
                <status-code>200</status-code>
                <details>Successfully deleted</details>
                <content>
                    <jeepney>
                        <id>1</id>
                        <driver>api/users/drivers/1</driver>
                        <route>/api/cities/1/routes/1</route>
                        <plate-number>OWO-UWU</plate-number>
                        <date-registered></date-registered>
                        <type>traditional</type>
                        <status>unavailable</status>
                        <reviews>
                            <word-cloud>
                                <not-good>34</not-good>
                                <very-cramped>12</very-cramped>
                                <more>-1</more>
                            </word-cloud>
                            <sentences>
                                <sentence>
                                    <user>/api/user/passengers/1</user>
                                    <comment>api/user/passengers/1/comments/1</comment>
                                </sentence>
                                <sentence>
                                    <user>/api/user/2</user>
                                    <comment>api/user/passengers/2/comments/1</comment>
                                </sentence>
                                <more></more>
                            </sentences>
                        </reviews>
                    </jeepney>
                </content>
            </response>

- ### *403 - FORBIDDEN*
    - *application/json* sample:

            {
                "status-code": 403,
                "details": "Deletion Forbidden",
                "content": "None"
            }

    - *application/xml* sample:

            <response>
                <status-code>403</status-code>
                <details>Deletion Forbidden</details>
                <content>None</content>
            </response>

- ### *404 - NOT FOUND*
    - *if JEEPNEY NOT FOUND*
        - *application/json* sample:

                {
                    "status-code": 404,
                    "details": "Jeepney Not Found",
                    "content": "None"
                }

        - *application/xml* sample:

                <response>
                    <status-code>404</status-code>
                    <details>Jeepney Not Found</details>
                    <content>None</content>
                </response>



> # DELETE - /api/users/drivers/{driver_id}

> ## RESPONSES: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully deleted",
                "content": {
                        "id": 1,
                        "name": "Unique Salonga",
                        "jeepney": "/api/jeepney/1"
                    }
            }

    - *application/xml* sample:

            <response>
                <status-code>200</status-code>
                <details>Succesfully created</details>
                <content>
                    <driver>
                        <id>1</id>
                        <name>Unique Salonga</name>
                        <jeepney>/api/jeepney/1</jeepney>
                    </driver>
                </content>
            </response>

- ### *403 - FORBIDDEN*
    - *application/json* sample:

            {
                "status-code": 403,
                "details": "Deletion Forbidden",
                "content": "None"
            }

    - *application/xml* sample:

            <response>
                <status-code>403</status-code>
                <details>Deletion Forbidden</details>
                <content>None</content>
            </response>

- ### *404 - NOT FOUND*
    - *if DRIVER NOT FOUND*
        - *application/json* sample:

                {
                    "status-code": 404,
                    "details": "Driver Not Found",
                    "content": "None"
                }

        - *application/xml* sample:

                <response>
                    <status-code>404</status-code>
                    <details>Driver Not Found</details>
                    <content>None</content>
                </response>

> # DELETE - /api/users/passengers/{passenger_id}

> ## RESPONSES: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully deleted",
                "content": {
                    "id": 1,
                    "name": "Zildjian Benitez",
                    "username": "zildbenitez",
                    "comments": [
                        "blah blah blah",
                        "luh luh luh"
                    ]
                }
            }

    - *application/xml* sample:

            <response>
                <status-code>200</status-code>
                <details>Succesfully deleted</details>
                <content>
                    <passenger>
                        <id>1</id>
                        <name>Zildjian Benitez</name>
                        <username>zildbenitez</username>
                        <comments>
                            <comment>blah blah blah</comment>
                            <comment>luh luh luh</comment>
                        </comments>
                    </passenger>
                </content>
            </response>

- ### *403 - FORBIDDEN*
    - *application/json* sample:

            {
                "status-code": 403,
                "details": "Deletion Forbidden",
                "content": "None"
            }

    - *application/xml* sample:

            <response>
                <status-code>403</status-code>
                <details>Deletion Forbidden</details>
                <content>None</content>
            </response>

- ### *404 - NOT FOUND*
    - *if PASSENGER NOT FOUND*
        - *application/json* sample:

                {
                    "status-code": 404,
                    "details": "Passenger Not Found",
                    "content": "None"
                }

        - *application/xml* sample:

                <response>
                    <status-code>404</status-code>
                    <details>Passenger Not Found</details>
                    <content>None</content>
                </response>

