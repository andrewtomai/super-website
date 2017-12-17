"""andrewtomai login helpers."""
import uuid
import hashlib
import flask
import andrewtomai


def calculate_hash(algorithm, salt, password):
    """Calculate the salted hash of a password."""
    if algorithm is None:
        algorithm = 'sha512'
    if salt is None:
        salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + password
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])
    return password_db_string


def check_password(username, password):
    """Test the given username password combo for validity."""
    database = andrewtomai.model.get_db()
    # grab the salted hash from the db
    salted_password_hash = database.execute(
        "SELECT password"
        " FROM users"
        " WHERE username = ?",
        (username,)
    )
    salted_password_hash = salted_password_hash.fetchone()
    if salted_password_hash is None:
        return False

    salted_password_hash = salted_password_hash['password']
    algorithm = salted_password_hash.split('$')[0]
    salt = salted_password_hash.split('$')[1]

    # now salt and hash the input password
    input_salted_password_hash = calculate_hash(algorithm, salt, password)
    return salted_password_hash == input_salted_password_hash
