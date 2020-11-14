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
import json
from abc import ABC
from abc import abstractmethod
from pathlib import Path
from typing import List
from typing import Tuple
from typing import Dict
from typing import Union

from edgebenchmark.utils import send_model
from edgebenchmark.utils import load_token_from_file
from edgebenchmark.settings import settings
from edgebenchmark.settings import available_benchmarks
from edgebenchmark.custom_types import verify_model_file


class EdgeBenchmark(ABC):
    def __init__(self):
        self._devices = ["all"]
        self._protocol_version = settings._PROTOCOL_VERSION
        self._features = {}
        self._args = self.default_args()

        try:
            self._token = load_token_from_file()
        except FileNotFoundError:
            print(f"{settings._CREDENTIALS_FILE_PATH} file does not exist.\n"
                  f"Set token with commmand: edgebenchmark configure",
                  file=sys.stderr)
            sys.exit(1)

    @property
    def devices(self):
        return self._devices

    @devices.setter
    def devices(self, value: List[str]):
        # TODO check device availability
        if not isinstance(value, Tuple):
            values = list(value)
        elif not isinstance(value, List):
            raise ValueError("Device names have to be stored inside of List or Tuple type")

        self._devices = value

    @property
    def features(self):
        return self._features

    @features.setter
    def features(self, value):
        if isinstance(value, str):
            features = json.loads(value)
        elif not isinstance(value, Dict):
            raise ValueError("Features have to stored in Dict or as a str type")

        self._feautures = value

    def run(self, model_path: Union[Path, str]):
        model_path = verify_model_file(model_path)

        response = send_model(
            self._protocol_version,
            self._token,
            model_path,
            self.devices,
            self.features,
            self.benchmark_type,
            self.args,
        )

    @property
    def args(self):
        return self._args

    @property
    @abstractmethod
    def benchmark_type(self):
        return None


class TFLiteBenchmark(EdgeBenchmark):
    def default_args(self):
        return {
            "num_threads": 1,
            "warmup_runs":  1,
            "num_runs": 50,
            "run_delay": -1.0,
            "use_nnapi": False,
            "use_legacy_nnapi": False,
            "use_gpu": False,
        }

    @property
    def benchmark_type(self):
        return available_benchmarks.tflite_basic

    @property
    def num_threads(self):
        return self._args["num_threads"]

    @num_threads.setter
    def num_threads(self, value: int):
        if not isinstance(value, int):
            raise ValueError("num_threads must be type of int")

        self._args["num_threads"] = value

    @property
    def warmup_runs(self):
        return self._args["warmup_runs"]

    @warmup_runs.setter
    def warmup_runs(self, value: int):
        if not isinstance(value, int):
            raise ValueError("warmup_runs must be type of int")

        self._args["warmup_runs"] = value

    @property
    def num_runs(self):
        return self._args["num_runs"]

    @num_runs.setter
    def num_runs(self, value: int):
        if not isinstance(value, int):
            raise ValueError("num_runs must be type of int")

        self._args["num_runs"] = value

    @property
    def run_delay(self):
        return self._args["run_delay"]

    @run_delay.setter
    def run_delay(self, value: float):
        if not isinstance(value, float):
            raise ValueError("run_delay must be type of float")

        self._args["run_delay"] = value

    @property
    def use_nnapi(self):
        return self._args["use_nnapi"]

    @use_nnapi.setter
    def use_nnapi(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("use_nnapi must be type of bool")

        self._args["use_nnapi"] = value

    @property
    def use_legacy_nnapi(self):
        return self._args["use_legacy_nnapi"]

    @use_legacy_nnapi.setter
    def use_legacy_nnapi(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("use_legacy_nnapi must be type of bool")

        self._args["use_legacy_nnapi"] = value

    @property
    def use_gpu(self):
        return self._args["use_gpu"]

    @use_gpu.setter
    def use_gpu(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("use_gpu must be type of bool")

        self._args["use_gpu"] = value


class NCNNBenchmark(EdgeBenchmark):
    def default_args(self):
        return {}

    @property
    def benchmark_type(self):
        return available_benchmarks.ncnn
