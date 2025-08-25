import os
import json
import requests
import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler 

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/artists":
            try:
                # Get today's date
                today = datetime.datetime.now()
                month = today.month
                day = today.day
                
                wiki_url = f"https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/births/{month}/{day}"
                print(f"Fetching from: {wiki_url}")
                
                response = requests.get(wiki_url)
                print(f"Response status: {response.status_code}")
                
                if not response.ok:
                    raise Exception(f"Wikipedia API error: {response.status_code}")
                
                data = response.json()
                print(f"Data keys: {list(data.keys()) if isinstance(data, dict) else 'Not a dict'}")
                
                # Check if 'births' exists in the response
                if 'births' not in data:
                    print(f"Available data: {data}")
                    raise Exception("No 'births' data in Wikipedia response")
                
                # Filter musicians more strictly - look for music-related keywords in the text
                musicians = []
                for item in data['births']:
                    text = str(item.get('text', '')).lower()
                    # More specific music-related keywords
                    music_keywords = [
                        'musician', 'singer', 'rapper', 'band', 'composer', 
                        'guitarist', 'drummer', 'bassist', 'pianist', 'violinist',
                        'producer', 'songwriter', 'vocalist', 'performer'
                    ]
                    
                    if any(keyword in text for keyword in music_keywords):
                        # Add Wikipedia link to each musician
                        artist_name = item.get('text', '').split(',')[0]  # Get just the name
                        wiki_link = f"https://en.wikipedia.org/wiki/{artist_name.replace(' ', '_')}"
                        item['wiki_link'] = wiki_link
                        musicians.append(item)
                
                print(f"Found {len(musicians)} musicians out of {len(data['births'])} total births")

                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(musicians).encode())
            except Exception as e:
                print(f"Error in /api/artists: {str(e)}")
                self.send_response(500)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
            return
        # JSON API endpoint
        if self.path == "/api/data":
            data = {"name": "Harrison", "project": "HTTP Server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
            return
        
        # If user visits "/", serve index.html
        if self.path == "/":
            filepath = "static/index.html"
        else:
            # Remove leading "/" from path and append to static folder
            filepath = os.path.join("static", self.path.lstrip("/"))
            
        # Check if file exists
        if os.path.exists(filepath) and os.path.isfile(filepath):
            # Determine content type
            if filepath.endswith(".html"):
                content_type = "text/html"
            elif filepath.endswith(".css"):
                content_type = "text/css"
            elif filepath.endswith(".js"):
                content_type = "application/javascript"
            elif filepath.endswith(".png") or filepath.endswith(".jpg") or filepath.endswith(".jpeg") or filepath.endswith(".gif"):
                content_type = "image/" + filepath.split(".")[-1]
            else:
                content_type = "application/octet-stream"
                
            # Read and send file
            with open(filepath, "rb") as f:
                content = f.read()
                self.send_response(200)
                self.send_header("Content-type", content_type)
                self.end_headers()
                self.wfile.write(content)
        else:
            # File not found - send 404
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>404 - File Not Found</h1><p>The requested file could not be found.</p>")
       
if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), SimpleHandler)
    print("Server is running on http://localhost:8000")
    server.serve_forever()