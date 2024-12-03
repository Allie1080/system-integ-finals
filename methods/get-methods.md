># GET - /api

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample:

            {
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
                            "name": "",
                            "jeepney": "/api/jeepney/1"
                        },
                        {
                            "id": 2,
                            "name": "",
                            "jeepney": "/api/jeepney/2"
                        },
                        "MORE"
                    ],
                    "passengers": [
                        {
                            "id": 1,
                            "name": "Zildjian Benitez",
                            "username": "",
                            "comments": [
                                "blah blah blah",
                                "luh luh luh"
                            ]
                        },
                        {
                            "id": 2,
                            "name": "Blaster Silonga",
                            "username": "",
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

       screenshot fujnnjf


> # GET - /api/cities

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample



    - *application/xml* sample
    

> # GET - /api/cities/1

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample



    - *application/xml* sample



- ### *404 - NOT FOUND ERROR*



> # GET - api/cities/{city}/routes

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample



    - *application/xml* sample



- ### *404 - NOT FOUND*
    - *if CITY NOT FOUND*



> # GET - api/cities/1/routes/1

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample



    - *application/xml* sample



- ### *404 - NOT FOUND*
    - *if CITY NOT FOUND*



    - *if ROUTE NOT FOUND*



> # GET - api/cities/1/routes/1/jeepneys

## Responses: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *application/json* sample



    - *application/xml* sample



- ### *404 - NOT FOUND*
    - *if CITY NOT FOUND*



    - *if ROUTE NOT FOUND*


># GET - api/cities/1/routes/1/jeepneys/1

> ## RESPONSES: 
- ### *200 - SUCCESSFUL RESPONSE*
    - *text/plain* sample

            /api/jeepneys/1

- ### *404 - NOT FOUND*
    - *if CITY NOT FOUND*



    - *if ROUTE NOT FOUND*



    - *if JEEPNEY NOT FOUND*

