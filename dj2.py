import requests

image_url = "https://media.geeksforgeeks.org/wp-content/uploads/20230505175603/100-Days-of-Machine-Learning.webp"
output_filename = "gfg_logo.png"

response = requests.get(image_url)

if response.status_code == 200:
	with open(output_filename, "wb") as file:
		file.write(response.content)
	print(f"Image downloaded successfully as {output_filename}")
else:
	print("Failed to download the image.")

