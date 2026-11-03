"""Outgoing webhooks."""

MAX_ATTEMPTS = 3


def deliver(send, event):
    response = None
    for _ in range(MAX_ATTEMPTS):
        response = send(event)
        if response.status_code >= 500:
            continue
        break
    return response
