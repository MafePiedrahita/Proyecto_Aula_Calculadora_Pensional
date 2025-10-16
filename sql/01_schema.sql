-- 1. Aportante (persona)
CREATE TABLE IF NOT EXISTS aportante (
  aportante_id SERIAL PRIMARY KEY,
  tipo_doc     VARCHAR(5)  NOT NULL CHECK (tipo_doc IN ('CC','CE','TI','PA')),
  nro_doc      VARCHAR(30) NOT NULL UNIQUE,
  nombres      VARCHAR(80) NOT NULL,
  apellidos    VARCHAR(80) NOT NULL,
  fecha_nac    DATE        NOT NULL,
  salario_prom NUMERIC(14,2) NOT NULL CHECK (salario_prom >= 0),
  semanas_cot  INTEGER NOT NULL CHECK (semanas_cot >= 0),
  edad         INTEGER NOT NULL CHECK (edad >= 0)
);

-- 2. Fondo privado (catálogo)
CREATE TABLE IF NOT EXISTS fondo_privado (
  fondo_id SERIAL PRIMARY KEY,
  nombre   VARCHAR(40) NOT NULL UNIQUE
);

INSERT INTO fondo_privado(nombre) VALUES ('Protección'),('Porvenir'),('Colfondos')
ON CONFLICT DO NOTHING;

-- 3. Cotización/ahorro histórico (resumen por aportante)
CREATE TABLE IF NOT EXISTS cotizacion (
  cotizacion_id SERIAL PRIMARY KEY,
  aportante_id  INTEGER NOT NULL REFERENCES aportante(aportante_id) ON DELETE CASCADE,
  fondo_id      INTEGER REFERENCES fondo_privado(fondo_id),
  saldo_acum    NUMERIC(16,2) NOT NULL CHECK (saldo_acum >= 0), -- para privados
  semanas_rep   INTEGER NOT NULL CHECK (semanas_rep >= 0),       -- para RPM
  periodo       DATERANGE NOT NULL,                               -- [inicio, fin)
  CHECK (lower(periodo) < upper(periodo))
);

-- 4. Simulación calculada (resultado)
CREATE TABLE IF NOT EXISTS simulacion (
  simulacion_id SERIAL PRIMARY KEY,
  aportante_id  INTEGER NOT NULL REFERENCES aportante(aportante_id) ON DELETE CASCADE,
  pilar         VARCHAR(10) NOT NULL CHECK (pilar IN ('PUBLICO','PRIVADO')),
  pension_mens  NUMERIC(16,2) NOT NULL CHECK (pension_mens >= 0),
  supuestos     JSONB NOT NULL,
  creado_en     TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Índices útiles
CREATE INDEX IF NOT EXISTS idx_cotiz_aportante ON cotizacion(aportante_id);
CREATE INDEX IF NOT EXISTS idx_sim_aportante  ON simulacion(aportante_id);
