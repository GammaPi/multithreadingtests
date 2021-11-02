import os


class Config:
    curDir = os.getcwd()
    tempDir = os.path.join(os.getcwd(), 'tmp')
