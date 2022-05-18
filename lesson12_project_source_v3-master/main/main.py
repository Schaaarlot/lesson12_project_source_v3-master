from flask import Blueprint, render_template, request
import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO)

from functions import load_posts

main_blueprint = Blueprint("main", __name__, url_prefix="/", template_folder="templates")


@main_blueprint.route("/", )
def main():
    return render_template("index.html")


@main_blueprint.route("/search/")
def search():
    search_by = request.args["s"]
    logging.info(f'Слово для поиска: {search_by}')
    posts = [x for x in load_posts() if search_by.lower() in x['content'].lower()]
    return render_template("post_list.html", search_by=search_by, posts=posts)
