from django.shortcuts import render, redirect
from .forms import CSVFileForm
from .models import CSVFile
import pandas as pd
import seaborn as sns
import os

def handle_uploaded_file(f):
    file_path = os.path.join('media/csvs', f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

def upload_csv(request):
    if request.method == 'POST':
        form = CSVFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save()
            file_path = handle_uploaded_file(request.FILES['file'])
            data = pd.read_csv(file_path)
            
            # Perform data analysis
            head = data.head()
            desc = data.describe()
            missing_values = data.isnull().sum()

            # Generate plots
            sns_plot = sns.histplot(data=data)
            plot_path = os.path.join('media', 'plot.png')
            sns_plot.figure.savefig(plot_path)

            context = {
                'form': form,
                'file_instance': file_instance,
                'head': head.to_html(),
                'desc': desc.to_html(),
                'missing_values': missing_values.to_html(),
                'plot_path': plot_path,
            }
            return render(request, 'analysis/results.html', context)
    else:
        form = CSVFileForm()
    return render(request, 'analysis/upload.html', {'form': form})
