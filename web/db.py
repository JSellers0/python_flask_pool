import requests

api_route = "http://192.168.0.202/api/pool/"

class API():
    def get_chemicals(self):
        result = requests.get(api_route + "chemicals")
        if result.status_code == 200:
            data = result.json()
        else:
            data = None
        return data

    def create_test_type(self, test):
        result = requests.post(api_route + "tests/types", params=test)
        if result.status_code == 200:
            return result.status_code
        elif result.status_code == 409:
            return result.status_code
        elif result.status_code == 404:
            return result.status_code
        else:
            # Error Response
            pass
