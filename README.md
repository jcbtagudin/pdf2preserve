# 🔧 PDF2Preserve

A professional PDF to text conversion tool with advanced formatting preservation, smart text structuring, and multiple export formats.

![PDF2Preserve Demo](https://img.shields.io/badge/Status-Active-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Flask](https://img.shields.io/badge/Framework-Flask-red) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

### 🔄 Multiple Export Formats
- **Plain Text (.txt)** - Simple text extraction
- **HTML (.html)** - Preserves bold, italic, headings with proper styling
- **Markdown (.md)** - GitHub/Notion compatible with structure preservation
- **Word Document (.docx)** - Full formatting with paragraph alignment

### 📐 Smart Text Structuring
- **Heading Detection** - Font size & weight analysis (H1-H6)
- **List Recognition** - Bullets (•, -, *), numbered (1.), lettered (a.), roman (i.)
- **Table Extraction** - Automatic table detection with headers
- **Text Alignment** - Preserves left, center, right alignment
- **Paragraph Spacing** - Intelligent paragraph break detection

### 🧠 Side-by-Side Viewer
- **PDF.js Integration** - High-quality PDF rendering in browser
- **Real-Time Text** - Live text extraction alongside PDF view
- **Navigation Controls** - Page navigation, zoom, format switching
- **Professional UI** - Perfect for legal teams, editors, translators

### 🔁 Batch Conversion
- **Multi-File Upload** - Drag & drop multiple PDFs
- **Bulk Download** - ZIP archive with organized folder structure
- **Progress Tracking** - Real-time conversion progress
- **Error Recovery** - Individual file failure handling

### 🔐 Export Limits & Authentication
- **Free Tier** - 10 exports per day for guests
- **Logged-in Users** - 30 exports per day
- **Session Tracking** - Persistent credit tracking
- **Smart UI** - Real-time limit indicators

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/pdf2preserve.git
cd pdf2preserve
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open your browser**
Navigate to `http://127.0.0.1:5000`

## 📦 Dependencies

- **Flask** - Web framework
- **PyMuPDF** - PDF processing and text extraction
- **python-docx** - Word document generation
- **markdown** - Markdown processing

## 🎯 Usage Examples

### Single File Conversion
1. Visit the main page
2. Select your export format (TXT, HTML, MD, DOCX)
3. Choose layout mode (Preserve Structure or Clean Text)
4. Upload a PDF and download the converted file

### Side-by-Side Viewer
1. Click "🧠 Side-by-Side Viewer"
2. Upload a PDF to view alongside extracted text
3. Switch between text formats in real-time
4. Perfect for document review and translation

### Batch Processing
1. Click "🔁 Batch Converter"
2. Upload multiple PDF files
3. Select formats and processing options
4. Download ZIP archive with all conversions

## 🏗️ Architecture

```
pdf2preserve/
├── app.py              # Main Flask application
├── index.html          # Main conversion interface
├── viewer.html         # Side-by-side viewer
├── batch.html          # Batch conversion interface
├── requirements.txt    # Python dependencies
├── uploads/           # Temporary file storage
└── README.md          # Project documentation
```

### Core Components

- **PDFFormatter Class** - Advanced PDF processing with formatting detection
- **Export Tracking** - Session-based usage limits and authentication
- **Multi-Format Output** - HTML, Markdown, DOCX generation with alignment
- **Real-Time Processing** - AJAX-based file processing and progress tracking

## 🔧 Configuration

### Export Limits
```python
GUEST_DAILY_LIMIT = 10        # Free tier daily limit
LOGGED_IN_DAILY_LIMIT = 30    # Registered user limit
```

### Text Processing
- **Heading Detection** - Font size and weight thresholds
- **Alignment Detection** - Position-based left/center/right analysis
- **List Recognition** - Pattern matching for various list formats
- **Table Extraction** - PyMuPDF built-in table recognition

## 🎨 UI Features

- **Responsive Design** - Works on desktop and mobile
- **Professional Styling** - Modern gradient themes and animations
- **Real-Time Updates** - Live status indicators and progress bars
- **Error Handling** - User-friendly error messages and recovery

## 🔒 Security Features

- **Session Management** - Secure user session handling
- **File Cleanup** - Automatic temporary file removal
- **Input Validation** - PDF file type verification
- **Error Recovery** - Graceful handling of processing failures

## 🚀 Deployment

For production deployment:

1. **Set a secure secret key**
```python
app.secret_key = 'your-secure-secret-key-here'
```

2. **Use a production WSGI server**
```bash
pip install gunicorn
gunicorn app:app
```

3. **Configure environment variables**
- Database URL (for persistent user storage)
- File upload limits
- Export limits per user tier

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation** - Check this README for setup and usage
- **Issues** - Report bugs via GitHub Issues
- **Features** - Request new features via GitHub Discussions

## 🎯 Roadmap

- [ ] OCR support for scanned PDFs
- [ ] Cloud storage integration (Google Drive, Dropbox)
- [ ] API endpoints for programmatic access
- [ ] Advanced user management and teams
- [ ] Custom export templates
- [ ] PDF password protection handling

## 📊 Stats

- **Languages** - Python, HTML, CSS, JavaScript
- **Framework** - Flask web application
- **Processing** - PyMuPDF for PDF manipulation
- **Export Formats** - 4 different output formats
- **Features** - 20+ major features implemented

---

**Made with ❤️ for document processing workflows**

Perfect for legal teams, content creators, developers, and anyone who needs reliable PDF to text conversion with formatting preservation.