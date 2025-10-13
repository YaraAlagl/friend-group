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

def max_group_age(group):
    """Return the maximum age in the group."""
    return max(person["age"] for person in group.values())

def mean_connection(group):
    """Return the average number of relations among members of the group."""
    from statistics import mean
    num_relations = [sum(len(names) for names in person["connections"].values()) for person in group.values()]
    return mean(num_relations) if num_relations else 0

def max_age_with_relation(group, relation_type):
    """Return the maximum age of members with at least one specified relation type."""
    return max(
        (person["age"] for person in group.values() if relation_type in person["connections"] and person["connections"][relation_type]),
        default=None
    )

def max_age_with_any_relation(group):
    """Return the maximum age of members with at least one relation of any type."""
    return max(
        (person["age"] for person in group.values() if any(person["connections"].values())),
        default=None
    )


if __name__ == "__main__":
        max_age = max_group_age(my_group)
        print(f"Maximum age in the group: {max_age}")
        mean_con = mean_connection(my_group)
        print(f"Average number of relations: {mean_con}")
        max_age_friend = max_age_with_relation(my_group, "Friend")
        print(f"Maximum age with at least one 'Friend' relation: {max_age_friend}")
        max_age_any = max_age_with_any_relation(my_group)
        print(f"Maximum age with at least one relation of any type: {max_age_any}")

