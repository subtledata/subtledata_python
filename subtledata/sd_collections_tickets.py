__author__ = 'gsibble'

from base_types import SDFirstClassCollection
from sd_ticket import SDTicket

class SDTicketCollection(SDFirstClassCollection):

    def __init__(self, parent, tickets):
        super(SDTicketCollection, self).__init__(parent)

        self.all = tickets

    def get_with_sd_id(self, ticket_id):
        for ticket in self.all:
            if ticket.ticket_id == ticket_id:
                return ticket_id
        else:
            return None

    def get_with_pos_id(self, pos_ticket_id):
        for ticket in self.all:
            if ticket.pos_ticket_id == pos_ticket_id:
                return ticket
        else:
            return None
