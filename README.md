# Django CSV Analysis Application

## Setup Instructions

### Prerequisites
- Python 3.x
- Django
- pandas
- matplotlib
- seaborn

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd csv_analysis_project

python -m venv env
source env/bin/activate  

pip install django pandas matplotlib seaborn

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

Additional Information
The application allows users to upload CSV files and performs data analysis using pandas and numpy.
Data visualizations are generated using matplotlib and seaborn.
The results are displayed on the web interface.
