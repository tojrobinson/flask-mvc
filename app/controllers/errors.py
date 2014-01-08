from flask import Blueprint, request, render_template

errors = Blueprint('errors', __name__, template_folder='views/errors')

@errors.app_errorhandler(403)
def forbidden(e):
   return "forbidden", 403

@errors.app_errorhandler(404)
def not_found(e):
   return "not found", 404

@errors.app_errorhandler(405)
def method_not_allowed(e):
   return "method not allowed", 405

@errors.app_errorhandler(500)
def server_error(e):
   return "server error", 500
