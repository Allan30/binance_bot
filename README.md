# binance_bot

## How to create conda environment

To create the environment, you have to install conda.

Then, use the following command to create environment.

```
conda env create -f etc/environment.yml
```

You can now activate it with :

```
conda activate binance-trading-bot
```

## How to run

The `main.py` file allow to run specific modules. You can run module using :

```
python src/main. -m {module}
```

## How to test

To run unit and integration test, use :

```
pytest
```

To run only unit test, use :

```
pytest -m "unit"
```

## Available modules

### Trade Scheduler

WIP

