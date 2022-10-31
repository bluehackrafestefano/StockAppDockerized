# StockApp - Yet Another Dockerized Django REST Project

This is a Django REST Framework project. I created it for experimentation and learning purposes. Then, I dockerized it to continue with CI and DevOps tools in the near future.


## Motivation

Keeping the transactions up-to-date of a commercial app is a common challenge. A complete project template may be beneficial for future use cases.


## Method and results

Using Django for the backend is one of the best solution for apps. Django has concise base classes. We can do things with little code.

In this project:
  - TokenAuthentication for authentication,
  - dj_rest_auth for login/logout and token creation,
  - swagger for testing and visualization of the project,
  - logger (file and console) for loggging,
  - redoc for documentation,
  - django_filters for filtering,
  - search,
  - nested serializers to show products under one brand etc.,
  - signals for token creation and updating different models at the same time,
  - DjangoModelPermissions to define granular permissions to different groups,
  - Viewset for logic,
  - DefaultRouter for url mapping,
are used.

And as best practices:
  - python-decouple is used to seperate sensitive data,
  - dev and prod environments are seperated,
  - project URLconf simply includes URLconfs from the applications,
  - abstract base class is used on models in order to implement DRY principle,
  - virtual environment is used while developing this project locally,
  - an updated requirements.txt file is used for collaborating properly with other developers,
  - plural related names are used to specify the reverse relation from the parent model back to the child model.


## Repository overview

Provide an overview of the directory structure and files, for example:

├── README.md
├── data
├── gen
│   ├── analysis
│   ├── data-preparation
│   └── paper
└── src
    ├── analysis
    ├── data-preparation
    └── paper


## Running instructions

Explain to potential users how to run/replicate your workflow. If necessary, touch upon the required input data, which secret credentials are required (and how to obtain them), which software tools are needed to run the workflow (including links to the installation instructions), and how to run the workflow.


## More resources

Point interested users to any related literature and/or documentation.


## About

Explain who has contributed to the repository. You can say it has been part of a class you've taken at Tilburg University.

