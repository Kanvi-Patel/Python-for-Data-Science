def count_unread_messages(messages):
    total=messages["count"]

    for group in messages["subgroups"]:
        total=total+count_unread_messages(group)

    return total


messages={
    "count":6,
    "subgroups": [
        {
            "count":3,
            "subgroups":[]
        },
        {
            "count":3,
            "subgroups":[]
        }
    ]
}

print("Total unread messages:",count_unread_messages(messages))
