# import socket
#
# HOST = 'http://35.226.102.237/'  # Standard loopback interface address (localhost)
# PORT = 8080        # Port to listen on (non-privileged ports are > 1023)
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
# s.listen(10)
# while True:
#     conn, addr = s.accept()
#     print('Connected by', addr)
#     data = conn.recv(1024)
#     if not data:
#         break
#     conn.sendall(data)
# s.close()
import bottle

@bottle.route("/")
def home():
    return "hewwo"

bottle.run(host="0.0.0.0", port=80, debug=True)
