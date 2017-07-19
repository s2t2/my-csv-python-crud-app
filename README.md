# My Python CSV CRUD Application

## Setup

Download the [prepared CSV file](https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-70-201706/master/projects/crud-app/products.csv) and save it as `data/products.csv`.

## Prerequisites

This application assumes you have installed Python 3.x and corresponding Pip. It may work, but is untested on Python 2.x.

## Installation

Download the source code:

```shell
git clone git@github.com:s2t2/python-csv-crud-app.git
cd python-csv-crud-app/
```

Install package dependencies:

```shell
pip3 install -r requirements.txt
```

## Usage

Run the application:

```shell
python3 app/products_app.py
```

Run tests:

```shell
pytest # ...OR... pytest --pdb to drop into an interactive shell upon test failure
```
