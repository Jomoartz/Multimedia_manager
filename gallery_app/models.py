from django.db import models

class MediaFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.ImageField(null= True, blank=False, upload_to='images/')
    profile = models.ImageField(null = False, blank='True', upload_to ='images/' )
    display_photo1 = models.ImageField(null = False, blank='false', upload_to ='images/' )
    display_photo2 = models.ImageField(null = False, blank='false', upload_to ='images/' )
    display_photo3 = models.ImageField(null = False, blank='false', upload_to ='images/' )
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)
