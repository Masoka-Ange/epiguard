# urls.py
from django.urls import path
from . import views
from .views import patient_form_view, contexte_form_view, signes_form_view,symptomes_generaux_form_view, symptomes_respiratoires_form_view,symptomes_digestifs_form_view,symptomes_neurologiques_view,symptomes_dermatologiques_view,symptomes_specifiques_view, success_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('patient/', patient_form_view, name='patient_form'),
    path('contexte/<int:patient_id>/', contexte_form_view, name='contexte_form'),
    path('signes/<int:patient_id>/', signes_form_view, name='signes_form'),
    path('symptomes-generaux/<int:patient_id>/', symptomes_generaux_form_view, name='symptomes_generaux_form'),
    path('symptomes-respiratoires/<int:patient_id>/', symptomes_respiratoires_form_view, name='symptomes_respiratoires_form'),
    path('symptomes-digestifs/<int:patient_id>/', symptomes_digestifs_form_view, name='symptomes_digestifs_form'),
    path('symptomes_neurologiques/<int:patient_id>/', symptomes_neurologiques_view, name='symptomes_neurologiques'),
    path('symptomes_dermatologiques/<int:patient_id>/', symptomes_dermatologiques_view, name='symptomes_dermatologiques'),
    path('symptomes_specifiques/<int:patient_id>/', symptomes_specifiques_view, name='symptomes_specifiques'),
    path('add_differenciation/', views.add_differenciation_maladie, name='add_differenciation_maladie'),
    path('success/<int:patient_id>/', views.success_view, name='success_view'),
    path('patient_pos/<int:patient_id>/symptomes/', views.save_and_display_positive_symptoms, name='symptomes_positifs'),
    path('symptomes_positifs/<int:patient_id>/prediction/', views.prediction_symptomes, name='prediction_symptomes'),
    path('add_province/', views.add_province, name='add_province'),
    path('add_hopital/', views.add_hopital, name='add_hopital'),
    path('add_medecin/', views.add_medecin, name='add_medecin'),
    path('provinces/', views.province_list, name='province_list'),
    path('home_admin/', views.home_admin, name='home_admin'),
    path('hopitaux/<int:province_id>/', views.hopital_list, name='hopital_list'),
    path('medecin_list/', views.medecin_list, name='medecin_list'),
    path('province-hopital/', views.province_hopital_form, name='province_hopital_form'),
    path('fetch-hopitals/', views.fetch_hopitals, name='fetch_hopitals'),
    path('dashboard/', views.hopital_dashboard, name='hopital_dashboard'),
    path('select-medecin/', views.select_medecin, name='select_medecin'),
    path('validate-medecin/', views.validate_medecin, name='validate_medecin'),
    path('welcome/', views.welcome_page, name='welcome_page'),
    path('hopital/<int:hopital_id>/medecins/', views.medecin_list_by_hopital, name='medecin_list_by_hopital'),
    path('home_admin/', views.home_admin, name='home_admin'),
    path('success/', views.success_page, name='success_page'),
    path('success_part/', views.success_page_part, name='success_page_part'),
    path('maladie_detectee_list/', views.maladie_detectee_list, name='maladie_detectee_list'),
    path('maladies/supprimer/<int:maladie_id>/', views.supprimer_maladie, name='supprimer_maladie'),

    ] 
