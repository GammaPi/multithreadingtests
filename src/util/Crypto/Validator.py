import hashlib


def sha256(filePath: str):
    with open(filePath, "rb") as f:
        file_hash = hashlib.sha256()
        chunkSize = 8192
        chunk = f.read(chunkSize)
        while chunk:
            file_hash.update(chunk)
            chunk = f.read(chunkSize)
    return file_hash.hexdigest()
