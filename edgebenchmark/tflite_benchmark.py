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
from edgebenchmark.tflite_benchmark_1_14_0 import TFLiteBenchmark_1_14_0
from edgebenchmark.tflite_benchmark_1_15_0 import TFLiteBenchmark_1_15_0
from edgebenchmark.tflite_benchmark_2_0_0 import TFLiteBenchmark_2_0_0
from edgebenchmark.tflite_benchmark_2_1_0 import TFLiteBenchmark_2_1_0
from edgebenchmark.tflite_benchmark_2_2_0 import TFLiteBenchmark_2_2_0
from edgebenchmark.tflite_benchmark_2_3_0 import TFLiteBenchmark_2_3_0
from edgebenchmark.tflite_benchmark_2_4_0 import TFLiteBenchmark_2_4_0


def TFLiteBenchmark(version: int):
    """
    """
    assert version in settings._TFLITE_VERSIONS

    if version in ("1.14.0"):
        b = TFLiteBenchmark_1_14_0
    elif version in ("1.15.0", "1.15.2", "1.15.3", "1.15.4"):
        b = TFLiteBenchmark_1_15_0
    elif version in ("2.0.0", "2.0.1", "2.0.2", "2.0.3"):
        b = TFLiteBenchmark_2_0_0
    elif version in ("2.1.0", "2.1.1", "2.1.2"):
        b = TFLiteBenchmark_2_1_0
    elif version in ("2.2.0", "2.2.1"):
        b = TFLiteBenchmark_2_2_0
    elif version in ("2.3.0"):
        b = TFLiteBenchmark_2_3_0
    elif version in ("2.4.0", "2.4.1"):
        b = TFLiteBenchmark_2_4_0
    else:
        raise ValueError(f"Invalid TFLite version number. Choose one of {settings._TFLITE_VERSIONS}")

    benchmark = b(version)
    benchmark.benchmark_type = available_benchmarks.tflite_basic
    return benchmark
