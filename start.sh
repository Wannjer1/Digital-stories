export SECRET_KEY='vhtnbcgdhghgiuhidhgiuuhgiu'
export MAIL_USERNAME='minuteP1tchez@gmail.com'
export MAIL_PASSWORD='morganTracy139'

python3 manage.py server
# python3 manage.py shell
# python3 manage.py db init
# python3 manage.py db migrate -m 'new schema'
# python3 manage.py db upgrade
# python3 manage.py test

# git push heroku master
# heroku config:set SECRET_KEY='\x92\xdb\xfe\x13\xa0\x03\x17\x81\x15*\x89A\xa6Sj\x'
# heroku config:set MAIL_USERNAME=minuteP1tchez@gmail.com
# heroku config:set MAIL_PASSWORD=morganTracy139
# heroku addons:create heroku-postgresql
# heroku run python manage.py db init
# python manage.py db migrate -m "Initial deployment commit"
# heroku run python manage.py db upgrade