# OpenCensus Python Quickstart

* Measure and record numerical quantities, a.k.a. _metrics_
* Associate _tags_ with the metrics
* Organize metrics into a _view_
* Export a view into a _backend_, viz. Prometheus

## Prereqs

```
brew install prometheus

pyenv install 2.7.15
pyenv local 2.7.15

pip install --upgrade pip
pip install --upgrade opencensus prometheus-client opencensus-ext-prometheus
```

## Run the thing

```
python repl.py
```

## Look at the graphs

```
prometheus --config.file=prometheus.yaml
```

open http://localhost:9090/graph
