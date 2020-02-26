from ci_output_parser.log_file_parsers.log_file_parser import LogFileParser
from ci_output_parser.regex_ci_parser import RegexCIParser


class RegexLogFileParser(LogFileParser):
    def __init__(self, log_file_path=None, parser_name=None, output_file_name=None,
                 file_parser_parameters=None, log_line_parser_parameters=None, lint_error_parser_parameters=None,
                 clean_lint_error_parser_parameters=None):
        """RegexFileParser initializer

        Same as LogFileParser with added regex parser dictionaries for each parsing step.
        Each parser parameters dictionary must have start_regex, stop_regex, and parse_regex keys.
        The values of each parser parameters dictionary key must be valid regex.
        If no parser dictionaries given, all default to:
            dict(start_regex=None, stop_regex=None, parse_regex=r'.*')

        Args:
            file_parser_parameters (dict or None): parameters to get log lines from log file
            log_line_parser_parameters (dict or None): parameters to get lint lines from log lines
            lint_error_parser_parameters (dict or None): parameters to get lint errors from lint lines
            clean_lint_error_parser_parameters (dict or None): parameters to get clean lint error lines from lint errors
        """
        super().__init__(log_file_path, parser_name, output_file_name)
        self.default_parser_parameters = dict(start_regex=None,
                                              stop_regex=None,
                                              parse_regex=r'.*')
        self.log_file_parser = self.regex_parser_set_up(file_parser_parameters)
        self.lint_parser = self.regex_parser_set_up(log_line_parser_parameters)
        self.lint_error_parser = self.regex_parser_set_up(lint_error_parser_parameters)
        self.clean_lint_error_parser = self.regex_parser_set_up(clean_lint_error_parser_parameters)

    def regex_parser_set_up(self, parser_parameters=None):
        """Initialize RegexCIParser parser with parameters given.

        self.default_parser_parameters used if none given.

        Args:
            parser_parameters (dict or None): parameters for RegexCIParser generation

        Returns:
            (RegexCIParser): lint parser with start, stop, and parse regex set to parameters given or default if none

        """
        if parser_parameters is None:
            parser_parameters = self.default_parser_parameters
        lint_parser = RegexCIParser(
            start_regex=parser_parameters.get("start_regex"),
            stop_regex=parser_parameters.get("stop_regex"),
            parse_regex=parser_parameters.get("parse_regex"))
        return lint_parser

    def get_log_lines_from_file(self):
        self.log_lines = self.log_file_parser.parse_file(self.log_file_path)

    def get_lint_lines(self):
        self.lint_lines = self.lint_parser.parse_line_list(self.log_lines)

    def get_lint_error_lines(self):
        self.lint_errors = self.lint_error_parser.parse_line_list(self.lint_lines)

    def clean_lint_error_lines(self):
        self.lint_errors = self.clean_lint_error_parser.parse_line_list(self.lint_errors)
