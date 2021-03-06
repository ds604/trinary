
class Register(object):

    def __init__(self, virtual_ndx = False, datatype = False):
        if virtual_ndx == False:
            self.virtual_ndx = -1
        else:
            self.virtual_ndx = virtual_ndx

        if datatype != False:
            self.datatype = datatype

        self.mem_loc = 0

    def __str__(self):
        return str(self.virtual_ndx)

    def set_virtual_ndx(self, virtual_ndx):
        self.virtual_ndx = virtual_ndx

    def get_virtual_ndx(self):
        return self.virtual_ndx

    def set_datatype(self, datatype):
        self.data_type = datatype

    def get_datatype(self):
        return self.datatype

    def set_mem_loc(self, loc):
        self.mem_loc = loc

    def get_mem_loc(self):
        return self.mem_loc
