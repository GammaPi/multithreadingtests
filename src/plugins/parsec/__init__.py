from pymacaroons import Verifier

from entity.BenchmarkPlugin import BenchmarkPlugin
from entity.PluginConfig import PluginConfig
from util.Crypto import Validator
from util.Network import Downloader
from userconfig.Config import Config
import os
import glog as log


class ParsecMain(BenchmarkPlugin):

    def __init__(self, pConfig: PluginConfig):
        super().__init__(pConfig=pConfig)

    def download(self):
        log.info('Downloading parsec main application')
        Downloader.download('https://parsec.cs.princeton.edu/download/3.0/parsec-3.0.tar.gz',
                            os.path.join(Config.tempDir), 'parsec3.tar.gz',
                            lambda filePath: Validator.sha256(filePath) == 'a12dda6ca245454ed94fe1f88c6da4977c2a6b5e31cc330b6e13221081cc7857')
        log.info('Downloading parsec dataset')
        Downloader.download('http://parsec.cs.princeton.edu/download/3.0/parsec-3.0-input-native.tar.gz',
                            os.path.join(Config.tempDir), 'parsec3-input.tar.gz',
                            lambda filePath: Validator.sha256(
                                filePath) == '7a566f14df7d663d1e8dc29453abb5fabf60638bcbd40de5fb03a8eaa4f78d04')

    def build(self):
        pass

    def run(self):
        pass