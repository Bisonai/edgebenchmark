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
    _PROTOCOL_VERSION = (0, 0, 1)

    # TODO receive devices from server?
    # e.g. edgebenchmark.com/devices/get
    _AVAILABLE_DEVICES=[
        "all",

        "OnePlus6t",
        "SamsungGalaxyNote3",
    ]

    _CONFIGURE_DIR = Path.home() / ".edgebenchmark"
    _CREDENTIALS_FILE_PATH = _CONFIGURE_DIR / "credentials"
    _TOKEN_LENGTH = 128
    _MODEL_ENDPOINT = "http://52.231.69.96/api/model"


class available_benchmarks(Enum):
    tflite_basic = 0
    tflite_profiling = 1
    ncnn = 2
