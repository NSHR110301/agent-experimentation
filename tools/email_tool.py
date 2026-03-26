def get_or_create_label(service, label_name):
    results = service.users().labels().list(userId="me").execute()
    labels = results.get("labels", [])

    for label in labels:
        if label["name"].lower() == label_name.lower():
            return label["id"]

    # Create label if not exists
    label_object = {
        "name": label_name,
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
    }

    created_label = (
        service.users().labels().create(userId="me", body=label_object).execute()
    )

    return created_label["id"]


def apply_label(service, message_id, label_id):
    service.users().messages().modify(
        userId="me", id=message_id, body={"addLabelIds": [label_id]}
    ).execute()
