__author__ = 'gsibble'

from base_types import SDFirstClassObject
import exceptions as Exceptions

class SDTicket(SDFirstClassObject):
    def __init__(self, parent, location, ticket_id, user_id=0, get_values=True, swagger_ticket=None, *args, **kwargs):
        """

        :param parent:
        :param location:
        :param ticket_id:
        :param user_id:
        :param get_values:
        :param swagger_ticket:
        :param args:
        :param kwargs:
        """
        super(SDTicket, self).__init__(parent, False)

        self.ticket_id = ticket_id
        self.user_id = user_id
        self.location = location

        if swagger_ticket is None or get_values == True:
            self.refresh()
        else:
            self.refresh(swagger_ticket=swagger_ticket)

    def refresh(self, swagger_ticket=None):
        """

        :param swagger_ticket:
        """
        if swagger_ticket is None:
            self._swagger_ticket = self._swagger_locations_api.getTicket(self.location.location_id, self.ticket_id, api_key=self._api_key)
        else:
            self._swagger_ticket = swagger_ticket

        if self._swagger_ticket is not None:
            for attribute in self._swagger_ticket.swaggerTypes:
                self.__setattr__(attribute, getattr(self._swagger_ticket, attribute))


    def add_item_to_order(self, item_id, quantity, instructions=None, modifiers=None):

        """

        :param item_id:
        :param quantity:
        :param instructions:
        :param modifiers:
        :return: :raise:
        """
        if hasattr(self, 'user_id') and hasattr(self, 'ticket_id'):

            #If we don't have a user_id, use the default user of 0
            if self.user_id is None:
                user_id = 0

            #But if we do have a user, use them
            else:
                user_id = self.user_id

            if self.ticket_id is not None:
                post_body = {
                    'item_id': int(item_id),
                    'quantity': quantity
                    }

                if instructions is not None:
                    post_body['instructions'] = instructions

                if modifiers is not None:
                    post_body['modifiers'] = modifiers

                #print post_body

                returned_status = self._swagger_locations_api.addItemsToOrder(location_id=self.location.location_id,
                                                                              ticket_id=self.ticket_id,
                                                                              user_id=user_id,
                                                                              api_key=self._api_key,
                                                                              body=post_body)

                return returned_status
            else:

                raise Exceptions.NoTicketID
        else:
            raise Exceptions.NoUserSetOnTicket

    def submit_order(self):
        """


        :return: :raise:
        """
        if hasattr(self, 'user_id') and hasattr(self, 'ticket_id'):

            #If we don't have a connected user, use the default user 0
            if self.user_id is None:
                user_id = 0
            else:
                user_id = self.user_id

            if self.ticket_id is not None:
                returned_status = self._swagger_locations_api.submitOrder(location_id=self.location.location_id,
                                                                          ticket_id=self.ticket_id,
                                                                          user_id=user_id,
                                                                          api_key=self._api_key)

                return returned_status
            else:
                raise Exceptions.NoTicketID
        else:
            raise Exceptions.NoUserSetOnTicket

    def add_discount(self, discount_type_id, discount, user_id=0):
        """

        :param discount_type_id:
        :param discount:
        :param user_id:
        :return: :raise:
        """
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

    def pay_with_external_source(self, amount, tip_amount, user_id, device_id, tender_type_id, payment_source_name):

        payment_body = {
          "payment_source_name": payment_source_name,
          "tip_amount": tip_amount,
          "amount_before_tip": amount,
          "tender_type_id": tender_type_id,
          "user_id": user_id,
          "device_id": device_id
        }

        paymentStatus = self._swagger_locations_api.addExternalPaymentToTicket(location_id=self.location.location_id,
                                                                               ticket_id=self.ticket_id,
                                                                               body=payment_body,
                                                                               api_key=self._api_key)
        self.refresh()

        return paymentStatus

    def void(self):
        voidStatus = self._swagger_locations_api.voidTicket(location_id=self.location.location_id,
                                                            ticket_id=self.ticket_id,
                                                            api_key=self._api_key)

        return voidStatus

    def cancel(self):

        return self.void()