import shutil

from pymacaroons import Verifier

from entity.BenchmarkPlugin import BenchmarkPlugin
from entity.PluginConfig import PluginConfig
from util.Crypto import Validator
from util.File import Extractor
from util.Network import Downloader
from userconfig.Config import Config
import os
import glog as log
import pathlib


class ParsecMain(BenchmarkPlugin):

    def __init__(self, pConfig: PluginConfig):
        super().__init__(pConfig=pConfig)

    def download(self):
        log.info('Downloading parsec main application')
        sourceFileName = 'parsec3.tar.gz'
        dataFileName = 'parsec3-input.tar.gz'
        Downloader.download('https://parsec.cs.princeton.edu/download/3.0/parsec-3.0.tar.gz',
                            os.path.join(Config.tempDir), sourceFileName,
                            lambda filePath: Validator.sha256(
                                filePath) == 'a12dda6ca245454ed94fe1f88c6da4977c2a6b5e31cc330b6e13221081cc7857')
        log.info('Downloading parsec dataset')
        Downloader.download('https://parsec.cs.princeton.edu/download/3.0/parsec-3.0-input-native.tar.gz',
                            os.path.join(Config.tempDir), dataFileName,
                            lambda filePath: Validator.sha256(
                                filePath) == '7a566f14df7d663d1e8dc29453abb5fabf60638bcbd40de5fb03a8eaa4f78d04')
        log.info('Extracting parsec source')
        shutil.rmtree(os.path.join(pathlib.Path(os.path.realpath(__file__)).parent, 'parsecsrc'))
        os.makedirs(os.path.join(pathlib.Path(os.path.realpath(__file__)).parent, 'parsecsrc'))
        Extractor.extractTar(os.path.join(Config.tempDir, sourceFileName),
                             os.path.join(pathlib.Path(os.path.realpath(__file__)).parent, 'parsecsrc'))

        log.info('Extracting parsec data')
        shutil.rmtree(os.path.join(pathlib.Path(os.path.realpath(__file__)).parent, 'parsecdata'))
        os.makedirs(os.path.join(pathlib.Path(os.path.realpath(__file__)).parent, 'parsecdata'))
        Extractor.extractTar(os.path.join(Config.tempDir, dataFileName),
                             os.path.join(pathlib.Path(os.path.realpath(__file__)).parent, 'parsecdata'))

    def build(self):
        pass

    def run(self):
        pass


from PluginConfig import ParsecConfig

ParsecMain(ParsecConfig()).download()
