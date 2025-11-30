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


if __name__ == "__main__":
    group = {
        "Alice": {"age": 30},
        "Bob": {"age": 40},
        "Charlie": {"age": 25},
    }

    assert average_age(group) == (30 + 40 + 25) / 3

    add_person(group, "Diana", 22, "New York")
    assert "Diana" in group

    remove_person(group, "Bob")
    assert "Bob" not in group

    print("All tests passed!")

