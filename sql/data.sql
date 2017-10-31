INSERT 
INTO users(
    username, 
    fullname,
    email, 
    password,
    usertype, 
    created)
VALUES (
    'atomai',
    'Andrew Tomai', 
    'atomai@umich.edu',
    'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8',
    '0',
    CURRENT_TIMESTAMP);

INSERT
INTO posts(
    banner,
    text,
    created)
VALUES(
    '122a7d27ca1d7420a1072f695d9290fad4501a41.jpg',
    'this is a sample blogpost',
    CURRENT_TIMESTAMP);

INSERT
INTO comments(
    owner,
    postid,
    text,
    created)
VALUES (
    'someotheruser',
    '1',
    'sample comment one',
    CURRENT_TIMESTAMP);
 
INSERT
INTO comments(
    owner,
    postid,
    text,
    created)
VALUES (
    'some_other_user',
    '1',
    'sample comment two',
    CURRENT_TIMESTAMP);
