import socket
import khongketnoimang
def is_connected():
    try:
        # connect to the Host -- tells us if the Host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False
def main():
    if is_connected() ==True:
        import kiemtraquyen as kt
        kt.main()
    else: khongketnoimang.main()

if __name__ == "__main__":
    main()