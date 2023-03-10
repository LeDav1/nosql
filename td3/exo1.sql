
-- Nombre total de relations friend/followers
select 'Nombre total de relations friend/followers: ' || count(*) from social_network;

-- Nombre d'utilisateurs ayant au moins un follower
select "Nombre d'utilisateurs ayant au moins un follower: " || count(distinct to_node) from social_network;

-- Nombre d'utilisateurs suivant au moins un utilisateur
select "Nombre d'utilisateurs suivant au moins un utilisateur: " || count(distinct from_node) from social_network;

-- Nombre maximum de followers par utilisateur
select "Nombre maximum de followers par utilisateur: " || MAX(num_followers) AS nb_max_followers FROM
    (SELECT to_node, COUNT(from_node) AS num_followers FROM social_network
    GROUP BY to_node) t;


-- Exemple d'utilisateur avec le nombre maximum de followers
select "Exemple d'utilisateur avec le nombre maximum de followers: " || to_node, COUNT(from_node) AS num_followers
FROM social_network
GROUP BY to_node
HAVING num_followers = (SELECT MAX(num_followers) FROM
    (SELECT to_node, COUNT(from_node) AS num_followers FROM social_network
    GROUP BY to_node) t) LIMIT 1;


-- Nombre minimum de followers par utilisateur
select "Nombre minimum de followers par utilisateur: " || MIN(num_followers) AS nb_min_followers FROM
    (SELECT to_node, COUNT(from_node) AS num_followers FROM social_network
    GROUP BY to_node) t;

-- Exemple d'utilisateur avec le nombre minimum de followers
select "Exemple d'utilisateur avec le nombre minimum de followers: " || to_node, COUNT(from_node) AS num_followers
FROM social_network
GROUP BY to_node
HAVING num_followers = (SELECT MIN(num_followers) FROM
    (SELECT to_node, COUNT(from_node) AS num_followers FROM social_network
    GROUP BY to_node) t) LIMIT 1;

