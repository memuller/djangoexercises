
Instrument                                 InstrumentType
--------------------------                 --------------------
 id         int autoinc           /----- 1  id     int autoinc
 name       varchar(200)          |         name   varchar(50)
 model      varchar(100)          |
 addedAt    datetime              |
 available  boolean               |
 kind       int            n <----/


https://docs.djangoproject.com/en/1.11/ref/models/fields/

# MySQL config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB_NAME',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# MySQL on C9
C9: env variables
IP
C9_USER
db: c9
port: 3306

mysql-ctl cli
mysql-ctl start

# Model querying
from polls.models import *

model.objects.all
objects.get(field=)
objects.filter(field=)

# Views
{{}} for printing
{% %} for running
