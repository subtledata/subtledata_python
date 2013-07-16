__author__ = 'gsibble'

from base_types import SDFirstClassObject
from sd_menu import SDMenu
from sd_pos_menu import SDPOSMenu
from sd_table import SDTable
from sd_ticket import SDTicket
from sd_collections_tables import SDTableCollection
from sd_collections_tickets import SDTicketCollection


class SDLocation(SDFirstClassObject):
    def __init__(self, parent, location_id, include_menu=False, use_cache=True, fetch=True, initial_data=None, *args,
                 **kwargs):
        """

        :param parent:
        :param location_id:
        :param include_menu:
        :param use_cache:
        :param fetch:
        :param initial_data:
        :param args:
        :param kwargs:
        """
        super(SDLocation, self).__init__(parent, use_cache)
        self._location_id = location_id
        self._include_menu = include_menu

        if fetch:
            self.refresh()
        else:
            if initial_data:
                self._set_attribs(initial_data)


    def refresh(self):
        #Get the location via swagger
        """


        """
        self._swagger_location = self._swagger_locations_api.getLocation(self._location_id, self._api_key,
                                                                         use_cache=self._use_cache)

        #Set attributes of first class Location to match Swagger Location object
        self._set_attribs(self._swagger_location)

        if self._include_menu:
            self.update_menu(self._use_cache)

    @property
    def tables(self):
        """


        :return:
        """
        return SDTableCollection(parent=self)

    def update_menu(self, use_cache=True):
        """

        :param use_cache:
        """
        if not self._use_cache:
            use_cache = False

        self._swagger_menu = self._swagger_locations_api.getLocationMenu(self._location_id, self._api_key,
                                                                         use_cache=use_cache)

    def update_pos_menu(self, use_cache=True):

        if not self._use_cache:
            use_cache = False

        self._swagger_pos_menu = self._swagger_locations_api.getLocationPOSMenu(self._location_id, self._api_key,
                                                                                use_cache=use_cache)

    @property
    def menu(self):
        """


        :return:
        """
        if not hasattr(self, '_swagger_menu'):
            self.update_menu()

        return SDMenu(self, self._swagger_menu)

    @property
    def pos_menu(self):

        if not hasattr(self, '_swagger_pos_menu'):
            self.update_pos_menu()

        return SDPOSMenu(self, self._swagger_pos_menu)

    @property
    def open_tables(self):
        """


        :return:
        """
        return []

    def open_ticket_for_take_out(self, user_id, device_id, revenue_center_id, number_of_people_in_party=1, business_expense=False, custom_ticket_name=None, table_id=None):
        """
        Open a ticket for take out

        :param user_id: SubtleData User ID for order
        :param device_id: User's associated device ID
        :param revenue_center_id: Revenue Center for Take Out orders
        :param number_of_people_in_party: Number of people in the party
        :param business_expense: Whether this is a business expense
        :param custom_ticket_name: Custom ticket name to display
        :param table_id: Table ID to use
        :return: SDTicket Object and Status
        :raise: RunTimeError with error details
        """
        ticket_body = {
            "revenue_center_id": revenue_center_id,
            "number_of_people_in_party": number_of_people_in_party,
            "user_id": user_id,
            "device_id": device_id,
            "business_expense": business_expense
        }

        if custom_ticket_name != None:
            ticket_body["custom_ticket_name"] = custom_ticket_name

        if table_id is not None:
            ticket_body['table_id'] = table_id

        ticket_response = self._swagger_locations_api.createTicket(location_id=self._location_id,
                                                                   api_key=self._api_key,
                                                                   ticket_type='take-out',
                                                                   body=ticket_body)
        if ticket_response.success == True:
            return SDTicket(parent=self, location=self, ticket_id=ticket_response.ticket_id, user_id=user_id, get_values=False)
        else:
            raise RuntimeError('Ticket Not Created: ' + ticket_response.error)

    def open_ticket_for_delivery(self, user_id):

        #Return a SDTicket
        pass

    @property
    def tickets(self):
        """


        :return:
        """
        return SDTicketCollection(parent=self)