import http.server
import socketserver
import json
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class PersistenceHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Set CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        if self.path == '/api/requirements':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            
            json_path = os.path.join(DIRECTORY, 'requerimientos.json')
            js_path = os.path.join(DIRECTORY, 'initial_data.js')
            
            data = []
            if os.path.exists(json_path):
                try:
                    with open(json_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    print(f"Loaded {len(data)} items from requerimientos.json")
                except Exception as e:
                    print("Error reading requerimientos.json:", e)
            elif os.path.exists(js_path):
                # Fallback: Parse from initial_data.js if json doesn't exist
                try:
                    with open(js_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    # Extract the JSON part from const INITIAL_REQUIREMENTS = [...]
                    start = content.find('[')
                    end = content.rfind(']') + 1
                    if start != -1 and end != -1:
                        data = json.loads(content[start:end])
                        print(f"Loaded {len(data)} items from initial_data.js fallback")
                except Exception as e:
                    print("Error parsing initial_data.js fallback:", e)
            
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api/requirements':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                requirements = json.loads(post_data.decode('utf-8'))
                if not isinstance(requirements, list):
                    raise ValueError("Data must be a list of requirements")
                
                # Write to requerimientos.json
                json_path = os.path.join(DIRECTORY, 'requerimientos.json')
                with open(json_path, 'w', encoding='utf-8') as f:
                    json.dump(requirements, f, indent=2, ensure_ascii=False)
                
                # Write to initial_data.js to synchronize it as well
                js_path = os.path.join(DIRECTORY, 'initial_data.js')
                with open(js_path, 'w', encoding='utf-8') as f:
                    f.write("// Datos iniciales de Requerimientos generados desde el Servidor\n")
                    f.write("const INITIAL_REQUIREMENTS = ")
                    json.dump(requirements, f, indent=2, ensure_ascii=False)
                    f.write(";\n")
                
                print(f"Successfully synchronized {len(requirements)} requirements on disk.")
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                response = {"status": "success", "message": f"Saved {len(requirements)} items successfully."}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
            except Exception as e:
                print("Error saving requirements:", e)
                self.send_response(400)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                response = {"status": "error", "message": str(e)}
                self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    # Enable reuse of the address
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), PersistenceHTTPRequestHandler) as httpd:
        print(f"Serving requirements tracker at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
            sys.exit(0)
