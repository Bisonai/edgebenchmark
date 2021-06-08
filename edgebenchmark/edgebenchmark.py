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
import json
import logging
from abc import ABC
from pathlib import Path
from typing import List
from typing import Tuple
from typing import Dict
from typing import Union
from typing import Any

from edgebenchmark.utils import send_model
from edgebenchmark.utils import load_token_from_file
from edgebenchmark.utils import CredentialsFormatException
from edgebenchmark.settings import settings
from edgebenchmark.custom_types import verify_model_file


class EdgeBenchmark(ABC):
    def __init__(self, version: int):
        self.version = version

        self._devices = ["all"]
        self._protocol_version = settings._PROTOCOL_VERSION
        self._features = {}
        self._args = {}

        try:
            self._token = load_token_from_file()
        except (FileNotFoundError, CredentialsFormatException):
            sys.exit(1)

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value: str):
        if not isinstance(value, str):
            value = str(value)
        self._version = value

    @property
    def devices(self):
        return self._devices

    @devices.setter
    def devices(self, value: List[str]):
        if not isinstance(value, Tuple):
            value = list(value)
        elif not isinstance(value, List):
            raise ValueError(
                "Device names have to be stored inside of List or Tuple type")

        self._devices = value

    @property
    def features(self):
        return self._features

    @features.setter
    def features(self, value):
        if isinstance(value, str):
            value = json.loads(value)
        elif not isinstance(value, Dict):
            raise ValueError(
                "Features have to stored in Dict or as a str type")

        self._features = value

    @property
    def args(self):
        return self._args

    def run(self, model_path: Union[Path, str]):
        model_path = verify_model_file(model_path)

        response = send_model(
            self._protocol_version,
            self._token,
            model_path,
            self.devices,
            self.features,
            self.benchmark_type,
            self.version,
            self.args,
        )

        if response.status_code != 200:
            response_msg = json.loads(response.content.decode("ascii"))["msg"]
            logging.debug(response_msg, file=sys.stderr)
        else:
            print("Model was successfuly sent for benchmarking. Please check the benchmarking result through https://edgebenchmark.com/app website")

    def help(self):
        """Print all supported parameters
        """
        padding = max(
            list(map(lambda x: len(x[0]), self.parameters().items())))
        for name, type in self.parameters().items():
            print(name.ljust(padding, " "), type)

    def supported(self, parameter_name: str):
        """Find out if `parameter_name` is supported.

        Args:
          parameter_name: name of parameter

        Raise:
          NameError: raise exception if `parameter_name` is not supported
        """
        if not any(list(map(lambda x: x[0] == parameter_name, self.parameters().items()))):
            raise NameError(f"{parameter_name} is not supported")

    @staticmethod
    def parameters():
        raise NotImplementedError

    @staticmethod
    def default():
        raise NotImplementedError

    def get_parameter(self, name: str):
        self.supported(name)
        return self._args[name]

    def set_parameter(self, name: str, value: Any):
        self.supported(name)
        self._args[name] = value
