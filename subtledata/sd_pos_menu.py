__author__ = 'gsibble'

from base_types import SDFirstClassObject
from sd_menu_item import SDMenuItem

class SDPOSMenu(SDFirstClassObject):

    def __init__(self, location, swagger_pos_menu, use_cache=True):

        """

        :param location:
        :param swagger_menu:
        :param use_cache:
        """
        super(SDPOSMenu, self).__init__(location, use_cache)

        #Store parent location
        self._location = location

        #Set up the public lists
        self.items = []
        self.categories = swagger_pos_menu

        #Set up the private item dictionaries
        self._item_name_dict = {}
        self._item_id_dict = {}

        #Set up private category dictionaries
        self._category_name_dict = {}
        self._category_id_dict = {}

        for category in swagger_pos_menu:

            #Store the items
            for index, item in enumerate(category.items):
                setattr(item, 'category', category.pos_category_name)
                sd_item = SDMenuItem(parent=self, location=self._location, swagger_menu_item=item, use_cache=self._use_cache)
                self.items.append(sd_item)
                self._item_name_dict[item.name] = sd_item
                self._item_id_dict[item.item_id] = sd_item
                category.items[index] = sd_item

            self._category_name_dict[category.pos_category_name] = category
            self._category_id_dict[category.pos_category_id] = category

    def get_category(self, category_id=None, category_name=None):

        """

        :param category_id:
        :param category_name:
        :return:
        """
        category_object = None

        if category_id is not None:
            category_object = self._category_id_dict[category_id]
        elif category_name is not None:
            category_object = self._category_name_dict[category_name]

        return category_object

    def get_item(self, item_id=None, item_name=None):

        """

        :param item_id:
        :param item_name:
        :return:
        """
        item_object = None

        if item_id is not None:
            item_object = self._item_id_dict[item_id]
        elif item_name is not None:
            item_object = self._category_name_dict[item_name]

        return item_object