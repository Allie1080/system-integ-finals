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

        <city>
            <id>0</id>
            <name>string</name>
            <routes>
                <route>
                    <id>0</id>
                    <name>string</name>
                    <city>redirect link to /api/cities/{city_name}</city>
                    <distance>0</distance>
                    <fare>
                        <fare>
                            <type>Full</type>
                            <amount>0.0</amount>
                        </fare>
                        <fare>
                            <type>Discounted</type>
                            <amount>0.0</amount>
                        </fare>
                    </fare>
                    <operating-hours>
                        <operating-hour>0</operating-hour>
                    </operating-hours>
                    <time>0</time>
                    <terminals>
                        <terminal>string</terminal>
                    </terminals>
                    <landmarks>
                        <landmark>string</landmark>
                    </landmarks>
                    <jeepneys>
                        <jeepney>redirect link to /api/jeepneys/{jeepney_id}</jeepney>
                    </jeepneys>
                    </route>
                </routes>
            </city>
        </cities>

## Responses:
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {   
                "status-code": 200,
                "details": "Successfully created"
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
                <details>Successfully created</details>
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

- ### *400 - BAD REQUEST*
    - *application/json* sample:

            {
                "status-code": 400,
                "details": "Formatting Error"
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
                <status-code>400</status-code>
                <details>Formatting Error</details>
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

- ### *404 - NOT FOUND*
    - *if CITY NOT FOUND*
        - *application/json* sample:

                {
                    "status-code": 404,
                    "details": "City Not Found"
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
                    <status-code>404</status-code>
                    <details>City Not Found</details>
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


> # POST - /api/cities/{city_name}/routes/{route_id}/jeepneys

## Request Body Schemas:
- *text/plain*:
        
        /api/jeepneys/{jeepney_id}

## Responses:
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully created"
                "content": "/api/jeepneys/1"
            }

    - *application/xml* sample:

            <response>
                <status-code>200</status-code>
                <details>Successfully created</details>
                <content>/api/jeepneys/1</content>
            </response>

- ### *400 - BAD REQUEST*
    - *application/json* sample:

            {
                "status-code": 400,
                "details": "Formatting Error"
                "content": "/api/jeepneys/1"
            }

    - *application/xml* sample:

            <response>
                <status-code>400</status-code>
                <details>Formatting Error</details>
                <content>/api/jeepneys/1</content>
            </response>


- ### *404 - NOT FOUND*
    - *if CITY NOT FOUND*
        - *application/json* sample:

                {
                    "status-code": 404,
                    "details": "City Not Found"
                    "content": "/api/jeepneys/1"
                }

        - *application/xml* sample:
                
                <response>
                    <status-code>404</status-code>
                    <details>City Not Found</details>
                    <content>/api/jeepneys/1</content>
                </response>

    - *if ROUTE NOT FOUND*
        - *application/json* sample:

                {
                    "status-code": 404,
                    "details": "Route Not Found"
                    "content": "/api/jeepneys/1"
                }
        - *application/xml* sample:
                
                <response>
                    <status-code>404</status-code>
                    <details>Route Not Found</details>
                    <content>/api/jeepneys/1</content>
                </response>

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

        <jeepney>
            <id>0</id>
            <driver>redirect link to api/users/drivers/{driver_id}</driver>
            <route>redirect link to /api/cities/{city_name}/routes/{route_id}</route>
            <plate-number>string</plate-number>
            <date-registered>string</date-registered>
            <type>string</type>
            <status>string</status>
            <reviews>
                <word-cloud>
                    <string>0</string>
                </word-cloud>
                <sentences>
                    users-passengers-comments-sentences-schema object
                </sentences>
            </reviews>
        </jeepney>



## Responses:
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully created"
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
                    <details>Successfully created</details>
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

- ### *400 - BAD REQUEST*
    - *application/json* sample:

            {
                "status-code": 400,
                "details": "Formatting Error"
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
                    <status-code>400</status-code>
                    <details>Formatting Error</details>
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

> # POST - /api/users/drivers

## Request Body Schemas:
- *application/json*:

        {
            "id": 0,
            "name": "string",
            "jeepney": "redirect link to /api/jeepneys/{jeepney_id}"
        }   

- *application/xml*:

        <driver>
            <id>0</id>
            <name>string</name>
            <jeepney>redirect link to /api/jeepneys/{jeepney_id}</jeepney>
        </driver>

## Responses:
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully created"
                "content": {
                    "id": 1,
                    "name": "Unique Salonga",
                    "jeepney": "/api/jeepney/1"
                }
            }

    - *application/xml* sample:
            
            <response>
                <status-code>200</status-code>
                <details>Successfully created</details>
                <content>
                    <driver>
                        <id>1</id>
                        <name>Unique Salonga</name>
                        <jeepney>/api/jeepney/1</jeepney>
                    </driver> 
                </content>
            </response>
          

- ### *400 - BAD REQUEST*
    - *application/json* sample:

            {
                "status-code": 400,
                "details": "Formatting Error"
                "content": {
                    "id": 1,
                    "name": "Unique Salonga",
                    "jeepney": "/api/jeepney/1"
                }
            }

    - *application/xml* sample:
            
            <response>
                <status-code>400</status-code>
                <details>Formatting Error</details>
                <content>
                    <driver>
                        <id>1</id>
                        <name>Unique Salonga</name>
                        <jeepney>/api/jeepney/1</jeepney>
                    </driver> 
                </content>
            </response>

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

        <passenger>
            <id>0</id>
            <name>string</name>
            <username>string</username>
            <comments>
                <comment>string</comment>
            </comments>
        </passenger>


## Responses:
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully created"
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
                <details>Successfully created</details>
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

- ### *400 - BAD REQUEST*
    - *application/json* sample:

            {
                "status-code": 400,
                "details": "Formatting Error"
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
                <status-code>400</status-code>
                <details>Formatting Error</details>
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








