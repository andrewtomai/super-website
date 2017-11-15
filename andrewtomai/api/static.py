"""
andrewtomai app helper to send static files.

URLs include:
/uploads/<filename>
/static/*
"""
import flask
import andrewtomai


@andrewtomai.app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Endpoint to get uploaded files."""
    return flask.send_from_directory(andrewtomai.app.config['UPLOAD_FOLDER'],
                                     filename)


@andrewtomai.app.route('/css/<filename>')
def access_style(filename):
    """Endpoint to get static css files."""
    return flask.send_from_directory('/static/css/style/', filename)


@andrewtomai.app.route('/images/<filename>')
def access_images(filename):
    """Endpoint to get static images."""
    return flask.send_from_directory('/static/images/', filename)
