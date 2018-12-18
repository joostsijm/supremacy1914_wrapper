"""The Supremacy 1914 class"""

import time
import json
import requests


class Supremacy():
    """The supremacy class allow easy asses to the Supremacy 1914 API"""

    game_id = None
    url = None
    debug = 0

    default_params = {
        "@c": "ultshared.action.UltUpdateGameStateAction",
        "playerID": 0,
        "userAuth": "787925a25d0c072c3eaff5c1eff52829475fd506",
        "tstamp": int(time.time())
    }

    headers = {
        "Host": "xgs8.c.bytro.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) " +
                      "Gecko/20100101 Firefox/57.0",
        "Accept": "text/plain, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://www.supremacy1914.nl",
        "DNT": "1",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }

    def __init__(self, game_id, url, debug=None):
        """Initialize api"""
        self.game_id = game_id
        self.url = url
        self.default_params["gameID"] = game_id
        if debug and isinstance(debug, int):
            self.debug = debug

    def all(self):
        """Return all information"""
        return self._request()

    def game(self):
        """Return game information"""
        return self._request(12)

    def coalitions(self):
        """Return coalition list and members"""
        result = self._request(2)
        return result["teams"]

    def players(self):
        """Return list of players"""
        return self._request(1)

    def market(self):
        """Return market prices"""
        return self._request(4)

    def score(self, day):
        """Return score of specified day"""
        return self._request(2, day)

    def relations(self):
        """Return list of relations between people"""
        return self._request(5)

    def _request(self, state_type=None, day=None):
        """Make request to the server"""
        params = self.default_params

        if state_type is not None:
            params["stateType"] = state_type

        if day is not None:
            params["option"] = day

        request = requests.post(self.url, headers=self.headers, json=params)
        response = json.loads(request.text)

        if self.debug >= 2:
            print_json(response)

        if response["result"]["@c"] == "ultshared.rpc.UltSwitchServerException":
            if "newHostName" in response["result"]:
                new_url = "http://%s" % response["result"]["newHostName"]
                if self.debug >= 1:
                    print("new host: %s for %s" % (new_url, self.game_id))
                raise ServerChangeError(new_url)
            else:
                if self.debug >= 1:
                    print("Game %s does not exist" % self.game_id)
                raise GameDoesNotExistError("Game %s is not found" % self.game_id)

        return response["result"]


class GameDoesNotExistError(Exception):
    """Raise when game does not exist"""


class ServerChangeError(Exception):
    """Raise when server has changed"""


def print_json(json_text):
    """Print data to console"""
    print(json.dumps(json_text, sort_keys=True, indent=4))
