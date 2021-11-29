from django.db import models

# Create your models here.
class paciente(models.Model):
    nombre= models.CharField( max_length=50)
    class Meta:
        verbose_name = ("paciente")
        verbose_name_plural = ("pacientes")

    def __str__(self):
        return self.nombre

    #def get_absolute_url(self):
      #  return reverse("_detail", kwargs={"pk": self.pk})


class tessiu(models.Model):

    temperature= models.FloatField(verbose_name="Temperatura:)") 
    color = models.FloatField()
    inflamation=models.FloatField(verbose_name="Inflamacion")
    nombre=models.ForeignKey(paciente, on_delete=models.CASCADE,blank=True, null=True)
    
    class Meta:
        verbose_name = "Tejido"
        verbose_name_plural = "Tejidos"

    def __str__(self):
        return 'temperatura: '+ str(self.temperature)+ 'Color: ' + str(self.color)

    #def get_absolute_url(self):
     #   return reverse("Tejido_detail", kwargs={"pk": self.pk})



