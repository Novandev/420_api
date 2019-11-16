from flask import make_response, abort
STRAINS = {
    "fire-og":{
        "strain":"Fire OG",
        "type":"Hybrid",
        "rating":4.5,
        "description":"Fire OG is a nice hybrid"
    },
    "durban-poison":{
        "strain":"Durban Poison",
        "type":"Sativa",
        "rating":4.1,
        "description":"Durban posion is an excelent sativa"
    },
    "grandaddy-purp":{
        "strain":"Grandaddy Purp",
        "type":"Indica",
        "rating":4.7,
        "description":"Grandaddy Purp is a nice indica"
    }
}

def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [STRAINS[strain] for strain in sorted(STRAINS.keys())]

def read_one(strain):
    if strain in STRAINS:
        return_strain = STRAINS[strain]
    else:
        abort(
             404, " {strain} not found in strains".format(strain=strain)
        )
    return return_strain