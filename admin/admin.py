from flask import Blueprint

admin_pb = Blueprint("admin_pb", __name__)

@admin_pb.route("/")
def admin_page():
    return return("admin page")