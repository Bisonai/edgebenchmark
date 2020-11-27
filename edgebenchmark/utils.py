# Copyright 2020 Bisonai Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import requests
import json
import time
import logging
import hashlib
from pathlib import Path

from typing import Tuple
from typing import List
from typing import Dict


def send_model(
        protocol_version: Tuple[int, int, int],
        token: str,
        model_path: Path,
        devices: List[str],
        features: Dict,
        benchmark_type,
        benchmark_args: Dict,
):
    from edgebenchmark.settings import settings

    header = {
        "token": token,
        "protocol_version": json.dumps(protocol_version),
    }

    body = {
        "time": time.time(),
        "model_hash": md5_hash(filepath=model_path),
        "model_name": model_path.name,
        "devices": devices,
        "features": features,
        "benchmark_type": benchmark_type.value,
        "benchmark_args": benchmark_args,
    }

    files = {
        "json": json.dumps({
            "header": header,
            "body": body,
        }),
        "model_file": open(model_path, "rb"),
    }

    response = requests.put(
        settings._MODEL_ENDPOINT,
        files=files,
    )

    return response


def md5_hash(
    data: bytes=None,
    filepath: Path=None,
    buffer_size: int=65_536,
):
    """
    Compute secure hash (md5) of given bytes data.  It is used to
    identify differences of file before sending from client and after
    receiving at server.

    https://docs.python.org/3/library/hashlib.html

    Args:
      data: Bytes to hash.
      filepath: If filepath is given,  file is loaded and encoded with
      hash function.
      buffer_size: Size of a buffer that is used during data hashing.
    """
    if filepath is not None:
        with open(filepath, "rb") as f:
            data = b"".join(f.readlines())

    md5 = hashlib.md5()
    for idx in range(0, len(data), buffer_size):
        md5.update(data[idx:idx+buffer_size])
    return md5.hexdigest()


def load_token_from_file():
    from edgebenchmark.settings import settings

    settings._CONFIGURE_DIR.mkdir(parents=True, exist_ok=True)

    if settings._CREDENTIALS_FILE_PATH.exists():
        with open(settings._CREDENTIALS_FILE_PATH, "r") as f:
            try:
                for line in f:
                    key, _, value = line.strip().split(" ")

                    if key == "edgebenchmark_token":
                        return value
            except Exception as e:
                print(f"Invalid format of credentials file located at {settings._CONFIGURE_DIR}", file=sys.stderr)
                sys.exit(1)
    else:
        raise FileNotFoundError
