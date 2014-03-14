import os
from conduit.base import Conduit
from conduit.process import ProcessConduit
from connector.base import AbstractConnector, ConnectorError

__author__ = 'mat'


def is_executable(file):
    return os.path.isfile(file) and os.access(file, os.X_OK)


class ProcessConnector(AbstractConnector):
    def __init__(self, image, args):
        super().__init__()
        self.image = image
        self.args = args

    def _connected(self):
        return self._conduit.open

    def _disconnect(self):
        pass  # nothing to do here - base class closes the conduit

    def _connect(self) -> Conduit:
        try:
            return ProcessConduit(self.image, *self.args)
        except (OSError, ValueError) as e:
            raise ConnectorError from e

    def _try_available(self):
        return is_executable(self.image)


