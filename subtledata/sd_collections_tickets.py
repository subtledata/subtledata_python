__author__ = 'gsibble'

from base_types import SDFirstClassCollection
from sd_ticket import SDTicket

class SDTicketCollection(SDFirstClassCollection):

    def __init__(self, parent):
        super(SDTicketCollection, self).__init__(parent)
        self.parent = parent
        self.location = parent
        self._all_tickets = None

    def get_with_sd_id(self, ticket_id):
        for ticket in self.all:
            if ticket.ticket_id == ticket_id:
                return ticket
        else:
            return None

    def get_with_pos_id(self, pos_ticket_id):
        for ticket in self.all:
            if ticket.pos_ticket_id == pos_ticket_id:
                return ticket
        else:
            return None

    def refresh(self):
        self._swagger_tickets = self._swagger_locations_api.getTickets(location_id=self.location.location_id,
                                                                       api_key=self._api_key)

        self._all_tickets = [SDTicket(parent=self, location=self.location, ticket_id=ticket.ticket_id, user_id=ticket.user_id, swagger_ticket=ticket, get_values=False) for ticket in self._swagger_tickets]

    @property
    def all(self):

        if self._all_tickets is None:
            self.refresh()

        return self._all_tickets