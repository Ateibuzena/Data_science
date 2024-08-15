CREATE database IF NOT EXISTS tienda;
USE tienda;
CREATE table marca (
	marca_id int unsigned auto_increment NOT NULL,
    nombre varchar(255),
    primary key (marca_id)
    );
CREATE table categoria (
	categoria_id int unsigned auto_increment NOT NULL,
    nombre varchar(255),
    primary key (categoria_id)
    );
CREATE table modelo (
	modelo_id int unsigned auto_increment NOT NULL,
    nombre varchar(255),
    marca_id int unsigned,
    primary key (modelo_id),
    foreign key (marca_id) references marca (marca_id) ON DELETE CASCADE
    );
CREATE table cliente (
	cliente_id int unsigned auto_increment NOT NULL,
    nombre varchar(255),
    direccion varchar (255),
    correo_electronico varchar(255),
    primary key (cliente_id)
    );
CREATE table producto (
	producto_id int unsigned auto_increment NOT NULL,
    nombre varchar(255),
    descripcion text,
	precio decimal(10,2),
    stock int,
    marca_id int unsigned ,
    categoria_id int unsigned,
    modelo_id int unsigned,
    primary key (producto_id),
    foreign key (marca_id) references marca (marca_id) ON DELETE CASCADE,
    foreign key (categoria_id) references categoria (categoria_id) ON DELETE SET NULL,
    foreign key (modelo_id) references modelo (modelo_id) ON DELETE CASCADE
    );
CREATE table caracteristicas (
	caracteristica_id int unsigned auto_increment NOT NULL,
    tipo varchar(255),
    valor varchar(255),
    producto_id int unsigned,
    primary key (caracteristica_id),
    foreign key (producto_id) references producto (producto_id) ON DELETE CASCADE
    );
CREATE table venta (
	id int unsigned auto_increment NOT NULL,
    fecha_venta date,
    cantidad int unsigned,
    producto_id int unsigned,
    cliente_id int unsigned,
    primary key (id),
    foreign key (cliente_id) references cliente (cliente_id) ON DELETE SET NULL,
    foreign key (producto_id) references producto (producto_id) ON DELETE SET NULL    
    );
CREATE table devolucion (
	devolucion_id int unsigned auto_increment NOT NULL,
    fecha_devolucion date,
    cantidad int unsigned,
    producto_id int unsigned,
    cliente_id int unsigned,
    primary key (devolucion_id),
    foreign key (producto_id) references producto (producto_id) ON DELETE SET NULL,
    foreign key (cliente_id) references cliente (cliente_id) ON DELETE SET NULL
    );
CREATE table historial_precio (
	historial_precio_id int unsigned auto_increment NOT NULL,
    fecha_cambio_precio date,
    precio_anterior decimal(10,2),
    precio_actual decimal(10,2),
    producto_id int unsigned,
    primary key (historial_precio_id),
    foreign key (producto_id) references producto (producto_id) ON DELETE SET NULL
    );