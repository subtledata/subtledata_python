__author__ = 'gsibble'

from base_types import SDFirstClassCollection

from sd_table import SDTable

class SDTableCollection(SDFirstClassCollection):

    def __init__(self, parent):
        """

        :param parent:
        """
        super(SDTableCollection, self).__init__(parent)
        self.parent = parent
        self.location = parent
        self._all_tables = None

    def get_with_pos_id(self, pos_table_id):
        """

        :param pos_table_id:
        :return:
        """
        for table in self.all:
            if table.pos_table_id == pos_table_id:
                return table
        else:
            return None

    def get_with_sd_id(self, sd_table_id):
        """

        :param sd_table_id:
        :return:
        """
        for table in self.all:
            if table.subtledata_id == sd_table_id:
                return table
        else:
            return None

    def refresh(self):
        """


        """
        self._swagger_tables = self._swagger_locations_api.getTableList(location_id=self.location.location_id,
                                                                        api_key=self._api_key)

        #Set the tables to be our type
        self._all_tables = [SDTable(parent=self, location=self.location, swagger_table=table) for table in self._swagger_tables]


    @property
    def all(self):

        """


        :return:
        """
        if self._all_tables is None:
            self.refresh()

        return self._all_tables