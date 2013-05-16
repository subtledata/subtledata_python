__author__ = 'gsibble'

from base_types import SDFirstClassCollection

from sd_user import SDUser

import exceptions as Exceptions

class SDUserCollection(SDFirstClassCollection):

    def __init__(self, parent):
        """
        Set up our user list
        :param parent:
        """
        super(SDUserCollection, self).__init__(parent)

    @property
    def all(self):
        """
        Get all users available with the current API Key

        :return: List of SDUser objects
        """
        return []


    def get(self, user_id, use_cache=True):
        """
        Get a user based upon user_id
        :param user_id:
        :param use_cache:
        :return: SDUser object
        """
        if not self._use_cache:
            use_cache = False

        return SDUser(self, user_id=user_id, use_cache=use_cache)

    def filter(self, first_name=None):
        """
        Get a user based upon other criteria
        :param first_name:
        :return:
        """
        return []

    def create(self, user_name, password, first_name,
               last_name, device_uuid,
               email_address, cell_phone,
               middle_name=None,
               dob=None,
               latitude=None, longitude=None):
        """
        Create a new user with the passed details
        :param user_name: SubtleData user name
        :param password: SubtleData user password
        :param device_uuid: The user's current device
        :param email_address: The user's email address
        :param cell_phone: The user's cell phone
        :return: SDUser object :raise: UserNotCreated if error
        """

        #Set up our new_user POST request
        new_user_body = {'user_name': user_name,
                         'password': password,
                         'first_name': first_name,
                         'last_name': last_name,
                         'device_uuid': device_uuid,
                         'email_address': email_address,
                         'cell_phone': cell_phone}

        #If we are passed a DOB, add it to the call
        if dob:
            new_user_body['dob'] = dob

        #If we are passed a middle name, add it to the call
        if middle_name:
            new_user_body['middle_name'] = middle_name

        #If we are passed a location, add it to the call
        if latitude and longitude:
            new_user_body['latitude'] = float(latitude)
            new_user_body['longitude'] = float(longitude)

        #Make the request to create the new user
        new_user_data = self._swagger_users_api.createUser(api_key=self._api_key, body=new_user_body)

        #Try to fetch the new user's details
        try:

            user_id = new_user_data.user_id
            device_id = new_user_data.device_id
            print user_id
            print device_id

        except KeyError:
            raise Exceptions.UserNotCreated

        #Create our User object by fetching all details
        new_user = self.get(user_id)

        #Set the device ID of the new user
        new_user.__setattr__('device_id', device_id)

        #Return our user object
        return new_user