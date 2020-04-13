Instruction Document


Packages for Python and Django


Numpy (pip install numpy)
Pandas (pip install pandas)
Geopandas (some of it’s pre-requirements)  (pip install geopandas)
Shapely (pip install Shapely)
Django (pip install django)
Django rest framework (pip install djangorestframework)
Django pandas (pip install django_pandas)
Django rest multiple models (pip install django-rest-multiple-models)




Instructions


1. Download the git folder corona_project from: https://github.com/GoCorona-org/Backend/tree/sanjanamoha/api
2. In Command terminal
   1. Go to the directory $ ./corona_project 
   2.  Run: python manage.py makemigrations corona_app
   3. Run: python manage.py migrate
   4. Run: python manage.py runserver
3. Open http://127.0.0.1:8000/  (No homepage rn)
4. Goto: http://127.0.0.1:8000/corona_app (This redirects to the intersection calculator page)
5. To see the results for the intersection calculator goto: http://127.0.0.1:8000/corona_app/result/
6. For medical form page: http://127.0.0.1:8000/corona_app/medmap/  **
7. To see the result goto: http://127.0.0.1:8000/corona_app/medmap/<int:id> ***




**This form saves each form entry as ‘i’th form and to see result of ith entry see ***
**In this form airports, country and states have to be filled in the same format as given in the csv files    with the corona_project folder




*** To see the result for your nth entry (say 1st form) type http://127.0.0.1:8000/corona_app/medmap/n/
(eg: http://127.0.0.1:8000/corona_app/medmap/1/ )