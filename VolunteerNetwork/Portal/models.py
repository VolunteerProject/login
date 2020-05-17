from django.db import models
from datetime import datetime
from django.db.models.signals import pre_save
from google_auth_oauthlib.flow import Flow
import os

os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1' #Because google oAUTH lib is fucked up and they give out random scopes for same emails.This is to fix that. 


class Volunteer(models.Model):
    user_id=models.AutoField(primary_key=True)
    state=models.CharField(max_length=100)
    oauth_code= models.CharField(max_length=100)
    token = models.CharField(max_length=200)

    def save_token(sender, instance, **kwargs):
        creds = {"web":{"client_id":"157368858787-habhg0s5c4c87i4c6absnlm5glkeskh7.apps.googleusercontent.com","project_id":"quickstart-1589721672163","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"ltRROJb2VUGpDbz-NCzig-yp","redirect_uris":["http://127.0.0.1:8200/logged_in"]}}
        flow=Flow.from_client_config(client_config=creds, scopes = ['email','https://www.googleapis.com/auth/userinfo.email','openid'], redirect_uri='http://127.0.0.1:8200/token_save/')
        token = flow.fetch_token(code=instance.oauth_code)
        instance.token = token['access_token']

pre_save.connect(Volunteer.save_token, sender=Volunteer)
