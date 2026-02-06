#Reclassify Poverty Level: 

def reclass (PovertyFloat):
    if PovertyFloat <= 4.94:
        return 1
    if PovertyFloat >= 4.940001 and PovertyFloat <= 9.24: 
        return 2
    if PovertyFloat >= 9.240001 and PovertyFloat <= 14.6: 
        return 3
    if PovertyFloat >= 14.60001 and PovertyFloat <= 22.91: 
        return 4
    if PovertyFloat >= 22.910001 and PovertyFloat <= 85.51: 
        return 5
    else: 
        return 0

#Reclassify Travel Time
def reclass (Traveltimefloat):
    if Traveltimefloat <= 3:
        return 1
    if Traveltimefloat >= 4 and Traveltimefloat <= 5: 
        return 2
    if Traveltimefloat >= 6 and Traveltimefloat <= 8: 
        return 3
    if Traveltimefloat >= 9 and Traveltimefloat <= 14: 
        return 4
    if Traveltimefloat >= 15 and Traveltimefloat <= 247: 
        return 5
    else: 
        return 0

#Reclassify Population to provider by quintile
def reclass (Poptoprov):
    if Poptoprov <= 457.1:
        return 1
    if Poptoprov >= 457.2 and Poptoprov <= 843: 
        return 2
    if Poptoprov >= 843.1 and Poptoprov <= 1552: 
        return 3
    if Poptoprov >= 1553 and Poptoprov <= 2939: 
        return 4
    if Poptoprov >= 2940 and Poptoprov <= 11150: 
        return 5
    else: 
        return 0

#Reclassify Population to Provider by septile 
def reclass (Poptoprov):
    if Poptoprov <= 368.4:
        return 1
    if Poptoprov >= 368.5 and Poptoprov <= 596.6: 
        return 2
    if Poptoprov >= 596.7 and Poptoprov <= 911.7: 
        return 3
    if Poptoprov >= 911.8 and Poptoprov <= 1417: 
        return 4
    if Poptoprov >= 1418 and Poptoprov <= 2248: 
        return 5
    if Poptoprov >= 2249 and Poptoprov <= 3526: 
        return 6
    if Poptoprov >= 3527 and Poptoprov <= 11150: 
        return 7
    else: 
        return 0

#Reclassify Population to Provider by Decile
def reclass (Poptoprov):
    if Poptoprov <= 296.9:
        return 1
    if Poptoprov >= 297 and Poptoprov <= 457.3: 
        return 2
    if Poptoprov >= 457.4 and Poptoprov <= 623.3: 
        return 3
    if Poptoprov >= 623.4 and Poptoprov <= 843.0: 
        return 4
    if Poptoprov >= 843.1 and Poptoprov <= 1135: 
        return 5
    if Poptoprov >= 1136 and Poptoprov <= 1552: 
        return 6
    if Poptoprov >= 1553 and Poptoprov <= 2154: 
        return 7
    if Poptoprov >= 2155 and Poptoprov <= 2939: 
        return 8
    if Poptoprov >= 2940 and Poptoprov <= 4123: 
        return 9
    if Poptoprov >= 4124 and Poptoprov <= 11150: 
        return 10

    else: 
        return 0

#Reclassify Frequent physical distress
def reclass (Physicaldistress):
    if Physicaldistress >= 13.5:
        return 1
    if Physicaldistress < 13.5:
        return 0

#Reclassify Mobility 
def reclass (Mobility):
    if Mobility >= 15.5:
        return 1
    if Mobility < 15.5:
        return 0

#Reclassify Self-Care

def reclass (SelfCare):
    if SelfCare >= 4.3:
        return 1
    if SelfCare < 4.3:
        return 0

#Reclassify Physical Inactivity

def reclass (PhysicalInactivity):
    if PhysicalInactivity >= 27.7:
        return 1
    if PhysicalInactivity < 27.7:
        return 0

#Reclassify Independent Living

def reclass (IndependentLiving):
    if IndependentLiving >= 9.1:
        return 1
    if IndependentLiving < 9.1:
        return 0

