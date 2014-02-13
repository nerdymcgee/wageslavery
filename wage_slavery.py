#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wage slavery.py
#  
#  Copyright 2014 Andre Chang <chang.r.andre@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# figure out how to run a salary calculator in python

monthly_needed=0
int(monthly_needed)

print "Welcome to the Hourly Salary calculator! Follow the instructions below."

monthly_needed = raw_input ("How much do you need to make per month?")

hourly_salary = raw_input("What is the offered hourly salary?")

week_hours = raw_input("How many hours do you expect to work?")

monthly_paid = 0

#formula to get monthly earnings from hourly wage

monthly_paid = (int(hourly_salary) * int(week_hours) )* 4 

print monthly_paid
if  int(monthly_paid) >= int(monthly_needed) :
	print "The job sounds good! You should go for it!"
else:
	print "You should reconsider applying for this one."

