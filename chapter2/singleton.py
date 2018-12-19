#!/bin/python3

class SingletonMeta(type):
  _instance_registry = {}    #Build an instance registry which tracks the different class objects
  def __call__(cls, *args, **kwargs):
    if cls not in cls._instance_registry:    # check, if the class has already been instantiated
      cls._instance_registry[cls] = super().__init__(*args, **kwargs)
    return cls._instance_registry[cls]

class Database(metaclass=SingletonMeta):
  def __init__(self, hostname, port, username, password, dbname, **kwargs):
    """Initialize the databases
    Initializes the database class, establishing a connection with the database and providing
    the functionality to call the database.
    :params hostname: The hostname on which the database server runs
    :parms port: The port on which database is listening
    :params username: The username to connect to database
    :params password: The password to connect to the database
    :params dbname: The name of the database to connect to
    """
    self.uri = build_uri(hostname, port, username, password, dbname)
    #self.db = connect_db()
    self.db_opts = kwargs
    #self.set_db_opts()

  def connect_db(self):
    """Establish a connection with the database."""
    pass
  def set_db_opts(self):
    """Setup the database connection options."""
    pass
