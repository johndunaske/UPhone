import socket
import threading
import translate

tLock = threading.Lock()
shutdown = False

def receving(name, sock):
     while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)


                if data.decode()[:4] == "John":
                    string = translate.translate_text(str(data.decode()), 'es')
                    print (str(string))
                elif data.decode()[:3] == "Ale":
                    string = translate.translate_text(str(data.decode()), 'en')
                    print (str(string))
        except:
            pass
        finally:
            tLock.release()

host = '127.0.0.1'
port = 0

server = ('127.0.0.1',5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receving, args=("RecvThread",s))
rT.start()

alias = raw_input("Name: ")
message = raw_input(alias + "-> ")
while message != 'q':
    if message != '':
        toSend = alias + ": " + message
        s.sendto(toSend.encode(), server)
    tLock.acquire()
    message = raw_input(alias + "-> ")
    tLock.release()
    ##time.sleep(0.2)

shudown = True
rT.join()
s.close()
