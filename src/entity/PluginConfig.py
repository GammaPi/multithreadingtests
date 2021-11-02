from enum import Enum


class PluginType(Enum):
    WORKLOAD = 0


class PluginConfig:
    def __init__(self, *, pName: str, pVer: str, pType: PluginType, pDesc: str):
        """
        @param pName: Plugin name
        @param pVer: Plugin version
        @param pType: Plugin type
        @param pDesc: Plugin description
        """
        self.pName = pName
        self.pVer = pVer
        self.pType = pType
        self.pDesc = pDesc
