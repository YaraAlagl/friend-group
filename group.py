"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "Jill": {
        "age": 26, 
        "job": "biologist",
        "connections": {
            "Friend" : ["Zalika"],
            "Partner" : ["John"]
        }
    },
    "Zalika" : {
        "age": 28, 
        "job": "artist",
        "connections": {
            "Friend" : ["Jill"]
        }
    },
    "John" : {
        "age": 27, 
        "job": "writer",
        "connections": {
            "Partner" : ["Jill"]
        }
    },
    "Nash": {
        "age": 34, 
        "job": "chef",
        "connections": {
            "Cousin" : ["John"],
            "Landlord" : ["Zalika"],
        }
    },
    "Yara": {
        "age": 25, 
        "job": "engineer",
        "connections": {},
    },
    "Andy": {
        "age": 22, 
        "job": "",
        "connections": {
            "Friend" : ["Yara"],
            "Gym Buddy" : ["Nash"]
        }
    },
}



def remove_person(group, name):
    if name in group:
        del group[name]


def add_person(group, name, age, city):
    group[name] = {"age": age, "city": city}

def average_age(group):
    ages = [p["age"] for p in group.values()]
    return sum(ages) / len(group)

def oldest_person(group):
    return max(group.items(), key=lambda item: item[1]["age"])[0]

remove_person("Andy", "Yara")
add_person("Sam", 30, "designer", {"Friend": ["Jill", "Zalika"]})
print(f"Average age: {average_age():.2f} years")

if __name__ == "__main__":
    for person, info in my_group.items():
        print(f"{person} ({info['age']} yrs, {info['job']}) connections:")
        for friend, relation in info["connections"].items():
            print(f"  - {relation} of {friend}")

