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
import sys
import requests
import json
import time
import hashlib
from pathlib import Path

from typing import (
    Dict,
    Optional,
    List,
    Tuple,
)


from edgebenchmark.settings import settings


class CredentialsFormatException(Exception):
    pass


def send_model(
        protocol_version: Tuple[int, int, int],
        token: str,
        model_path: Path,
        devices: List[str],
        features: Dict,
        benchmark_type,
        benchmark_version: str,
        benchmark_args: Dict,
):
    headers = {
        "Token": token,
    }

    data = {
        "protocol_version": json.dumps(protocol_version),
        "time": time.time(),
        "model_hash": md5_hash(filepath=model_path),
        "model_name": model_path.name,
        "devices": json.dumps(devices),
        "features": json.dumps(features),
        "benchmark_type": benchmark_type.value,
        "benchmark_version": benchmark_version,
        "benchmark_args": json.dumps(benchmark_args),
    }

    files = {
        "model_file": open(model_path, "rb"),
    }

    response = requests.put(
        settings._MODEL_ENDPOINT,
        headers=headers,
        files=files,
        data=data,
    )

    return response


def get_devices(
        protocol_version: Tuple[int, int, int],
        token: str,
):
    data = {
        "token": token,
        "protocol_version": protocol_version,
    }

    response = requests.get(
        settings._DEVICE_ENDPOINT,
        json=data,
    )

    return response


def md5_hash(
    data: bytes = None,
    filepath: Path = None,
    buffer_size: int = 65_536,
):
    """
    Compute secure hash (md5) of given bytes data.  It is used to
    identify differences of file before sending from client and after
    receiving at server.

    https://docs.python.org/3/library/hashlib.html

    Args:
      data: Bytes to hash.
      filepath: If filepath is given, file is loaded and encoded with
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


def load_token_from_file() -> Optional[str]:
    settings._CONFIGURE_DIR.mkdir(parents=True, exist_ok=True)

    if settings._CREDENTIALS_FILE_PATH.exists():
        with open(settings._CREDENTIALS_FILE_PATH, "r") as f:
            try:
                for line in f:
                    key, _, value = line.strip().split(" ")

                    if key == "edgebenchmark_token":
                        return value
            except Exception:
                print(
                    f"Invalid format of credentials file located at {settings._CONFIGURE_DIR}",
                    file=sys.stderr,
                )
                raise CredentialsFormatException
    else:
        print(
            f"{settings._CREDENTIALS_FILE_PATH} file does not exist.\n"
            "Set token with commmand: edgebenchmark configure",
            file=sys.stderr,
        )
        raise FileNotFoundError


def filter_dict(d: Dict):
    return dict(filter(lambda x: x[1], d.items()))
