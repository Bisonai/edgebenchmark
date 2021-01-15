# Edge Benchmark

Measure the speed of your machine learning models on real devices!

## Installation

```bash
pip install edgebenchmark
```

## First Use

Before you can use Edge Benchmark, [sign up](https://edgebenchmark.com/app/#/signup) and generate your secret token in [Profile section](https://edgebenchmark.com/app/#/profile).

Then, run following command

```bash
edgebenchmark configure
```

and insert your secret token when you see prompt as shown below.

```bash
Edge Benchmark Token [None]:
```

Your secret token is saved at `~/.edgebenchmark/token`.

## Edge Benchmark

Edge Benchmark can be either used directly from command line with `edgebenchmark` command, or from Python script.

### Edge Benchmark CLI

Edge Benchmark CLI tool offers several commands: `configure` and `tflite`.

```bash
edgebenchmark --help
```


```bash
Usage: edgebenchmark [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  configure
  devices
  tflite
```

`configure` command is explained in the [First use](https://github.com/bisonai/edgebenchmark#first-use) section.

`tflite` command is for benchmarking the speed of TensorFlow Lite models. You can setup many parameters to control the benchmarking process and also select devices (`--devices`) which you want to benchmark with. Below, you can see all options for `tflite` command.

```bash
edgebenchmark tflite --help
```


```bash
Usage: edgebenchmark tflite [OPTIONS]

Options:
  --features FEATURES
  -d, --device TEXT
  --model_path MODEL_PATH         [required]
  --num_threads INTEGER
  --warmup_runs INTEGER
  --num_runs INTEGER
  --run_delay FLOAT
  --use_nnapi / --no-use_nnapi
  --use_legacy_nnapi / --no-use_legacy_nnapi
  --use_gpu / --no-use_gpu
  --version [1.13.1|1.13.2|1.14.0|1.15.0|1.15.2|1.15.3|1.15.4|1.2.0|1.2.1|1.3.0|1.3.1|1.4.0|1.4.1|1.5.0|1.5.1|1.6.0|1.7.0|1.7.1|1.8.0|1.9.0|2.0.0|2.0.1|2.0.2|2.0.3|2.1.0|2.1.1|2.1.2|2.2.0|2.2.1|2.3.0|2.3.1|2.4.0]
  --help                          Show this message and exit.
```

### Edge Benchmark Python Package

If you prefer to benchmark your machine learning models directly from Python, you can use our Python package `edgebenchmark`.

```python
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
benchmark.version = "1.13.1"

model_path = "model.tflite"
benchmark.run(model_path)
```

## Currently available devices

If you want to select specific devices for benchmarking, but you are not sure what devices we currently supported, you can use `devices` command as shown below.

```bash
edgebenchmark devices
```

This command will return you a list of available devices which you can then specify for benchmarking using `--device` or `-d` parameter.

```bash
OnePlus6t
SamsungGalaxy3
```

## FAQ

Here, you can find the most common questions and their answers. If you would like to ask any question, feel free to open a new issue or send us email to contact@bisonai.com.

### How to select multiple devices?

Devices should be selected with `-d` od `--device` parameter. For example, following script will benchmark `model.tflite` model on `OnePlus6t` and `SonyXperiaZ5`.

```bash
edgebenchmark tflite \
  --model_path model.tflite \
  -d OnePlus6t \
  -d SonyXperiaZ5
```

### How to send extra `features` to Edge Benchmark?

If you want to attach aditional information to your benchmark, you can use `--features` pararemeter as shown below.

```bash
edgebenchmark tflite \
  --model_path model.tflite \
  -d OnePlus6t \
  --features "{'num_params': 100000}"
```


## Licence
[Apache License 2.0](https://github.com/bisonai/edgebenchmark/blob/master/LICENSE)
