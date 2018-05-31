from app.api.api import app 
# flask instance
from instance.config import app_config
# enviromnent configurations setting


if __name__ =="__main__":
    app.config.from_object(app_config['development'])
    app.run