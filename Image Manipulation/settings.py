import cloudinary
cloudinary.config(
    cloud_name = kongsberg,
    api_key = 141695982166226
    api_secret = KjoIgMD2WRUMu2WogLFcSOkTk-I
)

cloudinary.uploader.upload(car2.jpg)