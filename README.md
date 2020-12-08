# sphinx-hwt

[![Travis-ci Build Status](https://travis-ci.org/Nic30/sphinx-hwt.png?branch=master)](https://travis-ci.org/Nic30/sphinx-hwt)[![PyPI version](https://badge.fury.io/py/sphinx-hwt.svg)](http://badge.fury.io/py/sphinx-hwt)[![Coverage Status](https://coveralls.io/repos/github/Nic30/sphinx-hwt/badge.svg?branch=master)](https://coveralls.io/github/Nic30/sphinx-hwt?branch=master)[![Documentation Status](https://readthedocs.org/projects/sphinx-hwt/badge/?version=latest)](http://sphinx-hwt.readthedocs.io/en/latest/?badge=latest)
[![Python version](https://img.shields.io/pypi/pyversions/sphinx-hwt.svg)](https://img.shields.io/pypi/pyversions/sphinx-hwt.svg)
[ROADMAP](https://drive.google.com/file/d/1zyegLIf7VaBRyb-ED5vgOMmHzW4SRZLp/view?usp=sharing)

Extension for Sphinx document generator. Add automatically generated schemes and other visual documentation of hardware.
Currently mainly for [HWT library](https://github.com/Nic30/hwt.git) (but VHDL,Verilog -> HWT is possible).

Live demo is documentation of [hwtLib library](https://github.com/Nic30/hwtLib), this library contains many components. The schematic is in documentation of compoents for example there in documentation of [CRC generator](http://hwtlib.readthedocs.io/en/latest/_static/schematic_viewer/schematic_viewer.html?schematic=../../_static/hwt_schematics/hwtLib.logic.crc.Crc.json).


## Installation
Install as standard python package, using pip. If you have NPM installed javascript in package will be updated.
```
pip3 install sphinx-hwt
```

sphinx-hwt package provides sphinx_hwt extension for sphinx doc. gen. In order to use this extension you have to register in in your conf.py sphinx doc. configuration.

``` python
extensions = ['sphinx_hwt']
```

From now Sphinx will be able to use directives from sphinx-hwt to render schematics and others.



## Usage

Add hwt-schematic directive in docstring of Unit class like this.

```python
from hwt.synthesizer.unit import Unit

def explicit_constructor():
    return ExampleCls0()

class ExampleCls0(Unit):
    """
    .. hwt-schematic::

    or

    .. hwt-schematic:: explicit_constructor

    There are also other directives, read the feature list below.
    """


```

Link on schematic will be added to class documentation.



## Feature list
* hwt-params - generates a list of hwt Params for Interface/Unit classes with a information about value and type
* hwt-interface - generates a list of IO interfaces of the Interface/Unit class
* hwt-components - generates a list of components for the Unit class
* hwt-schematic:
  * generate interactive schematic for Unit instances (= module in verilog, entity + architecutere in VHDL).
    * zoom, pan, dynamic colapsing, net-select, searching and filtering
    * schematic rendered by [d3-hwschematic library](https://github.com/Nic30/d3-hwschematic)
    * Unit instances to graph conversion by [hwtGraph library](https://github.com/Nic30/hwtGraph)
* hwt-autodoc: hwt-params, hwt-interface, hwt-components and hwt-schematic at once
