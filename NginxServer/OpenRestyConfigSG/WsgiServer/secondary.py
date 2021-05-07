import time
import datetime
from flask import Flask


application = Flask(__name__)


@application.route("/secondary/<int:task_id>")
def index(task_id):
    print("================:", datetime.datetime.now())

    return "绫罗飘起遮住日落西，奏一回断肠的古曲"


@application.route("/secondary/get/<int:task_id>")
def get(task_id):
    print("---------------:", datetime.datetime.now())
    time.sleep(1)

    return "清明上河图"


if __name__ == '__main__':
    application.run("0.0.0.0", 8088, debug=True)

