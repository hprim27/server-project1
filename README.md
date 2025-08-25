# 🚀 Custom HTTP Server - Portfolio Project

A Python HTTP server built from scratch to showcase backend programming skills and full-stack development understanding.

## ✨ What This Project Demonstrates

- **Custom HTTP Server Implementation** - Built using Python's built-in libraries
- **Backend API Development** - Custom endpoints with external API integration
- **Full-Stack Architecture** - Server-side processing + frontend communication
- **Real-World API Integration** - Wikipedia API for dynamic content
- **Professional Code Quality** - Clean architecture and error handling

## 🛠️ Technologies Used

- **Python 3.x** - Core server language
- **http.server** - Built-in HTTP server framework
- **requests** - External API calls
- **HTML/CSS/JavaScript** - Frontend interface
- **Git** - Version control

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/server-project1.git
   cd server-project1
   ```

2. **Install dependencies**
   ```bash
   pip install requests
   ```

3. **Run the server**
   ```bash
   python server.py
   ```

4. **Open your browser**
   - Main portfolio: http://localhost:8000
   - Artist of the Day: http://localhost:8000/artist-of-day.html
   - About page: http://localhost:8000/about.html

## 📡 API Endpoints

### `/api/artists`
- **Method**: GET
- **Purpose**: Fetches musicians born on today's date
- **Features**: 
  - Real-time Wikipedia API integration
  - Server-side filtering for music artists
  - Automatic Wikipedia link generation
  - Dynamic date-based queries

### `/api/data`
- **Method**: GET
- **Purpose**: Returns basic project information
- **Response**: JSON with project details

## 🏗️ Project Structure

```
server-project1/
├── server.py              # Main HTTP server implementation
├── static/                # Static files served by the server
│   ├── index.html         # Main portfolio page
│   ├── about.html         # Project documentation
│   ├── artist-of-day.html # Interactive artist discovery
│   ├── style.css          # Main stylesheet
│   ├── artist-of-day.css  # Artist page styles
│   ├── script.js          # Frontend JavaScript
│   └── images/            # Portfolio images
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🎯 Key Features

### **HTTP Server Capabilities**
- Static file serving (HTML, CSS, JS, images)
- Custom API endpoint handling
- Proper HTTP status codes and headers
- Content-type detection and handling
- Error handling and 404 pages

### **API Integration**
- Wikipedia API consumption
- Real-time data fetching
- Server-side data processing
- JSON response formatting
- Error handling for external APIs

### **Frontend Features**
- Responsive portfolio design
- Interactive artist discovery
- Dynamic content loading
- Professional styling
- Cross-browser compatibility

## 🧠 Learning Outcomes

This project showcases understanding of:

- **HTTP Protocol** - Request/response handling, status codes, headers
- **API Development** - RESTful endpoints, data processing, error handling
- **Server Architecture** - Request routing, file serving, content delivery
- **External Integration** - Third-party API consumption and data processing
- **Full-Stack Development** - Backend logic + frontend communication

## 💼 Portfolio Value

This project demonstrates that I can:

- **Build from scratch** - Not just use frameworks
- **Understand web fundamentals** - HTTP, APIs, client-server architecture
- **Integrate external services** - Real-world API usage
- **Think architecturally** - Proper separation of concerns
- **Deliver working solutions** - Functional, production-ready code

## 🔧 Development

### **Adding New Endpoints**
```python
if self.path == "/api/new-endpoint":
    # Your custom logic here
    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps({"message": "New endpoint"}).encode())
    return
```

### **Serving New File Types**
```python
elif filepath.endswith(".pdf"):
    content_type = "application/pdf"
```

## 📚 Resources

- [Python http.server Documentation](https://docs.python.org/3/library/http.server.html)
- [HTTP Protocol](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [Wikipedia API Documentation](https://api.wikimedia.org/wiki/Main_Page)

## 🤝 Contributing

Feel free to contribute by:
- Adding new API endpoints
- Improving error handling
- Adding more file type support
- Enhancing the frontend design
- Adding tests and documentation

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Harrythewzrd** - Demonstrating Python backend development skills

---

**Note**: This is a learning project showcasing core networking concepts. For production use, consider established frameworks like Flask, FastAPI, or Django.
