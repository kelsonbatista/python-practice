# Exercício 4: Agora vamos para a camada de transporte. Crie
# um servidor TCP usando o módulo socketserver que já vem embutido
# com o Python. Nosso servidor TCP deverá:

# Responder com um “Olá, client”, logo quando estabelecer uma conexão.
# Imprimir no console todo dado recebido.
# Responder com os dados recebidos (como um eco).
# Utilizar a porta 8085.

import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 8085

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
