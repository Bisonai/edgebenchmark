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
from typing import Union
from pathlib import Path
import math
import json

import click

from edgebenchmark.settings import settings


class ModelPathClass(click.ParamType):
    name = "model_path"

    def convert(self, value, param, ctx):
        model_path = Path(value)

        if not model_path.exists():
            self.fail(f"Model file not found at {value!r}", param, ctx)

        model_size_MB = math.ceil(model_path.stat().st_size / 1_024 / 1_024)

        if model_size_MB > settings._MODEL_LIMIT_SIZE_MB:
            self.fail(f"Size of {value!r} is larger than {settings._MODEL_LIMIT_SIZE_MB}", param, ctx)

        return model_path

ModelPathType = ModelPathClass()


class FeaturesClass(click.ParamType):
    name = "features"

    def convert(self, value, param, ctx):
        features = value.replace("'", "\"")

        try:
            features = json.loads(features)
        except json.decoder.JSONDecodeError:
            self.fail(f"Invalid JSON format", param, ctx)

        return features


FeaturesType = FeaturesClass()


def verify_token_size(value):
    if len(value) != settings._TOKEN_LENGTH:
        raise ValueError
    else:
        return value


def verify_model_file(model_path: Union[Path, str]):
    if not isinstance(model_path, Path):
        model_path = Path(model_path)
    else:
        raise ValueError("model_path must be str or Path")

    if not model_path.exists():
        raise FileNotFoundError("Model file not found at {model_path}")

    model_size_MB = math.ceil(model_path.stat().st_size / 1_024 / 1_024)

    if model_size_MB > settings._MODEL_LIMIT_SIZE_MB:
        raise RuntimeError(f"Size of {value} is larger than {settings._MODEL_LIMIT_SIZE_MB}")

    return model_path
