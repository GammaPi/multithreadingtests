from enum import Enum

from entity.PluginConfig import PluginConfig, PluginType


class ParsecConfig(PluginConfig):
    def __init__(self):
        super().__init__(pName='Parsec3.0', pVer='1.0.0', pType=PluginType.WORKLOAD, pDesc='Parsec application')
