def application(env, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    message = (
        "we in this test image 🔥😩👌:\n    tiangolo/uwsgi-nginx:python3.9-2021-10-02"
    )
    return [message.encode("utf-8")]
