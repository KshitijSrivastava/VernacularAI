# VernacularAI

Python Docker used: 3.7-alpine
(image size of 139MB)

python ----- 3.7-alpine  -----      6ca3e0b1ab69  -----  2 weeks ago  -----   73.1MB

## Instructions

sudo docker-compose build

sudo docker-compose up


# REST API

## 1. POST API to validate a slot with a finite set of values.

Request
``` 
{
  "invalid_trigger": "invalid_ids_stated",
  "key": "ids_stated",
  "name": "govt_id",
  "reuse": true,
  "support_multiple": true,
  "pick_first": false,
  "supported_values": [
    "pan",
    "aadhaar",
    "college",
    "corporate",
    "dl",
    "voter",
    "passport",
    "local"
  ],
  "type": [
    "id"
  ],
  "validation_parser": "finite_values_entity",
  "values": [
    {
      "entity_type": "id",
      "value": "college"
    }
  ]
}
```
Response
```
{
    "filled": true,
    "partially_filled": false,
    "trigger": '',
    "parameters": {
        "ids_stated": ["COLLEGE"]
    }
}
```

## 2. POST API to validate a slot with a numeric value extracted and constraints on the value extracted

Request
```
{
  "invalid_trigger": "invalid_age",
  "key": "age_stated",
  "name": "age",
  "reuse": true,
  "pick_first": true,
  "type": [
    "number"
  ],
  "validation_parser": "numeric_values_entity",
  "constraint": "x>=18 and x<=30",
  "var_name": "x",
  "values": [
    {
      "entity_type": "number",
      "value": 23
    }
  ]
}
```

Response
```
{
    "filled": true,
    "partially_filled": false,
    "trigger": '',
    "parameters": {
        "age_stated": 23
    }
}
```
support_multiple = True  is shown by 

pick_first = False