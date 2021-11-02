import hashlib

from tqdm import tqdm
import os


def sha256(filePath: str):

    with open(filePath, "rb") as f:
        f.seek(0, os.SEEK_END)
        fizeSize=f.tell()
        f.seek(0, os.SEEK_SET)

        file_hash = hashlib.sha256()
        chunkSize = 8192
        chunk = f.read(chunkSize)
        with tqdm(total=fizeSize) as pbar:
            while chunk:
                file_hash.update(chunk)
                chunk = f.read(chunkSize)
                pbar.update(chunkSize)
    return file_hash.hexdigest()
