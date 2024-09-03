from django.contrib import admin

from .models import (
    Month,
    FoodInflation,
    FuelInflation,
    NonFoodNonFuelInflation,
    FoodAndNonAlcoholicBeverages,
    AlcoholicBeverages,
    ClothingAndFootwear,
    HousingAndWater,
    ElectricityAndGas,
    Furnishing,
    Health,
    Transport,
    InformationAndCommunication,
    RecreationAndSports,
    EducationServices,
    RestaurantsAndAccommodationServices,
    monthlyfoodinflation
    # Report
)

class FoodInflationAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')

class FuelInflationAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')

class NonFoodNonFuelInflationAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')

class FoodAndNonAlcoholicBeveragesAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')

class AlcoholicBeveragesAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')

class ClothingAndFootwearAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')

class HousingAndWaterAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')

class ElectricityAndGasAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')

class FurnishingAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')

class HealthAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')

class TransportAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')

class InformationAndCommunicationAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')

class RecreationAndSportsAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')

class EducationServicesAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')

class RestaurantsAndAccommodationServicesAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')

class monthlyfoodinflationAdmin(admin.ModelAdmin):
    list_display = ('month', 'value')
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

admin.site.register(FoodInflation, FoodInflationAdmin)
admin.site.register(FuelInflation, FuelInflationAdmin)
admin.site.register(NonFoodNonFuelInflation, NonFoodNonFuelInflationAdmin)
admin.site.register(FoodAndNonAlcoholicBeverages, FoodAndNonAlcoholicBeveragesAdmin)
admin.site.register(AlcoholicBeverages, AlcoholicBeveragesAdmin)
admin.site.register(ClothingAndFootwear, ClothingAndFootwearAdmin)
admin.site.register(HousingAndWater, HousingAndWaterAdmin)
admin.site.register(ElectricityAndGas, ElectricityAndGasAdmin)
admin.site.register(Furnishing, FurnishingAdmin)
admin.site.register(Health, HealthAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(InformationAndCommunication, InformationAndCommunicationAdmin)
admin.site.register(RecreationAndSports, RecreationAndSportsAdmin)
admin.site.register(EducationServices, EducationServicesAdmin)
admin.site.register(RestaurantsAndAccommodationServices, RestaurantsAndAccommodationServicesAdmin)
# admin.site.register(Report, ReportAdmin)

   
    
    
   
    
