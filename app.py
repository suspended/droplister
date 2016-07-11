import os
from droplister_application import app
from OpenSSL import SSL

__author__ = 'bryan'


root_dir = app.config['APP_ROOT']
server_key_file = os.path.join(root_dir, "ssl_certificates/server.key")
server_certificate_file = os.path.join(root_dir, "ssl_certificates/server.crt")

context = SSL.Context(SSL.SSLv23_METHOD)
context = (server_certificate_file, server_key_file)

#context.use_privatekey_file(server_key_file)
#context.use_certificate_file(server_certificate_file)


app.run(host='127.0.0.1', port=5800, debug=True, ssl_context=context)
# app.run(host='127.0.0.1', port=8090, debug=True)
