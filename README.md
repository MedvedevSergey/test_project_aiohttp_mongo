# Deploy project
## Create environment
```
python -m venv <venv_name>
```
## Activate environment

```
source /path/to/env/<venv_name>/bin/activate
```
## Install all dependences to your environment
```
pip install -r requirements.txt
```

## Set db
### Pull mongodb image
```
docker pull mongo
```
### Start mongodb
```
docker run -d  -p 27017:27017 mongo
```

# Start project
For start server need to execute command:
```
python aiohttp_store/main.py
```



# Get or create data

### Get all data about product you need to send request
```
http://0.0.0.0:8080
```

### Get one object by id
It's a POST request
Need to send JSON
```
{
    "id": <object_id>
}
```
```
http://0.0.0.0:8080/id
```

### Filter objects by title or parameters
It's a POST request
Need to send JSON
```
{
    "title": <title_object>
}
```
or
```
{
    "parameters": {
        "first_parameter": "value",
        "second_parameter": "value"
    }
}
```
```
http://0.0.0.0:8080/filter
```

# Example
## Create object

### request

```
curl -H "Content-Type: application/json" \
  --request POST \
  --data '{"title":"example_object", 
        "description": "some text",
        "parameters": {
            "created_by": "company",
            "serial_number": 12345
        }
    }' \
  http://localhost:8080/create
```

  ### response
  ```
 {
    "title": "example_object",
    "parameters": {
        "created_by": "company",
        "serial_number": 12345
    },
    "id": "5e79bf57fa45da08da6c5177",
    "description": "some text"
}
  ```

## Filter objects by paramters
### Filter by title
### request
```
curl -H "Content-Type: application/json" \
  --request POST \
  --data '{"title":"example_object"}' \
  http://localhost:8080/filter  
```
### response
```
[
    {
        "title": "example_object",
        "parameters": {
            "created_by": "company",
            "serial_number": 12345
        },
        "id": "5e79bf57fa45da08da6c5177",
        "description": "some text"
    }  
]

```

### Filter by parameters
### request
```
curl -H "Content-Type: application/json" \
  --request POST \
  --data '{"parameters": {"created_by": "company"}}' \
  http://localhost:8080/filter  
```
### response
```
[
    {
        "title": "example_object",
        "parameters": {
            "created_by": "company",
            "serial_number": 12345
        },
        "id": "5e79bf57fa45da08da6c5177",
        "description": "some text"
    }  
]

```

## Get detail about object by id

### request
```
curl -H "Content-Type: application/json" \
  --request POST \
  --data '{"id":"5e79bf57fa45da08da6c5177"}' \
  http://localhost:8080/id  
```

### response

```
[
    {
        "title": "example_object",
        "parameters": {
            "created_by": "company",
            "serial_number": 12345
        },
        "id": "5e79bf57fa45da08da6c5177",
        "description": "some text"
    }  
]
```