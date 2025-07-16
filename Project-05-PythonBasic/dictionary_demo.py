user_details = {
    "username":"John Doe",
    "email": "doe@gmail.com",
    "phone": "12345678",
    "password": "123456",
    "address": {
        "present_address":{
            "road": "12/A",
            "word_no": 10,
            "city": "dhaka"
        },
        "permanent_address":{
            "road": "123",
            "word_no": 5,
            "city": "NY"
        }
    },
    "age": 20,
    "tax": 10.5,
    "language": ["Bangla","English","Hindi","Arabic",{
        "hobbies": "Travel"
    }],
    "is_active": True,
    "skills" : [
        {"skill_name" :"C", "skill_level": "beginner"},
        {"skill_name" :"Java", "skill_level": "expert"},
        {"skill_name" :"Python", "skill_level": "advance"}
    ]
}


print(user_details["username"])
print(user_details["language"][0])
print(user_details["address"]["present_address"]["city"])
print(user_details["language"][4]["hobbies"])
print(user_details["skills"][2]["skill_level"])

user_details["color"] = "red"

print(user_details["color"])

print(user_details.items())