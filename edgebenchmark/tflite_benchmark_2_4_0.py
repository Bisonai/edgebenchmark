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


class TFLiteBenchmark_2_4_0(EdgeBenchmark):
    @staticmethod
    def default():
        return {
            "num_runs": 50,
            "min_secs": 1,
            "max_secs": 150,
            "run_delay": -1,
            "num_threads": 1,
            "use_caching": False,
            "benchmark_name": "",
            "output_prefix": "",
            "warmup_runs": 1,
            "warmup_min_secs": 0.5,
            "verbose": False,
            "input_layer": "",
            "input_layer_shape": "",
            "input_layer_value_range": "",
            "input_layer_value_files": "",
            "allow_fp16": False,
            "require_full_delegation": False,
            "enable_op_profiling": False,
            "max_profiling_buffer_entries": 1_024,
            "profiling_output_csv_file": "",
            "max_delegated_partitions": 0,
            "min_nodes_per_partition": 0,
            "external_delegate_path": "",
            "external_delegate_options": "",
            "use_gpu": False,
            "gpu_precision_loss_allowed": True,
            "gpu_experimental_enable_quant": True,
            "gpu_backend": "",
            "use_hexagon": False,
            "hexagon_lib_path": "/data/local/tmp",
            "hexagon_profiling": False,
            "use_nnapi": False,
            "nnapi_execution_preference": "",
            "nnapi_execution_priority": "",
            "nnapi_accelerator_name": "",
            "disable_nnapi_cpu": False,
            "nnapi_allow_fp16": False,
            "use_xnnpack": False,
        }

    @staticmethod
    def parameters():
        return {
            "num_runs": int,
            # "min_secs": int,
            "max_secs": int,
            "run_delay": int,
            "num_threads": int,
            "use_caching": bool,
            "benchmark_name": str,
            "output_prefix": str,
            "warmup_runs": int,
            # "warmup_min_secs": float,
            # "verbose": bool,
            "input_layer": str,
            "input_layer_shape": str,
            "input_layer_value_range": str,
            "input_layer_value_files": str,
            "allow_fp16": bool,
            # "require_full_delegation": bool,
            # "enable_op_profiling": bool,
            # "max_profiling_buffer_entries": int,
            # "profiling_output_csv_file": str,
            # "max_delegated_partitions": int,
            # "min_nodes_per_partition": int,
            # "external_delegate_path": str,
            # "external_delegate_options": str,
            # "use_gpu": bool,
            # "gpu_precision_loss_allowed": bool,
            # "gpu_experimental_enable_quant": bool,
            # "gpu_backend": str,
            # "use_hexagon": bool,
            # "hexagon_lib_path": str,
            # "hexagon_profiling": bool,
            # "use_nnapi": bool,
            # "nnapi_execution_preference": str,
            # "nnapi_execution_priority": str,
            # "nnapi_accelerator_name": str,
            # "disable_nnapi_cpu": bool,
            # "nnapi_allow_fp16": bool,
            # "use_xnnpack": bool,
        }

    @property
    def num_runs(self):
        """expected number of runs, see also min_secs, max_secs
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
    def max_secs(self):
        """maximum number of seconds to rerun for, potentially making
        the actual number of runs to be less than num_runs. Note if
        --max-secs is exceeded in the middle of a run, the benchmark
        will continue to the end of the run but will not start the
        next run.
        """
        return self.get_parameter("max_secs")

    @max_secs.setter
    def max_secs(self, value: Union[int, float]):
        if isinstance(value, int):
            value = float(value)

        if isinstance(value, float):
            self.set_parameter("max_secs", value)
        else:
            raise ValueError("max_secs must be type of float")

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
    def use_caching(self):
        """Enable caching of prepacked weights matrices in matrix
        multiplication routines. Currently implies the use of the Ruy
        library.
        """
        return self.get_parameter("use_caching")

    @use_caching.setter
    def use_caching(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("use_caching must be type of bool")
        self.set_parameter("use_caching", value)

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
    def verbose(self):
        """Whether to log parameters whose values are not set. By
        default, only log those parameters that are set by parsing
        their values from the commandline flags.
        """
        return self.get_parameter("verbose")

    @verbose.setter
    def verbose(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("verbose must be type of bool")
        self.set_parameter("verbose", value)

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
    def input_layer_value_range(self):
        """A map-like string representing value range for *integer*
        input layers. Each item is separated by ':', and the item
        value consists of input layer name and integer-only range
        values (both low and high are inclusive) separated by ',',
        e.g. input1,1,2:input2,0,254
        """
        return self.get_parameter("input_layer_value_range")

    @input_layer_value_range.setter
    def input_layer_value_range(self, value: str):
        if not isinstance(value, str):
            raise ValueError("input_layer_value_range must be type of str")
        self.set_parameter("input_layer_value_range", value)

    @property
    def input_layer_value_files(self):
        """A map-like string representing value file. Each item is
        separated by ',', and the item value consists of input layer
        name and value file path separated by ':',
        e.g. input1:file_path1,input2:file_path2. If the input_name
        appears both in input_layer_value_range and
        input_layer_value_files, input_layer_value_range of the
        input_name will be ignored.
        """
        return self.get_parameter("input_layer_value_files")

    @input_layer_value_files.setter
    def input_layer_value_files(self, value: str):
        if not isinstance(value, str):
            raise ValueError("input_layer_value_files must be type of str")
        self.set_parameter("input_layer_value_files", value)

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
    def require_full_delegation(self):
        """require delegate to run the entire graph
        """
        return self.get_parameter("require_full_delegation")

    @require_full_delegation.setter
    def require_full_delegation(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("require_full_delegation must be type of bool")
        self.set_parameter("require_full_delegation", value)

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

    @property
    def max_profiling_buffer_entries(self):
        """max profiling buffer entries
        """
        return self.get_parameter("max_profiling_buffer_entries")

    @max_profiling_buffer_entries.setter
    def max_profiling_buffer_entries(self, value: int):
        if not isinstance(value, int):
            raise ValueError(
                "max_profiling_buffer_entries must be type of int")
        self.set_parameter("max_profiling_buffer_entries", value)

    @property
    def profiling_output_csv_file(self):
        """File path to export profile data as CSV, if not set prints
        to stdout.
        """
        return self.get_parameter("profiling_output_csv_file")

    @profiling_output_csv_file.setter
    def profiling_output_csv_file(self, value: str):
        if not isinstance(value, str):
            raise ValueError("profiling_output_csv_file must be type of str")
        self.set_parameter("profiling_output_csv_file", value)

    @property
    def max_delegated_partitions(self):
        """Max partitions to be delegated.
        """
        return self.get_parameter("max_delegated_partitions")

    @max_delegated_partitions.setter
    def max_delegated_partitions(self, value: int):
        if not isinstance(value, int):
            raise ValueError("max_delegated_partitions must be type of int")
        self.set_parameter("max_delegated_partitions", value)

    @property
    def min_nodes_per_partition(self):
        """The minimal number of TFLite graph nodes of a partition
        that has to be reached for it to be delegated.A negative value
        or 0 means to use the default choice of each delegate.
        """
        return self.get_parameter("min_nodes_per_partition")

    @min_nodes_per_partition.setter
    def min_nodes_per_partition(self, value: int):
        if not isinstance(value, int):
            raise ValueError("min_nodes_per_partition must be type of int")
        self.set_parameter("min_nodes_per_partition", value)

    @property
    def external_delegate_path(self):
        """The library path for the underlying external.
        """
        return self.get_parameter("external_delegate_path")

    @external_delegate_path.setter
    def external_delegate_path(self, value: str):
        if not isinstance(value, str):
            raise ValueError("external_delegate_path must be type of str")
        self.set_parameter("external_delegate_path", value)

    @property
    def external_delegate_options(self):
        """Comma-separated options to be passed to the external delegate
        """
        return self.get_parameter("external_delegate_options")

    @external_delegate_options.setter
    def external_delegate_options(self, value: str):
        if not isinstance(value, str):
            raise ValueError("external_delegate_options must be type of str")
        self.set_parameter("external_delegate_options", value)

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
    def gpu_precision_loss_allowed(self):
        """Allow to process computation in lower precision than FP32
        in GPU. By default, it's enabled.
        """
        return self.get_parameter("gpu_precision_loss_allowed")

    @gpu_precision_loss_allowed.setter
    def gpu_precision_loss_allowed(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("gpu_precision_loss_allowed must be type of bool")
        self.set_parameter("gpu_precision_loss_allowed", value)

    @property
    def gpu_experimental_enable_quant(self):
        """Whether to enable the GPU delegate to run quantized models
        or not. By default, it's enabled.
        """
        return self.get_parameter("gpu_experimental_enable_quant")

    @gpu_experimental_enable_quant.setter
    def gpu_experimental_enable_quant(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError(
                "gpu_experimental_enable_quant must be type of bool")
        self.set_parameter("gpu_experimental_enable_quant", value)

    @property
    def gpu_backend(self):
        """Force the GPU delegate to use a particular backend for
        execution, and fail if unsuccessful. Should be one of: cl, gl
        """
        return self.get_parameter("gpu_backend")

    @gpu_backend.setter
    def gpu_backend(self, value: str):
        if not isinstance(value, str):
            raise ValueError("gpu_backend must be type of str")
        self.set_parameter("gpu_backend", value)

    @property
    def use_hexagon(self):
        """use nnapi delegate api
        """
        return self.get_parameter("use_hexagon")

    @use_hexagon.setter
    def use_hexagon(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("use_hexagon must be type of bool")
        self.set_parameter("use_hexagon", value)

    @property
    def hexagon_lib_path(self):
        """The library path for the underlying Hexagon libraries.
        """
        return self.get_parameter("hexagon_lib_path")

    @hexagon_lib_path.setter
    def hexagon_lib_path(self, value: str):
        if not isinstance(value, str):
            raise ValueError("hexagon_lib_path must be type of str")
        self.set_parameter("hexagon_lib_path", value)

    @property
    def hexagon_profiling(self):
        """Enables Hexagon profiling
        """
        return self.get_parameter("hexagon_profiling")

    @hexagon_profiling.setter
    def hexagon_profiling(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("hexagon_profiling must be type of bool")
        self.set_parameter("hexagon_profiling", value)

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
    def nnapi_execution_preference(self):
        """execution preference for nnapi delegate. Should be one of
        the following: fast_single_answer, sustained_speed, low_power,
        undefined
        """
        return self.get_parameter("nnapi_execution_preference")

    @nnapi_execution_preference.setter
    def nnapi_execution_preference(self, value: str):
        if not isinstance(value, str):
            raise ValueError("nnapi_execution_preference must be type of str")
        self.set_parameter("nnapi_execution_preference", value)

    @property
    def nnapi_execution_priority(self):
        """The model execution priority in nnapi, and it should be one
        of the following: default, low, medium and high. This requires
        Android 11+.
        """
        return self.get_parameter("nnapi_execution_priority")

    @nnapi_execution_priority.setter
    def nnapi_execution_priority(self, value: str):
        if not isinstance(value, str):
            raise ValueError("nnapi_execution_priority must be type of str")
        self.set_parameter("nnapi_execution_priority", value)

    @property
    def nnapi_accelerator_name(self):
        """the name of the nnapi accelerator to use (requires Android Q+)
        """
        return self.get_parameter("nnapi_accelerator_name")

    @nnapi_accelerator_name.setter
    def nnapi_accelerator_name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("nnapi_accelerator_name must be type of str")
        self.set_parameter("nnapi_accelerator_name", value)

    @property
    def disable_nnapi_cpu(self):
        """Disable the NNAPI CPU device
        """
        return self.get_parameter("disable_nnapi_cpu")

    @disable_nnapi_cpu.setter
    def disable_nnapi_cpu(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("disable_nnapi_cpu must be type of bool")
        self.set_parameter("disable_nnapi_cpu", value)

    @property
    def nnapi_allow_fp16(self):
        """Allow fp32 computation to be run in fp16
        """
        return self.get_parameter("nnapi_allow_fp16")

    @nnapi_allow_fp16.setter
    def nnapi_allow_fp16(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("nnapi_allow_fp16 must be type of bool")
        self.set_parameter("nnapi_allow_fp16", value)

    @property
    def use_xnnpack(self):
        """use XNNPack
        """
        return self.get_parameter("use_xnnpack")

    @use_xnnpack.setter
    def use_xnnpack(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("use_xnnpack must be type of bool")
        self.set_parameter("use_xnnpack", value)
