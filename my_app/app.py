import click
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


@api.route("/hello", defaults={"obj": "World"})
@api.route("/hello/<obj>")
class HelloWorld(Resource):
    def get(self, obj):
        return {"hello": obj}


# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo("Hello, Command-Line!")
