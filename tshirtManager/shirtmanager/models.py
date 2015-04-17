from django.db import models

class Team(models.Model):
    manager_name = models.CharField(max_length=20)
    team_number = models.IntegerField(default=0)

    def __str__(self):
        return str(self.team_number)

class HaveShirt(models.Model):
    owningTeam = models.ForeignKey(Team)
    belongingTeam = models.IntegerField(default=0)
    size = models.CharField(max_length=3)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return str(self.belongingTeam)


class WantShirt(models.Model):
    requestingTeam = models.ForeignKey(Team)
    belongingTeam = models.IntegerField(default=0)
    size = models.CharField(max_length=3)
    amount = models.IntegerField(default=1)