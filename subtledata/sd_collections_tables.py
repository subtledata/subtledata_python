__author__ = 'gsibble'

from base_types import SDFirstClassCollection

from sd_table import SDTable

class SDTableCollection(SDFirstClassCollection):

    def __init__(self, tables, parent):
        super(SDTableCollection, self).__init__(parent)
        self.all = tables

    def get_with_pos_id(self, pos_table_id):
        for table in self.all:
            if table.pos_table_id == pos_table_id:
                return table
        else:
            return None

    def get_with_sd_id(self, sd_table_id):
        for table in self.all:
            if table.subtledata_id == sd_table_id:
                return table

        else:
            return None