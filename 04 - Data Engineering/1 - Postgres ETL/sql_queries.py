# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""create table if not exists songplays 
                              (
                               songplay_id serial,
                               start_time timestamp not null,
                               user_id int not null, 
                               level varchar,
                               song_id varchar,
                               artist_id varchar,
                               sessionId int not null,
                               location varchar,
                               userAgent varchar,
                               primary key (songplay_id),
                               unique(sessionId, start_time)
                              )
                         """)

user_table_create = ("""create table if not exists users 
                          (
                           user_id int,
                           firstName varchar,
                           lastName varchar,
                           gender varchar,
                           level varchar,
                           primary key (user_id)
                          )
                     """)

song_table_create = ("""create table if not exists songs 
                          (
                           song_id varchar,
                           title varchar not null,
                           artist_id varchar,
                           year int,
                           duration numeric not null,
                           primary key(song_id)
                          )
                     """)

artist_table_create = ("""create table if not exists artists 
                            (
                             artist_id varchar,
                             name varchar not null,
                             location varchar,
                             latitude double precision,
                             longitude double precision,
                             primary key (artist_id)
                            )
                       """)

time_table_create = ("""create table if not exists time 
                          (
                           id serial,
                           timestamp timetz not null,
                           hour int,
                           day int,
                           weekofyear int,
                           month int,
                           year int,
                           weekday int,
                           primary key(id),
                           unique(timestamp, year, month, day)
                          )
                     """)

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays 
                                          (
                                           start_time,
                                           user_id,
                                           level,
                                           song_id,
                                           artist_id,
                                           sessionId,
                                           location,
                                           userAgent
                                          )
                                        values 
                                          (%s, %s, %s, %s, %s, %s, %s, %s)
                            on conflict (sessionId, start_time) do nothing""")

user_table_insert = ("""insert into users 
                                      (
                                       user_id,
                                       firstName,
                                       lastName,
                                       gender,
                                       level
                                      )
                                    values (%s, %s, %s, %s, %s)
                        on conflict (user_id) do update set level = EXCLUDED.level""")

song_table_insert = ("""insert into songs 
                                      (
                                       song_id,
                                       title,
                                       artist_id,
                                       year,
                                       duration
                                      )
                                    values (%s, %s, %s, %s, %s)
                        on conflict (song_id) do nothing""")
                          
artist_table_insert = ("""insert into artists 
                                        (
                                         artist_id,
                                         name,
                                         location,
                                         latitude,
                                         longitude
                                        )
                                      values (%s, %s, %s, %s, %s)
                          on conflict (artist_id) do nothing""")


time_table_insert = ("""insert into time 
                                      (
                                       timestamp,
                                       hour,
                                       day,
                                       weekofyear,
                                       month,
                                       year,
                                       weekday
                                      )
                                    values (%s, %s, %s, %s, %s, %s, %s)
                        on conflict (timestamp, year, month, day) do nothing""")

# FIND SONGS

song_select = ("""select s.song_id, a.artist_id 
                  from   songs as s 
                         join artists as a using (artist_id) 
                  where  s.title = (%s) 
                         and a.name = (%s)
                         and s.duration = (%s)
               """)

# QUERY LISTS

create_table_queries = [song_table_create, songplay_table_create, user_table_create, artist_table_create, time_table_create]
drop_table_queries = [song_table_drop, songplay_table_drop, user_table_drop, artist_table_drop, time_table_drop]