from flask import Blueprint, render_template

global_scope = Blueprint("views", __name__)


@global_scope.route("/", methods=['GET'])
def home():
    """Landing page route."""

    parameters = {"title": "Diana's Project",
                  "description": "This is a simple page for diana"
                  }

    return render_template("home.html", **parameters)

@global_scope.route("/ranking", methods=['GET'])
def ranking():
    "Page for the ranking"

    parameters = {"title": "Ranking",
                  "description": "Here is the ranking"
                  }

    return render_template("ranking.html", **parameters)
