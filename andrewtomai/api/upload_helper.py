"""Upload helpers."""
import os
import shutil
import tempfile
import hashlib
import andrewtomai
import flask


def upload_file():
    """Upload and save files."""
    # Save POST request's file object to a temp file
    dummy, temp_filename = tempfile.mkstemp()
    file = flask.request.files["file"]
    file.save(temp_filename)

    # Compute filename
    hash_txt = sha1sum(temp_filename)
    dummy, suffix = os.path.splitext(file.filename)
    hash_filename_basename = hash_txt + suffix
    hash_filename = os.path.join(
        andrewtomai.app.config["UPLOAD_FOLDER"],
        hash_filename_basename
    )

    # Move temp file to permanent location
    shutil.move(temp_filename, hash_filename)
    andrewtomai.app.logger.debug("Saved %s", hash_filename_basename)

    # return the hash_filename_basename
    return hash_filename_basename


def sha1sum(filename):
    """Return sha1 hash of file content, similar to UNIX sha1sum."""
    content = open(filename, 'rb').read()
    sha1_obj = hashlib.sha1(content)
    return sha1_obj.hexdigest()


def remove_file(filename):
    """Remove a file from the filesystem."""
    path = os.path.join(
        andrewtomai.app.config["UPLOAD_FOLDER"],
        filename
    )
    os.remove(path)
