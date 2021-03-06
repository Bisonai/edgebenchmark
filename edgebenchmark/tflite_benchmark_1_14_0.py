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
from typing import Union

from edgebenchmark.edgebenchmark import EdgeBenchmark


class TFLiteBenchmark_1_14_0(EdgeBenchmark):
    @staticmethod
    def default():
        return {
            "num_runs": 50,
            "min_secs": 1,
            "run_delay": -1,
            "num_threads": 1,
            "benchmark_name": "",
            "output_prefix": "",
            "warmup_runs":  1,
            "warmup_min_secs": 0.5,
            "input_layer": "",
            "input_layer_shape": "",
            "use_nnapi":  False,
            "use_legacy_nnapi": False,
            "use_gpu": False,
            "allow_fp16": False,
            "enable_op_profiling": False,
        }

    @staticmethod
    def parameters():
        return {
            "num_runs": int,
            # "min_secs": int,
            "run_delay": int,
            "num_threads": int,
            "benchmark_name": str,
            "output_prefix": str,
            "warmup_runs": int,
            # "warmup_min_secs": float,
            "input_layer": str,
            "input_layer_shape": str,
            # "use_nnapi": bool,
            # "use_legacy_nnapi": bool,
            # "use_gpu": bool,
            "allow_fp16": bool,
            # "enable_op_profiling": bool,
        }

    @property
    def num_runs(self):
        """minimum number of runs, see also min_secs
        """
        return self.get_parameter("num_runs")

    @num_runs.setter
    def num_runs(self, value: int):
        if not isinstance(value, int):
            raise ValueError("num_runs must be type of int")
        self.set_parameter("num_runs", value)

    @property
    def min_secs(self):
        """minimum number of seconds to rerun for, potentially making
        the actual number of runs to be greater than num_runs
        """
        return self.get_parameter("min_secs")

    @min_secs.setter
    def min_secs(self, value: Union[int, float]):
        if isinstance(value, int):
            value = float(value)

        if isinstance(value, float):
            self.set_parameter("min_secs", value)
        else:
            raise ValueError("min_secs must be type of float")

    @property
    def run_delay(self):
        """delay between runs in seconds
        """
        return self.get_parameter("run_delay")

    @run_delay.setter
    def run_delay(self, value: Union[int, float]):
        if isinstance(value, int):
            value = float(value)

        if isinstance(value, float):
            self.set_parameter("run_delay", value)
        else:
            raise ValueError("run_delay must be type of float")

    @property
    def num_threads(self):
        """number of threads
        """
        return self.get_parameter("num_threads")

    @num_threads.setter
    def num_threads(self, value: int):
        if not isinstance(value, int):
            raise ValueError("num_threads must be type of int")
        self.set_parameter("num_threads", value)

    @property
    def benchmark_name(self):
        """benchmark name
        """
        return self.get_parameter("benchmark_name")

    @benchmark_name.setter
    def benchmark_name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("benchmark_name must be type of str")
        self.set_parameter("benchmark_name", value)

    @property
    def output_prefix(self):
        """benchmark output prefix
        """
        return self.get_parameter("output_prefix")

    @output_prefix.setter
    def output_prefix(self, value: str):
        if not isinstance(value, str):
            raise ValueError("output_prefix must be type of str")
        self.set_parameter("output_prefix", value)

    @property
    def warmup_runs(self):
        """minimum number of runs performed on initialization, to
        allow performance characteristics to settle, see also
        warmup_min_secs
        """
        return self.get_parameter("warmup_runs")

    @warmup_runs.setter
    def warmup_runs(self, value: int):
        if not isinstance(value, int):
            raise ValueError("warmup_runs must be type of int")
        self.set_parameter("warmup_runs", value)

    @property
    def warmup_min_secs(self):
        """minimum number of seconds to rerun for, potentially making
        the actual number of warm-up runs to be greater than
        warmup_runs
        """
        return self.get_parameter("warmup_min_secs")

    @warmup_min_secs.setter
    def warmup_min_secs(self, value: Union[int, float]):
        if isinstance(value, int):
            value = float(value)

        if isinstance(value, float):
            self.set_parameter("warmup_min_secs", value)
        else:
            raise ValueError("warmup_min_secs must be type of float")

    @property
    def input_layer(self):
        """input layer names
        """
        return self.get_parameter("input_layer")

    @input_layer.setter
    def input_layer(self, value: str):
        if not isinstance(value, str):
            raise ValueError("input_layer must be type of str")
        self.set_parameter("input_layer", value)

    @property
    def input_layer_shape(self):
        """input layer shape
        """
        return self.get_parameter("input_layer_shape")

    @input_layer_shape.setter
    def input_layer_shape(self, value: str):
        if not isinstance(value, str):
            raise ValueError("input_layer_shape must be type of str")
        self.set_parameter("input_layer_shape", value)

    @property
    def use_nnapi(self):
        """use nnapi delegate api
        """
        return self.get_parameter("use_nnapi")

    @use_nnapi.setter
    def use_nnapi(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("use_nnapi must be type of bool")
        self.set_parameter("use_nnapi", value)

    @property
    def use_legacy_nnapi(self):
        """nnapi legacy delegate api
        """
        return self.get_parameter("use_legacy_nnapi")

    @use_legacy_nnapi.setter
    def use_legacy_nnapi(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("use_legacy_nnapi must be type of bool")
        self.set_parameter("use_legacy_nnapi", value)

    @property
    def use_gpu(self):
        """use gpu
        """
        return self.get_parameter("use_gpu")

    @use_gpu.setter
    def use_gpu(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("use_gpu must be type of bool")
        self.set_parameter("use_gpu", value)

    @property
    def allow_fp16(self):
        """use fp16
        """
        return self.get_parameter("allow_fp16")

    @allow_fp16.setter
    def allow_fp16(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("allow_fp16 must be type of bool")
        self.set_parameter("allow_fp16", value)

    @property
    def enable_op_profiling(self):
        """enable op profiling
        """
        return self.get_parameter("enable_op_profiling")

    @enable_op_profiling.setter
    def enable_op_profiling(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("enable_op_profiling must be type of bool")
        self.set_parameter("enable_op_profiling", value)
