"""
REST API for all posts
URLs include:
/api/p/
/api/p/<postId>
"""
import flask
import andrewtomai


@andrewtomai.app.route('/api/p/', methods=['GET', 'POST'])
def list_posts():
    """List all the most recent posts."""
    if flask.request.method == 'GET':
        # if this is a GET request, the user need not be logged in
        size = flask.request.args.get('size', default=5, type=int)
        page = flask.request.args.get('page', default=0, type=int)
        # error check this request
        if size < 0 or page < 0:
            return flask.jsonify({
                "message": "Bad Request",
                "status_code": 400}), 400
        return flask.jsonify(get_posts(size, page))
    else:
        # if this is a POST request, the user must be logged in as ME!
        pass


@andrewtomai.app.route('/api/p/<int:postid>', methods=['GET'])
def individual_post(postid):
    """Get an individual post."""
    database = andrewtomai.model.get_db()
    # get the specific post
    cursor = database.execute(
        "SELECT * "
        "FROM posts "
        "WHERE postid = ?;", str(postid)
    )
    post = cursor.fetchone()
    if post is None:
        return flask.jsonify({"message": "Not Found", "status_code": 404}), 404

    context = {
        'age': post['created'],
        'banner_url': flask.url_for(
            '.uploaded_file',
            filename=post['banner']
        ),
        'text': post['text']
    }
    return flask.jsonify(context)


def get_posts(size, page):
    """Get most recent posts."""
    database = andrewtomai.model.get_db()
    cursor = database.execute(
        "SELECT postid FROM posts "
        "ORDER BY postid DESC "
        "LIMIT ? "
        "OFFSET ?;",
        (size, size * page)
    )
    posts_list = cursor.fetchall()
    posts = {}
    posts['results'] = []
    for post in posts_list:
        posts['results'].append({'url': flask.url_for(
            '.individual_post',
            postid=post['postid']
        )})
    # get the number of total posts for the 'next' parameter
    cursor = database.execute(
        "SELECT COUNT(*) FROM posts"
    )
    total_posts = cursor.fetchone()['COUNT(*)']
    if total_posts > (size * page) + size:
        # there is a next page
        parameters = "?size=" + str(size) + "&page=" + str(page + 1)
        posts['next'] = flask.url_for('.list_posts') + parameters
    else:
        # there is no next page of posts
        posts['next'] = ''

    posts['url'] = flask.url_for('.list_posts')
    return posts
