import os
# users/gilbertocotzajay/desktop/operator-68/week-5/in-class
basedir = os.path.abspath(os.path.dirname(__file__))

# gives access to the project in any os we find ourselves in and
# allows outside files/folders to be added to the project from
# the base directory.


class Config:
    """" 
    set configuration variables for our falsk app here
    eventually will use hidden variable items - but for now, we'll leave them exposed in config
    """
    SECRET_KEY = "You will never guess..."
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATION = False
