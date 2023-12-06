USE sakila;

SELECT 
    title, description
FROM
    film;
---------------
SELECT 
    *
FROM
    customer;
---------------
SELECT 
    *
FROM
    actor;
--------------
SELECT 
    first_name, last_name
FROM
    actor;

-- WHERE
SELECT 
    *
FROM
    film
WHERE
    release_year = 2006;
    
--
SELECT 
    *
FROM
    customer
WHERE
    first_name = 'Jamie';
--

SELECT 
    *
FROM
    payment
WHERE
    amount <> 0.99;
--

SELECT 
    *
FROM
    film
WHERE
    title LIKE 'B%';
--

SELECT 
    *
FROM
    customer
WHERE
    store_id = 1 AND active = 1;
--

SELECT 
    *
FROM
    customer
WHERE
    last_name IN ('Smith' , 'Johnson', 'Williams');

-- ORDER BY
SELECT 
    *
FROM
    customer
ORDER BY last_name ASC;

-- LIMIT 
SELECT 
    *
FROM
    rental
LIMIT 10;

-- AGG FUNCTIONS
SELECT 
    COUNT(*)
FROM
    inventory;
--

SELECT 
    AVG(length)
FROM
    film;
--

SELECT 
    AVG(rental_rate)
FROM
    film;
--

SELECT 
    SUM(amount)
FROM
    payment;
--

SELECT 
    MAX(rental_rate)
FROM
    film;
--

SELECT 
    MIN(replacement_cost)
FROM
    film;
--

SELECT 
    COUNT(*)
FROM
    customer;
--

SELECT 
    COUNT(DISTINCT language_id)
FROM
    film;

-- AGG FUNTIONS GROUP BY
SELECT 
    country_id, COUNT(*)
FROM
    city
GROUP BY country_id;
--

SELECT 
    rating, AVG(rental_rate), SUM(rental_rate), MAX(rental_rate)
FROM
    film
GROUP BY rating;
--

SELECT 
    rating, COUNT(*)
FROM
    film
GROUP BY rating;
--

SELECT 
    customer_id, MAX(amount) AS max_payment
FROM
    payment
GROUP BY customer_id;
--

SELECT 
    staff_id, SUM(amount), AVG(amount)
FROM
    payment
GROUP BY staff_id;

-- HAVING
SELECT 
    rating, COUNT(*)
FROM
    film
GROUP BY rating
HAVING COUNT(*) > 200;
--

SELECT 
    length, AVG(rental_rate)
FROM
    film
GROUP BY length
HAVING AVG(rental_rate) > 2.5;
---

SELECT 
    customer_id,
    COUNT(*) AS total_rentals,
    AVG(amount) AS average_payment
FROM
    payment
GROUP BY customer_id
HAVING total_rentals > 30 AND average_payment > 3.0;

---
SELECT 
    customer_id,
    COUNT(*) AS total_rentals,
    AVG(amount) AS average_payment
FROM
    payment
GROUP BY customer_id
HAVING average_payment BETWEEN 3.00 AND 3.50;


-- JOIN
SELECT 
    *
FROM
    rental
        JOIN
    customer ON rental.customer_id = customer.customer_id;
--

SELECT 
    customer.store_id, AVG(payment.amount) AS average_payment
FROM
    payment
        JOIN
    customer ON payment.customer_id = customer.customer_id
GROUP BY customer.store_id;
--

SELECT 
    film.title, inventory.inventory_id, inventory.store_id
FROM
    film
        JOIN
    inventory ON film.film_id = inventory.film_id
WHERE
    film.rating = 'PG-13'
        AND inventory.store_id = 2;
--

SELECT 
    customer.first_name,
    customer.last_name,
    SUM(payment.amount) AS total_payments
FROM
    customer
        JOIN
    payment ON customer.customer_id = payment.customer_id
        JOIN
    rental ON payment.rental_id = rental.rental_id
WHERE
    rental.return_date >= '2005-08-01'
        AND rental.return_date < '2005-09-01'
GROUP BY customer.customer_id
HAVING total_payments > 50;


/*SELECT 
    rental_duration,
    rating,
    MIN(length) AS min_length,
    MAX(length) AS max_length,
    SUM(length) AS sum_length,
    ROUND(AVG(length), 3) AS avg_length,
    COUNT(length) AS total_length
FROM
    film
WHERE 
	rental_rate < 1.00
GROUP BY rental_duration , rating
HAVING AVG(rental_rate) > 0 AND min_length > 60 AND rating = "R"
ORDER BY rental_duration , rating
LIMIT 4; */

/*SELECT 
    store_id, COUNT(store_id)
FROM
    customer
GROUP BY
	store_id;*/
    
    
SELECT * FROM actor;



