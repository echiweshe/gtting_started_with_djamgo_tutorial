from django import forms

from .models import DescriptiveStats

class DescriptiveStatsForm(forms.ModelForm):
    class Meta:
        model = DescriptiveStats
        fields = ['question_copy', 'vars_data_set', 'sample_or_population_choice', 'maximum_max', 'minimum_mib', 'range_R', 'size_n', 'sum_z', 'mean_x_bar', 'median_x_tilda', 'mode_mode', 'std_dev_s', 'variabce_s2', 'first_quartile_pos', 'second_quartile_pos', 'third_quartile_pos', 'first_quartile', 'second_quartile_MR', 'third_quartile', 'inter_quartile_range_IQR', 'outliers', 'sum_of_squares_SS', 'mean_absolute', 'deviation_MAD', 'root_mean_square_RMS', 'std_error_of_mean_SEx_bar', 'skewness_y1', 'kurtosis_B2', 'kurtosis_excess', 'kurtosis_in_excel_and_sheets_α4', 'coefficient_of_variation_CV', 'relative_standard_deviation_RSD']
        
        '''
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'input', 'placeholder' : 'Your Name'}),
            'email' : forms.EmailInput(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
            'message': forms.Textarea(attrs={'class': 'textarea', 'rows': 10, 'placeholder' : 'Your message...'}),
        }
        '''

