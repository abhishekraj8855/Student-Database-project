import pandas as pd 
import random
import numpy as np

# phle existing .csv load kare
df = pd.read_csv("studentsheet.csv")

names = ["Ankit","Riya","Priya","Aman","Neha","Rohit","Simarn","Vikas","Pooja","pooja","mohan","Senha","Raj","Meena","Rahul","Sanjay","Divya","Manish","Aarti"]
courses = ["Data science","AI","Web development","IOT","Cyber Security"]
df['course'] = np.random.choice(courses, size=len(df))
print(df)

#subject map course wise
subject_map = {
    "Data Science": ["Python","Machine Learning"],
    "AI": ["Neural Networks","NLP","Computer version"],
    "Web Development": ["HTML","CSS","Javascript"],
    "IOT": ["Sensors", "Embeded System ", "Ardunio"],
    "Cyber Security": ["Cryptography", "Network Security", "Ethical"]
}
# subject assign based on course 
df['subject'] = df['course'].apply(
    lambda c: np.random.choice(subject_map.get(c, ["General"])))
print(df)
    
# 100 new row generate kre
new_rows = []
for i in range(1):  # loops 500 times chalega
    new_rows.append({
        "name": random.choice(names),
        "age": random.randint(20, 25),       # 20-25 age
        "marks": random.randint(60, 80),    # 60-80 marks
        "course": random.choice(courses)
    })

# DataFrame me convert new data
new_df = pd.DataFrame(new_rows) 

# old + new data combine
df = pd.concat([df, new_df], ignore_index=True)   

# save back to csv
df.to_csv("studentsheet.csv", index=False)

print("1 new rows added successfully")
