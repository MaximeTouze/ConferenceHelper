#!/bin/bash
cd /var/www/multilingOEG22/;
echo `pwd`; 
source env/bin/activate
pip list > pip-env.log
set FLASK_APP=app.py;
echo $FLASK_APP;
flask run -p 443 2>error-run.log;
