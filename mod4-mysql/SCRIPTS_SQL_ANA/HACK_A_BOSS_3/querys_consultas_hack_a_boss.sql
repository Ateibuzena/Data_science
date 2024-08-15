USE hack_a_boss;

-- ¿Que bootcamp tiene más estudiantes?
SELECT bootcamp, count(estudiantes.estudiante_id) as numero_alumnos
FROM bootcamps
JOIN estudiantes
ON bootcamps.bootcamp_id =  estudiantes.bootcamp_id
GROUP BY bootcamps.bootcamp
ORDER BY numero_alumnos desc limit 1;

-- ¿Cuantos bootcamps no tienen estudiantes?
SELECT bootcamp, count(estudiantes.estudiante_id) as numero_alumnos
FROM bootcamps
JOIN estudiantes
ON bootcamps.bootcamp_id =  estudiantes.bootcamp_id
GROUP BY bootcamps.bootcamp
HAVING numero_alumnos = 0;

-- ¿Que estudiantes tienen más asistencias?
SELECT nombre, sum(asistencias.asistencia) as numero_asistencias
FROM estudiantes
JOIN asistencias
ON estudiantes.estudiante_id =  asistencias.estudiante_id
GROUP BY nombre
ORDER BY numero_asistencias desc;

-- ¿Que estudiantes tienen menos asistencias?
SELECT nombre, sum(asistencias.asistencia) as numero_asistencias
FROM estudiantes
JOIN asistencias
ON estudiantes.estudiante_id =  asistencias.estudiante_id
GROUP BY nombre
ORDER BY numero_asistencias;

-- ¿Que modulo tiene mas puntuación de media?
SELECT modulos.modulos, mb.modulo_id, AVG(mb.puntuacion) as media_puntuacion
FROM modulo_bootcamp mb
JOIN modulos
ON mb.modulo_id = modulos.modulo_id
GROUP BY mb.modulo_id
ORDER BY media_puntuacion DESC LIMIT 1;

-- ¿Que modulo tiene menos puntuación de media?
SELECT modulos.modulos, mb.modulo_id, AVG(mb.puntuacion) as media_puntuacion
FROM modulo_bootcamp mb
JOIN modulos
ON mb.modulo_id = modulos.modulo_id
GROUP BY mb.modulo_id
ORDER BY media_puntuacion LIMIT 1;

-- ¿Qué bootcamp tiene mayor puntuación de media?
SELECT 
	bootcamps.bootcamp, 
	mb.bootcamp_id, 
	AVG(mb.puntuacion) as media_puntuacion
FROM modulo_bootcamp mb
JOIN bootcamps
ON mb.bootcamp_id = bootcamps.bootcamp_id
GROUP BY bootcamp_id
ORDER BY media_puntuacion DESC LIMIT 1;

-- ¿Qué bootcamp tiene mas asistencias?
SELECT tabla1.bootcamp, sum(n_asistencias) as total_asistencias
FROM (SELECT b.bootcamp, sum(asistencias.asistencia) as n_asistencias
FROM asistencias 
JOIN estudiantes e
ON asistencias.estudiante_id = e.estudiante_id
JOIN bootcamps b
ON e.bootcamp_id = b.bootcamp_id
GROUP BY asistencias.estudiante_id
ORDER BY n_asistencias DESC) tabla1
GROUP BY tabla1.bootcamp
ORDER BY total_asistencias DESC LIMIT 1;

-- ¿Qué bootcamp tiene menos asistencias?
SELECT tabla1.bootcamp, sum(n_asistencias) as total_asistencias
FROM (SELECT b.bootcamp, sum(asistencias.asistencia) as n_asistencias
FROM asistencias 
JOIN estudiantes e
ON asistencias.estudiante_id = e.estudiante_id
JOIN bootcamps b
ON e.bootcamp_id = b.bootcamp_id
GROUP BY asistencias.estudiante_id
ORDER BY n_asistencias DESC) tabla1
GROUP BY tabla1.bootcamp
ORDER BY total_asistencias LIMIT 1;

-- Otra manera de responder a la pregunta ¿Qué bootcamp tiene más asistencias?
SELECT b.bootcamp, COUNT(a.asistencia) AS total_asistencias
FROM asistencias a
JOIN estudiantes e ON a.estudiante_id = e.estudiante_id
JOIN bootcamps b ON e.bootcamp_id = b.bootcamp_id
WHERE a.asistencia = True 
GROUP BY b.bootcamp
ORDER BY total_asistencias DESC LIMIT 1;

-- Otra manera de responder a la pregunta ¿Qué bootcamp tiene menos asistencias?
SELECT b.bootcamp, COUNT(a.asistencia) AS total_asistencias
FROM asistencias a
JOIN estudiantes e ON a.estudiante_id = e.estudiante_id
JOIN bootcamps b ON e.bootcamp_id = b.bootcamp_id
WHERE a.asistencia = True 
GROUP BY b.bootcamp
ORDER BY total_asistencias LIMIT 1;

-- ¿Qué día tiene el mayor número de asistencias?
SELECT asistencias.fecha, count(asistencias.asistencia) as n_asistencias
FROM asistencias
WHERE asistencias.asistencia = True
GROUP BY asistencias.fecha
ORDER BY n_asistencias DESC LIMIT 1;

-- ¿Qué día tiene el menor número de asistencias?
SELECT asistencias.fecha, count(asistencias.asistencia) as n_asistencias
FROM asistencias
WHERE asistencias.asistencia = True
GROUP BY asistencias.fecha
ORDER BY n_asistencias LIMIT 1;

-- ¿Cuales bootcamps le dan 10 al modulo de Machine Learning?
SELECT bootcamps.bootcamp, modulos.modulos, modulo_bootcamp.puntuacion
FROM modulos
JOIN modulo_bootcamp ON modulos.modulo_id = modulo_bootcamp.modulo_id
JOIN bootcamps ON modulo_bootcamp.bootcamp_id = bootcamps.bootcamp_id
WHERE modulos.modulos = "Machine Learning" AND modulo_bootcamp.puntuacion = 10
GROUP BY bootcamps.bootcamp;

-- Muestra los estudiantes del bootcamp que tenga más asistencias.
SELECT e.nombre, b.bootcamp
FROM estudiantes e
JOIN bootcamps b ON e.bootcamp_id = b.bootcamp_id
WHERE b.bootcamp_id = (SELECT b.bootcamp_id
					   FROM asistencias a
					   JOIN estudiantes e ON a.estudiante_id = e.estudiante_id
					   JOIN bootcamps b ON e.bootcamp_id = b.bootcamp_id
					   WHERE a.asistencia = True 
					   GROUP BY b.bootcamp_id
					   ORDER BY COUNT(a.asistencia) DESC LIMIT 1);

