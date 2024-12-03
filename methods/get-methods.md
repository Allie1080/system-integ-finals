> # GET - /api

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully found",
                "content": {
                    "cities": [
                        {
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
                        },
                        "MORE"
                    ],
                    "jeepneys": [
                        {
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
                        },
                        {
                            "id": 2,
                            "driver": "api/users/drivers/2",
                            "route": "/api/cities/1/routes/1",
                            "plate-number": "UWU-OWO",
                            "date-registered": "",
                            "type": "modern",
                            "status": "available",
                            "reviews": {
                                "word-cloud": {
                                    "too cold": 13,
                                    "spacious": 19,
                                    "scary fast": 5,
                                    "MORE": -1
                                },
                                "sentences": [
                                    {
                                        "user": "/api/user/passengers/1",
                                        "comment": "api/user/passengers/1/comments/2"
                                    },
                                    {
                                        "user": "/api/user/2",
                                        "comment": "api/user/passengers/2/comments/2"
                                    },
                                    "MORE"
                                ]
                            }
                        },
                        "MORE"
                    ],
                    "users": {
                        "drivers": [
                            {
                                "id": 1,
                                "name": "Unique Salonga",
                                "jeepney": "/api/jeepney/1"
                            },
                            {
                                "id": 2,
                                "name": "Badjao de Castro",
                                "jeepney": "/api/jeepney/2"
                            },
                            "MORE"
                        ],
                        "passengers": [
                            {
                                "id": 1,
                                "name": "Zildjian Benitez",
                                "username": "zildbenitez",
                                "comments": [
                                    "blah blah blah",
                                    "luh luh luh"
                                ]
                            },
                            {
                                "id": 2,
                                "name": "Blaster Silonga",
                                "username": "blastersilonga",
                                "comments": [
                                    "bleh bleh bleh",
                                    "duh duh duh"
                                ]
                            },
                            "MORE"
                        ]
                    }
                }
            }
    
    - *application/xml* sample:

            <response>
                <status-code>200</status-code>
                <details>Successfuly found</details>
                <content>
                    <cities>
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
                    </cities>
                    <jeepneys>
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
                        <jeepney>
                            <id>2</id>
                            <driver>api/users/drivers/2</driver>
                            <route>api/cities/1/routes/1</route>
                            <plate-number>UWU-OWO</plate-number>
                            <date-registered></date-registered>
                            <type>modern</type>
                            <status>available</status>
                            <reviews>
                                <word-cloud>
                                    <too-cold>13</too-cold>
                                    <spacious>19</spacious>
                                    <scary-fast>5</scary-fast>
                                    <more>-1</more>
                                </word-cloud>
                                <sentences>
                                    <sentence>
                                        <user>/api/user/passengers/1</user>
                                        <comment>api/user/passengers/1/comments/2</comment>
                                    </sentence>
                                    <sentence>
                                        <user>/api/user/2</user>
                                        <comment>api/user/passengers/2/comments/2</comment>
                                    </sentence>
                                    <more></more>
                                </sentences>
                            </reviews>
                        </jeepney>
                    </jeepneys>
                    <users>
                        <drivers>
                            <driver>
                                <id>1</id>
                                <name>Unique Salonga</name>
                                <jeepney>/api/jeepney/1</jeepney>
                            </driver>
                            <driver>
                                <id>2</id>
                                <name>Badjao de Castro</name>
                                <jeepney>/api/jeepney/2</jeepney>
                            </driver>
                            <more></more>
                        </drivers>
                        <passengers>
                            <passenger>
                                <id>1</id>
                                <name>Zildjian Benitez</name>
                                <username>zildbenitez</username>
                                <comments>
                                    <comment>blah blah blah</comment>
                                    <comment>luh luh luh</comment>
                                </comments>
                            </passenger>
                            <passenger>
                                <id>2</id>
                                <name>Blaster Silonga</name>
                                <username>blastersilonga</username>
                                <comments>
                                    <comment>bleh bleh bleh</comment>
                                    <comment>duh duh duh</comment>
                                </comments>
                            </passenger>
                            <more></more>
                        </passengers>
                    </users>
                </content>
            </response>

> # GET - /api/cities

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully found",
                "content": [
                    {
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
                    },
                    "MORE"
                ]
            }

    - *application/xml* sample:

            <response>
                <status-code>200</status-code>
                <details>Successfully found</details>
                <content>
                    <cities>
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
                    </cities>
                </content>
            </response>


> # GET - /api/cities/{city_name}

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully found",
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
                <details>Successfully found</details>
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

> # GET - /api/cities/{city_name}/routes

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully found",
                "content": [
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



    - *application/xml* sample:

            <response>
                <status-code>200</status-code>
                <details>Successfully found</details>
                <content>
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
                </content>
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

> # GET - /api/cities/{city_name}/routes/{route_id}

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully found",
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
                <details>Successfully found</details>
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



> # GET - /api/cities/{city_name}/routes/{route_id}/jeepneys

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully found",
                "content": [
                    "/api/jeepneys/1",
                    "/api/jeepneys/2",
                    "/api/jeepneys/3",
                    "/api/jeepneys/4",
                    "MORE"
                ]
            }



    - *application/xml* sample:

            <response>
                <status-code>200</status-code>
                <details>Successfully found</details>
                <content>
                    <jeepneys>
                        <jeepney>/api/jeepneys/1</jeepney>
                        <jeepney>/api/jeepneys/2</jeepney>
                        <jeepney>/api/jeepneys/3</jeepney>
                        <jeepney>/api/jeepneys/4</jeepney>
                        <more></more>
                    </jeepneys>
                </content>
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


