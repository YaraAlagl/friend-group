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



def forget(person1, person2):
    """Remove person2 from person1's connections."""
    for relation, people in my_group[person1]["connections"].items():
        if person2 in people:
            people.remove(person2)
            if not people:  # If the list is empty, remove the relation
                del my_group[person1]["connections"][relation]
            break

def add_person(name, age, job, relations):
    """Add a new person to the group."""
    if name in my_group:
        print(f"{name} already exists in the group.")
        return
    my_group[name] = {
        "age": age,
        "job": job,
        "connections": relations
    }


forget("Andy", "Yara")
add_person("Sam", 30, "designer", {"Friend": ["Jill", "Zalika"]})

def average_age():
    """Calculate the average age of the group."""
    total_age = sum(info["age"] for info in my_group.values())
    return total_age / len(my_group)

def max_age():
    """Find the maximum age in the group."""
    return max(info["age"] for info in my_group.values())

def average_relations():
    """Calculate the average number of connections per person."""
    total_relations = sum(len(info["connections"]) for info in my_group.values())
    return total_relations / len(my_group)

def max_age_with_relations():
    """Find the maximum age among those with at least one connection."""
    return max(info["age"] for info in my_group.values() if info["connections"])

def max_age_with_friends():
    return max(info["age"] for info in my_group.values() if "Friend" in info["connections"] and info["connections"]["Friends"])

def max_age_with_friends():
    """Find the maximum age among those with at least one friend."""
    return max(
        info["age"] 
        for info in my_group.values() 
        if "Friend" in info["connections"] and info["connections"]["Friend"]
    )

if __name__ == "__main__":
    for person, info in my_group.items():
        print(f"{person} ({info['age']} yrs, {info['job']}) connections:")
        for friend, relation in info["connections"].items():
            print(f"  - {relation} of {friend}")

print(f"Average age: {average_age():.2f} years")
print(f"Maximum age: {max_age():.2f} years")
print(f"Average number of relations: {average_relations():.2f} relations")
print(f"Maximum age of people with at least 1 relation: {max_age_with_relations():.2f} years")
print(f"Maximum age of people with at least 1 friend: {max_age_with_friends():.2f} years")