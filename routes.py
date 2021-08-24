from wsgi import app
from admin.admin import admin_pb

app.register_blueprint(admin_pb, url_prefix="/admin")

@app.route("/")
def home():
    return "Hello"