from ooiservices.controller.base import BaseController

from ooiservices.model.base import BaseModel

__author__ = "Brian McKenna"

class PlatformController(BaseController):

#    def _model(adapter):
#        return BaseModel() # TODO

    def __init__(self):
        super(BaseController, self).__init__()