> # GET - /api/cities/{city_name}/routes/{route_id}/jeepneys/{jeepney_index}

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully found",
                "content": "/api/jeepneys/1"
            }



    - *application/xml* sample:

            <response>
                <status-code>200</status-code>
                <details>Successfully found</details>
                <content>/api/jeepneys/1</content>
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
                    "details": "Jeepney Not Found",
                    "content": "None"
                }

        - *application/xml* sample:

                <response>
                    <status-code>404</status-code>
                    <details>Jeepney Not Found</details>
                    <content>None</content>
                </response>


> # GET - /api/users

> ## RESPONSES: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully created",
                "content": {
                    "drivers": [
                        {
                            "id": 1,
                            "name": "Unique Salonga",
                            "jeepney": "/api/jeepney/1"
                        },
                        {
                            "id": 2,
                            "name": "Badjao de Castro",
                            "jeepney": "/api/jeepney/2"
                        },
                        "MORE"
                    ],
                    "passengers": [
                        {
                            "id": 1,
                            "name": "Zildjian Benitez",
                            "username": "zildbenitez",
                            "comments": [
                                "blah blah blah",
                                "luh luh luh"
                            ]
                        },
                        {
                            "id": 2,
                            "name": "Blaster Silonga",
                            "username": "blastersilonga",
                            "comments": [
                                "bleh bleh bleh",
                                "duh duh duh"
                            ]
                        },
                        "MORE"
                    ]
                }
            }

    - *application/xml* sample:

            <response>
                <status-code>200</status-code>
                <details>Succesfully created</details>
                <content>
                    <users>
                        <drivers>
                            <driver>
                                <id>1</id>
                                <name>Unique Salonga</name>
                                <jeepney>/api/jeepney/1</jeepney>
                            </driver>
                            <driver>
                                <id>2</id>
                                <name>Badjao de Castro</name>
                                <jeepney>/api/jeepney/2</jeepney>
                            </driver>
                            <more></more>
                        </drivers>
                        <passengers>
                            <passenger>
                                <id>1</id>
                                <name>Zildjian Benitez</name>
                                <username>zildbenitez</username>
                                <comments>
                                    <comment>blah blah blah</comment>
                                    <comment>luh luh luh</comment>
                                </comments>
                            </passenger>
                            <passenger>
                                <id>2</id>
                                <name>Blaster Silonga</name>
                                <username>blastersilonga</username>
                                <comments>
                                    <comment>bleh bleh bleh</comment>
                                    <comment>duh duh duh</comment>
                                </comments>
                            </passenger>
                            <more></more>
                        </passengers>
                    </users>
                </content>
            </response>

> # GET - /api/users/drivers

> ## RESPONSES: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully created",
                "content": [
                        {
                            "id": 1,
                            "name": "Unique Salonga",
                            "jeepney": "/api/jeepney/1"
                        },
                        {
                            "id": 2,
                            "name": "Badjao de Castro",
                            "jeepney": "/api/jeepney/2"
                        },
                        "MORE"
                    ]
            }

    - *application/xml* sample:

            <response>
                <status-code>200</status-code>
                <details>Succesfully created</details>
                <content>
                    <drivers>
                        <driver>
                            <id>1</id>
                            <name>Unique Salonga</name>
                            <jeepney>/api/jeepney/1</jeepney>
                        </driver>
                        <driver>
                            <id>2</id>
                            <name>Badjao de Castro</name>
                            <jeepney>/api/jeepney/2</jeepney>
                        </driver>
                        <more></more>
                    </drivers>
                </content>
            </response>

> # GET - /api/users/drivers/{driver_id}

> ## RESPONSES: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully created",
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


> # GET - /api/users/passengers

> ## RESPONSES: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully created",
                "content": [
                    {
                        "id": 1,
                        "name": "Zildjian Benitez",
                        "username": "zildbenitez",
                        "comments": [
                            "blah blah blah",
                            "luh luh luh"
                        ]
                    },
                    {
                        "id": 2,
                        "name": "Blaster Silonga",
                        "username": "blastersilonga",
                        "comments": [
                            "bleh bleh bleh",
                            "duh duh duh"
                        ]
                    },
                    "MORE"
                ]
            }

    - *application/xml* sample:

            <response>
                <status-code>200</status-code>
                <details>Succesfully created</details>
                <content>
                    <passengers>
                        <passenger>
                            <id>1</id>
                            <name>Zildjian Benitez</name>
                            <username>zildbenitez</username>
                            <comments>
                                <comment>blah blah blah</comment>
                                <comment>luh luh luh</comment>
                            </comments>
                        </passenger>
                        <passenger>
                            <id>2</id>
                            <name>Blaster Silonga</name>
                            <username>blastersilonga</username>
                            <comments>
                                <comment>bleh bleh bleh</comment>
                                <comment>duh duh duh</comment>
                            </comments>
                        </passenger>
                        <more></more>
                    </passengers>
                </content>
            </response>

> # GET - /api/users/passengers/{pasenger_id}

> ## RESPONSES: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
                "status-code": 200,
                "details": "Successfully created",
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
                <details>Succesfully created</details>
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

