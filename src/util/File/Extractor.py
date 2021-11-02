import tarfile
from tqdm import tqdm
import subprocess

from exception.TestException import MTException


def extractTar(filePath: str, dstFolderPath: str, usePythonLib=True):
    if usePythonLib:
        with tarfile.open(name=filePath) as tar:
            # Go over each member
            for member in tqdm(iterable=tar.getmembers(), total=len(tar.getmembers())):
                # Extract member
                tar.extract(member=member, path=dstFolderPath)
    else:
        result = subprocess.run(['tar', '-xf', filePath, '-C', dstFolderPath], stdout=subprocess.PIPE)
        if result.returncode != 0:
            raise MTException("tar execution failed %s", result.stderr)
