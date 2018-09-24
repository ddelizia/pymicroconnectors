# Py Micro Connectors

[![made-with-python](https://img.shields.io/badge/pypi-pymicroconnectors-green.svg?style=flat-square)](https://pypi.org/project/pymicroconnectors/)
[![licence](https://img.shields.io/badge/licence-MIT-green.svg?style=flat-square)](https://github.com/ddelizia/pymicroconnectors/LICENCE)


This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Installation

```
pip install pymicroconnectors
```


# Modules


## Config

## Logger

Adding colored logs to the application in an easy and configurable way

### Usage

```
import pymicroconnectors.logger as logger

logger.init()
```

## Ebay

For more documentation refere to: https://github.com/timotheus/ebaysdk-python

### Usage
```
import pymicroconnectors.ebay as ebay

ebay.init()

response = ebay.api.execute('findItemsAdvanced', {'keywords': 'legos'})

assert(response.reply.ack == 'Success')
assert(type(response.reply.timestamp) == datetime.datetime)
assert(type(response.reply.searchResult.item) == list)

item = response.reply.searchResult.item[0]
assert(type(item.listingInfo.endTime) == datetime.datetime)
assert(type(response.dict()) == dict)

```

### Configuration

```
ebay:
  # https://developer.ebay.com/DevZone/account/
  # for production use api.ebay.com
  domain: "api.sandbox.ebay.com"
  # Italy
  siteid: "101"
  debug: false
  appid: "DaniloDe-0000-0000-0000-7dfc559109d4"
  devid: "d948e9b0-0000-0000-0000-7a3c10c696e7"
  certid: "346c76cc-0000-0000-0000-c664833c101d"
  token: "AgAAAA..."
```

# Dev Notes

```
python3 setup.py sdist bdist_wheel
twine upload dist/*
```
