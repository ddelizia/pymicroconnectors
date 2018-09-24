# Py Micro Connectors

[![made-with-python](https://img.shields.io/badge/pypi-pymicroconnectors-green.svg?style=flat-square)](https://pypi.org/project/pymicroconnectors/)
[![licence](https://img.shields.io/badge/licence-MIT-green.svg?style=flat-square)](https://github.com/ddelizia/pymicroconnectors/LICENCE)


This package tries to provide a simple and easy to use connection to different services as also makes easy the configuration of flask for running simple microservices.

## Installation

```
pip install pymicroconnectors
```


# Modules

Configuration need to be stored on the following path `config/config.yml`

## Config

```
import pymicroconnectors.config as config

config.get_value('x.y.w')
```

Example yaml file

```
x:
  y:
    w: "Hello This is the property"
```



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


## Flask

For more documentation refer to: https://github.com/pallets/flask

### Usage

```
import pymicroconnectors.flask as flask

flask.init()

flask.run()
```

### Configuration

```
flask:
  name: "myserver"
  server:
    port: 5000
```

## Flask Assistant

For more documentation refer to: https://github.com/treethought/flask-assistan

```
import pymicroconnectors.flask as flask
import pymicroconnectors.flask_assistant as flask_assistant

flask_assistant.init()

flask.run()
```

### Configuration

Start Flask assistant under prefix `/assistant`

```
flask:
  assistant:
    context: "assistant"
```

## Flask Ask

For more documentation refer to: https://github.com/johnwheeler/flask-ask

```
import pymicroconnectors.flask as flask
import pymicroconnectors.flask_ask as flask_ask

flask_ask.init()

flask.run()
```

### Configuration

Start Flask ask under prefix `/ask`

```
flask:
  ask:
    context: "ask"
```

## Flask Restful

## Flask Graphql

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
