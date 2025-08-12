from flask import Flask, request, jsonify
import fitz  # PyMuPDF
import tempfile
import os
import json
import base64
from io import BytesIO

app = Flask(__name__)

def handler(request):
    """Main Vercel serverless function handler"""
    if request.method == 'POST':
        try:
            # Get file from request
            if 'pdf_file' not in request.files:
                return jsonify({"error": "No PDF file provided"}), 400
            
            file = request.files['pdf_file']
            export_format = request.form.get('export_format', 'txt')
            layout_mode = request.form.get('layout_mode', 'preserve')
            
            # Process in memory instead of file system
            pdf_data = file.read()
            
            # Open PDF from memory
            doc = fitz.open(stream=pdf_data, filetype="pdf")
            
            if export_format == "txt":
                # Simple text extraction
                full_text = ""
                for page in doc:
                    full_text += page.get_text("text") + "\n"
                
                doc.close()
                
                return jsonify({
                    "success": True,
                    "content": full_text,
                    "format": "txt",
                    "filename": f"{file.filename.rsplit('.', 1)[0]}.txt"
                })
            
            elif export_format == "html":
                # Basic HTML extraction
                html_content = ['<!DOCTYPE html>', '<html>', '<head>', 
                               '<meta charset="UTF-8">', '<title>PDF Content</title>', 
                               '</head>', '<body>']
                
                for page in doc:
                    blocks = page.get_text("dict")["blocks"]
                    for block in blocks:
                        if "lines" in block:
                            for line in block["lines"]:
                                line_text = ""
                                for span in line["spans"]:
                                    text = span["text"].strip()
                                    if text:
                                        flags = span["flags"]
                                        is_bold = bool(flags & 2**4)
                                        is_italic = bool(flags & 2**1)
                                        
                                        if is_bold and is_italic:
                                            text = f'<strong><em>{text}</em></strong>'
                                        elif is_bold:
                                            text = f'<strong>{text}</strong>'
                                        elif is_italic:
                                            text = f'<em>{text}</em>'
                                        
                                        line_text += text + ' '
                                
                                if line_text.strip():
                                    html_content.append(f'<p>{line_text.strip()}</p>')
                
                html_content.extend(['</body>', '</html>'])
                doc.close()
                
                return jsonify({
                    "success": True,
                    "content": '\n'.join(html_content),
                    "format": "html",
                    "filename": f"{file.filename.rsplit('.', 1)[0]}.html"
                })
            
            else:
                doc.close()
                return jsonify({"error": "Unsupported format for serverless"}), 400
                
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    return jsonify({"error": "Method not allowed"}), 405

# Export for Vercel
def api_handler(request):
    return handler(request)