#Reclassify Arthritis

def reclass (Arthritis):
    if Arthritis >= 23.5:
        return 1
    if Arthritis < 23.5:
        return 0

#Reclassify Obesity

def reclass (Obesity):
    if Obesity >= 37.3:
        return 1
    if Obesity < 37.3:
        return 0

#Reclassify Stroke

def reclass (Stroke):
    if Stroke >= 3.5:
        return 1
    if Stroke < 3.5:
        return 0

#Reclassify Transportation barriers

def reclass (Transportation):
    if Transportation >= 10.2:
        return 1
    if Transportation < 10.2:
        return 0

#Reclassify Lack of health insurance 

def reclass (PhysicalInactivity):
    if PhysicalInactivity >= 19.8:
        return 1
    if PhysicalInactivity < 19.8:
        return 0

#Calculate RPSA1
!TexasCensusTract_SpatialJoin11.Popprovscore10! + !TexasCensusTract_SpatialJoin11.Percentbelowpovertyscore! + !TexasCensusTract_SpatialJoin11.Timetonsc_score! + !TexasCensusTract_SpatialJoin11.Frequentphysicaldistressscore! + !TexasCensusTract_SpatialJoin11.Mobilitydisabilityscore! + !TexasCensusTract_SpatialJoin11.Selfcarescore! + !TexasCensusTract_SpatialJoin11.Physicalinactivityscore! + !TexasCensusTract_SpatialJoin11.Independentlivingscore!
#Calculate RPSA2
!TexasCensusTract_SpatialJoin11.Popprovscore7! + !TexasCensusTract_SpatialJoin11.Percentbelowpovertyscore! + !TexasCensusTract_SpatialJoin11.Timetonsc_score! + !TexasCensusTract_SpatialJoin11.Frequentphysicaldistressscore! + !TexasCensusTract_SpatialJoin11.Mobilitydisabilityscore! + !TexasCensusTract_SpatialJoin11.Selfcarescore! + !TexasCensusTract_SpatialJoin11.Physicalinactivityscore! + !TexasCensusTract_SpatialJoin11.Independentlivingscore! + !TexasCensusTract_SpatialJoin11.Arthritisscore! + !TexasCensusTract_SpatialJoin11.Obesityscore! + !TexasCensusTract_SpatialJoin11.Strokescore!

#Calculate RPSA3
!TexasCensusTract_SpatialJoin11.Popprovscore5!+ !TexasCensusTract_SpatialJoin11.Percentbelowpovertyscore! + !TexasCensusTract_SpatialJoin11.Timetonsc_score! + !TexasCensusTract_SpatialJoin11.Frequentphysicaldistressscore! + !TexasCensusTract_SpatialJoin11.Mobilitydisabilityscore! + !TexasCensusTract_SpatialJoin11.Selfcarescore! + !TexasCensusTract_SpatialJoin11.Physicalinactivityscore! + !TexasCensusTract_SpatialJoin11.Independentlivingscore! + !TexasCensusTract_SpatialJoin11.Arthritisscore! + !TexasCensusTract_SpatialJoin11.Obesityscore! + !TexasCensusTract_SpatialJoin11.Strokescore! + !TexasCensusTract_SpatialJoin11.Transportationscore! + !TexasCensusTract_SpatialJoin11.Healthinsurancescore!

#Calculate RPSA4
!TexasCensusTract_SpatialJoin11.Popprovscore10!+ !TexasCensusTract_SpatialJoin11.Percentbelowpovertyscore! + !TexasCensusTract_SpatialJoin11.Timetonsc_score! + !TexasCensusTract_SpatialJoin11.Physicalinactivityscore! + !TexasCensusTract_SpatialJoin11.Arthritisscore! + !TexasCensusTract_SpatialJoin11.Obesityscore! + !TexasCensusTract_SpatialJoin11.Strokescore! + !TexasCensusTract_SpatialJoin11.Transportationscore! + !TexasCensusTract_SpatialJoin11.Healthinsurancescore!
