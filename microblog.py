from app_package import app
import random
import sqlalchemy as sa
import sqlalchemy.orm as so
from app_package import app, db
from app_package.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
  #app.run(host='0.0.0.0', debug=True)
  app.run(host='0.0.0.0')
  #app.run(host='0.0.0.0', port=random.randint(2000, 9000))  # Debugger