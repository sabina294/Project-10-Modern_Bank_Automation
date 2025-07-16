try:
    file_in_project = open("demo.txt")
    print(file_in_project.read())
    file_in_project.close()
except Exception as e:
    print("Error:", e)

file_local_driver = open("E:\\BITM_6\\17th Class\\Class 17.txt")
print(file_local_driver.read())
file_local_driver.close()

