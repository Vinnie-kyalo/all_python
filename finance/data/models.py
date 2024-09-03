from django.db import models

class Month(models.Model):
    month = models.CharField(max_length=20, unique=True)

class FoodInflation(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    value = models.FloatField()

class FuelInflation(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    value = models.FloatField()

class NonFoodNonFuelInflation(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    value = models.FloatField()

class FoodAndNonAlcoholicBeverages(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    value = models.FloatField()

class AlcoholicBeverages(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    value = models.FloatField()

class ClothingAndFootwear(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    value = models.FloatField()

class HousingAndWater(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    value = models.FloatField()

class ElectricityAndGas(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    value = models.FloatField()

class Furnishing(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    value = models.FloatField()

class Health(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    value = models.FloatField()

class Transport(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    value = models.FloatField()

class InformationAndCommunication(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    value = models.FloatField()

class RecreationAndSports(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    value = models.FloatField()

class EducationServices(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    value = models.FloatField()

class RestaurantsAndAccommodationServices(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    value = models.FloatField()

class monthlyfoodinflation(models.Model):
    Month = models. CharField(max_length=255, default='august')
    food_inflation =models.FloatField(max_length=3, default='7')

class InflationData(models.Model):
    month = models.CharField(max_length=50)
    food_inflation = models.FloatField()
    fuel_inflation = models.FloatField()