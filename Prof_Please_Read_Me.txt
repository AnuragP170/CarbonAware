django_project file format
.
└── ./djangoDSAG
    ├── ./djangoDSAG/CarbonAware
    │   ├── ./djangoDSAG/CarbonAware/admin.py
    │   ├── ./djangoDSAG/CarbonAware/apps.py
    │   ├── ./djangoDSAG/CarbonAware/commandExecuter.py
    │   ├── ./djangoDSAG/CarbonAware/__init__.py
    │   ├── ./djangoDSAG/CarbonAware/models.py
    │   ├── ./djangoDSAG/CarbonAware/tests.py
    │   └── ./djangoDSAG/CarbonAware/views.py [Important for Marking, contains backend processing code for website.]
    |
    |
    |
    |
    ├── ./djangoDSAG/djangoDSAG
    │   ├── ./djangoDSAG/djangoDSAG/asgi.py
    │   ├── ./djangoDSAG/djangoDSAG/__init__.py
    │   ├── ./djangoDSAG/djangoDSAG/settings.py
    │   ├── ./djangoDSAG/djangoDSAG/urls.py
    │   └── ./djangoDSAG/djangoDSAG/wsgi.py
    |
    |
    |
    |
    ├── ./djangoDSAG/html
    │   ├── ./djangoDSAG/html/css
    │   │   └── ./djangoDSAG/html/css/styles.css
    │   ├── ./djangoDSAG/html/display.html
    │   ├── ./djangoDSAG/html/img
    │   │   ├── ./djangoDSAG/html/img/djangoDSAG_bg2.png
    │   │   └── ./djangoDSAG/html/img/msntemplate13.png
    │   ├── ./djangoDSAG/html/index.html
    │   ├── ./djangoDSAG/html/index.html.bak
    │   ├── ./djangoDSAG/html/login.html
    │   ├── ./djangoDSAG/html/mrtMap.html
    │   └── ./djangoDSAG/html/navbar.html
    |
    |
    |
    ├── ./djangoDSAG/manage.py  [Important if you wish to install and run the application.]
    |
    |
    |
    ├── ./djangoDSAG/processing  [Important for Marking, contains all backend processing code for website.]
    │   ├── ./djangoDSAG/processing/carbon_emission_calculator.bak
    │   ├── ./djangoDSAG/processing/carbon_emission_calculator.py
    │   ├── ./djangoDSAG/processing/cec_iframe.py
    │   ├── ./djangoDSAG/processing/concatDir.py
    │   ├── ./djangoDSAG/processing/distances.xlsx
    │   ├── ./djangoDSAG/processing/mrtMap_IMG.py
    │   └── ./djangoDSAG/processing/mrt_route_optimizer_final.py 
    |
    |
    |   
    ├── ./djangoDSAG/Procfile
    ├── ./djangoDSAG/requirements.txt   [Important if you wish to install and run the application.]
    ├── ./djangoDSAG/requirements.txt.bak   [Important if you wish to install and run the application.]
    └── ./djangoDSAG/staticfiles
