USE `curso-24165`;

CREATE TABLE usuarios (
  id INT NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  activo BOOLEAN NOT NULL,
  PRIMARY KEY (id)
);