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
import os
from enum import Enum
from pathlib import Path


class settings:
    _MODEL_LIMIT_SIZE_MB = 30
    _PROTOCOL_VERSION = [0, 0, 2]

    _CONFIGURE_DIR = Path.home() / ".edgebenchmark"
    _CREDENTIALS_FILE_PATH = _CONFIGURE_DIR / "credentials"
    _TOKEN_LENGTH = 128
    _WEB_SERVER_URL = "https://edgebenchmark.com" if not os.environ.get("EDGEBENCHMARK_DRY_RUN") else "http://localhost"
    _MODEL_ENDPOINT = f"{_WEB_SERVER_URL}/api/model"
    _DEVICE_ENDPOINT = f"{_WEB_SERVER_URL}/api/devices"

    _NCNN_VERSIONS = [
        "20210124",
    ]

    _TFLITE_VERSIONS = [
        "1.14.0",
        "1.15.0",
        "1.15.2",
        "1.15.3",
        "1.15.4",
        "2.0.0",
        "2.0.1",
        "2.0.2",
        "2.0.3",
        "2.1.0",
        "2.1.1",
        "2.1.2",
        "2.2.0",
        "2.2.1",
        "2.3.0",
        "2.3.1",
        "2.4.0",
        "2.4.1",
    ]


class available_benchmarks(Enum):
    tflite_basic = 1
    tflite_profiling = 2
    ncnn_basic = 3
    ncnn_profiling = 4
