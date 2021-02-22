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
from edgebenchmark.settings import settings
from edgebenchmark.settings import available_benchmarks
from edgebenchmark.ncnn_benchmark_20210124 import NcnnBenchmark_20210124


def NcnnBenchmark(version: int):
    """
    """
    assert version in settings._NCNN_VERSIONS

    if version in ("20210124"):
        b = NcnnBenchmark_20210124
    else:
        raise ValueError(f"Invalid Ncnn version number. Choose one of {settings._NCNN_VERSIONS}")

    benchmark = b(version)
    benchmark.benchmark_type = available_benchmarks.ncnn_basic
    return benchmark
