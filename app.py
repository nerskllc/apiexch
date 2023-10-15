from flask import Flask, request, send_file, jsonify
from handlers.tikdler import get_video

app = Flask(__name__)

# API information dictionary 
api_info = {
    "name": "TikDl API",
    "description": "Advanced Tik Tok Downloader API",
    "version": "1.0",
    "creator": "api-exchange",
    "github_repo": "https://github.com/yourusername/api-exchange",
}

@app.route('/')
def home():
    return jsonify(api_info)


@app.route('/download', methods=['POST'])
def download_video():
        # Get the video URL from the request body
    video_url = request.json['video_url']

    if not video_url:
        return jsonify({"error": "Video URL is required"}), 400

        # Download the video
    download_response = get_video(video_url)
    
    return jsonify(download_response)

if __name__ == '__main__':
    app.run(debug=True)