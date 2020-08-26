import api.config

connex_app = api.config.connex_app

connex_app.add_api("swagger.yml")

if __name__ == "__main__":
    connex_app.run(port=5004, debug=True)