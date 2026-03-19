from http.server import HTTPServer, BaseHTTPRequestHandler

class Servidor(BaseHTTPRequestHandler):


    def do_GET(self): #método get
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Servidor funcionando com GET")

def do_POST(self): #método post

    tamanho = int(self.headers['Content-Length']) #pega o tamanho dos dados da requisição

    dados = self.rfile.read(tamanho) #lê os dados

    print("Dados recebidos:", dados.decode()) #mostra os dados no terminal

    self.send_response(200) #envia o código "200" para o cliente quando a conexão da certo
    self.end_headers()
    self.wfile.write(b"POST recebido") #envia "post recebido" para o cliente quando der certo


HTTPServer(("0.0.0.0", 8000), Servidor).serve_forever()