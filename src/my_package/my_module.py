from result import Result, Ok


def hello_world() -> Result[str, Exception]:
    return Ok("Hello world!")
