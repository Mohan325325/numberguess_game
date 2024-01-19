from django.db import models

# Create your models here.
class session(models.Model):
    player_name = models.CharField(max_length=50)
    secret_number = models.IntegerField()
    attempts = models.IntegerField()
    is_winner = models.BooleanField()

    def __str__(self):
        return f"{self.player_name} - {'Winner' if self.is_winner else 'Loser'}"
