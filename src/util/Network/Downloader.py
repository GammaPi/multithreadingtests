import urllib3
import os
import glog as log
import pathlib

from tqdm import tqdm

from exception.TestException import MTException


def download(url: str, dir: str, fileName: str, verifier: callable):
    log.info('Downloading %s to %s' % (url, os.path.join(dir, fileName)))
    # Verify the existence first.
    if os.path.exists(os.path.join(dir, fileName)):
        log.info('%s already exists' % (fileName))
        if verifier is None:
            log.info('No validator, assume validation succeeded')
        else:
            log.info('Validating file..')
            if verifier(os.path.join(dir, fileName)):
                log.info('%s validation passed, no need to download' % (os.path.join(dir, fileName)))
                return
            else:
                log.info('%s validation failed, re-download' % (os.path.join(dir, fileName)))

    os.makedirs(dir, exist_ok=True)
    http = urllib3.PoolManager()
    r = http.request("GET", url, preload_content=False)
    totalSize = r.headers['Content-Length']
    curSize = 0
    chunkSize = 1024 * 1024
    with open(os.path.join(dir, fileName), 'wb') as f:
        with tqdm(total=totalSize) as pbar:
            while True:
                data = r.read(chunkSize)
                if not data:
                    break
                f.write(data)
                pbar.update(len(data))
    if verifier and not verifier(os.path.join(dir, fileName)):
        raise MTException('File %s validation failed' % (os.path.join(dir, fileName)))
