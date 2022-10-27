# SQL CRUD

An assignment to design relational database tables with particular applications in mind.

The contents of this file will be deleted and replaced with the content described in the [instructions](./instructions.md)
## Part 1: Restaurant
Link to the csv file is [here](./data/restaurant.csv).
### Create table
The table named `restaurant` is first created manually with the stucture:
````
CREATE TABLE restaurant (
    id INTEGER PRIMARY KEY,
    category TEXT,
    price_tier TEXT,
    open_time TEXT,
    close_time TEXT,
    neighborhood TEXT,
    average_rating FLOAT,
    good_for_kids TEXT
);
````
Then, a temporary table, `temp_res`, for holding imported data from the csv data file is created using:
.mode csv
.import data/restaurant.csv temp_res
 It is merged into `restaurant` table using `INSERT INTO restaurant SELECT * FROM temp_res`. The primary key is set to be the `id` column, holding the unique id number for each restaurant listed.
### Queries
#### 1. Find all cheap restaurants in a particular neighborhood (pick any neighborhood as an example).
For example, to find all cheap restaurants in Penn South, the query `SELECT * FROM restaurant WHERE neighborhood="Chelsea" AND price_tier="cheap";` will give all rows of information of restaurants satisfying the requirement.

#### 2. Find all restaurants in a particular genre (pick any genre as an example) with 3 stars or more, ordered by the number of stars in descending order.
To get a listing of all Cafe with 3 stars or more in average rating, I use `Select * from restaurant Where average_rating>=3 AND category="cafe" ORDER BY average_rating DESC;` to return in descending order. 

#### 3. Find all restaurants that are open now.
Using the query `Select * from restaurant where open_time<=strftime('%H:%M', 'now') AND close_time>=strftime('%H:%M', 'now');` will return all restaurants that are open now, based on the UTC time. It literally compares open time and close time of each resraurant, and make sure that the current time is in between. 

#### 4. Leave a review for a restaurant (pick any restaurant as an example).
First, add a new column named "review" of TEXT to the table `restaurant` by `ALTER TABLE restaurant ADD review TEXT`; now each item it holds exmpty chars. Then, given the restaurant's id, we can add/update by, for example, `UPDATE restaurant SET review = "Best restaurant I have ever been. Wonderful experience." WHERE id=8;`.
Fetch your review by `SELECT review FROM restaurant WHERE id=8;`.

#### 5. Delete all restaurants that are not good for kids.
Use `DELETE FROM restaurant WHERE good_for_kids="false";` to remove all restaurants what are not suitable for kids from the table.

#### 6. Find the number of restaurants in each NYC neighborhood.
The query `SELECT neighborhood,COUNT(*) FROM restaurant GROUP BY neighborhood;` returns the the name of each NYC neighborhood and the corresponding count of the restaurants in that area. 

## Part 2: Social media app
Click on [users](./data/users.csv) or [posts](./data/posts.csv) to check out the csv files imported for this database.
### Create table
The table named `users` is created manually with the stucture:
````
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT,
    username TEXT,
    password TEXT
);
````
and another table named `posts` is created for storing both messages and stories:
````
CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    posts TEXT,
    id_from_user INTEGER,
    id_to_user INTEGER,
    time TEXT,
    content TEXT,
    viewed TEXT,
    FOREIGN KEY(id_from_user) REFERENCES users(id),
    FOREIGN KEY(id_to_user) REFERENCES users(id)
);
````
Using the same procesdure of importing from csv and insert into self-constructed tables, we successfully made a table `users` with 1000 user info and `posts` with 2000 posts containing messages and stories of 1000 each. The "post" field in `posts` has two values, message or story. If the post if of story kind, its "id_to_user" field is set to 0, indicating no user as a receiver as the user id starts from 1, while "id_from_user" indicates the owner's user id. If the post if of message, then these both field has a non-zero integer indicating sender and receiver user id's. <br>

The "viewed" field of table `posts` indicats the status of each post. It is 4 different values in total. Given a post is of category message, it has two "viewed" status: 1) "yes" - This message has been viewed by receiver and therefore becomes invisible 2) "no" - The message has not been viewed yet, so it is visible. Otherwise, given a post is of category story, it also has two "viewed" status: 1) "public" - The story is visible to the public, which means it is posted within 24 hours from the current time (By default, the csv file is created with all story being public regardless of the time. This will be changed in Q6 of this section.). 2) "invisible" - The story is expired as 24 hours has passed, thus invisible. 

