import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import app, db


app.config.from_object(os.environ['APP_CONFIG'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('migrate', MigrateCommand)


if __name__ == '__main__':
    manager.run()