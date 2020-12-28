streamraider_levels_golds=[10,25,35,50,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,450,500,550,600,675,750,825,900,1000,1200]
streamraider_levels_scrolls=[5,15,20,25,50,60,70,80,90,100,110,120,130,140,150,1160,170,180,190,200,220,240,260,280,300,320,340,360,380,400]

def calculations(calculation,currentLevel,targetLevel):
    summ=0
    
    if calculation=="gold":
        
        for i in streamraider_levels_golds[currentLevel:targetLevel]:
            summ+=i
        return str(summ)+"  golds"
    else:
        
        for i in streamraider_levels_scrolls[currentLevel:targetLevel]:
            summ+=i
        return str(summ) + "  scrolls"
calculation=input("gold or scroll")
currentLevel=int(input("what is your current level?"))
targetLevel=int(input("what is your target level?"))
print("you will need "+calculations(calculation,currentLevel,targetLevel))