### Queries
#### 1. Register a new User.
For the new user to be registered, his id must be unique, so we set this new id as +1 of the largest id of the table to ensure uniqueness. For example, I would like to resgitser myself, and I use query `INSERT INTO users(id, email, username, password) SELECT MAX(id)+1,"wy818@nyu.edu","wy818","abcd1234" FROM users;` and now I'm the no.1001 user on the table.

#### 2. Create a new Message sent by a particular User to a particular User (pick any two Users for example).
For exmaple, if I(the no.1001 user) want to send a message "Hello world!" to the no.1 user on the user table, and user no.1 haven't viewed it yet, then the query `INSERT INTO posts(id,posts,id_from_user,id_to_user,time,content,viewed) SELECT MAX(id)+1,"message",1001,1,strftime('%Y-%m-%d %H:%M:%S','now'),"Hello world!","no" FROM posts;` is used for creating message, where time is fetch using SQLite strftime(), post categoty is manually set as "message", and the post's id is unique and max(id)+1, same as the logic in Q1.

#### 3. Create a new Story by a particular User (pick any User for example).
The no.1 user on the user table would like post a new story "This is my latest story.". The query `INSERT INTO posts(id,posts,id_from_user,id_to_user,time,content,viewed) SELECT MAX(id)+1,"story",1,0,strftime('%Y-%m-%d %H:%M:%S','now'),"This is my latest story.",public FROM posts;` will make this user's request possible. 

#### 4. Show the 10 most recent visible Messages and Stories, in order of recency.
To get the top 10 most recent visible Messages, use `SELECT * FROM posts WHERE posts = "message" AND viewed = "no" ORDER BY time DESC LIMIT 10;`<br><br>
To get the top 10 most recent visible Stories, use `SELECT * FROM posts WHERE posts = "story" AND viewed = "public" AND ROUND((JULIANDAY('now') - JULIANDAY(time)) * 24)< 24 ORDER BY time DESC LIMIT 10;`<br><br>
To get the top 10 most recnet visible Messages or Stories, use `SELECT * FROM posts WHERE viewed = "no" OR (posts = "story" AND ROUND((JULIANDAY('now') - JULIANDAY(time)) * 24)< 24 AND viewed = "public") ORDER BY time DESC LIMIT 10;`.<br><br>
To get the top 10 most recnet visible Messages and Stories, use:
````
SELECT * FROM
(SELECT * FROM posts WHERE posts = "message" AND viewed = "no" ORDER BY time DESC LIMIT 10)
UNION
SELECT * FROM
(SELECT * FROM posts WHERE posts = "story" AND viewed = "public" AND ROUND((JULIANDAY('now') - JULIANDAY(time)) * 24)< 24 ORDER BY time DESC LIMIT 10)
ORDER BY posts,time DESC;
````

#### 5. Show the 10 most recent visible Messages sent by a particular User to a particular User (pick any two Users for example), in order of recency.
For exmple, the company want to see all visible message from user with id no.2 to user with id no.1, they can use the query `SELECT id,id_from_user,id_to_user,content,time FROM posts WHERE posts = "message" AND viewed = "no" AND id_from_user = 2 AND id_to_user = 1 ORDER BY time DESC LIMIT 10;` to check for recent listing of 10. 

#### 6. Make all Stories that are more than 24 hours old invisible.
Note that the database initially has all stories's "view" field as "public", regardless of the time. Now we need to change all stories that are created for more than 24 hours invisible: `UPDATE posts SET viewed = "invisible" WHERE posts = "story" AND ROUND((JULIANDAY('now') - JULIANDAY(time)) * 24) >= 24;`.

#### 7. Show all invisible Messages and Stories, in order of recency.
Use query `SELECT * FROM posts WHERE viewed = "yes" OR viewed = "invisible" ORDER BY time DESC;`. Invisible messages and stories are mixed together and listed in order of recency.

#### 8. Show the number of posts by each User.
Use `SELECT users.id, username, COUNT(*) FROM users INNER JOIN posts ON users.id = posts.id_from_user GROUP BY users.id;` to show the list of post by each user as well as corresponding id and username.

#### 9. Show the post text and email address of all posts and the User who made them within the last 24 hours.
The query `SELECT id_from_user, email, content FROM users INNER JOIN posts ON users.id = posts.id_from_user WHERE ROUND((JULIANDAY('now') - JULIANDAY(time)) * 24) < 24;` displays all posts within 24 hours and coresponding user's info. 

#### 10. Show the email addresses of all Users who have not posted anything yet.
`SELECT email FROM users LEFT JOIN posts ON users.id = posts.id_from_user WHERE posts.id is NULL;` shows the email addresses of all users who have not made any post.





