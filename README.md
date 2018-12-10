# Supremacy 1914 API Wrapper

This unofficial API wrapper is an implementation of the Supremacy 1914 API.
This wrapper support API data as far as known and is intended to be easy to use.
You'll only need to supply the server URL and the game\_id before you'll be able to get data.

## Install

```bash
$ pip install supremacy1914-wrapper

```

## Simple Demo

```python
from supremacy1914_wrapper import Supremacy

# Create an instance using game_id and host:

sup = Supremacy("2502620", "http://xgs1.c.bytro.com")

# get players in JSON format 
sup.players()
```

## Documentation

Other information about functions and exceptions can be found on the [wiki.](https://github.com/joostsijm/supremacy1914_wrapper/wiki)

## Development

I'll try to improve the wrapper as far as I need.
If you'd like to see a new feature you can open an issue or make pull request.
