$uri = "http://localhost:5000/download"
$headers = @{
    "Content-Type" = "application/json"
}
$body = @{
    "video_url" = "https://www.tiktok.com/@asmr_segments/video/7268358314453503239?is_from_webapp=1&sender_device=pc&web_id=7272443566856439301"
}

$response = Invoke-WebRequest -Uri $uri -Method POST -Headers $headers -Body ($body | ConvertTo-Json) -ContentType "application/json" -UseBasicParsing

# Display the response content (e.g., the downloaded video file)
$response.Content
$ curl -X POST -H "Content-Type: application/json" -d '{"video_url": "https://www.tiktok.com/@tiktok/video/7106594312292453675?is_copy_url=1&is_from_webapp=v1"}' http://localhost:5000/download
