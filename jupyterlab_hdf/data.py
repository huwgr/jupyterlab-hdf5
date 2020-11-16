# -*- coding: utf-8 -*-

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from .baseHandler import HdfFileManager, HdfBaseHandler
from .util import dsetChunk, dsetContentDict, parseSubindex

__all__ = ['HdfDataManager', 'HdfDataHandler']


## manager
class HdfDataManager(HdfFileManager):
    """Implements HDF5 data handling
    """
    def _getFromFile(self, f, uri, ixstr, subixstr, **kwargs):
        # uncomment for debug logging
        logd = dsetContentDict(f[uri], ixstr=ixstr)
        logd['subixstr'] = subixstr
        if subixstr is not None:
            logd['ixcompound'] = parseSubindex(ixstr, subixstr, f[uri].shape)
        self.log.info('{}'.format(logd))

        return dsetChunk(f[uri], ixstr, subixstr)


## handler
class HdfDataHandler(HdfBaseHandler):
    """A handler for HDF5 data
    """
    managerClass = HdfDataManager
