import geopandas as gpd
import numpy as np
import csv

from geopandas import GeoDataFrame, GeoSeries, overlay
from shapely.geometry import Point, Polygon
from math import exp

from medicalmap.models import MedicalMap


def MedicalScoreCalculator(map):
	age_weights = {1: 0.2, 2: 1, 3: 0.8, 4: 0.4}
	# 0-20	0.2
	# 20-40	1
	# 40-60	0.8
	# 60-100	0.4

	P = 0
	alpha = 0 
	p = 0
	q = 0
	r = 0
	h1 = 0
	h2 = 0
	d = 0
	T = 0
	F = 0
	Shades = ''

	alpha_max = 100 
	p_max = 54
	q_max = 37
	r_max = 24
	d_max = 10
	gamma_max = 100
	i_max = 5
	T_max = 100

	fth = 0.65

	work = option_array(map.work,5)

	age = map.age
	height = map.height
	weight = map.weight

	# gahw_arr = np.array([self_else, gender, age, height, weight])

	airport_from = map.domestic_airport_from
	airport_to = map.domestic_airport_to
	current_state = map.current_state
	airport_filename = "domestic_airport.csv"
	state_filename = "state.csv"

	A = float(csv_reader(airport_filename, airport_from))
	B = float(csv_reader(airport_filename, airport_to))
	print("airport from: ", A)
	print("airport to: ", B)

	C = float(csv_reader(state_filename, current_state))
	print("state weight: ", C)
	D = age_weights[age_range(age)]
	print(age, D)

	P_arr = np.array([A, B, C, D])

	#Prev Conditions
	#Diabetes
	diab = int(map.diabetes)

	#Kidney
	k = int(map.kidney)
	#Asthma
	asth = int(map.asthma)
	#Heart
	hrt = int(map.heart)
	#Lungs
	l = int(map.lungs)
	#Stroke
	s = int(map.stroke)
	#Hypertension
	h =  int(map.hypertension)

	prev_cond_2 = np.array([k, asth, hrt, l, s, h])

	#Immunocompromised
	immuno = int(map.immuno)


	prev_cond = np.array([diab, int(prev_cond_2.any()), immuno])


	sm = int(map.smoker)

	#Symptoms

	#Fever
	#either no or one of the four yes options
	fever = option_array(map.fever,5)
	#Cough
	cough = option_array(map.cough,5)
	#Shortness of breadth
	sb = int(map.breathlessness)
	#Fatigue
	ftg = int(map.fatigue)
	#Joint/Muscle pain
	j = int(map.joint_pain)
	#Loss of taste/smell          #Rare Case
	ts = int(map.loss_of_taste_and_smell)

	symptoms_sev_mod = np.append(fever, cough)
	symptoms_sev_mod = np.append(symptoms_sev_mod, sb)
	symptoms_sev_mod = np.append(symptoms_sev_mod, ftg)
	symptoms_sev_mod = np.append(symptoms_sev_mod, j)
	symptoms_sev_mod = np.append(symptoms_sev_mod, ts)

	#Other Symptoms
	#Sore throat
	#headache
	#muscle pain
	#chills
	#nausea/vomiting
	#nasal congestion
	#diarrhea
	os_mild = np.array([int(map.sore_throat), int(map.nasal_congestion), int(map.headache), int(map.chills), int(map.nausea_or_vomiting), int(map.diarrhea), int(map.conjunctival_congestion)])

	#Improvement
	sym_impr = option_array(map.symptoms_improvement,4)

	#Travel info
	#flight, train, auto, cab
	domestic_mode = np.array([int(map.domestic_flight), int(map.domestic_train), int(map.domestic_auto), int(map.domestic_cab)])
	international_mode = int(map.international_mode)
	

	#### WEIGHTS 

	# SELF, GENDER, AGE, HEIGHT, WEIGHT weights
	weight_gahw = np.array([0,0,0,0,0])  #4
	#Heart Rate/BP weights
	weight_hb = np.array([0,0])  #2
	weights_P = np.array([0.3, 0.3, 0.3, 0.1])

	#work weights
	weight_work = np.array([0, 0.4, 0.6, 0.8, 1])

	#Prev Conditions
	weight_pc = np.array([2,2,3])  #6

	#Symptoms
	#Fever
	weight_f_mod = np.array([0,17,0,17,16])  #7
	weight_f_sev = np.array([0,0,18,0,0])  #7
	#Cough
	weight_c_mod = np.array([0,0,0,14,14])  #7
	weight_c_sev = np.array([0,14,9,0,0])  #7

	#Shortness of breadth
	weight_sb_mod = np.array([0])  #7
	weight_sb_sev = np.array([8])  #7

	#Fatigue
	weight_ftg_mod = np.array([0])   #1
	weight_ftg_sev = np.array([8])   #1

	#Joint/muscle pain
	weight_j_mod = np.array([0])   #1
	weight_j_sev = np.array([6])   #1

	#Loss of taste/smell
	weight_ts_mod = np.array([6])  #1
	weight_ts_sev = np.array([0])  #1

	weights_symptoms_mod = np.append(weight_f_mod, weight_c_mod)
	weights_symptoms_mod = np.append(weights_symptoms_mod, weight_sb_mod)
	weights_symptoms_mod = np.append(weights_symptoms_mod, weight_ftg_mod)
	weights_symptoms_mod = np.append(weights_symptoms_mod, weight_j_mod)
	weights_symptoms_mod = np.append(weights_symptoms_mod, weight_ts_mod)

	weights_symptoms_sev = np.append(weight_f_sev, weight_c_sev)
	weights_symptoms_sev = np.append(weights_symptoms_sev, weight_sb_sev)
	weights_symptoms_sev = np.append(weights_symptoms_sev, weight_ftg_sev)
	weights_symptoms_sev = np.append(weights_symptoms_sev, weight_j_sev)
	weights_symptoms_sev = np.append(weights_symptoms_sev, weight_ts_sev)

	#Other Symptoms
	weight_os_mild = np.array([4,3,4,4,3,3,3])   #7

	#Improvement
	weight_impr = np.array([0,0,3,4])

	#Domestic Travel
	weight_domestic = np.array([5, 3, 1.5, 0.5])


	#### SCORE CALCULATION
	W_scores = work*weight_work
	W = np.sum(W_scores)

	P_scores = P_arr*weights_P
	P = np.sum(P_scores)

	pc_scores = prev_cond*weight_pc
	h1 = np.sum(pc_scores)

	sev_symptoms_scores = symptoms_sev_mod*weights_symptoms_sev
	p = np.sum(sev_symptoms_scores)

	# print(sev_symptoms_scores)
	# print(p)

	mod_symptoms_scores = symptoms_sev_mod*weights_symptoms_mod
	q = np.sum(mod_symptoms_scores)
	# print(mod_symptoms_scores)
	# print(q)

	mild_symptoms_scores = os_mild*weight_os_mild
	r = np.sum(mild_symptoms_scores)

	domestic_scores = domestic_mode * weight_domestic
	d = np.sum(domestic_scores)

	improvement_scores = sym_impr * weight_impr
	h2 = np.sum(improvement_scores)

	alpha = p + q + r + h1 + h2

	if(international_mode):
		country_travelled = map.country_travelled
		country_filename = 'country.csv'
		gamma_inter = float(csv_reader(country_filename, country_travelled))
		i = 2+3*(gamma_inter/gamma_max)
		T = 0.5*(alpha/alpha_max)+ 0.3*(d/d_max) + 0.2*(i/i_max) 

	else:
		T = 0.7*(alpha/alpha_max) + 0.3*(d/d_max)


	# t = T/T_max
	# FINAL SCORE --- F
	F = 100 * (0.85*T + 0.1*P + 0.05*W)

	### PROBABILITY CALCULATION
	 
	c_factor = 1
	tao = 48
	beta = 0.1

	Probability = 1 - exp( -1 * ((exp(c_factor*F - tao))**beta))


	print("SCORE: ", F)

	if map.travel_filled:

		Fth1 = 50
		Fth2 = 30

	else:
		Fth1 = 35
		Fth2 = 20

	colors = ['#ff0000', '#e50000', '#cc0000', '#b20000', '#990000']


	if (F > Fth1):
		div = (100 - Fth1)/len(colors)
		index = int((F - Fth1)/div)
		Shades = colors[index]

	elif ((F>Fth2) and (((q + r)/(q_max + r_max)) > fth)):
		Shades = '#785027'

	else:
		Shades = "Null"


	print("Score color: ", Shades)
	
	return (F, Shades, Probability)



def csv_reader(filename, key):
	with open(filename, mode='r') as infile:
		reader = csv.reader(infile)
		mydict = {rows[0]:rows[1] for rows in reader}

	return mydict[key]

def option_array(element, max):
	opt_arr = np.zeros((max,), dtype=int)
	opt_arr[element] = 1
	return opt_arr

def age_range(age):
	if (age<20):
		return 1
	elif (age<40):
		return 2
	elif (age<60):
		return 3
	else:
		return 4

