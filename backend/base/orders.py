from django.db import models 
from .products import Products 
from .user import User
import datetime 


class Order(models.Model): 
	product = models.ForeignKey(Products, 
								on_delete=models.CASCADE) 
	user = models.ForeignKey(User, 
								on_delete=models.CASCADE) 
	quantity = models.IntegerField(default=1) 
	price = models.IntegerField() 
	address = models.CharField(max_length=50, default='', blank=True) 
	phone = models.CharField(max_length=50, default='', blank=True) 
	date = models.DateField(default=datetime.datetime.today) 
	status = models.BooleanField(default=False) 

	def placeOrder(self): 
		self.save() 

	@staticmethod
	def get_orders_by_User(User_id): 
		return Order.objects.filter(user=User_id).order_by('-date') 

from django.shortcuts import render, redirect 
from django.contrib.auth.hashers import check_password 
from .user import User
from django.views import View 
from .products import Products 
from .orders import Order 




class OrderView(View): 

	def get(self, request): 
		customer = request.session.get('customer') 
		orders = Order.get_orders_by_customer(customer) 
		print(orders) 
		return render(request, 'orders.html', {'orders': orders}) 
