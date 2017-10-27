# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
import re #imports regular expressions
import bcrypt 

# Create your models here.

class UserManager(models.Manager):
    
    def loginVal(self, postData):
        results = {'errors':[], 'status': False, 'user': None}
        username_matches = self.filter(username=postData['username'])
        if len(username_matches) == 0:
            results['errors'].append('Please check your username and password and try again.')
            results['status'] = True
        else:
            results['user'] = username_matches[0]
#            bcrypt.checkpw('test'.encode(), hash1)
            if not bcrypt.checkpw(postData['password'].encode(), results['user'].password.encode()):
                results['errors'].append('Please check your username and password and try again.')
                results['status'] = True
        return results
    
    def createUser(self, postData):
        #password = bcrypt.hashpw('test', bcrypt.gensalt()) #insert postData['password'] in first parameter
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        print password
        self.create(name = postData['name'], username = postData['username'], password = password)
    
    def registerVal(self, postData):
        #validator - shows error messages to user
        results = {'errors':[], 'status': False}
        
        if len(postData['name']) < 2:
            results['status'] = True
            results['errors'].append('Name is too short.')  
            
#        if not postData['first_name'].isalpha():
#            results['status'] = True
#            results['errors'].append('Please use alphanumeric characters only.')
        
        if len(postData['username']) < 2:
            results['status'] = True
            results['errors'].append('Username is too short.')
            
#        if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
#            results['status'] = True
#            results['errors'].append('Not a valid email.')
        
        if len(postData['password']) < 3:
            results['status'] = True
            results['errors'].append('Password is too short.')
            
        if postData['password'] != postData['c_password']:
            results['status'] = True
            results['errors'].append('Passwords do not match')
            
        user = self.filter(username = postData['username'])
        
        if len(user) > 0:
            results['status'] = True
            results['errors'].append('username already exists in database.')
        
        hireday = postData['hireday']
        if len(hireday) == 10:
            byear = int(hireday[:4])
            bmonth = int(hireday[5:7])
            bday = int(hireday[8:])
            if datetime.date.today() < datetime.date(byear, bmonth, bday):
                results['status'] = True
                results['errors'].append('Invalid hire date')
        else:
            results['status'] = True
            results['errors'].append('Not a valid hire date.')
        return results
    
class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    objects = UserManager()