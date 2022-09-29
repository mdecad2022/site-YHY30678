from cmsimde import flaskapp
from gevent.pywsgi import WSGIServer

#flaskapp.app.run(host="0.0.0.0",debug=ture)
http_server = WSGISever(('0.0.0.0',8080),flaskapp.app)
http_server.server_forever()
