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

print(my_group)

def forget(person1, person2):
    """Remove person2 from person1's connections."""
    for relation, people in my_group[person1]["connections"].items():
        if person2 in people:
            people.remove(person2)
            if not people:  # If the list is empty, remove the relation
                del my_group[person1]["connections"][relation]
            break

forget("Andy", "Yara")
if __name__ == "__main__":
    for person, info in my_group.items():
        print(f"{person} ({info['age']} yrs, {info['job']}) connections:")
        for friend, relation in info["connections"].items():
            print(f"  - {relation} of {friend}")