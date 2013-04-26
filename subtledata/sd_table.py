__author__ = 'gsibble'

from base_types import SDFirstClassObject
from sd_ticket import SDTicket
from sd_collections_tickets import SDTicketCollection

class SDTable(SDFirstClassObject):

    def __init__(self, parent, location, swagger_table, use_cache=True):
        """

        :param parent:
        :param location:
        :param swagger_table:
        :param use_cache:
        """
        super(SDTable, self).__init__(location, use_cache)
        self.parent = parent
        self.location = location
        self.open_tickets = []
        self.refresh(swagger_table=swagger_table)

    def refresh(self, swagger_table=None):

        """

        :param swagger_table:
        :raise:
        """
        if swagger_table == None:
            if hasattr(self, 'table_id'):
                self._swagger_table = self._swagger_locations_api.getTable(location_id=self.location.location_id,
                                                                           table_id=self.table_id,
                                                                           api_key=self._api_key)
            else:
                raise ValueError('Table has no ID')
        else:
            self._swagger_table = swagger_table

        for attribute in self._swagger_table.swaggerTypes:
            self.__setattr__(attribute, getattr(self._swagger_table, attribute))

        ticket_list = [SDTicket(parent=self, location=self.location, ticket_id=ticket.ticket_id, user_id=ticket.user_id, swagger_ticket=ticket, get_values=False) for ticket in self.open_tickets]
        self.open_tickets = ticket_list

    def open_ticket(self, user_id, device_id, number_of_people_in_party=1, business_expense=False, custom_ticket_name=None, return_ticket_details=False):

        """

        :param user_id:
        :param device_id:
        :param number_of_people_in_party:
        :param business_expense:
        :param custom_ticket_name:
        :param return_ticket_details:
        :return: :raise:
        """
        if hasattr(self, 'revenue_center_id') and hasattr(self, 'subtledata_id'):
            ticket_body = {
                "revenue_center_id": self.revenue_center_id,
                "number_of_people_in_party": number_of_people_in_party,
                "user_id": user_id,
                "device_id": device_id,
                "table_id": self.subtledata_id,
                "business_expense": business_expense,
                "custom_ticket_name": custom_ticket_name
            }
        else:
            raise KeyError('Table missing key data')

        #Send the request
        ticket_response = self._swagger_locations_api.createTicket(self.location._location_id, self._api_key, ticket_type='dine-in', body=ticket_body)

        if return_ticket_details:
            #Get the totals
            return SDTicket(parent=self, location=self.location, ticket_id=ticket_response.ticket_id, user_id=user_id, get_values=True)

        else:
            return SDTicket(parent=self, location=self.location, ticket_id=ticket_response.ticket_id, user_id=user_id, get_values=False)

