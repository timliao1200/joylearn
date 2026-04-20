#!/usr/bin/env python3
"""
享學課件本地儲存 Server
用途：讓瀏覽器的「下載儲存」能直接寫回專案資料夾

使用方式：
  cd projects/享學/courses
  python3 server.py

然後在瀏覽器開啟：
  http://localhost:8765/courses/week4-v2.html
"""

import json
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8765
COURSES_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(COURSES_DIR)          # 享學/ (parent)
VERSIONS_DIR = os.path.join(COURSES_DIR, "versions")
MAIN_FILE = os.path.join(COURSES_DIR, "week4-v2.html")


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def log_message(self, format, *args):
        if self.path in ("/save", "/"):
            super().log_message(format, *args)

    def _send_cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors()
        self.end_headers()

    def do_GET(self):
        # Legacy redirect: /week4-v2.html → /courses/week4-v2.html
        if self.path == "/week4-v2.html":
            self.send_response(302)
            self.send_header("Location", "/courses/week4-v2.html")
            self.end_headers()
            return
        super().do_GET()

    def do_POST(self):
        if self.path != "/save":
            self.send_error(404)
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        try:
            data = json.loads(body)
            filename = data["filename"]
            html = data["html"]
        except (json.JSONDecodeError, KeyError):
            self.send_error(400, "Invalid JSON")
            return

        # Sanitize filename — strip any path components
        filename = os.path.basename(filename)
        if not filename.endswith(".html"):
            filename += ".html"

        os.makedirs(VERSIONS_DIR, exist_ok=True)

        # Save versioned snapshot
        version_path = os.path.join(VERSIONS_DIR, filename)
        with open(version_path, "w", encoding="utf-8") as f:
            f.write(html)

        # Overwrite main file so next open sees the latest version
        with open(MAIN_FILE, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"  ✓ 已儲存：courses/versions/{filename}")
        print(f"  ✓ 已更新：courses/week4-v2.html")

        response = json.dumps({"ok": True, "saved": filename}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self._send_cors()
        self.end_headers()
        self.wfile.write(response)


def main():
    os.chdir(BASE_DIR)
    server = HTTPServer(("localhost", PORT), Handler)
    print(f"\n享學課件 Server 已啟動")
    print(f"  → 請在瀏覽器開啟：http://localhost:{PORT}/courses/week4-v2.html")
    print(f"  → 首頁（課程列表）：http://localhost:{PORT}/index.html")
    print(f"  → 版本存放於：{VERSIONS_DIR}")
    print(f"  → 按 Ctrl+C 停止\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer 已停止。")
        sys.exit(0)


if __name__ == "__main__":
    main()
