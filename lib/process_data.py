#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json 
class ProcessData:
  def execute(self, path):
  	with open(path) as data_file:
  		data = json.load(data_file)
  	for element in data:
    		print(element["text"])
