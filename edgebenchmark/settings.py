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
from enum import Enum
from pathlib import Path


class settings:
    _MODEL_LIMIT_SIZE_MB = 30
    _PROTOCOL_VERSION = [0, 0, 1]

    _CONFIGURE_DIR = Path.home() / ".edgebenchmark"
    _CREDENTIALS_FILE_PATH = _CONFIGURE_DIR / "credentials"
    _TOKEN_LENGTH = 128
    _MODEL_ENDPOINT = "https://edgebenchmark.com/api/model"
    _DEVICE_ENDPOINT = "https://edgebenchmark.com/api/devices"

    _TFLITE_VERSIONS = [
        "1.13.1",
        "1.13.2",
        "1.14.0",
        "1.15.0",
        "1.15.2",
        "1.15.3",
        "1.15.4",
        "1.2.0",
        "1.2.1",
        "1.3.0",
        "1.3.1",
        "1.4.0",
        "1.4.1",
        "1.5.0",
        "1.5.1",
        "1.6.0",
        "1.7.0",
        "1.7.1",
        "1.8.0",
        "1.9.0",
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
    ]


class available_benchmarks(Enum):
    tflite_basic = 0
    tflite_profiling = 1
    ncnn = 2
