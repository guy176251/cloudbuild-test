def application(env, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    message = "This change was made on Mon Oct 25, 9:49AM"
    return [message.encode("utf-8")]
