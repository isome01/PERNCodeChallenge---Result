DROP TABLE pcc_movies;

CREATE TABLE pcc_movies(movie_id SERIAL PRIMARY KEY, avg_rating FLOAT, created_at timestamptz, updated_at timestamptz, title VARCHAR(256), rating_classification VARCHAR(24), description VARCHAR(256), release_date timestamptz, runtime VARCHAR(256));

INSERT INTO pcc_movies(avg_rating, created_at, updated_at, title, rating_classification, description, release_date, runtime)
VALUES ('3.5','2020-06-13T04:16:14.813Z','2020-06-13T04:16:14.813Z','Oceans 11','PG-13','YUP','2001-12-07T00:00:00.000Z','{"hours": "1", "minutes": "56"}')
RETURNING *; 
