-- Script SQL - RecetaAPI
-- Base de datos: recetario_db

CREATE DATABASE IF NOT EXISTS recetario_db;
USE recetario_db;

-- Tabla recetas
CREATE TABLE IF NOT EXISTS recetas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    categoria VARCHAR(100),
    area VARCHAR(100),
    instrucciones TEXT,
    imagen VARCHAR(500),
    fecha_guardado DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla ingredientes
CREATE TABLE IF NOT EXISTS ingredientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    medida VARCHAR(100),
    id_receta INT NOT NULL,
    FOREIGN KEY (id_receta) REFERENCES recetas(id) ON DELETE CASCADE
);

-- Consulta util 1: Ver recetas con sus ingredientes
SELECT r.nombre, r.categoria, r.area, i.nombre AS ingrediente, i.medida
FROM recetas r
JOIN ingredientes i ON r.id = i.id_receta
ORDER BY r.nombre;

-- Consulta util 2: Contar ingredientes por receta
SELECT r.nombre, COUNT(i.id) AS total_ingredientes
FROM recetas r
LEFT JOIN ingredientes i ON r.id = i.id_receta
GROUP BY r.id, r.nombre;

-- Consulta util 3: Recetas por categoria
SELECT categoria, COUNT(*) AS total_recetas
FROM recetas
GROUP BY categoria
ORDER BY total_recetas DESC;