__author__ = 'gsibble'

#Custom Exceptions

class NoUserSetOnTicket(Exception):
    pass

class NoTicketID(Exception):
    pass

class UserNotCreated(Exception):
    pass

class UserLoginError(Exception):
    pass