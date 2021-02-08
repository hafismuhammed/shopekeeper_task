from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File


class Products(models.Model):
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    shopekeeper_id = models.CharField(max_length=100)
    barcode = models.ImageField(upload_to='media/barcodes')


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(
            f'''Name: {self.name},
            product: {self.product},
            description: {self.description},
            price: {self.price},
            shopekeeper_id: {self.shopekeeper_id}
             ''',writer=ImageWriter()).write(rv)
        self.barcode.save(f'{self.name}.png', File(rv), save=False)
        return super().save(*args, **kwargs)




