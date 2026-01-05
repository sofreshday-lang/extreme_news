import http.server
import socketserver
import os
import json
from api.news import handler as news_handler
from dotenv import load_dotenv

# .env 파일 로드 (부모 폴더 또는 현재 폴더)
load_dotenv()
if not os.environ.get("NAVER_CLIENT_ID"):
    load_dotenv("../.env")

PORT = 8000

class CombinedHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path.startswith('/api/news'):
            news_handler.do_POST(self)
        else:
            super().do_POST()

    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return super().do_GET()

    def do_OPTIONS(self):
        if self.path.startswith('/api/news'):
            news_handler.do_OPTIONS(self)
        else:
            super().do_OPTIONS()

print(f"서버가 http://localhost:{PORT} 에서 실행 중입니다.")
with socketserver.TCPServer(("", PORT), CombinedHandler) as httpd:
    httpd.serve_forever()
