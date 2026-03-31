def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    if not isinstance(attendees, list):
        print("Error: attendees must be a list")
        return

    for person in attendees:
        if not isinstance(person, dict):
            print("Error: attendees must be a list of dictionaries")
            return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i, person in enumerate(attendees, start=1):
        output_text = template

        name = person.get("name")
        if name is None:
            name = "N/A"

        event_title = person.get("event_title")
        if event_title is None:
            event_title = "N/A"

        event_date = person.get("event_date")
        if event_date is None:
            event_date = "N/A"

        event_location = person.get("event_location")
        if event_location is None:
            event_location = "N/A"

        output_text = output_text.replace("{name}", str(name))
        output_text = output_text.replace("{event_title}", str(event_title))
        output_text = output_text.replace("{event_date}", str(event_date))
        output_text = output_text.replace("{event_location}", str(event_location))

        filename = f"output_{i}.txt"
        with open(filename, "w") as file:
            file.write(output_text)
        