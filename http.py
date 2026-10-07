#HTTP - HyperText Tranfer Protocol

#Is a set of rules which allow computers to communicate over the internet.

#https://jobsy.co.ke

#HTTP REQUEST AND RESPONSE

#Request - A request is a message sent by the client to the server asking for a resource.
#Response - A response is a message sent by the server to the client in reply to a request.

#Browser - Request - Server
#Browser - Response - Server

#Server - A server is a computer that provides data to other computers. It can serve data to systems on a local area network (LAN) or a wide area network (WAN) over the Internet.

#API - Application Programming Interface
#example of API - https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY

#HTTP METHODS
#GET - Get information
#POST - Send/create information
#PUT - Update information
#PATCH - partially update information
#DELETE - Delete information

#GET Request
#GET /users

#POST Request
#POST /users
{
    "name": "John Doe",
    "email": "john@example.com"
}

#HTTP status codes
#200 - OK
#201 - Created
#204 - No Content
#400 - Bad Request
#401 - Unauthorized
#403 - Forbidden
#404 - Not Found
#500 - Internal Server Error

import requests
reponse = requests.get("https://example.com")

print(response.status_code)