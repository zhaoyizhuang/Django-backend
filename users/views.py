"""
View RESTful Web service API for users resource
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerializer
from .models import User


# using HTTP endpoints /users
class PersonView(APIView):
    """
    Define the following HTTP endpoints:
    <ul>
        <li> POST /users to create a new user instance
        </li>
        <li> GET /users to retrieve all user instances
        </li>
    </ul>
    """

    # POST Request
    def post(self, request):
        """
        Post Request, create a new user instance.

        @param request: Represents request from client, including body
        containing the JSON object for the new user to be inserted in the
        database
        Response: Represents response to client, including the
        body formatted as JSON containing the new user that was inserted in the
        database
        """
        serial = PersonSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response({"status": "success",
                             "data": serial.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error",
                             "data": serial.errors}, status=status.HTTP_400_BAD_REQUEST)

    # GET Request
    def get(self, request):
        """
        Retrieve a list of users' information in JSON format.

        @param request: Represents request from client.

        Response: Represents response to client, including the
        body in JSON array containing user objects
        """
        users = User.objects.all()
        serial = PersonSerializer(users, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)


# using HTTP endpoints /users/:uid
class PersonDetailView(APIView):
    """
    Define the following HTTP endpoints:
    <ul>
        <li> DELETE /users/:uid to remove a particular user instance
        </li>
        <li> PUT /users/:uid to update a particular user instances
        </li>
    </ul>
    """

    # help function
    def get_user(self, uid):
        """
        Retrieve a user instance from database based on user's primary key.

        @param uid User's primary key
        @return user instance
        """
        try:
            return User.objects.get(id=uid)
        except User.DoesNotExist:
            return None

    # DELETE Request
    def delete(self, request, uid):
        """
        Delete a user instance from the database based on user's primary key

        @param request: Represents request from client, including path
        parameter uid identifying the primary key of the user to
        be removed

        Response: Empty Response, only bad request status in console.
        """
        user_instance = self.get_user(uid)
        if not user_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user_instance.delete()
        return Response(status=status.HTTP_200_OK)

    # PUT Request
    def put(self, request, uid):
        """
        Update a existing user based on the update body and user's primary key.
        Not all properties need to be provided in the request.
        Properties that are not included should not be updated.

        @param request: Represents request from client, including path
        parameter uid identifying the primary key of the user to
        be updated and body contains update information of the user.

        Response: Represents response to client, including all the properties of the user.
        """
        user_instance = self.get_user(uid)
        if not user_instance:
            return Response({"res": "User Doesn't Exist"}, status=status.HTTP_400_BAD_REQUEST)

        if request.data.get("first_name") is not None:
            user_instance.first_name = request.data.get("first_name")
        if request.data.get("last_name") is not None:
            user_instance.last_name = request.data.get("last_name")
        if request.data.get("phone_number") is not None:
            user_instance.phone_number = request.data.get("phone_number")
        if request.data.get("email") is not None:
            user_instance.email = request.data.get("email")
        if request.data.get("role") is not None:
            user_instance.role = request.data.get("role")

        serial = PersonSerializer(instance=user_instance, data=request.data, partial=True)
        if serial.is_valid():
            user_instance.save()
            return Response({"status": "updated",
                             "data": serial.data}, status=status.HTTP_200_OK)
        return Response({"status": "error",
                         "data": serial.errors}, status=status.HTTP_200_OK)
