#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import urllib.request;
import wget;

url = 'https://youtu.be/qIs7fVkCyeU';
response = urllib.request.urlopen(url);
data = response.read();      # a `bytes` object
text = data.decode('utf-8'); # a `str`; this step can't be used if data is binary

if text == "data":
	print("Sikeres");
	
url = 'https://i1.wp.com/python3.codes/wp-content/uploads/2015/06/Python3-powered.png?fit=650%2C350'  
wget.download(url, '/Users/scott/Downloads/cat4.jpg') 
