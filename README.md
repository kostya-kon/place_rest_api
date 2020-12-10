# place_rest_api
## Actually it is demonstration of my REST skills, but i can also found it usefull.

### Description
By this API u can add/get/update/delete notices about some places

Structure of Notice:
```
"notices": {
            "title": "POST_TEST",
            "address": "POST_TEST ADDRESS",
            "description": "ITS WORKS",
            "author_id": 1
        }
```
# API 1.0 (/api/places/)

## GET (/api/places/)
Use it to get JSON list of ur places

Response:
```
{
    "notices": [
        {
            "title": "Awful place",
            "address": "kosmonavta komarova 1",
            "description": "NAU really not good.",
            "author_id": 1
        }
    ]
}
```

## POST (/api/places/)
Use it to add some notice to ur list

Exaple: 
```
{
    "notice": {
        "title": "POST_TEST",
        "address": "POST_TEST ADDRESS",
        "description": "ITS WORKS",
        "author_id": 1
    }
}
```
Response:
```
{
    "success": "Article 'POST_TEST' created successfully"
}
```

## PUT (/api/places/<int:pk>)
Use it to update info about any Notice, wich already created

Example(/api/places/1):
```
{
    "notice": {
        "title": "PUT_TEST"
    }
}
```
Response:
```
{
    "success": "Article 'PUT_TEST' updated successfully"
}
```
## DELETE (/api/places/<int:pk>)
Use it for delete any Notice

Response(/api/places/1):
```
{
    "message": "Article with id `1` has been deleted."
}
```
