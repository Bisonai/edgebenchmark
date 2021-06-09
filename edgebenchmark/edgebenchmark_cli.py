# Copyright 2021 Bisonai Authors. All Rights Reserved.
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
from typing import Dict
from typing import Tuple
from typing import Any
from pathlib import Path

import click

from edgebenchmark.utils import send_model
from edgebenchmark.utils import get_devices
from edgebenchmark.utils import load_token_from_file
from edgebenchmark.utils import CredentialsFormatException
from edgebenchmark.settings import available_benchmarks
from edgebenchmark.settings import settings
from edgebenchmark.custom_types import ModelPathType
from edgebenchmark.custom_types import FeaturesType
from edgebenchmark.custom_types import verify_token_size
from edgebenchmark.utils import filter_dict

from edgebenchmark.tflite_benchmark import TFLiteBenchmark_1_14_0
from edgebenchmark.tflite_benchmark import TFLiteBenchmark_1_15_0
from edgebenchmark.tflite_benchmark import TFLiteBenchmark_2_0_0
from edgebenchmark.tflite_benchmark import TFLiteBenchmark_2_1_0
from edgebenchmark.tflite_benchmark import TFLiteBenchmark_2_2_0
from edgebenchmark.tflite_benchmark import TFLiteBenchmark_2_3_0
from edgebenchmark.tflite_benchmark import TFLiteBenchmark_2_4_0

from edgebenchmark.ncnn_benchmark import NcnnBenchmark_20210124


@click.group()
def cli_configure():
    pass


@click.group()
def cli_devices():
    pass


@click.group()
def cli_tflite():
    pass


@click.group()
def cli_ncnn():
    pass


@cli_configure.command()
def configure():
    token_placeholder = "None"

    try:
        current_token = load_token_from_file()
        if current_token:
            token_placeholder = current_token[:3] + 3 * "*" + current_token[-3:]
    except FileNotFoundError:
        current_token = ""

    try:
        token = click.prompt(
            f"Edge Benchmark Token [{token_placeholder}]",
            type=str,
            show_default=False,
            default=current_token,
            value_proc=verify_token_size,
        )
    except ValueError:
        print(f"Edge Benchmark Token must have exactly {settings._TOKEN_LENGTH} characters. Please use valid token.")
        sys.exit(1)

    if token != "":
        with open(settings._CONFIGURE_DIR / "credentials", "w") as f:
            f.write(f"edgebenchmark_token = {token}\n")


@cli_devices.command()
def devices():
    try:
        token = load_token_from_file()
    except (FileNotFoundError, CredentialsFormatException):
        sys.exit(1)

    response = get_devices(
        settings._PROTOCOL_VERSION,
        token,
    )

    if response.status_code != 200:
        response_msg = json.loads(response.content.decode("ascii"))["msg"]
        print(response_msg, file=sys.stderr)
        sys.exit(1)

    response_data = json.loads(response.content.decode("ascii"))["data"]
    for d in response_data:
        print(d)


def common_benchmark_options(fn):
    fn = click.option("--model_path", required=True, type=ModelPathType)(fn)
    fn = click.option("--device", "-d", default=["all"], type=str, multiple=True)(fn) # TODO custom check
    fn = click.option("--features", type=FeaturesType, default="{}")(fn)
    return fn


def tflite_options(TFLiteBenchmark_class):
    def wrapper(fn):
        for name, type in TFLiteBenchmark_class.parameters().items():
            fn = click.option(f"--{name}", type=type)(fn)
        return fn

    return wrapper


@cli_tflite.group()
def tflite():
    pass


@tflite.command("1.14.0")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_1_14_0)
def tflite_1_14_0(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "1.14.0",
        benchmark_args,
    )


@tflite.command("1.15.0")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_1_15_0)
def tflite_1_15_0(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "1.15.0",
        benchmark_args,
    )


@tflite.command("1.15.2")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_1_15_0)
def tflite_1_15_2(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "1.15.2",
        benchmark_args,
    )


@tflite.command("1.15.3")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_1_15_0)
def tflite_1_15_3(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "1.15.3",
        benchmark_args,
    )


@tflite.command("1.15.4")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_1_15_0)
def tflite_1_15_4(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "1.15.4",
        benchmark_args,
    )


@tflite.command("2.0.0")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_2_0_0)
def tflite_2_0_0(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "2.0.0",
        benchmark_args,
    )


@tflite.command("2.0.1")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_2_0_0)
def tflite_2_0_1(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "2.0.1",
        benchmark_args,
    )


@tflite.command("2.0.2")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_2_0_0)
def tflite_2_0_2(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "2.0.2",
        benchmark_args,
    )


@tflite.command("2.0.3")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_2_0_0)
def tflite_2_0_3(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "2.0.3",
        benchmark_args,
    )


@tflite.command("2.1.0")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_2_1_0)
def tflite_2_1_0(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "2.1.0",
        benchmark_args,
    )


@tflite.command("2.1.1")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_2_1_0)
def tflite_2_1_1(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "2.1.1",
        benchmark_args,
    )


@tflite.command("2.1.2")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_2_1_0)
def tflite_2_1_2(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "2.1.2",
        benchmark_args,
    )


@tflite.command("2.2.0")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_2_2_0)
def tflite_2_2_0(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "2.2.0",
        benchmark_args,
    )


@tflite.command("2.2.1")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_2_2_0)
def tflite_2_2_1(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "2.2.1",
        benchmark_args,
    )


@tflite.command("2.3.0")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_2_3_0)
def tflite_2_3_0(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "2.3.0",
        benchmark_args,
    )


@tflite.command("2.4.0")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_2_4_0)
def tflite_2_4_0(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "2.4.0",
        benchmark_args,
    )


@tflite.command("2.4.1")
@common_benchmark_options
@tflite_options(TFLiteBenchmark_2_4_0)
def tflite_2_4_1(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        "2.4.1",
        benchmark_args,
    )


def ncnn_options(NcnnBenchmark_class):
    def wrapper(fn):
        for name, type in NcnnBenchmark_class.parameters().items():
            fn = click.option(f"--{name}", type=type)(fn)
        return fn

    return wrapper


@cli_ncnn.group()
def ncnn():
    pass


@ncnn.command("20210124")
@common_benchmark_options
@ncnn_options(NcnnBenchmark_20210124)
def ncnn_20210124(model_path, device, features, **benchmark_args):
    benchmark_args = filter_dict(benchmark_args)

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.ncnn_basic,
        "20210124",
        benchmark_args,
    )


def benchmark(
        model_path: Path,
        devices: Tuple[str],
        features: str,
        benchmark_type,
        benchmark_version: str,
        args: Dict[str, Any],
):
    try:
        token = load_token_from_file()
    except (FileNotFoundError, CredentialsFormatException):
        sys.exit(1)

    response = send_model(
        settings._PROTOCOL_VERSION,
        token,
        model_path,
        devices,
        features,
        benchmark_type,
        benchmark_version,
        args,
    )

    if response.status_code != 200:
        try:
            response_msg = json.loads(response.content.decode("ascii"))["msg"]
            print(response_msg, file=sys.stderr)
            sys.exit(1)
        except Exception:
            print("Unexpected error", file=sys.stderr)
            sys.exit(1)
    else:
        print("Model was successfuly sent for benchmarking. Please check the benchmarking result through https://edgebenchmark.com/app website")


cli = click.CommandCollection(sources=[cli_configure, cli_devices, cli_tflite, cli_ncnn])


if __name__ == "__main__":
    cli()
