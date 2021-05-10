# tracert-mapper

A simple python script that maps traceroute IP addresses using [gmplot](https://github.com/gmplot/gmplot)

## Installation

Use git to clone the directory on your local machine

```bash
$git clone https://github.com/amo-simo/tracert-mapper.git
```

`cd` to the project directory and install the dependencies using pip.

```bash
$cd tracert-mapper
$python3 -m pip install -r requirements.txt
```

## Usage
```bash
$python3 tracer.py [ADDRESS/DOMAIN]
```
### Examples
```bash
python3 tracer.py facebook.com
```

```bash
python3 tracer.py 188.184.21.108
```
