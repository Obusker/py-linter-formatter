def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [{"line": second_error["line_number"],
                    "column": second_error["column_number"],
                    "message": second_error["text"],
                    "name": second_error["code"],
                    "source": "flake8"}
                   for second_error in errors],
        "path": file_path,
        "status": "passed" if len(errors) is None else "failed"}


def format_linter_report(linter_report: dict) -> list:
    return [
        {"errors": [{"line": third_error["line_number"],
                     "column": third_error["column_number"],
                     "message": third_error["text"],
                     "name": third_error["code"],
                     "source": "flake8"}
                    for third_error in errors],
         "path": keys,
         "status": "passed" if len(errors) < 1 else "failed"}
        for keys, errors in linter_report.items()
    ]
