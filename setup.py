from setuptools import setup

requires = [
    'bcrypt', # Modern password hashing for your software and your servers
    'deform', # library for generating HTML forms on the server side
    'psycopg2', # DB, PostgreSQL database adapter
    'pyramid', # lightweight Python web framework
    'pyramid_chameleon', # Chameleon template compiler
    'pyramid_tm', # transaction manager, allows Pyramid requests to join the active transaction
    'sqlalchemy', # DB, SQL Toolkit and Object Relational Mapper
    'waitress', # WSGI server. It supports HTTP/1.0 and HTTP/1.1.
    'wtforms', # flexible forms validation and rendering library
    'zope.sqlalchemy', # DB transaction management
]

setup(name='dashboard',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = dashboard:main
      [console_scripts]
      initialize_dashboard_db = dashboard.initialize_db:main
      """,
)