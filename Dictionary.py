students={"Ronit":80,"Uttam":82,"Mahadev":84,"Ankit":86,"Abrojit":88,"Rohan":90,"Jyotismith":92}
Name=input("Enter the student's name: ")
if Name in students:
    print(Name + "'s mark:",students[Name])
else:
    print("Student not found:")