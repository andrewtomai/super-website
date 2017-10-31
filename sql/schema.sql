CREATE TABLE users(
  username VARCHAR(20) NOT NULL,
  fullname VARCHAR(40) NOT NULL,
  email VARCHAR(40) NOT NULL,
  password VARCHAR(256) NOT NULL,
  created TIMESTAMP,
  usertype INT NOT NULL,
  PRIMARY KEY(username)
);

CREATE TABLE posts(
  postid INTEGER PRIMARY KEY AUTOINCREMENT,
  banner VARCHAR(64) NOT NULL,
  text VARCHAR(4096) NOT NULL,
  created TIMESTAMP
);

CREATE TABLE comments(
  commentid INTEGER PRIMARY KEY AUTOINCREMENT,
  owner VARCHAR(20) NOT NULL,
  postid INT NOT NULL,
  text VARCHAR(1024) NOT NULL,
  created TIMESTAMP,
  FOREIGN KEY(owner)
    REFERENCES users(username)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  FOREIGN KEY(postid) 
    REFERENCES posts(postid) 
    ON UPDATE CASCADE
    ON DELETE CASCADE
);
