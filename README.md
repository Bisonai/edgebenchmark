# Edge Benchmark

Measure the speed of your machine learning models on real devices!

## Installation

```bash
pip install edgebenchmark
```

## First Use

Before you can use Edge Benchmark, register at [https://edgebenchmark.com/app#/register](https://edgebenchmark.com/app#/register) and generate your secret token in profiel section.

Then, run following command

```bash
edgebenchmark configure
```

and insert your secret token when you see prompt as shown below.

```bash
Edge Benchmark Token [None]:
```

Your secret token is saved at `~/.edgebenchmark/token`.

## Edge Benchmark Usage

Edge Benchmark can be either used directly from command line with `edgebenchmark` command, or from Python script.

### Edge Benchmark CLI

Edge Benchmark CLI tool offers several commands: `configure`, `ncnn` and `tflite`.

```bash
edgebenchmark --help
```

```bash
Usage: edgebenchmark [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  configure
  ncnn
  tflite
```

`configure` command is explained in the [First use](https://github.com/bisonai/edgebenchmark#first-use) section.

`tflite` command is for benchmarking the speed of TensorFlow Lite models.
You can setup many parameters to control the benchmarking process and also select devices (`--devices`) which you want to benchmark with.
Below, you can see all options for `tflite` command.

```
edgebenchmark tflite --help
Usage: edgebenchmark tflite [OPTIONS]

Options:
  --features FEATURES
  -d, --devices TEXT              [required]
  --model_path MODEL_PATH         [required]
  --num_threads INTEGER
  --warmup_runs INTEGER
  --num_runs INTEGER
  --run_delay FLOAT
  --use_nnapi / --no-use_nnapi
  --use_legacy_nnapi / --no-use_legacy_nnapi
  --use_gpu / --no-use_gpu
  --help                          Show this message and exit.
```

### Edge Benchmark Python Package

If you prefer to benchmark your machine learning models directly from Python, you can use our Python package `edgebenchmark`.

```
from edgebenchmark import TFLiteBenchmark

benchmark = TFLiteBenchmark()

benchmark.num_threads = 2
benchmark.warmup_runs = 10
benchmark.num_runs = 13
benchmark.run_delay = 3.3
benchmark.use_nnapi = False
benchmark.use_legacy_nnapi = False
benchmark.use_gpu = False
benchmark.features = "{}"
benchmark.devices = ["SamsungGalaxyNote3"]

model_path = "model.tflite"
benchmark.run(model_path)
```


## Licence
[Apache License 2.0](https://github.com/bisonai/edgebenchmark/blob/master/LICENSE)
