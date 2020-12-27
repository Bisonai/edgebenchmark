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
from typing import Dict
from typing import Tuple
from typing import Any
from pathlib import Path

import click

from edgebenchmark.utils import send_model
from edgebenchmark.utils import get_devices
from edgebenchmark.utils import load_token_from_file
from edgebenchmark.settings import available_benchmarks
from edgebenchmark.settings import settings
from edgebenchmark.custom_types import ModelPathType
from edgebenchmark.custom_types import FeaturesType
from edgebenchmark.custom_types import verify_token_size


@click.group()
def cli_configure():
    pass

@cli_configure.command()
def configure():
    try:
        current_token = load_token_from_file()
        token_placeholder = current_token[:3] + 3 * "*" + current_token[-3:]
    except FileNotFoundError:
        current_token = ""
        token_placeholder = "None"

    try:
        token = click.prompt(
            f"Edge Benchmark Token [{token_placeholder}]",
            type=str,
            show_default=False,
            default=current_token,
            value_proc=verify_token_size,
        )
    except ValueError as e:
        print(f"Edge Benchmark Token must have exactly {settings._TOKEN_LENGTH} characters. Please use valid token.")
        sys.exit(1)

    if token != "":
        with open(settings._CONFIGURE_DIR / "credentials", "w") as f:
            f.write(f"edgebenchmark_token = {token}\n")


def common_benchmark_options(fn):
    fn = click.option("--model_path", required=True, type=ModelPathType)(fn)
    fn = click.option("--device", "-d", default=["all"], type=str, multiple=True)(fn) # TODO custom check
    fn = click.option("--features", type=FeaturesType, default="{}")(fn)
    return fn


@click.group()
def cli_tflite():
    pass


@cli_tflite.command()
@common_benchmark_options
@click.option("--num_threads", type=int, default=1)
@click.option("--warmup_runs", type=int, default=1)
@click.option("--num_runs", type=int, default=50)
@click.option("--run_delay", type=float, default=-1.0)
@click.option("--use_nnapi/--no-use_nnapi", default=False)
@click.option("--use_legacy_nnapi/--no-use_legacy_nnapi", default=False)
@click.option("--use_gpu/--no-use_gpu", default=False)
@click.option("--version", default=settings._TFLITE_VERSIONS[-1], type=click.Choice(settings._TFLITE_VERSIONS, case_sensitive=True))
def tflite(model_path, device, features, num_threads, warmup_runs, num_runs, run_delay, use_nnapi, use_legacy_nnapi, use_gpu, version):
    args = {
        "num_threads": num_threads,
        "warmup_runs": warmup_runs,
        "num_runs": num_runs,
        "run_delay": run_delay,
        "use_nnapi": use_nnapi,
        "use_legacy_nnapi": use_legacy_nnapi,
        "use_gpu": use_gpu,
    }

    benchmark(
        model_path,
        device,
        features,
        available_benchmarks.tflite_basic,
        version,
        args,
    )


# @click.group()
# def cli_ncnn():
    # pass


# @cli_ncnn.command()
# @common_benchmark_options
# def ncnn(model_path, devices, features):
    # args = {}

    # benchmark(
    #     model_path,
    #     devices,
    #     features,
    #     available_benchmarks.ncnn,
    #     args,
    # )


@click.group()
def cli_devices():
    pass


@cli_devices.command()
def devices():
    import requests

    token = load_token_from_file()

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


def benchmark(
        model_path: Path,
        devices: Tuple[str],
        features: str,
        benchmark_type,
        benchmark_version: str,
        args: Dict[str, Any],
):
    token = load_token_from_file()

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
        response_msg = json.loads(response.content.decode("ascii"))["msg"]
        print(response_msg, file=sys.stderr)
        sys.exit(1)
    else:
        print("Model was successfuly sent for benchmarking. Please check the benchmarking result through https://edgebenchmark.com/app website")


cli = click.CommandCollection(sources=[cli_configure, cli_tflite, cli_devices])


if __name__ == "__main__":
    cli()
