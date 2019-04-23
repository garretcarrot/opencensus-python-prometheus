# OpenCensus Python Quickstart

## Prereqs

Prometheus:

```bash
brew install prometheus
prometheus --config.file=prometheus.yaml
```

Python:

```bash
pyenv install 2.7.15
pyenv local 2.7.15
```

Deps:

```bash
pip install --upgrade pip
pip install --upgrade opencensus prometheus-client opencensus-ext-prometheus
```

## What

* Measure and record numerical quantities, a.k.a. _metrics_
* Associate _tags_ with the metrics
* Organize metrics into a _view_
* Export a view into a _backend_, viz. Prometheus
