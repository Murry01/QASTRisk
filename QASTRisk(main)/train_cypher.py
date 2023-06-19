examples = """

# What is the list of works in the tunnel project? 
match(n:Tunnel)-[:has_work_type]->(m:wbs) return m.name As response

# What are the risks associated with the tunnel project? 
match(n:risk) return n.name + " - " +  " Risk Category: " + n.riskcategory as response limit 20

# What are the risk factors associated with the tunnel project?
match(n:riskfactor) return n.Riskfactor As response limit 20

# List risks associated with the "Geotechnical Investigation" of the tunnel project.
match(n:wbs{name:"Geotechnical Investigation"})-[:has_risk]->(m:risk) return "Risk: "+ m.name + " - "+ "Risk Category: " + m.riskcategory As response 

# What are the risk factors of "Geotechnical Investigation" of the tunnel project?
match(n:wbs{name:"Geotechnical Investigation"})-[:has_risk]->(m:risk)-[:has_riskfactor]->(l:riskfactor) return  "Risk: "+ m.name + " - Risk Factor: " + l.Riskfactor As response 

# List risks associated with the "Shaft part Work" of the tunnel project.
match(n:wbs{name:"Shaft part Work"})-[:has_risk]->(m:risk) return "Risk: "+ m.name + " - "+ "Risk Category: " + m.riskcategory As response 

# What are the risk factors of "Shaft part Work" of the tunnel project?
match(n:wbs{name:"Shaft part Work"})-[:has_risk]->(m:risk)-[:has_riskfactor]->(l:riskfactor) return  "Risk: "+ m.name + " - Risk Factor: " + l.Riskfactor As response 

# List risks associated with the "Lining" of the tunnel project.
match(n:wbs{name:"Lining"})-[:has_risk]->(m:risk) return "Risk: "+ m.name + " - "+ "Risk Category: " + m.riskcategory As response 

# What are the risk factors of "Lining" of the tunnel project?
match(n:wbs{name:"Lining"})-[:has_risk]->(m:risk)-[:has_riskfactor]->(l:riskfactor) return  "Risk: "+ m.name + " - Risk Factor: " + l.Riskfactor As response 

# List risks associated with the "Excavation" of the tunnel project.
match(n:wbs{name:"Excavation"})-[:has_risk]->(m:risk) return "Risk: "+ m.name + " - "+ "Risk Category: " + m.riskcategory As response 

# What are the risk factors of "Excavation" of the tunnel project?
match(n:wbs{name:"Excavation"})-[:has_risk]->(m:risk)-[:has_riskfactor]->(l:riskfactor) return  "Risk: "+ m.name + " - Risk Factor: " + l.Riskfactor As response 

# How many risks are in the project? 
match(n:risk) return count(n) As response

# How many risk factors are in the project?
match(n:riskfactor) return count(n) As response

# List the risk category associated with the tunnel project.
match (n:risk) return distinct n.riskcategory as response 

"""
