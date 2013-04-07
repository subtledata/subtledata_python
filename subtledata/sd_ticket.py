__author__ = 'gsibble'

from base_types import SDFirstClassObject
import constants as C

class SDTicket(SDFirstClassObject):
    def __init__(self, parent, location, ticket_id, user_id=0, get_values=True, swagger_ticket=None, *args, **kwargs):
        super(SDTicket, self).__init__(parent, False)

        self.ticket_id = ticket_id
        self.user_id = user_id
        self.location = location

        if swagger_ticket is None or get_values == True:
            self.refresh()
        else:
            self.refresh(swagger_ticket=swagger_ticket)

    def refresh(self, swagger_ticket=None):

        if swagger_ticket is None:
            self._swagger_ticket = self._swagger_locations_api.getTicket(self.location.location_id, self.ticket_id, api_key=self._api_key)
        else:
            self._swagger_ticket = swagger_ticket

        if self._swagger_ticket is not None:
            for attribute in self._swagger_ticket.swaggerTypes:
                self.__setattr__(attribute, getattr(self._swagger_ticket, attribute))


    def add_item_to_order(self, item_id, quantity, instructions=None, modifiers=None):

        if hasattr(self, 'user_id') and hasattr(self, 'ticket_id'):
            if self.user_id is not None and self.ticket_id is not None:
                post_body = {
                    'item_id': int(item_id),
                    'quantity': quantity,

                    }

                if instructions is not None:
                    post_body['instructions'] = instructions

                if modifiers is not None:
                    post_body['modifiers'] = modifiers

                print post_body

                returned_status = self._swagger_locations_api.addItemsToOrder(location_id=self.location.location_id,
                                                                              ticket_id=self.ticket_id,
                                                                              user_id=self.user_id,
                                                                              api_key=self._api_key,
                                                                              body=post_body)

                return returned_status

            else:

                raise C.NoUserSetOnTicket
        else:
            raise C.NoUserSetOnTicket

    def submit_order(self):

        if hasattr(self, 'user_id') and hasattr(self, 'ticket_id'):
            if self.user_id is not None and self.ticket_id is not None:

                returned_status = self._swagger_locations_api.submitOrder(location_id=self.location.location_id,
                                                                          ticket_id=self.ticket_id,
                                                                          user_id=self.user_id,
                                                                          api_key=self._api_key,
                                                                          body={'send': True})

                return returned_status
            else:
                raise C.NoUserSetOnTicket
        else:
            raise C.NoUserSetOnTicket

    def add_discount(self, discount_type_id, discount, user_id=0):
        if discount > self.total:
            raise ValueError('You cannot discount a ticket more than its total amount')

        discountBody = {
            'discount_type': discount_type_id,
            'discount_amount': discount,
            'user_id': user_id
        }

        discountStatus = self._swagger_locations_api.discountTicket(location_id=self.location.location_id,
                                                                    ticket_id=self.ticket_id,
                                                                    api_key=self._api_key,
                                                                    body=discountBody)

        self.refresh()

        return discountStatus