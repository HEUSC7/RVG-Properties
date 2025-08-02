# Let me download the RVG Properties files first and prepare them for GitHub upload
import requests
import os

# URLs of the RVG Properties files
files_to_download = {
    "index.html": "https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/cd990e3ba462fba8ec2f68c07a9649ef/b8ba426b-e07c-4a38-870c-fd47eb2b8660/index.html",
    "style.css": "https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/cd990e3ba462fba8ec2f68c07a9649ef/b8ba426b-e07c-4a38-870c-fd47eb2b8660/style.css", 
    "app.js": "https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/cd990e3ba462fba8ec2f68c07a9649ef/b8ba426b-e07c-4a38-870c-fd47eb2b8660/app.js"
}

# Create a directory for the project
project_dir = "RVG-Properties"
if not os.path.exists(project_dir):
    os.makedirs(project_dir)

# Download each file
for filename, url in files_to_download.items():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(project_dir, filename), 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"✅ Downloaded {filename} ({len(response.text)} characters)")
        else:
            print(f"❌ Failed to download {filename}: Status {response.status_code}")
    except Exception as e:
        print(f"❌ Error downloading {filename}: {e}")

# Create a README.md file for the project
readme_content = """# RVG Properties - Real Estate Platform

A comprehensive real estate website built with HTML, CSS, and JavaScript, featuring property listings, search functionality, and an admin dashboard.

## Features

### User Features
- 🏠 Property search and filtering
- 📱 Responsive design for all devices
- 💼 Property listing for sellers
- 🔍 Advanced search with multiple filters
- 📧 Contact system and inquiries
- ⭐ User reviews and testimonials

### Admin Features
- 🔐 Admin dashboard with login (rvgproperties@gmail.com / RVG@admin)
- 📊 Analytics and statistics
- ✅ Property approval workflow
- 👥 User management
- 📧 Inquiry management
- 🎯 Content management

## Technologies Used
- HTML5
- CSS3 (with Flexbox and Grid)
- JavaScript (Vanilla)
- Font Awesome Icons
- Google Fonts (Poppins)

## Getting Started

1. Clone the repository
2. Open `index.html` in your browser
3. For admin access, use credentials: rvgproperties@gmail.com / RVG@admin

## Project Structure
```
RVG-Properties/
├── index.html      # Main HTML file
├── style.css       # Styles and layout
├── app.js          # JavaScript functionality
└── README.md       # Project documentation
```

## Demo
The website includes sample properties, users, and data for demonstration purposes.

## License
This project is open source and available under the MIT License.
"""

with open(os.path.join(project_dir, "README.md"), 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("\n✅ Created README.md file")
print(f"\n📁 Project files are ready in the '{project_dir}' directory:")
print("   - index.html")
print("   - style.css") 
print("   - app.js")
print("   - README.md")
print("\nFiles are now ready to upload to GitHub!")