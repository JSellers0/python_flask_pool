import requests

api_route = "http://localhost:5002/api/pool/"

class API():
    def get_chemicals():
        result = requests.get(api_route + "chemicals")
        if result.status_code == 200:
            data = result.json()
        else:
            data = None
        return data
