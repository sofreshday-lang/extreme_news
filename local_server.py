import http.server
import socketserver
import os
import json
from api.news import handler

PORT = 8000

# .env 파일을 수동으로 로드하는 함수 (사용자 규칙 가이드를 준수하며 환경 변수만 설정)
def load_env():
    # 현재 폴더 또는 상위 폴더에서 .env 탐색
    env_paths = [
        os.path.join(os.getcwd(), '.env'),
        os.path.join(os.path.dirname(os.getcwd()), '.env')
    ]
    for path in env_paths:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    if '=' in line and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        # 따옴표 제거 및 환경 변수 설정
                        os.environ[key] = value.strip('"').strip("'")
            print(f"✅ 환경 변수 로드 완료: {path}")
            return True
    return False

class LocalHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path.startswith('/api/news'):
            # API 핸들러 호출
            api_handler = handler(self.request, self.client_address, self.server)
            return
        else:
            super().do_POST()

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

    def do_OPTIONS(self):
        if self.path.startswith('/api/news'):
            api_handler = handler(self.request, self.client_address, self.server)
            return
        else:
            super().do_OPTIONS()

if __name__ == "__main__":
    if not load_env():
        print("⚠️ 경고: .env 파일을 찾을 수 없습니다. 환경 변수가 시스템에 설정되어 있지 않으면 오류가 발생할 수 있습니다.")
    
    with socketserver.TCPServer(("", PORT), LocalHandler) as httpd:
        print(f"🚀 서버 실행 중: http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n서버를 종료합니다...")
            httpd.server_close()
