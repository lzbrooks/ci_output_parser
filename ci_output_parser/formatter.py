def format_lint_lines(parser_name, parser_lint, lint_log_lines=None):
    if lint_log_lines is None:
        lint_log_lines = []
    lint_log_lines = format_lint_title(parser_name, lint_log_lines)
    lint_log_lines = format_lint_error_lines(parser_lint, lint_log_lines)
    return lint_log_lines


def format_lint_error_lines(parser_lint, lint_log_lines):
    lint_log_lines.append("```\n")
    if not parser_lint:
        lint_log_lines.append("No errors to report\n")
    lint_log_lines.extend(parser_lint)
    lint_log_lines.append("```\n")
    return lint_log_lines


def format_lint_title(parser_name, lint_log_lines):
    lint_log_lines.extend([
        "\n",
        "## {0}\n".format(parser_name),
        "\n"])
    return lint_log_lines
