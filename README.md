# Supremacy 1914 API Wrapper

This unofficial API wrapper is an implementation of the Supremacy 1914 API.
This wrapper support API data as far as known and is intended to be easy to use.
You'll only need to supply the server URL and the game\_id before you'll be able to get data.

## Install

```bash
$ pip install supremacy1914-wrapper
```

## Demo

It's advised to store the server url for the game you want to request. If you don't have the server url you can make a Supremacy instance without the url parameter, wrap it in a try except to get the server url.

```python
from supremacy1914_wrapper import Supremacy, ServerChangeError 

# Create a Supremacy instance using game id
supremacy = Supremacy("2502620")

# Send a request and except server change error
try:
    result = supremacy.players()
except ServerChangeError as exception:
    # update the url in the Supremacy instance
    supremacy.url = str(exception)
    result = supremacy.players()
```

When you have to server url from the game you can pass it into the Supremacy constructor. Make sure to use a try except because the server changes over time.

```python
from supremacy1914_wrapper import Supremacy, ServerChangeError 

# Create a Supremacy instance using game id and server url
supremacy = Supremacy("2502620", "http://xgs1.c.bytro.com")

# Send a request and except server change error
try:
    result = supremacy.players()
except ServerChangeError as exception:
    # update the url in the Supremacy instance
    supremacy.url = str(exception)
    result = supremacy.players()
```

## Documentation

Other information about functions and exceptions can be found on the [wiki.](https://github.com/joostsijm/supremacy1914_wrapper/wiki)

## Tests

Testing is done with PyTest, to run the tests use the command `pytest`. The following environment variables are required: `TEST_GAME_ID` and `TEST_GAME_URL`, save those in the `.env` file for convince

## Development

I'll try to improve the wrapper as far as I need.
If you'd like to see a new feature you can open an issue or make pull request.
