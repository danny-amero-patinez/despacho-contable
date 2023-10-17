-- Crear la tabla 'clientes'
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    direccion VARCHAR(100),
    regimen_fiscal VARCHAR(50)
);

-- Insertar algunos datos de ejemplo en la tabla 'clientes'
INSERT INTO clientes (nombre, apellido, direccion, regimen_fiscal)
VALUES
    ('Cliente1', 'Apellido1', 'Dirección1', 'Regimen1'),
    ('Cliente2', 'Apellido2', 'Dirección2', 'Regimen2'),
    ('Cliente3', 'Apellido3', 'Dirección3', 'Regimen3');

-- Crear la tabla 'usuarios'
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) NOT NULL,
    salt VARCHAR(32) NOT NULL,
    contraseña VARCHAR(100) NOT NULL,
    CONSTRAINT uq_nombre_usuario UNIQUE (nombre_usuario)
);

-- Generar una sal única y calcular el hash de la contraseña para el usuario 'ivan'
INSERT INTO usuarios (nombre_usuario, salt, contraseña)
VALUES
    ('ivan', 'unique_salt_for_ivan', SHA2(CONCAT('1234', 'unique_salt_for_ivan'), 256));

-- Crear la tabla 'administradores'
CREATE TABLE administradores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_admin VARCHAR(50) NOT NULL,
    salt VARCHAR(32) NOT NULL,
    contraseña VARCHAR(100) NOT NULL,
    CONSTRAINT uq_nombre_admin UNIQUE (nombre_admin)
);

-- Generar una sal única y calcular el hash de la contraseña para el administrador 'emmanuel'
INSERT INTO administradores (nombre_admin, salt, contraseña)
VALUES
    ('emmanuel', 'unique_salt_for_emmanuel', SHA2(CONCAT('123456', 'unique_salt_for_emmanuel'), 256));
