"""
Simple Frontend Server
Serves the frontend with proper headers to avoid CORS issues
"""
import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "frontend"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print("=" * 60)
        print(f"Frontend Server Running!")
        print("=" * 60)
        print(f"\n🌐 Open your browser and go to:")
        print(f"\n   http://localhost:{PORT}/module.html")
        print(f"\n")
        print("✓ This server serves the frontend without CORS issues")
        print("✓ Make sure the backend is also running on port 5000")
        print("\nPress Ctrl+C to stop")
        print("=" * 60)
        httpd.serve_forever()
