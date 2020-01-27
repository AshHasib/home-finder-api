# basha_chai api

This is the REST backend for my app 'basha_chai'. There are certain methods which supports GET, POST, PUT, DELETE methods
 for app's operations. These are the endpoints: 

 - /hello/ **GET** - a hello message
 - /authhello/ **GET** - a hello message with authentication
 - /register/ **POST** - sign up as a new user (fullName, userName, phoneNumber, email, password)
 - /gettoken/ **POST** - get your token by providing username and password
 - /rents/ **POST** - post a rent with necessary credentials