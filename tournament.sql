-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- if exist drop

CREATE DATABASE tournament;

\c tournament;

create table players (id serial PRIMARY KEY, name varchar(30));

create table matches (id serial PRIMARY KEY, 
					  player1 integer REFERENCES players(id),
					  player2 integer REFERENCES players(id),
					  winner integer REFERENCES players(id));

	
-- this view shows the the list of all players and their associated wins
create view wins as 
	select players.id,players.name, count(matches.id) as wins 
	from players left join matches on matches.winner=players.id 
	group by players.id 
	order by wins desc;
	
-- this view shows the list of all players in matches (doesn't include 0)
create view allmatchplayers as 
	select player1 as id from matches union all select player2 as id from matches;

-- this view shows a list of players with their total games (doesn't include 0)
create view totalgames as 
	 select count(id) as total from allmatchplayers group by id;

-- this view shows to wins the total number of games 
create view standings as 
	select wins.*, coalesce(totalgames.total,0) as matches
    from wins left join totalgames 
    on wins.id=totalgames.id;

-- this view lists the players and their wins with row numbers to be used later
-- this list is ordered by wins
create view winsrows as 
	select id, name, wins, row_number() over (order by wins desc) as rn 
	from wins;

# adds the index to winsrows table to match rows.
create view winsrowsready as
	select *, rn/2+rn%2 as x
	from winsrows;

# select pairs which are near each other (by wins number)
create view pairs as
	 select a.id as id1, a.name as name1, b.id as id2, b.name as name2 
	 from winsready a, winsready b 
	 where a.x=b.x and a.id<b.id;

