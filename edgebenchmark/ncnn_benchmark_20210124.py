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
from edgebenchmark.edgebenchmark import EdgeBenchmark


class NcnnBenchmark_20210124(EdgeBenchmark):
    @staticmethod
    def default():
        return {
            "loop_count": 4,
            "num_threads": -1,
            "powersave": 0,
            "gpu_device": -1,
            "cooling_down": 1,

            "height": 227,
            "width": 227,
            "channels": 3,
        }

    @staticmethod
    def parameters():
        return {
            "loop_count": int,
            "num_threads": int,
            "powersave": int,
            "gpu_device": int,
            "cooling_down": int,
            "height": int,
            "width": int,
            "channels": int,
        }

    @property
    def loop_count(self):
        """
        """
        return self.get_parameter("loop_count")

    @loop_count.setter
    def loop_count(self, value: int):
        if not isinstance(value, int):
            raise ValueError("loop_count must be type of int")
        self.set_parameter("loop_count", value)

    @property
    def num_threads(self):
        """
        -1=max_cpu_count
        """
        return self.get_parameter("num_threads")

    @num_threads.setter
    def num_threads(self, value: int):
        if not isinstance(value, int):
            raise ValueError("num_threads must be type of int")
        self.set_parameter("num_threads", value)

    @property
    def powersave(self):
        """
        0=all cores
        1=little cores only
        2=big cores only
        """
        return self.get_parameter("powersave")

    @powersave.setter
    def powersave(self, value: int):
        if not isinstance(value, int):
            raise ValueError("powersave must be type of int")
        self.set_parameter("powersave", value)

    @property
    def gpu_device(self):
        """
        -1=cpu-only
        0=gpu0
        1=gpu1
        ...
        """
        return self.get_parameter("gpu_device")

    @gpu_device.setter
    def gpu_device(self, value: int):
        if not isinstance(value, int):
            raise ValueError("gpu_device must be type of int")
        self.set_parameter("gpu_device", value)

    @property
    def cooling_down(self):
        """
        0=disable
        1=enable
        """
        return self.get_parameter("cooling_down")

    @cooling_down.setter
    def cooling_down(self, value: int):
        if not isinstance(value, int):
            raise ValueError("cooling_down must be type of int")
        self.set_parameter("cooling_down", value)
