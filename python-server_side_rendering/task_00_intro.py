#!/usr/bin/env python3
"""Generate personalized invitation files from a template."""

import logging
import os
import re

logging.basicConfig(level=logging.ERROR)


def generate_invitations(template, attendees):
    """Generate output_X.txt invitation files from a template and attendees.

    Args:
        template (str): Template containing placeholders.
        attendees (list): List of dictionaries containing attendee data.
    """
    if not isinstance(template, str):
        logging.error(
            "Invalid input: template must be a string, got %s.",
            type(template).__name__
        )
        return

    if not isinstance(attendees, list):
        logging.error(
            "Invalid input: attendees must be a list, got %s.",
            type(attendees).__name__
        )
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        logging.error(
            "Invalid input: attendees must be a list of dictionaries."
        )
        return

    if not template:
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    placeholders = re.findall(r"\{(\w+)\}", template)

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for placeholder in placeholders:
            value = attendee.get(placeholder)

            if value is None:
                value = "N/A"

            invitation = invitation.replace(
                "{" + placeholder + "}",
                str(value)
            )

        output_filename = "output_{}.txt".format(index)

        try:
            with open(output_filename, "w", encoding="utf-8") as output_file:
                output_file.write(invitation)
        except OSError as error:
            logging.error(
                "Could not write %s: %s", output_filename, error
            )
