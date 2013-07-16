__author__ = 'gsibble'

from base_types import SDFirstClassObject

class SDMenuItem(SDFirstClassObject):

    def __init__(self, parent, location, swagger_menu_item, use_cache=True):

        super(SDMenuItem, self).__init__(parent, use_cache)
        self.parent = parent
        self.location = location
        self.refresh(swagger_menu_item=swagger_menu_item)

    def refresh(self, swagger_menu_item=None):

        if swagger_menu_item == None:
            if hasattr(self, 'item_id'):
                self._swagger_menu_item = self._swagger_locations_api.getMenuItem(location_id=self.location.location_id,
                                                                                  item_id=self.item_id,
                                                                                  api_key=self._api_key)
            else:
                raise ValueError('Item has no item_id')
        else:
            self._swagger_menu_item = swagger_menu_item

        for attribute in self._swagger_menu_item.swaggerTypes:
            self.__setattr__(attribute, getattr(self._swagger_menu_item, attribute))

    @property
    def local_modifier_categories(self):

        if not hasattr(self, '_local_modifiers'):
            self._swagger_menu_item = self._swagger_locations_api.getMenuItem(location_id=self.location.location_id,
                                                                                      item_id=self.item_id,
                                                                                      api_key=self._api_key)

        if hasattr(self._swagger_menu_item, 'local_modifier_categories'):
            self._local_modifier_categories = self._swagger_menu_item.local_modifier_categories
        else:
            self._local_modifier_categories = []
        return self._local_modifier_categories

    @property
    def mapped_modifier_categories(self):

        if not hasattr(self, '_mapped_modifiers'):
            self._swagger_menu_item = self._swagger_locations_api.getMenuItem(location_id=self.location.location_id,
                                                                                      item_id=self.item_id,
                                                                                      api_key=self._api_key)
        if hasattr(self._swagger_menu_item, 'mapped_modifier_categories'):
            self._mapped_modifier_categories = self._swagger_menu_item.mapped_modifier_categories
        else:
            self._mapped_modifier_categories = []
        return self._mapped_modifier_categories