from abc import ABC, abstractmethod

from entity.PluginConfig import PluginConfig


class BenchmarkPlugin(ABC):
    def __init__(self, *, pConfig: PluginConfig):
        self.pConfig = pConfig
        pass

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def run(self):
        pass
