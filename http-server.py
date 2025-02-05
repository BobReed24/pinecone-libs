import argparse
import http.server
import socketserver
import flask
import sys

def run_server(ip, inbound_port, outbound_port):
    handler = http.server.SimpleHTTPRequestHandler

    server_address = (ip, inbound_port)
    httpd = socketserver.TCPServer(server_address, handler)

    print(f"Starting server on {ip}:{inbound_port} and redirecting to outbound port {outbound_port}...")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a local HTTP server.")
    parser.add_argument('--ip', type=str, default='127.0.0.1', help="IP address to bind the server to (default: 127.0.0.1)")
    parser.add_argument('--inbound-port', type=int, default=8080, help="Inbound port to bind the server to (default: 8080)")
    parser.add_argument('--outbound-port', type=int, default=8080, help="Outbound port for traffic redirection (default: 8000)")
    
    args = parser.parse_args()

    run_server(args.ip, args.inbound_port, args.outbound_port)
