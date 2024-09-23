from flask import Flask, send_file, render_template_string
import pdfkit
import os

app = Flask(__name__)

# Define an API route to generate PDF
@app.route('/generate-pdf', methods=['GET'])
def generate_pdf():
    # Your HTML content for the PDF
    html_content = '''
    <html>
    <head>
        <title>Sample PDF</title>
    </head>
    <body>
        <h1>Hello, this is a PDF document!</h1>
        <p>This is a sample paragraph in the PDF.</p>
    </body>
    </html>
    '''
    
    # Generate the PDF file from HTML string
    pdf_file_path = 'output.pdf'
    pdfkit.from_string(html_content, pdf_file_path)

    # Send the generated PDF file as a downloadable response
    return send_file(pdf_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
