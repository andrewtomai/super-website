"""
REST API for all posts.

URLs include:
/api/p/
/api/p/<postId>
"""
import andrewtomai
import flask


@andrewtomai.app.route('/api/p/<int:postid>/comments/', methods=['GET', 'POST'])
def comments(postid):
    """Get a list of comments for this post."""
    if flask.request.method == 'GET':
        # if this is a GET request, the user need not be logged in
        return flask.jsonify(get_comments(postid))
    else:
        # if this is a POST request, the user must be logged in!
        if 'logname' not in flask.session:
            return flask.jsonify({
                "message": "Unauthorized",
                "status_code": 401}), 401
        return flask.jsonify(post_comment(postid))


def get_comments(postid):
    """Get the comments for this post."""
    database = andrewtomai.model.get_db()
    cursor = database.execute(
        "SELECT commentid, owner, text, created FROM comments "
        "WHERE postid = ? "
        "ORDER BY commentid DESC;",
        (postid,)
    )
    comments_list = cursor.fetchall()
    return {'comments': comments_list}


def post_comment(postid):
    """Post a comment for this post."""
    database = andrewtomai.model.get_db()
    database.execute(
        "INSERT INTO comments("
        "owner, postid, text, created) "
        "VALUES (?, ?, ?, CURRENT_TIMESTAMP);",
        (flask.session['logname'], postid, flask.request.form['comment_text'])
    )
    database.commit()
    return {'status': 'success'}


