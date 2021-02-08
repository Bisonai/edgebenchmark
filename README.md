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

`tflite` command is for benchmarking the speed of TensorFlow Lite models. You can setup many parameters to control the benchmarking process and also select devices (`--devices`) which you want to benchmark with.

We support several different TFLite version. All supported version can be shown by executing the help command below.
```bash
edgebenchmark tflite --help
```


```bash
Usage: edgebenchmark tflite [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  1.14.0
  1.15.0
  1.15.2
  1.15.3
  1.15.4
  2.0.0
  2.0.1
  2.0.2
  2.0.3
  2.1.0
  2.1.1
  2.1.2
  2.2.0
  2.2.1
  2.3.0
  2.4.0
  2.4.1
```

Each TfLite version has a little bit different parameter set. For example, if you want to see supported parameters for TFLite version 1.14.0, run the command below.

```bash
edgebenchmark tflite 1.14.0 --help
```

```bash
Usage: edgebenchmark tflite 1.14.0 [OPTIONS]

Options:
  --features FEATURES
  -d, --device TEXT
  --model_path MODEL_PATH   [required]
  --allow_fp16 BOOLEAN
  --input_layer_shape TEXT
  --input_layer TEXT
  --warmup_runs INTEGER
  --output_prefix TEXT
  --benchmark_name TEXT
  --num_threads INTEGER
  --run_delay INTEGER
  --num_runs INTEGER
  --help                    Show this message and exit.

```


### Edge Benchmark Python Package

If you prefer to benchmark your machine learning models directly from Python, you can use our Python package `edgebenchmark`.

```python
from edgebenchmark import TFLiteBenchmark

benchmark = TFLiteBenchmark("1.14.0")

benchmark.num_threads = 2
benchmark.warmup_runs = 10
benchmark.num_runs = 20
benchmark.devices = ["LGG6"]
benchmark.features = {"num_params": 14000}
benchmark.run("model.tflite")
```

## Currently available devices

If you want to select specific devices for benchmarking, but you are not sure what devices we currently support, you can use `devices` command as shown below.

```bash
edgebenchmark devices
```

This command will return you a set of available devices which you can then specify for benchmarking using `--device` or `-d` parameter.

```bash
OnePlus6t
SamsungGalaxy3
```

## FAQ

Here, you can find the most common questions and their answers. If you would like to ask any question, feel free to open a new issue or send us email to contact@bisonai.com.

### How to select multiple devices?

Devices should be selected with `-d` od `--device` parameter. For example, following script will benchmark `model.tflite` model on `OnePlus6t` and `SonyXperiaZ5`.

```bash
edgebenchmark tflite 1.14.0 \
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
  --features "{'num_params': 14000}"
```


## Licence
[Apache License 2.0](https://github.com/bisonai/edgebenchmark/blob/master/LICENSE)
