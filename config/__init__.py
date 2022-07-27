ENV = "dev"


class DefaultConfig:
    graphql_route = "/graphql"


class ProdConfig(DefaultConfig):
    host = "0.0.0.0"
    port = 8080


class DevConfig(DefaultConfig):
    host = "localhost"
    port = 8080


config = DevConfig() if ENV == "dev" else ProdConfig()
