My API title
============

    # Install the command line client
    $ pip install coreapi-cli
    

    <!-- Load the JavaScript client library -->
    <script src="/static/rest_framework/js/coreapi-0.1.1.js"></script>
    <script src="/api_doc/schema.js"></script>
    

    # Install the Python client library
    $ pip install coreapi
    

corona\_app[](#corona_app)
--------------------------
### list[](#corona_app-list)

GET `/corona_app/`

    # Load the schema document
    $ coreapi get http://localhost:8000/api_doc/
    
    # Interact with the API endpoint
    $ coreapi action corona_app list
    

    var coreapi = window.coreapi  // Loaded by `coreapi.js`
    var schema = window.schema    // Loaded by `schema.js`
    
    // Initialize a client
    var client = new coreapi.Client()
    
    // Interact with the API endpoint
    var action = ["corona_app", "list"]
    client.action(schema, action).then(function(result) {
        // Return value is in 'result'
    })
    

    import coreapi
    
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://localhost:8000/api_doc/")
    
    # Interact with the API endpoint
    action = ["corona_app", "list"]
    result = client.action(schema, action)

### list

* * *

### create[](#corona_app-create)

POST `/corona_app/`

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

Parameter

Description

`name`

`status`

`latitude`

`longitude`

`diabetes`

    # Load the schema document
    $ coreapi get http://localhost:8000/api_doc/
    
    # Interact with the API endpoint
    $ coreapi action corona_app create -p name=... -p status=... -p latitude=... -p longitude=... -p diabetes=...
    

    var coreapi = window.coreapi  // Loaded by `coreapi.js`
    var schema = window.schema    // Loaded by `schema.js`
    
    // Initialize a client
    var client = new coreapi.Client()
    
    // Interact with the API endpoint
    var action = ["corona_app", "create"]
    var params = {
        name: ...,
        status: ...,
        latitude: ...,
        longitude: ...,
        diabetes: ...,
    }
    client.action(schema, action, params).then(function(result) {
        // Return value is in 'result'
    })
    

    import coreapi
    
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://localhost:8000/api_doc/")
    
    # Interact with the API endpoint
    action = ["corona_app", "create"]
    params = {
        "name": ...,
        "status": ...,
        "latitude": ...,
        "longitude": ...,
        "diabetes": ...,
    }
    result = client.action(schema, action, params=params)

### create

Name 

Status 

Latitude 

Longitude 

 Diabetes 

* * *

### read\_1[](#corona_app-read_1)

GET `/corona_app/result{format}`

#### Path Parameters

The following parameters should be included in the URL path.

Parameter

Description

`format` required

    # Load the schema document
    $ coreapi get http://localhost:8000/api_doc/
    
    # Interact with the API endpoint
    $ coreapi action corona_app read_1 -p format=...
    

    var coreapi = window.coreapi  // Loaded by `coreapi.js`
    var schema = window.schema    // Loaded by `schema.js`
    
    // Initialize a client
    var client = new coreapi.Client()
    
    // Interact with the API endpoint
    var action = ["corona_app", "read_1"]
    var params = {
        format: ...,
    }
    client.action(schema, action, params).then(function(result) {
        // Return value is in 'result'
    })
    

    import coreapi
    
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://localhost:8000/api_doc/")
    
    # Interact with the API endpoint
    action = ["corona_app", "read_1"]
    params = {
        "format": ...,
    }
    result = client.action(schema, action, params=params)
    
### read\_1

* * *

### read[](#corona_app-read)

GET `/corona_app/{id}/`

#### Path Parameters

The following parameters should be included in the URL path.

Parameter

Description

`id` required

A unique integer value identifying this corona app.

    # Load the schema document
    $ coreapi get http://localhost:8000/api_doc/
    
    # Interact with the API endpoint
    $ coreapi action corona_app read -p id=...
    

    var coreapi = window.coreapi  // Loaded by `coreapi.js`
    var schema = window.schema    // Loaded by `schema.js`
    
    // Initialize a client
    var client = new coreapi.Client()
    
    // Interact with the API endpoint
    var action = ["corona_app", "read"]
    var params = {
        id: ...,
    }
    client.action(schema, action, params).then(function(result) {
        // Return value is in 'result'
    })
    

    import coreapi
    
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://localhost:8000/api_doc/")
    
    # Interact with the API endpoint
    action = ["corona_app", "read"]
    params = {
        "id": ...,
    }
    result = client.action(schema, action, params=params)
    

Data Raw

### read

ID \* 

A unique integer value identifying this corona app.

* * *

### update[](#corona_app-update)

PUT `/corona_app/{id}/`

#### Path Parameters

The following parameters should be included in the URL path.

Parameter

Description

`id` required

A unique integer value identifying this corona app.

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

Parameter

Description

`name`

`status`

`latitude`

`longitude`

`diabetes`

    # Load the schema document
    $ coreapi get http://localhost:8000/api_doc/
    
    # Interact with the API endpoint
    $ coreapi action corona_app update -p id=... -p name=... -p status=... -p latitude=... -p longitude=... -p diabetes=...
    

    var coreapi = window.coreapi  // Loaded by `coreapi.js`
    var schema = window.schema    // Loaded by `schema.js`
    
    // Initialize a client
    var client = new coreapi.Client()
    
    // Interact with the API endpoint
    var action = ["corona_app", "update"]
    var params = {
        id: ...,
        name: ...,
        status: ...,
        latitude: ...,
        longitude: ...,
        diabetes: ...,
    }
    client.action(schema, action, params).then(function(result) {
        // Return value is in 'result'
    })
    

    import coreapi
    
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://localhost:8000/api_doc/")
    
    # Interact with the API endpoint
    action = ["corona_app", "update"]
    params = {
        "id": ...,
        "name": ...,
        "status": ...,
        "latitude": ...,
        "longitude": ...,
        "diabetes": ...,
    }
    result = client.action(schema, action, params=params)
    

Data Raw

### update

ID \* 

A unique integer value identifying this corona app.

Name 

Status 

Latitude 

Longitude 

 Diabetes 

* * *

Awaiting request

Close Send Request

Interact

### delete[](#corona_app-delete)

DELETE `/corona_app/{id}/`

#### Path Parameters

The following parameters should be included in the URL path.

Parameter

Description

`id` required

A unique integer value identifying this corona app.

    # Load the schema document
    $ coreapi get http://localhost:8000/api_doc/
    
    # Interact with the API endpoint
    $ coreapi action corona_app delete -p id=...
    

    var coreapi = window.coreapi  // Loaded by `coreapi.js`
    var schema = window.schema    // Loaded by `schema.js`
    
    // Initialize a client
    var client = new coreapi.Client()
    
    // Interact with the API endpoint
    var action = ["corona_app", "delete"]
    var params = {
        id: ...,
    }
    client.action(schema, action, params).then(function(result) {
        // Return value is in 'result'
    })
    

    import coreapi
    
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://localhost:8000/api_doc/")
    
    # Interact with the API endpoint
    action = ["corona_app", "delete"]
    params = {
        "id": ...,
    }
    result = client.action(schema, action, params=params)
    

Data Raw

### delete

ID \* 

A unique integer value identifying this corona app.

* * *
### read\_0[](#corona_app-read_0)

GET `/corona_app/{id}{format}`

#### Path Parameters

The following parameters should be included in the URL path.

Parameter

Description

`id` required

A unique integer value identifying this corona app.

`format` required

    # Load the schema document
    $ coreapi get http://localhost:8000/api_doc/
    
    # Interact with the API endpoint
    $ coreapi action corona_app read_0 -p id=... -p format=...
    

    var coreapi = window.coreapi  // Loaded by `coreapi.js`
    var schema = window.schema    // Loaded by `schema.js`
    
    // Initialize a client
    var client = new coreapi.Client()
    
    // Interact with the API endpoint
    var action = ["corona_app", "read_0"]
    var params = {
        id: ...,
        format: ...,
    }
    client.action(schema, action, params).then(function(result) {
        // Return value is in 'result'
    })
    

    import coreapi
    
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://localhost:8000/api_doc/")
    
    # Interact with the API endpoint
    action = ["corona_app", "read_0"]
    params = {
        "id": ...,
        "format": ...,
    }
    result = client.action(schema, action, params=params)
    

Data Raw

### read\_0

ID \* 

A unique integer value identifying this corona app.

format \* 

* * *

### update\_0[](#corona_app-update_0)

PUT `/corona_app/{id}{format}`

#### Path Parameters

The following parameters should be included in the URL path.

Parameter

Description

`id` required

A unique integer value identifying this corona app.

`format` required

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

Parameter

Description

`name`

`status`

`latitude`

`longitude`

`diabetes`

    # Load the schema document
    $ coreapi get http://localhost:8000/api_doc/
    
    # Interact with the API endpoint
    $ coreapi action corona_app update_0 -p id=... -p format=... -p name=... -p status=... -p latitude=... -p longitude=... -p diabetes=...
    

    var coreapi = window.coreapi  // Loaded by `coreapi.js`
    var schema = window.schema    // Loaded by `schema.js`
    
    // Initialize a client
    var client = new coreapi.Client()
    
    // Interact with the API endpoint
    var action = ["corona_app", "update_0"]
    var params = {
        id: ...,
        format: ...,
        name: ...,
        status: ...,
        latitude: ...,
        longitude: ...,
        diabetes: ...,
    }
    client.action(schema, action, params).then(function(result) {
        // Return value is in 'result'
    })
    

    import coreapi
    
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://localhost:8000/api_doc/")
    
    # Interact with the API endpoint
    action = ["corona_app", "update_0"]
    params = {
        "id": ...,
        "format": ...,
        "name": ...,
        "status": ...,
        "latitude": ...,
        "longitude": ...,
        "diabetes": ...,
    }
    result = client.action(schema, action, params=params)
    

Data Raw

### update\_0

ID \* 

A unique integer value identifying this corona app.

format \* 

Name 

Status 

Latitude 

Longitude 

 Diabetes 

* * *

### delete\_0[](#corona_app-delete_0)

DELETE `/corona_app/{id}{format}`

#### Path Parameters

The following parameters should be included in the URL path.

Parameter

Description

`id` required

A unique integer value identifying this corona app.

`format` required

    # Load the schema document
    $ coreapi get http://localhost:8000/api_doc/
    
    # Interact with the API endpoint
    $ coreapi action corona_app delete_0 -p id=... -p format=...
    

    var coreapi = window.coreapi  // Loaded by `coreapi.js`
    var schema = window.schema    // Loaded by `schema.js`
    
    // Initialize a client
    var client = new coreapi.Client()
    
    // Interact with the API endpoint
    var action = ["corona_app", "delete_0"]
    var params = {
        id: ...,
        format: ...,
    }
    client.action(schema, action, params).then(function(result) {
        // Return value is in 'result'
    })
    

    import coreapi
    
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://localhost:8000/api_doc/")
    
    # Interact with the API endpoint
    action = ["corona_app", "delete_0"]
    params = {
        "id": ...,
        "format": ...,
    }
    result = client.action(schema, action, params=params)
    

Data Raw

### delete\_0

ID \* 

A unique integer value identifying this corona app.

format \* 

* * *

### result > list[](#corona_app-result-list)

GET `/corona_app/result/`

    # Load the schema document
    $ coreapi get http://localhost:8000/api_doc/
    
    # Interact with the API endpoint
    $ coreapi action corona_app result list
    

    var coreapi = window.coreapi  // Loaded by `coreapi.js`
    var schema = window.schema    // Loaded by `schema.js`
    
    // Initialize a client
    var client = new coreapi.Client()
    
    // Interact with the API endpoint
    var action = ["corona_app", "result &gt; list"]
    client.action(schema, action).then(function(result) {
        // Return value is in 'result'
    })
    

    import coreapi
    
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://localhost:8000/api_doc/")
    
    # Interact with the API endpoint
    action = ["corona_app", "result &gt; list"]
    result = client.action(schema, action)
    

Data Raw

### result > list

* * *

### read[](#-read)

GET `/corona_app{format}`

#### Path Parameters

The following parameters should be included in the URL path.

Parameter

Description

`format` required

    # Load the schema document
    $ coreapi get http://localhost:8000/api_doc/
    
    # Interact with the API endpoint
    $ coreapi action read -p format=...
    

    var coreapi = window.coreapi  // Loaded by `coreapi.js`
    var schema = window.schema    // Loaded by `schema.js`
    
    // Initialize a client
    var client = new coreapi.Client()
    
    // Interact with the API endpoint
    var action = ["read"]
    var params = {
        format: ...,
    }
    client.action(schema, action, params).then(function(result) {
        // Return value is in 'result'
    })
    

    import coreapi
    
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://localhost:8000/api_doc/")
    
    # Interact with the API endpoint
    action = ["read"]
    params = {
        "format": ...,
    }
    result = client.action(schema, action, params=params)
    

Data Raw

### read

format \* 

* * *

### create[](#-create)

POST `/corona_app{format}`

#### Path Parameters

The following parameters should be included in the URL path.

Parameter

Description

`format` required

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

Parameter

Description

`name`

`status`

`latitude`

`longitude`

`diabetes`

    # Load the schema document
    $ coreapi get http://localhost:8000/api_doc/
    
    # Interact with the API endpoint
    $ coreapi action create -p format=... -p name=... -p status=... -p latitude=... -p longitude=... -p diabetes=...
    

    var coreapi = window.coreapi  // Loaded by `coreapi.js`
    var schema = window.schema    // Loaded by `schema.js`
    
    // Initialize a client
    var client = new coreapi.Client()
    
    // Interact with the API endpoint
    var action = ["create"]
    var params = {
        format: ...,
        name: ...,
        status: ...,
        latitude: ...,
        longitude: ...,
        diabetes: ...,
    }
    client.action(schema, action, params).then(function(result) {
        // Return value is in 'result'
    })
    

    import coreapi
    
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://localhost:8000/api_doc/")
    
    # Interact with the API endpoint
    action = ["create"]
    params = {
        "format": ...,
        "name": ...,
        "status": ...,
        "latitude": ...,
        "longitude": ...,
        "diabetes": ...,
    }
    result = client.action(schema, action, params=params)
    

Data Raw

### create

format \* 

Name 

Status 

Latitude 

Longitude 

 Diabetes 

* * *

Awaiting request

Close Send Request

### Token Authentication

Scheme:

 Either a registered authentication scheme such as `Bearer`, or a custom schema such as `Token` or `JWT`.

Token:

 A valid API token.

Close Use Token Authentication

### Basic Authentication

Username:

Password:

Close Use Basic Authentication

### Session Authentication

#### You need to log in to enable Session Authentication.
