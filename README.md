#-----------------------------------------------------------------------------
# WEBAPP: Dashboard by Nikos
#-----------------------------------------------------------------------------
# Infra y recursos
* Lenguaje y framework:
    * Python (vs 3)
    * Pyramid (vs 1.9.2)
* SO:
    * Ubuntu (vs 16.04.5 LTS Xenial Xerus)
* Database: 
    * PostgreSQL (vs 9.5)
    * ORM: SQLAlchemy
    * TM para DB: zope.sqlalchemy
        
# Documentos:
* environment.md
    * full step by step para install del ambiente y recursos
* README.md
    * este documento
* howto.md
    * Que es? y como se armo este proyecto?
* task.md
    * Scope y tareas
 
#-----------------------------------------------------------------------------
# Install de WEBAPP: Dashboard by Nikos
#-----------------------------------------------------------------------------

PostgreSQL DB
--------------------

## Setup PostgreSQL
vim /etc/postgresql/9.5/main/pg_hba.conf

    # Database administrative login by Unix domain socket
    # esta linea no hace falta agregarla, es default de una instalacion normal de psotgresl
    # se agrega con fines de informacion, y recordatorioa para agregarla en caso de ausencia
    local   all             postgres                                peer

    # dashboard setup
    local   dashboard    dashboard                                    peer
    host    dashboard    dashboard            127.0.0.1/32               md5

service postgresql restart

## Recursos, CREATE
rm /tmp/dashboard-db-create.psql

echo "
CREATE USER dashboard;
ALTER USER dashboard WITH ENCRYPTED PASSWORD 'securePassword';
CREATE DATABASE dashboard OWNER dashboard;
" >> /tmp/dashboard-db-create.psql

cat /tmp/dashboard-db-create.psql

sudo -u postgres psql postgres < /tmp/dashboard-db-create.psql

rm /tmp/dashboard-db-create.psql

Dashboard by Nikos: install
-------------------------------
cd workspace

git clone URLgithub

cd proyecto

pwd
* copiar PATH y crear variable de entorno

export VENV=PATH

export 
VENV=/media/littleBoss/workspaceDev/nikos/repos-nikos/training/training_python/pyramid/kenwin_exercise

echo $VENV
* se deberia observar el path completo

Dashboard by Nikos: virtual environment
-------------------------------
cd $VENV

pipenv install

pipenv shell

pip install -e .

Dashboard by Nikos: modelos de base de datos
-------------------------------
cd $VENV

initialize_dashboard_db development.ini

initialize_dashboard_db production.ini

Dashboard by Nikos: ejecutar e iniciar el server en modo develop/debug
-------------------------------
cd $VENV

pip install pyramid_debugtoolbar

pserve $VENV/development.ini --reload

Dashboard by Nikos: ejecutar e iniciar el server en modo production
-------------------------------
cd $VENV

pserve $VENV/production.ini --reload

Dashboard by Nikos: uso
-------------------------------

# url home y login
http://localhost:6543/
* autorizado para ALL
* es el home del proyecto
* permite llamar e iniciar el login en la app


# url zona segura
http://localhost:6543/dashboard
* escenario user ya logueado
    * permite acceso
    * permite logout
* escenario user sin login
    * impide acceso
    * pide login
* nota:
    * deberia poder verse el dashboard: Sufee HTML5 Admin Dashboard Template
* credenciales de acceso:
    * usuario: admin
    * password: admin


 
#-----------------------------------------------------------------------------
# Informacion adicional para Debug y Troubleshooting
#-----------------------------------------------------------------------------

# PostgreSQL DB
## PostgreSQL password reset
* no necesario, pero si hiciera falta
sudo -u postgres psql

    psql (9.5.14)

    Type "help" for help.

    postgres=# ALTER USER postgres PASSWORD 'toor';

## Recursos, DROP all
rm /tmp/dashboard-db-drop.psql

echo "
DROP DATABASE dashboard;
DROP USER dashboard;
" >> /tmp/dashboard-db-drop.psql

cat /tmp/dashboard-db-drop.psql

sudo -u postgres psql postgres < /tmp/dashboard-db-drop.psql

rm /tmp/dashboard-db-drop.psql

## test: db
### connection
sudo -u postgres psql -h 127.0.0.1 -U dashboard -W -d dashboard

    securePassword

### derechos sobre recursos
dashboard=> CREATE TABLE test (id INTEGER PRIMARY KEY, name VARCHAR);
    CREATE TABLE

dashboard=> \dt
            List of relations
    Schema | Name  | Type  |   Owner   
    --------+-------+-------+-----------
    public | leads | table | dashboard
    (1 row)

dashboard=> drop table test;

    DROP TABLE

dashboard=> \dt
    No relations found.
