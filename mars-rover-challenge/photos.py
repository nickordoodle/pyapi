#!/usr/bin/python3

import requests
import pprint as pprint

def main():

    all_rovers = ['curiosity', 'opportunity', 'spirit']
    all_cams = ["FHAZ", "RHAZ", "MAST", "CHEMCAM", "NAVCAM"]
    user_cam_input = input(f"Which camera do you want the pictures from: {' '.join(all_cams)} >>").strip().upper()

    # Return links of one photo from each rover
    all_rover_photos = []
    for rover in all_rovers:
        roverresp = requests.get(
            f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?sol=1000&api_key=QQW0pSzIa5xdXxCTgsoIcCpU9hxrpnKLgro4QDHD").json()
        for photo in roverresp['photos']:
            if photo['camera']['name'] == user_cam_input:
                date_taken = photo['earth_date']
                img_url = photo['img_src']
                rover_dict = {
                    "ROVER": rover,
                    "DATE": date_taken,
                    "PHOTO_URL": img_url
                }
                all_rover_photos.append(rover_dict)

    for rover_photo in all_rover_photos:
        print(rover_photo)

if __name__ == "__main__":
    main()




