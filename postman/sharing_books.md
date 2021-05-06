### All Sharing Offers

<br/>

<b>GET</b> REQUEST to <b>{{BASE_URL}}/sharing_offers/</b>

```
pm.test("Request is successful with a status code of 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response time is less than 500ms", function() {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

pm.test("Check that it returns an array", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an("array");
});

var schema = pm.globals.get("SHARRING_BOOKS_SCHEMA");


pm.test("Schema is valid", function () {
    var jsonData = pm.response.json();
    pm.expect(tv4.validate(jsonData, schema)).to.be.true;
    // pm.response.to.have.jsonSchema(schema);
});
```

<br/>

### Get Shared Book By Id

<br/>

<b>GET</b> REQUEST to <b>{{BASE_URL}}/sharing_offers/create?book_id=3&condition=fine&address=uiewhduwih</b>

```
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});

var schema = pm.globals.get("BOOK_SCHEMA");

pm.test("Schema is valid", function () {
    var jsonData = pm.response.json();
    pm.expect(tv4.validate(jsonData, schema)).to.be.true;
});
```

<br/>

### Get Book

<br/>

<b>GET</b> REQUEST to <b>{{BASE_URL}}/sharing_offers/request_book?sharing_offer_id=1</b>

```
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response time is less than 500ms", function() {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

pm.test("Check that it returns an array", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an("array");
});

var schema = pm.globals.get("SHARRING_BOOKS_SCHEMA");

pm.test("Schema is valid", function () {
    var jsonData = pm.response.json();
    pm.expect(tv4.validate(jsonData, schema)).to.be.true;
});
```

<br/>

### Share Book

<br/>

<b>POST</b> REQUEST to <b>{{BASE_URL}}/sharing_offers</b>

```
pm.test("Status code is 201", function () {
    pm.response.to.have.status(201);
});

pm.test("Response time is less than 300ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(300);
});

pm.test("Condition is bad", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.condition).to.eql("bad");
});
```

<br/>

### Share Book Not In Database

<br/>

<b>POST</b> REQUEST to <b>{{BASE_URL}}/sharing_offers</b>

```
pm.test("Status code is 404", function () {
    pm.response.to.have.status(404);
});

pm.test("Response time is less than 300ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(300);
});
```

<br/>

## Global Variables

```
BOOK_SCHEMA = {
    "type": "object",
    "properties": {
        "id" : {
            "type": "integer"
        },
        "title": {
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "cover": {
            "type": "string"
        },
        "year": {
            "type": "integer"
        },
        "rate": {
            "type": "string"
        },
        "created_at": {
            "type": "string"
        },
        "updated_at": {
            "type": "string"
        },
        "authors_list": {
            "type": "string"
        },
        "genres_list": {
            "type": "string"
        },
        "publishers_list": {
            "type": "string"
        },
        "authors": {
            "type": "array",
            "items": [{
                "id": {
                    "type": "integer"
                },
                "last_name": {
                    "type": "string"
                },
                "first_name": {
                    "type": "string"
                },
                "middle_name": {
                    "type": "string"
                },
                "surname" : {
                    "type": "string"
                },
                "photo": {
                    "type": "string"
                },
                "bio": {
                    "type": "string"
                },
                "created_at": {
                    "type": "string"
                },
                "updated_at": {
                    "type": "string"
                },
                "full_name": {
                    "type": "string"
                },
                "pivot": {
                    "type": "object",
                    "items" : {
                        "book_id": {
                            "type": "integer"
                        },
                        "author_id": {
                            "type": "integer"
                        }
                    }
                }
            }],
            "genres": {
                "type": "array"
            },
            "publishers": {
                "type": "array",
                "items": [{
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    },
                    "created_at": {
                        "type": "string"
                    },
                    "updated_at": {
                        "type": "string"
                    },
                    "pivot": {
                        "type": "object",
                        "items": {
                            "book_id": {
                                "type": "integer"
                            },
                            "publisher_id": {
                                "type": "integer"
                            }
                        }
                    }
                }]
            }
        }
    }
}

SHARING_BOOKS_SCHEMA = {
    "type": "array",
    "items": [{
        "type": "object",
        "properties": {
            "id" : {
                "type": "integer"
            },
            "condition": {
                "type": "string"
            },
            "available": {
                "type": "boolean"
            },
            "address": {
                "type": "string"
            },
            "user_id": {
                "type": "integer"
            },
            "book_id": {
                "type": "integer"
            },
            "created_at": {
                "type": "string"
            },
            "updated_at": {
                "type": "string"
            },
            "user_name": {
                "type": "string"
            },
            "cover": {
                "type": "string"
            },
            "title": {
                "type": "string"
            },
        }
    }]
}
```