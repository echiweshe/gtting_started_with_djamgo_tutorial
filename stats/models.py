from django.db import models

from django.urls import reverse

class DescriptiveStats(models.Model):
    ''' Descriptive Statistics Calculator '''

    # Choice definitions
    SAMPLE_OR_POPULATION_CHOICE = [
        ('S', 'Sample'),
        ('P', 'Population'),
    ]


    # Input <div>
    question_copy = models.TextField()
    vars_data_set = models.TextField()
    sample_or_population_choice = models.CharField(max_length=2, choices=SAMPLE_OR_POPULATION_CHOICE)
    
    # Data Statistics: <div>
    maximum_max	= models.DecimalField(decimal_places=8, max_digits=10000)	
    minimum_mib	= models.DecimalField(decimal_places=8, max_digits=10000)		
    range_R = models.DecimalField(decimal_places=8, max_digits=10000)	
    size_n = models.IntegerField()	
    sum_z = models.DecimalField(decimal_places=8, max_digits=10000)	

    # CentralTendency orLocation <div>
    mean_x_bar = models.DecimalField(decimal_places=8, max_digits=10000)
    median_x_tilda = models.DecimalField(decimal_places=8, max_digits=10000)
    mode_mode = models.DecimalField(decimal_places=8, max_digits=10000)

    # Dispersion orVariability <div>
    std_dev_s = models.DecimalField(decimal_places=8, max_digits=10000)
    variabce_s2 = models.DecimalField(decimal_places=8, max_digits=10000)	
    
    # Quartile and CoefficientofVariation <div>
    first_quartile_pos = models.DecimalField(decimal_places=8, max_digits=10000)
    second_quartile_pos = models.DecimalField(decimal_places=8, max_digits=10000)
    third_quartile_pos = models.DecimalField(decimal_places=8, max_digits=10000)		

    first_quartile = models.DecimalField(decimal_places=8, max_digits=10000)
    second_quartile_MR = models.DecimalField(decimal_places=8, max_digits=10000)
    third_quartile = models.DecimalField(decimal_places=8, max_digits=10000)

    inter_quartile_range_IQR = models.DecimalField(decimal_places=8, max_digits=10000)
    outliers = models.DecimalField(decimal_places=8, max_digits=10000)		

    # Input <div>
    sum_of_squares_SS =	models.DecimalField(decimal_places=8, max_digits=10000)
    mean_absolute = models.DecimalField(decimal_places=8, max_digits=10000)
    deviation_MAD =	models.DecimalField(decimal_places=8, max_digits=10000)
    root_mean_square_RMS = models.DecimalField(decimal_places=8, max_digits=10000)
    std_error_of_mean_SEx_bar = models.DecimalField(decimal_places=8, max_digits=10000)

    # Input <div>	
    skewness_y1 = models.DecimalField(decimal_places=8, max_digits=10000)
    kurtosis_B2 = models.DecimalField(decimal_places=8, max_digits=10000)
    kurtosis_excess = models.DecimalField(decimal_places=8, max_digits=10000)
    kurtosis_in_excel_and_sheets_α4 = models.DecimalField(decimal_places=8, max_digits=10000)
    coefficient_of_variation_CV = models.DecimalField(decimal_places=8, max_digits=10000)
    relative_standard_deviation_RSD = models.DecimalField(decimal_places=8, max_digits=10000)    
  
    def get_absolute_url(self):
        return reverse("descriptivestats:descriptivestats-detail", kwargs={"id": self.id}) #f"/descriptivestats/{self.id}/"